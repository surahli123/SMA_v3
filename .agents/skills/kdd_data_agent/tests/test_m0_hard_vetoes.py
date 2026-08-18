from __future__ import annotations

import pytest

from kdd_data_agent.m0.validation import (
    FIXTURE_MATRIX,
    HardVetoKind,
    ReviewerProvenance,
    hard_veto,
    execute_fixture_corpus,
    validate_trivial_baselines,
)
from kdd_data_agent.m0.packet import AnalysisUse

from ._m0_fixtures import build_contract, packet_for, result_with_body


def test_required_threshold_free_fixture_matrix_is_sealed_and_complete():
    scenarios = {item.scenario for item in FIXTURE_MATRIX}
    for required in ("trusted", "pre-runtime directional", "material validity failure", "materiality unknown", "conflicting reads", "stale read", "partial read", "unauthorized read", "superseded packet", "reviewer materiality conflict"):
        assert required in scenarios
    assert all(item.fixture_digest.startswith("sha256:") for item in FIXTURE_MATRIX)


def test_always_ready_and_always_blocked_are_both_contradicted():
    observed = execute_fixture_corpus(build_contract)
    assert validate_trivial_baselines(observed) == ("always_ready:contradicted", "always_blocked:contradicted")
    assert observed == {item.case_id: item.expected_analysis_use for item in FIXTURE_MATRIX}


def test_all_three_required_adversarial_decoys_are_preregistered():
    assert {item.decoy_kind for item in FIXTURE_MATRIX if item.decoy_kind} == {
        "metric_definition_version", "cuped_mode", "source_identity"
    }


@pytest.mark.parametrize(
    "changes,check_id",
    [
        ({"metric_definition_version": "decoy-version"}, "CHK-03"),
        ({"cuped_mode": "adjusted"}, "CHK-11"),
        ({"source_version": "decoy-source"}, "CHK-12"),
    ],
)
def test_each_adversarial_decoy_is_caught_by_its_exact_validator(changes, check_id):
    packet = packet_for(build_contract(), reported=result_with_body(**changes))
    assert next(item for item in packet.checks if item.check_id == check_id).outcome.value == "FAIL"
    assert packet.analysis_use is AnalysisUse.NOT_PERMITTED


def test_reviewer_provenance_requires_independence_or_disclosed_conflict():
    with pytest.raises(ValueError, match="disclosed conflict"):
        ReviewerProvenance("same", "same", "independent")
    conflict = next(item for item in FIXTURE_MATRIX if item.case_id == "m0-reviewer-conflict")
    assert conflict.provenance.independence == "conflict_disclosed"
    assert conflict.provenance.disclosed_conflict


@pytest.mark.parametrize("kind", list(HardVetoKind))
def test_each_security_or_false_readiness_condition_is_a_hard_no_go(kind):
    result = hard_veto(kind)
    assert result.no_go is True
    assert result.reasons == (kind,)


def test_no_invented_numeric_go_threshold_exists_in_validation_matrix():
    assert not any("threshold" in item.scenario.lower() for item in FIXTURE_MATRIX)
