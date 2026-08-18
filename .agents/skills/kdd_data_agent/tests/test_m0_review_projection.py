from __future__ import annotations

from kdd_data_agent.m0.packet import synthetic_review_projection

from ._m0_fixtures import packet_for


def test_synthetic_projection_is_packet_centered_and_receipt_reachable():
    packet = packet_for()
    projection = synthetic_review_projection(packet)
    assert projection["scenario_id"] == "VAL-UI-001"
    assert projection["packet_digest"] == packet.packet_digest
    assert projection["source_receipt_ids"]
    assert projection["derivation_receipt_ids"]
    assert projection["check_receipt_ids"]


def test_projection_does_not_imply_production_cause_or_p3_closure():
    projection = synthetic_review_projection(packet_for())
    forbidden = {"cause", "recommendation", "candidate_diff", "win_loss", "production_capability", "committee_acceptance"}
    assert forbidden.isdisjoint(projection)
    assert projection["live_review_scenario"] == "VAL-UI-101:open_external_P3_gate"
