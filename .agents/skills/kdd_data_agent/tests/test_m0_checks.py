from __future__ import annotations

from dataclasses import replace

import pytest

from kdd_data_agent.core.identity import AuthorizationState
from kdd_data_agent.core.unknown import MISSING
from kdd_data_agent.m0.checks import (
    CHECK_REGISTRY,
    FIXED_FLOOR_CHECK_IDS,
    CheckError,
    CheckOutcome,
    CoreCheckSet,
    evaluate_checks,
)
from kdd_data_agent.m0.contracts import ArmIdentity, SufficiencyKind, SufficiencyRule
from kdd_data_agent.m0.packet import AnalysisUse, NextSafeActionKind

from ._m0_fixtures import build_contract, packet_for, reported_result, result_with_body


def _reported_with_observation(check_id, replacement):
    observations = {
        key: dict(value) if isinstance(value, dict) else value
        for key, value in reported_result().body["check_observations"].items()
    }
    observations[check_id] = replacement
    return result_with_body(check_observations=observations)


def test_frozen_registry_has_all_nineteen_checks_exactly_once_and_fixed_floor():
    assert [item.check_id for item in CHECK_REGISTRY] == [f"CHK-{index:02d}" for index in range(1, 20)]
    assert {item.check_id for item in CHECK_REGISTRY if item.core_floor} == FIXED_FLOOR_CHECK_IDS
    assert CoreCheckSet("m0-core-check-set/v1").check_ids == tuple(item.check_id for item in CHECK_REGISTRY)
    with pytest.raises(CheckError, match="fixed-floor"):
        CoreCheckSet("m0-core-check-set/v1", tuple(item.check_id for item in CHECK_REGISTRY if item.check_id != "CHK-16"))


def test_complete_fixture_is_decision_grade_and_eligible():
    packet = packet_for()
    assert packet.analysis_use is AnalysisUse.DECISION_GRADE
    assert packet.post_analysis_eligibility.value == "eligible"
    assert len(packet.checks) == 19


def test_preregistered_runtime_failure_is_directional_only():
    packet = packet_for(build_contract(observed_runtime_units=9))
    assert packet.analysis_use is AnalysisUse.DIRECTIONAL_ONLY
    assert packet.blockers == ("CHK-02",)
    assert packet.post_analysis_eligibility.value == "blocked"


def test_pre_runtime_expiry_cannot_outlive_the_preregistered_runtime_end():
    with pytest.raises(ValueError, match="expiry cannot exceed"):
        build_contract(observed_runtime_units=9, expiry="2026-08-18T00:00:00+00:00")


def test_runtime_and_sample_missing_observation_is_contract_incomplete():
    contract = build_contract(
        sufficiency_rule=SufficiencyRule(SufficiencyKind.RUNTIME_AND_SAMPLE, "sample/v1", 10, 100, ("input/v1",)),
        observed_sample_units=MISSING,
    )
    packet = packet_for(contract)
    assert packet.analysis_use is AnalysisUse.NOT_PERMITTED
    assert "CHK-19" in packet.blockers
    assert packet.next_safe_action.kind is NextSafeActionKind.CONTRACT_CORRECTION


def test_sample_insufficiency_is_directional_without_post_hoc_power():
    contract = build_contract(
        sufficiency_rule=SufficiencyRule(SufficiencyKind.RUNTIME_AND_SAMPLE, "sample/v1", 10, 100, ("input/v1",)),
        observed_sample_units=99,
    )
    packet = packet_for(contract)
    assert packet.analysis_use is AnalysisUse.DIRECTIONAL_ONLY
    assert all("power" not in str(check.to_canonical()).lower() for check in packet.checks)


def test_missing_arm_identity_is_material_and_evidence_collection():
    incomplete = ArmIdentity("control", MISSING, "alias", "acl", "pipeline")
    packet = packet_for(build_contract(arms=(incomplete,)))
    assert packet.analysis_use is AnalysisUse.NOT_PERMITTED
    assert "CHK-05" in packet.blockers
    assert packet.next_safe_action.kind is NextSafeActionKind.EVIDENCE_COLLECTION


def test_versioned_rule_alone_can_make_arm_parity_not_applicable():
    packet = packet_for(build_contract(arms=(), arm_parity_consistent=MISSING, arm_parity_applicability_rule_id="m0-alignment-v1#arm-parity-applicability"))
    check = packet.checks[4]
    assert check.outcome is CheckOutcome.NOT_APPLICABLE
    assert check.rule_source == "m0-alignment-v1#arm-parity-applicability"


def test_divergent_applicable_arms_are_a_material_failure():
    packet = packet_for(build_contract(arm_parity_consistent=False))
    assert packet.checks[4].outcome is CheckOutcome.FAIL
    assert packet.analysis_use is AnalysisUse.NOT_PERMITTED


def test_absent_validator_and_evidence_never_default_to_pass():
    checks = evaluate_checks(build_contract(), validator_results={})
    assert len(checks) == 19
    assert all(item.outcome is CheckOutcome.MISSING for item in checks)
    assert all(not item.evidence_ids for item in checks)


