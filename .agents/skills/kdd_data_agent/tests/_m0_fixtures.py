"""Deterministic builders shared by the M0 acceptance tests."""

from __future__ import annotations

from dataclasses import replace
from pathlib import Path

from kdd_data_agent.adapters.base import ReadRequest
from kdd_data_agent.adapters.fixture import FixtureReadAdapter
from kdd_data_agent.core.identity import AuthorizationState, RedactionState, SourceIdentity, TimeInterval
from kdd_data_agent.core.unknown import MISSING
from kdd_data_agent.m0.contracts import (
    ArmIdentity,
    DecisionMetricPolicy,
    EvidenceClass,
    ExperimentReadContract,
    FrozenM0Binding,
    HumanRoles,
    MetricDefinition,
    MetricRole,
    QuerySuccessDefinition,
    SufficiencyKind,
    SufficiencyRule,
)
from kdd_data_agent.m0.evaluator import DecisionMetricOutput, build_recomputation_evidence, evaluate_flight

PACKAGE_ROOT = Path(__file__).resolve().parent.parent
FIXTURE_ROOT = PACKAGE_ROOT / "evals" / "fixtures" / "m0"
T0 = "2026-08-01T00:00:00+00:00"
T1 = "2026-08-15T00:00:00+00:00"


def build_contract(**overrides) -> ExperimentReadContract:
    query_success = QuerySuccessDefinition(
        "traditional-result-success/v1",
        "ai-answer-success/v1",
        "query",
        "eligible_queries",
        "flight_analysis_window",
        "query-success-overlap/v1",
        "query-success-thresholds/v1",
    )
    policy = DecisionMetricPolicy(
        "decision-metric-policy/v1", "one", "co-primary-conflict/v1", "m0-comparison-rule/v1", query_success
    )
    metric = MetricDefinition(
        "synthetic_click_through_rate", "v3", MetricRole.DECISION, "ratio", "difference_in_means",
        "fixture-source/v1", "metric-owner", "unadjusted", "delta_method/v1"
    )
    defaults = dict(
        flight_id="flight-fixture-001",
        contract_version="experiment-read-contract/v1",
        binding=FrozenM0Binding(),
        evidence_class=EvidenceClass.FIXTURE,
        metrics=(metric,),
        decision_metric_policy=policy,
        assignment_unit="user",
        analysis_unit="user",
        population="eligible fixture queries",
        eligibility="preregistered fixture eligibility/v1",
        exclusions=("bot traffic",),
        tenant_scope="fixture-tenant",
        surface="fixture-search",
        locale="en-US",
        exposure_definition="assigned and served",
        join_keys=("query_id",),
        analysis_window=TimeInterval(T0, T1),
        timezone="UTC",
        planned_runtime_units=10,
        observed_runtime_units=10,
        observed_sample_units=MISSING,
        source=SourceIdentity("fixture-metric-store", "synthetic_metric_store", "synthetic://metric-store/exp-1001/primary-read", "snap-2026-08-16-0001", "synthetic-experiment-platform-team"),
        authorization_state=AuthorizationState.AUTHORIZED,
        redaction_state=RedactionState.NOT_REQUIRED,
        recipient_scope="m0-local-review",
        retention_rule_id="fixture-retention/v1",
        load_limit_rule_id="fixture-load/v1",
        halt_rule_id="fixture-halt/v1",
        export_rule_id="fixture-export/v1",
        sufficiency_rule=SufficiencyRule(SufficiencyKind.RUNTIME_ONLY, "runtime-only/v1", 10),
        arms=(
            ArmIdentity("control", "idx-c", "alias-c", "acl-c", "pipe-c"),
            ArmIdentity("treatment", "idx-t", "alias-t", "acl-t", "pipe-t"),
        ),
        arm_parity_consistent=True,
        arm_parity_applicability_rule_id=MISSING,
        core_check_set_revision="m0-core-check-set/v1",
        roles=HumanRoles("experiment-owner", "independent-ds", "committee-route"),
        expiry=T1,
    )
    defaults.update(overrides)
    return ExperimentReadContract(**defaults)


def reported_result(case_id="m0-read-trusted-001"):
    adapter = FixtureReadAdapter(FIXTURE_ROOT)
    return adapter.read(
        ReadRequest("m0-reported-read", "fixture-metric-store", case_id)
    )


def reported_receipt():
    return reported_result().receipt


def result_with_body(**changes):
    result = reported_result()
    body = dict(result.body)
    body.update(changes)
    receipt = replace(result.receipt, body=body, receipt_id="", digest="")
    return replace(result, body=body, receipt=receipt)


def packet_for(contract=None, *, independence_class=None, disagreements=(), recomputed_output=None, reported=None):
    contract = contract or build_contract()
    if reported is None:
        base = reported_result()
        observations = {key: dict(value) for key, value in base.body["check_observations"].items()}
        observations["CHK-02"] = {"observed_runtime_units": contract.observed_runtime_units}
        if independence_class is not None:
            observations["CHK-14"] = {
                "comparison_rule_id": contract.decision_metric_policy.comparison_rule_id,
                "independence_class": independence_class.value,
            }
        if contract.sufficiency_rule.kind is SufficiencyKind.RUNTIME_AND_SAMPLE and isinstance(contract.observed_sample_units, int):
            observations["CHK-19"] = {
                "sufficiency_kind": "runtime_and_sample",
                "sample_units": contract.observed_sample_units,
                "sample_input_ids": list(contract.sufficiency_rule.sample_input_ids),
            }
        reported = result_with_body(check_observations=observations)
    kwargs = {}
    if independence_class is not None:
        kwargs["independence_class"] = independence_class
    recomputation = build_recomputation_evidence(
        contract,
        reported,
        recomputed_output=recomputed_output or DecisionMetricOutput(
            "synthetic_click_through_rate", "v3", "fixture-source/v1", "unadjusted", "ratio", 0.1278884462151394
        ),
        **kwargs,
    )
    return evaluate_flight(
        contract,
        recomputation,
        disagreements=disagreements,
    )
