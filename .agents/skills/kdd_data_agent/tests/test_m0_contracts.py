from __future__ import annotations

import dataclasses

import pytest

from kdd_data_agent.core.identity import AuthorizationState, RedactionState
from kdd_data_agent.core.unknown import MISSING
from kdd_data_agent.m0.contracts import (
    ARCHITECTURE_SHA256,
    PACKET_SHA256,
    ArmIdentity,
    ContractError,
    FrozenM0Binding,
    QuerySuccessDefinition,
    SufficiencyKind,
    SufficiencyRule,
)
from kdd_data_agent.m0.packet import AnalysisUse, PostAnalysisEligibility

from ._m0_fixtures import build_contract, packet_for


def test_contract_is_bound_to_the_exact_frozen_packet_and_architecture():
    contract = build_contract()
    assert contract.binding.packet.packet_digest == PACKET_SHA256
    assert contract.binding.architecture_digest == ARCHITECTURE_SHA256
    with pytest.raises(ContractError, match="exact frozen architecture"):
        FrozenM0Binding(architecture_digest="sha256:" + "0" * 64)


@pytest.mark.parametrize("field", ["flight_id", "assignment_unit", "analysis_unit", "population", "recipient_scope"])
def test_contract_required_fields_fail_closed(field):
    with pytest.raises((ValueError, TypeError)):
        build_contract(**{field: " "})


def test_query_success_is_an_explicit_two_component_union():
    definition = build_contract().decision_metric_policy.query_success.to_canonical()
    assert definition["formula"] == "TraditionalResultSuccess OR AIAnswerSuccess"
    assert definition["traditional_component_id"] != definition["ai_answer_component_id"]
    with pytest.raises(ContractError, match="distinct"):
        QuerySuccessDefinition("same", "same", "grain", "population", "window", "overlap/v1", "threshold/v1")


def test_sufficiency_is_preregistered_and_has_no_power_surface():
    rule = SufficiencyRule(SufficiencyKind.RUNTIME_AND_SAMPLE, "sample/v1", 10, 100, ("sample-input/v1",))
    assert rule.sample_threshold_units == 100
    assert "power" not in rule.to_canonical()
    with pytest.raises(ContractError, match="sample threshold"):
        SufficiencyRule(SufficiencyKind.RUNTIME_AND_SAMPLE, "sample/v1", 10)
    with pytest.raises(TypeError):
        SufficiencyRule(kind="runtime_only", rule_id="x/v1", runtime_threshold_units=1)


def test_authorization_and_redaction_are_independent_axes():
    contract = build_contract(authorization_state=AuthorizationState.AUTHORIZED, redaction_state=RedactionState.FAILED)
    assert contract.authorization_state is AuthorizationState.AUTHORIZED
    assert contract.redaction_state is RedactionState.FAILED
    assert packet_for(contract).analysis_use is AnalysisUse.NOT_PERMITTED


def test_packet_stores_only_analysis_use_and_derives_eligibility():
    packet = packet_for()
    canonical = packet.to_canonical()
    assert canonical["analysis_use"] == "decision_grade"
    assert "post_analysis_eligibility" not in canonical
    assert packet.post_analysis_eligibility is PostAnalysisEligibility.ELIGIBLE
    assert "post_analysis_eligibility" not in {item.name for item in dataclasses.fields(packet)}


def test_contract_and_packet_are_immutable():
    contract = build_contract()
    packet = packet_for(contract)
    with pytest.raises(dataclasses.FrozenInstanceError):
        contract.flight_id = "changed"
    with pytest.raises(dataclasses.FrozenInstanceError):
        packet.analysis_use = AnalysisUse.NOT_PERMITTED
