"""Exact frozen nineteen-check registry and deterministic check records."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from ..core.coverage_gap import Materiality, require_registered_rule_source
from ..core.digest import content_digest
from .contracts import ExperimentReadContract


class CheckError(ValueError):
    pass


class CheckOutcome(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    MISSING = "MISSING"
    UNKNOWN = "UNKNOWN"
    NOT_APPLICABLE = "NOT_APPLICABLE"


@dataclass(frozen=True)
class CheckDefinition:
    check_id: str
    title: str
    core_floor: bool
    rule_source: str

    def to_canonical(self) -> dict[str, Any]:
        return {
            "check_id": self.check_id,
            "title": self.title,
            "core_floor": self.core_floor,
            "rule_source": self.rule_source,
        }


_CHECK_TITLES = (
    "Flight identity and contract version",
    "Preregistered versus observed runtime",
    "Decision-metric registration, definition version, role, and policy",
    "Assignment-unit and analysis-unit consistency",
    "Assignment, exposure integrity, and arm parity",
    "SRM and applicable compositional SRM",
    "Population, eligibility, exclusions, and scope consistency",
    "Numerator, denominator, grain, joins, units, ratios, and percent handling",
    "Completeness, freshness, late arrival, pagination, and partial reads",
    "Estimator and variance-method consistency",
    "CUPED-mode identity and non-interchangeability",
    "Source, lineage, metric-definition, and source-owner identity",
    "Primary-source versus scorecard or UI reconciliation",
    "Reported decision metric versus independent recomputation",
    "Source-change revalidation",
    "Authorization, ACL, recipient, redaction, retention, load, and halt",
    "Attribution, freshness, and scope across every read",
    "Disagreements, contradictions, and Coverage Gap closure",
    "Preregistered sample or unit sufficiency",
)

FIXED_FLOOR_CHECK_IDS = frozenset(
    {"CHK-01", "CHK-03", "CHK-05", "CHK-06", "CHK-08", "CHK-12", "CHK-14", "CHK-16", "CHK-19"}
)

CHECK_REGISTRY = tuple(
    CheckDefinition(
        check_id=f"CHK-{index:02d}",
        title=title,
        core_floor=f"CHK-{index:02d}" in FIXED_FLOOR_CHECK_IDS,
        rule_source=f"m0-alignment-v1#CHK-{index:02d}",
    )
    for index, title in enumerate(_CHECK_TITLES, 1)
)

if len(CHECK_REGISTRY) != 19 or len({item.check_id for item in CHECK_REGISTRY}) != 19:
    raise RuntimeError("the frozen M0 check registry must contain CHK-01 through CHK-19 exactly once")


@dataclass(frozen=True)
class CoreCheckSet:
    revision: str
    check_ids: tuple[str, ...] = tuple(item.check_id for item in CHECK_REGISTRY)
    digest: str = field(init=False)

    def __post_init__(self) -> None:
        if self.revision != "m0-core-check-set/v1":
            raise CheckError("core check set revision must be m0-core-check-set/v1")
        object.__setattr__(self, "check_ids", tuple(self.check_ids))
        if len(self.check_ids) != len(set(self.check_ids)):
            raise CheckError("core check set cannot contain duplicate checks")
        if not FIXED_FLOOR_CHECK_IDS.issubset(self.check_ids):
            raise CheckError("core check set cannot omit a fixed-floor check")
        if set(self.check_ids) != {item.check_id for item in CHECK_REGISTRY}:
            raise CheckError("fixture M0 executes the exact frozen nineteen-check inventory")
        object.__setattr__(self, "digest", content_digest(self.to_canonical(include_digest=False)))

    def to_canonical(self, *, include_digest: bool = True) -> dict[str, Any]:
        payload = {"revision": self.revision, "check_ids": list(self.check_ids)}
        if include_digest:
            payload["digest"] = self.digest
        return payload


@dataclass(frozen=True)
class CheckResult:
    check_id: str
    outcome: CheckOutcome
    materiality: Materiality
    rule_source: str
    materiality_rule_id: str
    evidence_ids: tuple[str, ...]
    receipt_ids: tuple[str, ...]
    reason: str
    reopen_condition: str
    affected_scope: str
    ruling_actor: str
    result_digest: str = field(init=False)

    def __post_init__(self) -> None:
        if self.check_id not in {item.check_id for item in CHECK_REGISTRY}:
            raise CheckError(f"unknown check id {self.check_id!r}")
        if not isinstance(self.outcome, CheckOutcome):
            raise TypeError("outcome must be CheckOutcome")
        if not isinstance(self.materiality, Materiality):
            raise TypeError("materiality must be Materiality")
        require_registered_rule_source(self.rule_source)
        require_registered_rule_source(self.materiality_rule_id)
        object.__setattr__(self, "evidence_ids", tuple(self.evidence_ids))
        object.__setattr__(self, "receipt_ids", tuple(self.receipt_ids))
        for name, value in (
            ("reason", self.reason), ("reopen_condition", self.reopen_condition),
            ("affected_scope", self.affected_scope), ("ruling_actor", self.ruling_actor),
        ):
            if not isinstance(value, str) or not value.strip():
                raise CheckError(f"{name} is required")
        if self.outcome is CheckOutcome.NOT_APPLICABLE and "applicability" not in self.rule_source:
            raise CheckError("NOT_APPLICABLE requires a registered applicability rule")
        if self.outcome is CheckOutcome.PASS and (not self.evidence_ids or not self.receipt_ids):
            raise CheckError("PASS requires check-specific evidence and a proving receipt")
        object.__setattr__(self, "result_digest", content_digest(self.to_canonical(include_digest=False)))

    def to_canonical(self, *, include_digest: bool = True) -> dict[str, Any]:
        payload = {
            "check_id": self.check_id,
            "outcome": self.outcome.value,
            "materiality": self.materiality.value,
            "rule_source": self.rule_source,
            "materiality_rule_id": self.materiality_rule_id,
            "evidence_ids": list(self.evidence_ids),
            "receipt_ids": list(self.receipt_ids),
            "reason": self.reason,
            "reopen_condition": self.reopen_condition,
            "affected_scope": self.affected_scope,
            "ruling_actor": self.ruling_actor,
        }
        if include_digest:
            payload["result_digest"] = self.result_digest
        return payload


@dataclass(frozen=True)
class ValidatorResult:
    """One validator's explicit outcome and check-specific evidence binding."""

    outcome: CheckOutcome
    evidence_ids: tuple[str, ...]
    receipt_ids: tuple[str, ...]
    materiality: Materiality = Materiality.MATERIAL
    reason: str = "validator passed"
    reopen_condition: str = "reopen on a superseding read"
    rule_source: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.outcome, CheckOutcome):
            raise TypeError("validator outcome must be CheckOutcome")
        if not isinstance(self.materiality, Materiality):
            raise TypeError("validator materiality must be Materiality")
        object.__setattr__(self, "evidence_ids", tuple(self.evidence_ids))
        object.__setattr__(self, "receipt_ids", tuple(self.receipt_ids))
        if self.outcome is CheckOutcome.PASS and (not self.evidence_ids or not self.receipt_ids):
            raise CheckError("PASS requires check-specific evidence and a proving receipt")


