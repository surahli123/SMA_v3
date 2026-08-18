"""Deterministic replay.

Identical frozen inputs must produce byte-identical serialized receipts and
identical digests. These tests also close the specific doors that would make
that false later: wall-clock reads, random identifiers, hash-seed-dependent
iteration order, and dictionary insertion order.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from kdd_data_agent.adapters.base import ReadRequest
from kdd_data_agent.adapters.fixture import FixtureReadAdapter
from kdd_data_agent.core.capabilities import Capability
from kdd_data_agent.core.canonical_json import CanonicalJSONError, canonical_encode, canonical_loads
from kdd_data_agent.core.digest import is_digest
from kdd_data_agent.runner.hermetic import (
    FoundationRunInput,
    FoundationRunResult,
    run_foundation,
    run_fixture_root,
)

FROZEN_TIMESTAMP = "2026-08-16T00:00:00+00:00"
SOURCE_ID = "fixture-metric-store"


def build_run(fixture_root: Path, case_ids: tuple[str, ...]) -> FoundationRunInput:
    return FoundationRunInput(
        run_id="m0-foundation-run-0001",
        recorded_at=FROZEN_TIMESTAMP,
        source_id=SOURCE_ID,
        case_ids=case_ids,
    )


def test_two_runs_over_identical_frozen_inputs_produce_identical_bytes(fixture_root: Path):
    case_ids = FixtureReadAdapter(fixture_root).case_ids()

    first = run_foundation(build_run(fixture_root, case_ids), FixtureReadAdapter(fixture_root))
    second = run_foundation(build_run(fixture_root, case_ids), FixtureReadAdapter(fixture_root))

    assert first.serialize() == second.serialize()
    assert first.digest() == second.digest()
    assert first.revision_log.digest() == second.revision_log.digest()
    assert first.build_receipt.digest == second.build_receipt.digest


def test_golden_foundation_run_vector_locks_all_receipt_identity_fields(fixture_root: Path):
    case_ids = FixtureReadAdapter(fixture_root).case_ids()
    result = run_foundation(build_run(fixture_root, case_ids), FixtureReadAdapter(fixture_root))
    assert len(result.serialize()) == 50174
    assert result.digest() == "sha256:97367abac41207e506b9448aed56461987a8a267cb124f20fa29a5ee3726c83b"


def test_receipt_ids_repeat_across_runs(fixture_root: Path):
    case_ids = FixtureReadAdapter(fixture_root).case_ids()
    first = run_fixture_root(build_run(fixture_root, case_ids), fixture_root)
    second = run_fixture_root(build_run(fixture_root, case_ids), fixture_root)

    assert [item.receipt.receipt_id for item in first.read_results] == [
        item.receipt.receipt_id for item in second.read_results
    ]


def test_serialized_output_round_trips_byte_identically(fixture_root: Path):
    case_ids = FixtureReadAdapter(fixture_root).case_ids()
    result = run_fixture_root(build_run(fixture_root, case_ids), fixture_root)

    serialized = result.serialize()
    assert canonical_encode(canonical_loads(serialized.decode("utf-8"))) == serialized


def test_a_different_input_produces_a_different_digest(fixture_root: Path):
    full = FixtureReadAdapter(fixture_root).case_ids()
    baseline = run_fixture_root(build_run(fixture_root, full), fixture_root)
    subset = run_fixture_root(build_run(fixture_root, full[:2]), fixture_root)

    assert baseline.digest() != subset.digest()


def test_case_order_is_taken_from_the_input_not_the_filesystem(fixture_root: Path):
    full = FixtureReadAdapter(fixture_root).case_ids()
    forward = run_fixture_root(build_run(fixture_root, full), fixture_root)
    reversed_order = run_fixture_root(build_run(fixture_root, tuple(reversed(full))), fixture_root)

    assert forward.digest() != reversed_order.digest()
    assert [item.outcome for item in reversed_order.read_results] == list(
        reversed([item.outcome for item in forward.read_results])
    )


def test_the_run_receipts_every_case_exactly_once(fixture_root: Path):
    case_ids = FixtureReadAdapter(fixture_root).case_ids()
    result = run_fixture_root(build_run(fixture_root, case_ids), fixture_root)

    assert len(result.read_results) == len(case_ids)
    # one revision per source read plus one build receipt
    assert len(result.revision_log) == len(case_ids) + 1
    assert sum(result.outcome_counts.values()) == len(case_ids)
    assert is_digest(result.digest())
    assert result.revision_log.is_sealed is True
    result.revision_log.verify_chain()


def test_completed_run_collections_are_detached_and_immutable(fixture_root: Path):
    case_ids = FixtureReadAdapter(fixture_root).case_ids()
    result = run_fixture_root(build_run(fixture_root, case_ids), fixture_root)
    original_bytes = result.serialize()
    original_digest = result.digest()

    with pytest.raises(TypeError):
        result.outcome_counts["trusted"] = 999
    with pytest.raises(AttributeError):
        result.revision_log._revisions.clear()

    assert result.serialize() == original_bytes
    assert result.digest() == original_digest


def test_completed_run_cannot_bypass_the_readiness_seam(fixture_root: Path):
    case_ids = FixtureReadAdapter(fixture_root).case_ids()
    result = run_fixture_root(build_run(fixture_root, case_ids), fixture_root)

    with pytest.raises(ValueError, match="ALIGNMENT_PENDING"):
        FoundationRunResult(
            run_input=result.run_input,
            read_results=result.read_results,
            coverage_gaps=result.coverage_gaps,
            revision_log=result.revision_log,
            build_receipt=result.build_receipt,
            readiness="ready",
            outcome_counts=result.outcome_counts,
        )


def test_foundation_result_rejects_an_unsealed_log(fixture_root: Path):
    result = run_fixture_root(build_run(fixture_root, FixtureReadAdapter(fixture_root).case_ids()), fixture_root)
    from kdd_data_agent.core.revisions import RevisionLog

    with pytest.raises(ValueError, match="sealed revision log"):
        FoundationRunResult(
            run_input=result.run_input,
            read_results=result.read_results,
            coverage_gaps=result.coverage_gaps,
            revision_log=RevisionLog(),
            build_receipt=result.build_receipt,
            outcome_counts=result.outcome_counts,
        )


def test_runner_rejects_an_adapter_result_for_a_different_request(fixture_root: Path):
    class RepeatingAdapter(FixtureReadAdapter):
        def read(self, request):
            fixed = ReadRequest(
                request_id="wrong-request",
                source_id=request.source_id,
                locator="m0-read-trusted-001",
                purpose=request.purpose,
            )
            return super().read(fixed)

    adapter = RepeatingAdapter(fixture_root)
    run_input = build_run(fixture_root, adapter.case_ids())
    with pytest.raises(ValueError, match="does not answer request"):
        run_foundation(run_input, adapter)


def test_the_build_receipt_binds_the_input_digest_and_the_log(fixture_root: Path):
    case_ids = FixtureReadAdapter(fixture_root).case_ids()
    run_input = build_run(fixture_root, case_ids)
    result = run_foundation(run_input, FixtureReadAdapter(fixture_root))

    detail = result.build_receipt.detail
    assert detail["input_digest"] == run_input.digest()
    assert detail["case_count"] == len(case_ids)
    assert detail["adapter"] == "FixtureReadAdapter"
    assert detail["effective_capabilities"] == tuple(
        sorted(capability.value for capability in Capability)
    )
    assert detail["revision_log_digest"] != result.revision_log.digest(), (
        "the build receipt digests the log as it stood before the receipt itself was appended"
    )
    assert result.build_receipt.derivation_inputs == tuple(
        item.receipt.receipt_id for item in result.read_results
    )


def test_no_hash_seed_dependent_container_can_reach_serialization():
    with pytest.raises(CanonicalJSONError, match="no canonical order"):
        canonical_encode({"ids": {"b", "a"}})
    with pytest.raises(CanonicalJSONError, match="no canonical order"):
        canonical_encode({"ids": frozenset({"b", "a"})})


def test_a_run_requires_at_least_one_case_and_a_timezone_aware_timestamp(fixture_root: Path):
    with pytest.raises(ValueError, match="at least one fixture case"):
        FoundationRunInput(
            run_id="r", recorded_at=FROZEN_TIMESTAMP, source_id=SOURCE_ID, case_ids=()
        )
    with pytest.raises(ValueError):
        FoundationRunInput(
            run_id="r",
            recorded_at="2026-08-16T00:00:00",
            source_id=SOURCE_ID,
            case_ids=("m0-read-trusted-001",),
        )
