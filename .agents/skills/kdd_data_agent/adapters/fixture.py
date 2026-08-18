"""Fixture-only read adapter.

This is the only source of "data" in the M0 slice. It reads JSON files from one
declared fixture root and nothing else: no credential, no network, no
subprocess, no publication, no write of any kind, and no path outside the root.
Case ids are validated against a strict pattern, so path traversal is not
blocked by a check that could be bypassed — it has no expressible form.

The adapter validates fixture integrity strictly and fails closed. An unknown
outcome string, an unknown field, a retained body on an unauthorized read, or a
non-trusted read with no stated Coverage Gap is a fixture error, not a silently
absorbed edge case. It still makes no readiness judgement: it types the read
and stops.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from ..core.canonical_json import canonical_loads
from ..core.capabilities import Capability
from ..core.coverage_gap import (
    COVERAGE_GAP_KIND_REGISTRY,
    CoverageGap,
    CoverageGapKind,
    resolve_coverage_gap_kind,
)
from ..core.identity import (
    AUTHORIZATION_STATES_PERMITTING_BODY,
    REDACTION_STATES_PERMITTING_BODY,
    Actor,
    ActorKind,
    AuthorizationState,
    RedactionState,
    SourceIdentity,
    TimeInterval,
    validate_timestamp,
)
from ..core.receipts import Receipt, ReceiptKind
from ..core.unknown import MISSING, UNKNOWN, is_sentinel
from .base import ReadAdapter, ReadRequest, ReadResult
from .outcomes import (
    DEFAULT_GAP_KIND_BY_OUTCOME,
    OUTCOMES_REQUIRING_COVERAGE_GAP,
    OUTCOMES_WITHOUT_RETAINED_BODY,
    ReadOutcome,
    parse_read_outcome,
)

FIXTURE_SCHEMA_VERSION = "m0-fixture-read/v0"
MANIFEST_NAME = "manifest.json"
MANIFEST_SCHEMA_VERSION = "m0-fixture-manifest/v0"

CASE_ID_PATTERN = re.compile(r"[a-z0-9][a-z0-9-]{2,63}")

_REQUIRED_FIXTURE_KEYS = frozenset(
    {
        "schema_version",
        "case_id",
        "declared_outcome",
        "source",
        "authorization",
        "observed_interval",
        "recorded_at",
        "body",
        "coverage_gaps",
        "disagreements",
        "expected_final_readiness",
        "notes",
    }
)
_REQUIRED_SOURCE_KEYS = frozenset({"source_id", "source_kind", "locator", "snapshot_id", "owner"})
_REQUIRED_AUTHORIZATION_KEYS = frozenset({"state", "recipient_scope", "redaction"})

EXPECTED_READINESS_PLACEHOLDER = "alignment_pending"
"""Fixtures state their expected read outcome, never their expected readiness.

