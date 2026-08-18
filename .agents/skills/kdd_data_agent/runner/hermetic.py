"""Hermetic foundation runner.

Runs the whole Phase A path end to end: frozen input, fixture reads, typed
receipts, append-only log, build receipt. Everything it needs is passed in —
fixture root, run id, timestamp, actor — so two runs over identical frozen
inputs produce identical bytes. There is no clock read, no random id, no
environment lookup, and no ordering that depends on filesystem iteration.

Where it stops matters as much as what it does. The run reports a readiness of
`ALIGNMENT_PENDING`, not a decision, and `decide_readiness()` raises. Readiness
is the frozen packet's to define.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, NoReturn

from ..adapters.base import ReadRequest, ReadResult
from ..adapters.fixture import FixtureReadAdapter
from ..alignment.seams import ALIGNMENT_PENDING, require_alignment
from ..core.canonical_json import canonical_encode
from ..core.capabilities import Capability, assert_capabilities
from ..core.coverage_gap import CoverageGap
from ..core.digest import content_digest
from ..core.identity import (
    Actor,
    ActorKind,
    AuthorizationState,
    SourceIdentity,
    TimeInterval,
    validate_timestamp,
)
from ..core.immutability import deep_freeze
from ..core.receipts import Receipt, ReceiptKind, record_receipt
from ..core.revisions import RevisionLog

RUN_SCHEMA_VERSION = "m0-foundation-run/v0"

RUNNER_CAPABILITIES = frozenset(
    {Capability.LOCAL_DETERMINISTIC_COMPUTE, Capability.IN_MEMORY_APPEND}
)

RUNNER_ACTOR = Actor(
    actor_id="m0-hermetic-foundation-runner",
    actor_kind=ActorKind.DETERMINISTIC_VALIDATOR,
)


@dataclass(frozen=True)
class FoundationRunInput:
    """The complete frozen input to one foundation run."""

    run_id: str
    recorded_at: str
    source_id: str
    case_ids: tuple[str, ...]
    purpose: str = "m0-pre-alignment-foundation"

    def __post_init__(self) -> None:
        if not self.run_id.strip():
            raise ValueError("run_id is required")
        if not self.source_id.strip():
            raise ValueError("source_id is required")
        validate_timestamp(self.recorded_at, "run recorded_at")
        if not self.case_ids:
            raise ValueError("a run must read at least one fixture case")
        object.__setattr__(self, "case_ids", tuple(self.case_ids))

    def to_canonical(self) -> dict[str, Any]:
        return {
            "schema_version": RUN_SCHEMA_VERSION,
            "run_id": self.run_id,
            "recorded_at": self.recorded_at,
            "source_id": self.source_id,
            "case_ids": list(self.case_ids),
            "purpose": self.purpose,
        }

    def digest(self) -> str:
        return content_digest(self.to_canonical())


@dataclass(frozen=True)
class FoundationRunResult:
    """The output of one foundation run, addressed by content digest."""

    run_input: FoundationRunInput
    read_results: tuple[ReadResult, ...]
    coverage_gaps: tuple[CoverageGap, ...]
    revision_log: RevisionLog
    build_receipt: Receipt
    readiness: Any = ALIGNMENT_PENDING
    outcome_counts: Mapping[str, int] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.readiness is not ALIGNMENT_PENDING:
            raise ValueError("readiness must remain ALIGNMENT_PENDING until SEAM-M0-01 is frozen")
        if not self.revision_log.is_sealed:
            raise ValueError("a foundation result requires a sealed revision log")
        object.__setattr__(self, "read_results", tuple(self.read_results))
        object.__setattr__(self, "coverage_gaps", tuple(self.coverage_gaps))
        object.__setattr__(self, "outcome_counts", deep_freeze(self.outcome_counts))

    def to_canonical(self) -> dict[str, Any]:
        return {
            "schema_version": RUN_SCHEMA_VERSION,
            "run_input": self.run_input.to_canonical(),
            "input_digest": self.run_input.digest(),
            "read_results": [result.to_canonical() for result in self.read_results],
            "coverage_gaps": [gap.to_canonical() for gap in self.coverage_gaps],
            "outcome_counts": dict(sorted(self.outcome_counts.items())),
            "revision_log": self.revision_log.to_canonical(),
            "revision_log_digest": self.revision_log.digest(),
            "build_receipt": self.build_receipt.to_canonical(),
            "readiness": self.readiness,
        }

    def serialize(self) -> bytes:
        """Canonical bytes for the whole run. This is what replay compares."""
        return canonical_encode(self.to_canonical())

    def digest(self) -> str:
        return content_digest(self.to_canonical())


def run_foundation(run_input: FoundationRunInput, adapter: FixtureReadAdapter) -> FoundationRunResult:
    """Read every case in `run_input`, receipt it, and seal a build receipt."""
    assert_capabilities(RUNNER_CAPABILITIES, "FoundationRunner")
    log = RevisionLog()
    results: list[ReadResult] = []
    gaps: list[CoverageGap] = []
    counts: dict[str, int] = {}
    seen_receipt_ids: set[str] = set()

    for index, case_id in enumerate(run_input.case_ids):
        request = ReadRequest(
            request_id=f"{run_input.run_id}-req-{index:03d}",
            source_id=run_input.source_id,
            locator=case_id,
            purpose=run_input.purpose,
        )
        result = adapter.read(request)
        if result.request != request:
            raise ValueError(f"adapter result does not answer request {request.request_id!r}")
        if result.receipt.receipt_id in seen_receipt_ids:
            raise ValueError(f"adapter repeated receipt {result.receipt.receipt_id!r}")
        seen_receipt_ids.add(result.receipt.receipt_id)
        record_receipt(log, result.receipt, entity_kind="source_read_receipt")
        results.append(result)
        gaps.extend(result.coverage_gaps)
        counts[result.outcome.value] = counts.get(result.outcome.value, 0) + 1

    log.verify_chain()

    build_receipt = Receipt(
        receipt_kind=ReceiptKind.BUILD,
        source=SourceIdentity(
            source_id=run_input.source_id,
            source_kind="local_fixture_directory",
            locator=str(adapter.root.name),
            snapshot_id=run_input.run_id,
            owner="m0-foundation",
        ),
        actor=RUNNER_ACTOR,
        authorization_state=AuthorizationState.NOT_EVALUATED,
        observed_interval=TimeInterval(),
        recorded_at=run_input.recorded_at,
        outcome="foundation_run_complete",
        derivation_inputs=tuple(result.receipt.receipt_id for result in results),
        detail={
            "adapter": type(adapter).__name__,
            "effective_capabilities": sorted(
                capability.value for capability in RUNNER_CAPABILITIES | adapter.capabilities
            ),
            "input_digest": run_input.digest(),
            "case_count": len(results),
            "outcome_counts": dict(sorted(counts.items())),
            "coverage_gap_count": len(gaps),
            "revision_log_digest": log.digest(),
            "readiness": ALIGNMENT_PENDING,
        },
    )
    record_receipt(log, build_receipt, entity_kind="build_receipt")
    log.seal()

    return FoundationRunResult(
        run_input=run_input,
        read_results=tuple(results),
        coverage_gaps=tuple(gaps),
        revision_log=log,
        build_receipt=build_receipt,
        outcome_counts=counts,
    )


def run_fixture_root(
    run_input: FoundationRunInput,
    fixture_root: Path,
) -> FoundationRunResult:
    """Convenience entry point: build the adapter and run."""
    return run_foundation(run_input, FixtureReadAdapter(fixture_root))


def decide_readiness(_results: Sequence[ReadResult]) -> NoReturn:
    """Blocked: the readiness decision belongs to the frozen alignment packet."""
    require_alignment("SEAM-M0-01-READINESS-OUTCOME")