def test_complete_fixture_has_distinct_check_specific_evidence():
    packet = packet_for()
    evidence_ids = [item.evidence_ids[0] for item in packet.checks]
    validator_receipt_ids = [item.receipt_ids[-1] for item in packet.checks]
    assert len(evidence_ids) == len(set(evidence_ids)) == 19
    assert len(validator_receipt_ids) == len(set(validator_receipt_ids)) == 19


def test_arbitrary_present_payloads_cannot_mint_pass():
    observations = {
        item.check_id: {"validator_executed": False, "result": "FAIL", "garbage": "present"}
        for item in CHECK_REGISTRY
    }
    packet = packet_for(reported=result_with_body(check_observations=observations))
    assert all(item.outcome is not CheckOutcome.PASS for item in packet.checks)
    assert packet.analysis_use is AnalysisUse.NOT_PERMITTED


@pytest.mark.parametrize(
    "check_id,replacement",
    [
        ("CHK-01", {"flight_id": "wrong", "contract_version": "experiment-read-contract/v1"}),
        ("CHK-02", {"observed_runtime_units": 9}),
        ("CHK-03", {"metric_id": "wrong", "definition_version": "v3", "role": "decision", "policy_id": "decision-metric-policy/v1"}),
        ("CHK-04", {"assignment_unit": "user", "analysis_unit": "query", "metric_unit": "ratio", "variance_method": "delta_method/v1"}),
        ("CHK-05", {"arm_ids": ["control"], "exposure_counts": {"control": 1004000}}),
        ("CHK-06", {"observed_counts": {"control": 1004000, "treatment": 0}, "expected_proportions": {"control": 0.5, "treatment": 0.5}, "preregistered_alpha": 0.05}),
        ("CHK-07", {"population": "wrong", "eligibility": "preregistered fixture eligibility/v1", "exclusions": ["bot traffic"], "tenant_scope": "fixture-tenant", "surface": "fixture-search", "locale": "en-US"}),
        ("CHK-08", {"numerator": 128400, "denominator": 1004000, "value": 0.9, "operation": "numerator_over_denominator", "join_keys": ["query_id"], "unit": "ratio"}),
        ("CHK-09", {"page_count": 1, "expected_page_count": 2, "partial_read": True, "late_arrival_count": 0, "snapshot_id": "snap-2026-08-16-0001"}),
        ("CHK-10", {"estimator": "wrong", "variance_method": "delta_method/v1"}),
        ("CHK-11", {"reported_cuped_mode": "adjusted", "registered_cuped_mode": "unadjusted"}),
        ("CHK-12", {"source_id": "fixture-metric-store", "snapshot_id": "wrong", "source_version": "fixture-source/v1", "source_owner": "synthetic-experiment-platform-team", "metric_owner": "metric-owner"}),
        ("CHK-13", {"primary_value": 0.1278884462151394, "scorecard_value": 0.2, "unit": "ratio"}),
        ("CHK-14", {"comparison_rule_id": "wrong", "independence_class": "independent_transform"}),
        ("CHK-15", {"contract_source_version": "fixture-source/v1", "observed_source_version": "fixture-source/v2", "change_event_ids": ["change-1"]}),
        ("CHK-16", {"recipient_scope": "wrong", "retention_rule_id": "fixture-retention/v1", "load_limit_rule_id": "fixture-load/v1", "halt_rule_id": "fixture-halt/v1", "export_rule_id": "fixture-export/v1"}),
        ("CHK-17", {"source_id": "fixture-metric-store", "snapshot_id": "snap-2026-08-16-0001", "window": {"start": "2026-08-01T00:00:00+00:00", "end": "2026-08-15T00:00:00+00:00"}, "tenant_scope": "wrong"}),
        ("CHK-18", {"open_disagreement_ids": [], "open_gap_check_ids": ["CHK-06"]}),
        ("CHK-19", {"sufficiency_kind": "runtime_and_sample", "applicability_rule_id": "wrong"}),
    ],
)
def test_each_public_validator_rejects_a_semantic_contradiction(check_id, replacement):
    packet = packet_for(reported=_reported_with_observation(check_id, replacement))
    check = next(item for item in packet.checks if item.check_id == check_id)
    assert check.outcome is CheckOutcome.FAIL
    assert packet.analysis_use is AnalysisUse.NOT_PERMITTED


def test_malformed_observation_is_unknown_and_hits_the_materiality_ceiling():
    packet = packet_for(reported=_reported_with_observation("CHK-07", "malformed"))
    check = next(item for item in packet.checks if item.check_id == "CHK-07")
    assert check.outcome is CheckOutcome.UNKNOWN
    assert check.materiality.value == "unknown"
    assert packet.analysis_use is AnalysisUse.NOT_PERMITTED


def test_absent_observation_is_missing_never_pass():
    observations = dict(reported_result().body["check_observations"])
    observations.pop("CHK-08")
    packet = packet_for(reported=result_with_body(check_observations=observations))
    assert next(item for item in packet.checks if item.check_id == "CHK-08").outcome is CheckOutcome.MISSING
    assert packet.analysis_use is AnalysisUse.NOT_PERMITTED
