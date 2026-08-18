from __future__ import annotations

import hashlib

from kdd_data_agent.m0.packet import FlightReadinessPacket
from kdd_data_agent.m0.evaluator import (
    DecisionMetricOutput,
    EvaluationHardVeto,
    build_recomputation_evidence,
    evaluate_flight,
)

from ._m0_fixtures import build_contract, packet_for, reported_result
from .canonical_packet_builder import canonical_packet_evidence


def test_named_canonical_builder_reports_both_digest_namespaces_truthfully():
    packet = packet_for()
    evidence = canonical_packet_evidence()
    assert evidence["serialized_byte_count"] == len(packet.serialize())
    assert evidence["serialized_byte_sha256"] == hashlib.sha256(packet.serialize()).hexdigest()
    assert evidence["internal_content_digest"] == packet.packet_digest
    assert evidence["serialized_byte_sha256"] != evidence["internal_content_digest"]


def test_verified_deserialization_round_trips_the_canonical_document():
    packet = packet_for()
    assert FlightReadinessPacket.deserialize(
        packet.serialize(),
        expected_packet_digest=packet.packet_digest,
        trusted_source_body=reported_result().body,
    )["packet_digest"] == packet.packet_digest


def test_hard_veto_packet_preserves_the_typed_serialized_relation_graph():
    contract = build_contract()
    recomputation = build_recomputation_evidence(
        contract,
        reported_result(),
        recomputed_output=DecisionMetricOutput(
            "synthetic_click_through_rate", "v3", "fixture-source/v1",
            "unadjusted", "ratio", 0.1278884462151394,
        ),
    )
    packet = evaluate_flight(
        contract, recomputation,
        hard_vetoes=(EvaluationHardVeto.FALSE_READINESS,),
    )
    document = FlightReadinessPacket.deserialize(
        packet.serialize(),
        expected_packet_digest=packet.packet_digest,
        trusted_source_body=reported_result().body,
    )
    assert document["analysis_use"] == "not_permitted"
    assert document["blockers"] == ("CHK-16",)