def evaluate_checks(
    contract: ExperimentReadContract,
    *,
    validator_results: dict[str, ValidatorResult],
) -> tuple[CheckResult, ...]:
    """Seal exactly one explicit result per validator; absence fails closed."""
    validator_results = dict(validator_results)
    unknown = set(validator_results) - {item.check_id for item in CHECK_REGISTRY}
    if unknown:
        raise CheckError(f"validator results name unknown checks: {sorted(unknown)}")

    results: list[CheckResult] = []
    for definition in CHECK_REGISTRY:
        result = validator_results.get(definition.check_id)
        if result is None:
            result = ValidatorResult(
                CheckOutcome.MISSING,
                (),
                (),
                Materiality.MATERIAL,
                "validator result or check-specific evidence is absent",
                "run the named validator with check-specific evidence",
            )
        rule_source = result.rule_source or definition.rule_source
        results.append(
            CheckResult(
                check_id=definition.check_id,
                outcome=result.outcome,
                materiality=result.materiality,
                rule_source=rule_source,
                materiality_rule_id="m0-alignment-v1#materiality-rule",
                evidence_ids=result.evidence_ids,
                receipt_ids=result.receipt_ids,
                reason=result.reason,
                reopen_condition=result.reopen_condition,
                affected_scope=contract.flight_id,
                ruling_actor="m0-deterministic-validator",
            )
        )
    return tuple(results)