Readiness is `SEAM-M0-01-READINESS-OUTCOME`. Until the packet is frozen, every
fixture records this placeholder so Phase B has an explicit slot to fill rather
than an assumption to discover.
"""

FIXTURE_ACTOR = Actor(actor_id="m0-local-fixture-adapter", actor_kind=ActorKind.FIXTURE)


class FixtureIntegrityError(ValueError):
    """Raised when a fixture file is malformed or self-contradictory."""


class FixtureNotFoundError(FileNotFoundError):
    """Raised when a requested fixture case does not exist under the root."""


def _require_mapping(value: Any, field: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise FixtureIntegrityError(f"{field} must be an object, got {type(value).__name__}")
    return value


def _require_exact_keys(value: Mapping[str, Any], expected: frozenset[str], field: str) -> None:
    present = frozenset(value)
    missing = expected - present
    unexpected = present - expected
    if missing:
        raise FixtureIntegrityError(f"{field} is missing required keys: {sorted(missing)}")
    if unexpected:
        raise FixtureIntegrityError(f"{field} has unrecognised keys: {sorted(unexpected)}")


def validate_case_id(case_id: str) -> str:
    """Validate a fixture case id. Rejects anything that could name a path."""
    if not isinstance(case_id, str) or CASE_ID_PATTERN.fullmatch(case_id) is None:
        raise FixtureIntegrityError(
            f"invalid fixture case id {case_id!r}; expected lowercase letters, digits, and hyphens"
        )
    return case_id


class FixtureReadAdapter(ReadAdapter):
    """Reads typed M0 source-read fixtures from one local directory."""

    capabilities = frozenset({Capability.FIXTURE_READ, Capability.LOCAL_DETERMINISTIC_COMPUTE})

    def __init__(self, fixture_root: Path) -> None:
        super().__init__()
        root = Path(fixture_root).resolve()
        if not root.is_dir():
            raise FixtureNotFoundError(f"fixture root is not a directory: {root}")
        self._root = root
        self._byte_digests: dict[str, str] = {}

    @property
    def root(self) -> Path:
        return self._root

    def _case_path(self, case_id: str) -> Path:
        validate_case_id(case_id)
        path = (self._root / f"{case_id}.json").resolve()
        if not path.is_relative_to(self._root):
            raise FixtureIntegrityError(f"fixture case {case_id!r} resolves outside the fixture root")
        if not path.is_file():
            raise FixtureNotFoundError(f"no fixture file for case {case_id!r} under {self._root}")
        return path

    def load_raw(self, case_id: str) -> Mapping[str, Any]:
        """Return the parsed fixture document without interpreting it."""
        import hashlib

        text = self._case_path(case_id).read_text(encoding="utf-8")
        self._byte_digests[case_id] = hashlib.sha256(text.encode("utf-8")).hexdigest()
        document = canonical_loads(text)
        fixture = _require_mapping(document, f"fixture {case_id!r}")
        _require_exact_keys(fixture, _REQUIRED_FIXTURE_KEYS, f"fixture {case_id!r}")
        if fixture["schema_version"] != FIXTURE_SCHEMA_VERSION:
            raise FixtureIntegrityError(
                f"fixture {case_id!r} declares schema {fixture['schema_version']!r}, "
                f"expected {FIXTURE_SCHEMA_VERSION!r}"
            )
        if fixture["case_id"] != case_id:
            raise FixtureIntegrityError(
                f"fixture file {case_id!r} declares case_id {fixture['case_id']!r}"
            )
        if fixture["expected_final_readiness"] != EXPECTED_READINESS_PLACEHOLDER:
            raise FixtureIntegrityError(
                f"fixture {case_id!r} states expected_final_readiness "
                f"{fixture['expected_final_readiness']!r}; before the packet is frozen it must be "
                f"{EXPECTED_READINESS_PLACEHOLDER!r}"
            )
        return fixture

    def case_ids(self) -> tuple[str, ...]:
        """Case ids listed in the manifest, in manifest order."""
        return tuple(entry["case_id"] for entry in self.load_manifest()["cases"])

    def load_manifest(self) -> Mapping[str, Any]:
        """Load and validate the fixture manifest."""
        path = (self._root / MANIFEST_NAME).resolve()
        if not path.is_relative_to(self._root):
            raise FixtureIntegrityError(f"{MANIFEST_NAME} resolves outside the fixture root")
        if not path.is_file():
            raise FixtureNotFoundError(f"no {MANIFEST_NAME} under {self._root}")
        manifest = _require_mapping(canonical_loads(path.read_text(encoding="utf-8")), MANIFEST_NAME)
        _require_exact_keys(manifest, frozenset({"schema_version", "description", "cases"}), MANIFEST_NAME)
        if manifest["schema_version"] != MANIFEST_SCHEMA_VERSION:
            raise FixtureIntegrityError(
                f"{MANIFEST_NAME} declares schema {manifest['schema_version']!r}, "
                f"expected {MANIFEST_SCHEMA_VERSION!r}"
            )
        seen: set[str] = set()
        for entry in manifest["cases"]:
            case = _require_mapping(entry, f"{MANIFEST_NAME} case entry")
            _require_exact_keys(
                case,
                frozenset({"case_id", "expected_read_outcome", "expected_final_readiness"}),
                f"{MANIFEST_NAME} case entry",
            )
            validate_case_id(case["case_id"])
            parse_read_outcome(case["expected_read_outcome"])
            if case["case_id"] in seen:
                raise FixtureIntegrityError(f"{MANIFEST_NAME} lists case {case['case_id']!r} twice")
            seen.add(case["case_id"])
            if case["expected_final_readiness"] != EXPECTED_READINESS_PLACEHOLDER:
                raise FixtureIntegrityError(
                    f"{MANIFEST_NAME} case {case['case_id']!r} must record "
                    f"expected_final_readiness {EXPECTED_READINESS_PLACEHOLDER!r}"
                )
        return manifest

    def _load_sealed_corpus(self) -> Mapping[str, Any]:
        """Load the byte-bound executable M0 corpus through the fixture seam."""
        path = (self._root / "sealed-corpus.json").resolve()
        if not path.is_relative_to(self._root) or not path.is_file():
            raise FixtureNotFoundError("sealed-corpus.json is missing from the fixture root")
        document = _require_mapping(canonical_loads(path.read_text(encoding="utf-8")), "sealed-corpus.json")
        _require_exact_keys(document, frozenset({"schema_version", "fixture_byte_sha256", "cases"}), "sealed-corpus.json")
        return document

    def _fixture_byte_sha256(self, case_id: str) -> str:
        """Return the actual fixture-file digest without exposing filesystem authority."""
        if case_id not in self._byte_digests:
            self.load_raw(case_id)
        return self._byte_digests[case_id]

    def read(self, request: ReadRequest) -> ReadResult:
        """Resolve `request.locator` as a fixture case id and type the read."""
        if is_sentinel(request.locator):
            raise FixtureIntegrityError("fixture reads require a locator naming the case id")
        case_id = str(request.locator)
        fixture = self.load_raw(case_id)

        outcome = parse_read_outcome(fixture["declared_outcome"])
        expected_outcomes = {
            entry["case_id"]: parse_read_outcome(entry["expected_read_outcome"])
            for entry in self.load_manifest()["cases"]
        }
        if case_id not in expected_outcomes:
            raise FixtureIntegrityError(f"fixture {case_id!r} is not listed in {MANIFEST_NAME}")
        if outcome is not expected_outcomes[case_id]:
            raise FixtureIntegrityError(
                f"fixture {case_id!r} declares outcome {outcome.value!r}, but {MANIFEST_NAME} "
                f"expects {expected_outcomes[case_id].value!r}"
            )
        source = self._build_source(fixture["source"], case_id)
        if source.source_id != request.source_id:
            raise FixtureIntegrityError(
                f"fixture {case_id!r} belongs to source {source.source_id!r}, "
                f"request asked for {request.source_id!r}"
            )

        authorization = _require_mapping(fixture["authorization"], f"fixture {case_id!r} authorization")
        _require_exact_keys(authorization, _REQUIRED_AUTHORIZATION_KEYS, f"fixture {case_id!r} authorization")
        authorization_state = self._parse_authorization_state(authorization["state"], case_id)
        redaction_state = self._parse_redaction_state(authorization["redaction"], case_id)

        interval_fields = _require_mapping(
            fixture["observed_interval"], f"fixture {case_id!r} observed_interval"
        )
        _require_exact_keys(interval_fields, frozenset({"start", "end"}), f"fixture {case_id!r} observed_interval")
        observed_interval = TimeInterval(start=interval_fields["start"], end=interval_fields["end"])
        recorded_at = validate_timestamp(fixture["recorded_at"], f"fixture {case_id!r} recorded_at")

        body = fixture["body"]
        self._enforce_body_policy(case_id, outcome, authorization_state, redaction_state, body)

        coverage_gaps = self._build_coverage_gaps(fixture["coverage_gaps"], outcome, case_id)
        disagreements = tuple(
            dict(_require_mapping(item, f"fixture {case_id!r} disagreement"))
            for item in fixture["disagreements"]
        )

        receipt = Receipt(
            receipt_kind=ReceiptKind.SOURCE_READ,
            source=source,
            actor=FIXTURE_ACTOR,
            authorization_state=authorization_state,
            redaction_state=redaction_state,
            observed_interval=observed_interval,
            recorded_at=recorded_at,
            outcome=outcome.value,
            derivation_inputs=(f"fixture:{case_id}",),
            coverage_gaps=coverage_gaps,
            detail={
                "request": request.to_canonical(),
                "fixture_schema_version": FIXTURE_SCHEMA_VERSION,
                "recipient_scope": authorization["recipient_scope"],
                "redaction": redaction_state.value,
                "disagreement_count": len(disagreements),
                "notes": fixture["notes"],
            },
            body=body,
        )

        return ReadResult(
            request=request,
            outcome=outcome,
            receipt=receipt,
            body=body,
            coverage_gaps=coverage_gaps,
            disagreements=disagreements,
        )

    @staticmethod
    def _build_source(raw: Any, case_id: str) -> SourceIdentity:
        fields = _require_mapping(raw, f"fixture {case_id!r} source")
        _require_exact_keys(fields, _REQUIRED_SOURCE_KEYS, f"fixture {case_id!r} source")
        return SourceIdentity(
            source_id=fields["source_id"],
            source_kind=fields["source_kind"],
            locator=fields["locator"],
            snapshot_id=fields["snapshot_id"],
            owner=fields["owner"],
        )

    @staticmethod
    def _parse_authorization_state(value: Any, case_id: str) -> AuthorizationState:
        if not isinstance(value, str):
            raise FixtureIntegrityError(f"fixture {case_id!r} authorization.state must be a string")
        try:
            return AuthorizationState(value)
        except ValueError:
            allowed = ", ".join(item.value for item in AuthorizationState)
            raise FixtureIntegrityError(
                f"fixture {case_id!r} authorization.state {value!r} is not one of: {allowed}"
            ) from None

    @staticmethod
    def _parse_redaction_state(value: Any, case_id: str) -> RedactionState:
        if is_sentinel(value):
            return RedactionState.UNKNOWN
        if not isinstance(value, str):
            raise FixtureIntegrityError(f"fixture {case_id!r} authorization.redaction must be a string")
        try:
            return RedactionState(value)
        except ValueError:
            allowed = ", ".join(item.value for item in RedactionState)
            raise FixtureIntegrityError(
                f"fixture {case_id!r} authorization.redaction {value!r} is not one of: {allowed}"
            ) from None

    @staticmethod
    def _enforce_body_policy(
        case_id: str,
        outcome: ReadOutcome,
        authorization_state: AuthorizationState,
        redaction_state: RedactionState,
        body: Any,
    ) -> None:
        body_present = not is_sentinel(body)
        if outcome in OUTCOMES_WITHOUT_RETAINED_BODY and body_present:
            raise FixtureIntegrityError(
                f"fixture {case_id!r} declares outcome {outcome.value} but retains a body; "
                "no body may be retained for this outcome"
            )
        if body_present and authorization_state not in AUTHORIZATION_STATES_PERMITTING_BODY:
            raise FixtureIntegrityError(
                f"fixture {case_id!r} retains a body under authorization state "
                f"{authorization_state.value}; only an explicit authorized state may carry one"
            )
        if body_present and redaction_state not in REDACTION_STATES_PERMITTING_BODY:
            raise FixtureIntegrityError(
                f"fixture {case_id!r} retains a body under redaction state "
                f"{redaction_state.value}; redaction must be applied or not required"
            )
        if outcome is ReadOutcome.TRUSTED:
            if authorization_state is not AuthorizationState.AUTHORIZED:
                raise FixtureIntegrityError(
                    f"fixture {case_id!r} declares a trusted read under authorization state "
                    f"{authorization_state.value}"
                )
            if not body_present:
                raise FixtureIntegrityError(
                    f"fixture {case_id!r} declares a trusted read with no body"
                )

    @staticmethod
    def _build_coverage_gaps(raw: Any, outcome: ReadOutcome, case_id: str) -> tuple[CoverageGap, ...]:
        if not isinstance(raw, list):
            raise FixtureIntegrityError(f"fixture {case_id!r} coverage_gaps must be a list")
        gaps: list[CoverageGap] = []
        for entry in raw:
            fields = _require_mapping(entry, f"fixture {case_id!r} coverage gap")
            _require_exact_keys(
                fields,
                frozenset({"kind", "reason", "next_safe_check"}),
                f"fixture {case_id!r} coverage gap",
            )
            kind_value = fields["kind"]
            if is_sentinel(kind_value):
                kind = DEFAULT_GAP_KIND_BY_OUTCOME.get(outcome, CoverageGapKind.UNCHECKED_PLANE)
            else:
                try:
                    kind = resolve_coverage_gap_kind(kind_value)
                except (TypeError, ValueError):
                    allowed = ", ".join(COVERAGE_GAP_KIND_REGISTRY)
                    raise FixtureIntegrityError(
                        f"fixture {case_id!r} coverage gap kind {kind_value!r} is not one of: {allowed}"
                    ) from None
            gaps.append(
                CoverageGap(
                    kind=kind,
                    reason=fields["reason"],
                    next_safe_check=fields["next_safe_check"],
                )
            )
        if outcome in OUTCOMES_REQUIRING_COVERAGE_GAP and not gaps:
            raise FixtureIntegrityError(
                f"fixture {case_id!r} declares outcome {outcome.value} with no Coverage Gap; "
                "incomplete coverage must be recorded, not implied"
            )
        if outcome is ReadOutcome.TRUSTED and gaps:
            raise FixtureIntegrityError(
                f"fixture {case_id!r} declares a trusted read that also carries Coverage Gaps"
            )
        return tuple(gaps)


__all__ = [
    "CASE_ID_PATTERN",
    "EXPECTED_READINESS_PLACEHOLDER",
    "FIXTURE_ACTOR",
    "FIXTURE_SCHEMA_VERSION",
    "FixtureIntegrityError",
    "FixtureNotFoundError",
    "FixtureReadAdapter",
    "MANIFEST_NAME",
    "MANIFEST_SCHEMA_VERSION",
    "MISSING",
    "UNKNOWN",
    "validate_case_id",
]
