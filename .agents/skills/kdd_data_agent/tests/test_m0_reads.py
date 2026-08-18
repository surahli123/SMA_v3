from __future__ import annotations

from kdd_data_agent.adapters.base import ReadRequest
from kdd_data_agent.adapters.fixture import FixtureReadAdapter
from kdd_data_agent.m0.contracts import IndependenceClass
from kdd_data_agent.m0.evaluator import DecisionMetricOutput, admit_observed_evidence, build_recomputation_evidence, evaluate_flight
from kdd_data_agent.m0.packet import AnalysisUse

from ._m0_fixtures import FIXTURE_ROOT, build_contract, packet_for, reported_result


MATCHING_OUTPUT = DecisionMetricOutput(
    "synthetic_click_through_rate", "v3", "fixture-source/v1", "unadjusted", "ratio", 0.1278884462151394
)


def test_only_the_trusted_fixture_can_admit_observed_evidence():
    adapter = FixtureReadAdapter(FIXTURE_ROOT)
    admitted = {}
    for case_id in adapter.case_ids():
        result = adapter.read(ReadRequest(f"req-{case_id}", "fixture-metric-store", case_id))
        admitted[case_id] = admit_observed_evidence(result)
    assert admitted["m0-read-trusted-001"] is not None
    assert all(value is None for case_id, value in admitted.items() if case_id != "m0-read-trusted-001")


def test_reported_and_recomputed_metric_have_distinct_receipts_and_shared_snapshot_gap():
    contract = build_contract()
    evidence = build_recomputation_evidence(
        contract,
        reported_result(),
        recomputed_output=MATCHING_OUTPUT,
    )
    assert evidence.reported_receipt.receipt_id != evidence.recomputed_receipt.receipt_id
    assert evidence.recomputed_receipt.derivation_inputs[0] == evidence.reported_receipt.receipt_id
    assert evidence.shared_source_gap.kind.value == "shared_source_snapshot"
    assert evidence.independence_class is IndependenceClass.INDEPENDENT_TRANSFORM
    assert evidence.recomputed_receipt.detail["decision_bindings"] == ("D4", "D6")
    assert evidence.comparison_rule_id == contract.decision_metric_policy.comparison_rule_id


def test_same_pipeline_recomputation_is_unknown_and_fail_closed():
    packet = packet_for(independence_class=IndependenceClass.SAME_PIPELINE)
    assert packet.checks[13].outcome.value == "UNKNOWN"
    assert packet.analysis_use is AnalysisUse.NOT_PERMITTED


def test_reported_recomputation_disagreement_stays_visible_and_fail_closed():
    contract = build_contract()
    evidence = build_recomputation_evidence(
        contract,
        reported_result(),
        recomputed_output=DecisionMetricOutput(
            "synthetic_click_through_rate", "v3", "fixture-source/v1", "unadjusted", "ratio", 0.5
        ),
    )
    from kdd_data_agent.m0.evaluator import evaluate_flight

    packet = evaluate_flight(contract, evidence)
    assert packet.checks[13].outcome.value == "FAIL"
    assert packet.analysis_use is AnalysisUse.NOT_PERMITTED
    assert packet.disagreements[0]["kind"] == "reported_vs_recomputed"


def test_case_receipts_are_isolated_and_do_not_overwrite_each_other():
    adapter = FixtureReadAdapter(FIXTURE_ROOT)
    receipts = [
        adapter.read(ReadRequest(f"req-{case_id}", "fixture-metric-store", case_id)).receipt
        for case_id in adapter.case_ids()
    ]
    assert len({item.receipt_id for item in receipts}) == len(receipts)
    assert len({item.source.locator for item in receipts}) == len(receipts)


def test_actual_unauthorized_fixture_fails_closed_before_recomputation():
    contract = build_contract()
    result = reported_result("m0-read-unauthorized-001")
    evidence = build_recomputation_evidence(contract, result, recomputed_output=MATCHING_OUTPUT)
    packet = evaluate_flight(contract, evidence)
    assert evidence.admitted_reported is None
    assert packet.analysis_use is AnalysisUse.NOT_PERMITTED
    assert next(item for item in packet.checks if item.check_id == "CHK-16").outcome.value == "FAIL"


def test_recomputation_api_has_no_caller_comparison_boolean():
    assert "comparison_matches" not in build_recomputation_evidence.__code__.co_varnames
