from __future__ import annotations

from dataclasses import replace

import pytest

from kdd_data_agent.m0.packet import (
    AnalysisUse,
    FlightReadinessPacket,
    PacketAcknowledgement,
    PacketError,
    invalidate_acknowledgement,
)
from kdd_data_agent.core.canonical_json import canonical_encode, canonical_loads
from kdd_data_agent.core.digest import content_digest, stable_id

from ._m0_fixtures import build_contract, packet_for, reported_result


def _reseal_outer(document):
    identity = dict(document)
    identity.pop("packet_digest", None)
    document["packet_digest"] = content_digest(identity)
    return canonical_encode(document)


def _reseal_receipt(receipt):
    identity = dict(receipt)
    identity.pop("receipt_id", None)
    identity.pop("digest", None)
    receipt["receipt_id"] = stable_id("rcpt", identity)
    receipt["digest"] = content_digest(identity)


def _reseal_check(check):
    identity = dict(check)
    identity.pop("result_digest", None)
    check["result_digest"] = content_digest(identity)


def _reseal_gap(gap):
    identity = dict(gap)
    identity.pop("gap_id", None)
    gap["gap_id"] = stable_id("gap", identity)


def _validator_evidence_identity(check_id, receipt, admitted_evidence):
    detail = receipt["detail"]
    return content_digest({
        "check_id": check_id,
        "validator_actor": receipt["actor"],
        "validator_id": detail["validator_id"],
        "outcome": receipt["outcome"],
        "reason": detail["reason"],
        "contract_digest": detail.get("contract_digest", receipt["derivation_inputs"][1]),
        "source_receipt_id": detail.get("source_receipt_id", receipt["derivation_inputs"][0]),
        "source_body_digest": detail["source_body_digest"],
        "observation_digest": detail["observation_digest"],
        "derivation_inputs": receipt["derivation_inputs"],
        "admitted_evidence": admitted_evidence,
    })


def _validator_receipt(document, check_id):
    actor_id = f"m0-validator-{check_id.lower()}/v1"
    return next(
        receipt for receipt in document["derivation_receipts"]
        if receipt["actor"]["actor_id"] == actor_id
    )


def _replace_validator_binding(document, check, receipt):
    source_receipt_id = document["source_receipts"][0]["receipt_id"]
    check["receipt_ids"] = [source_receipt_id, receipt["receipt_id"]]
    check["evidence_ids"] = [
        _validator_evidence_identity(check["check_id"], receipt, document["admitted_evidence"])
    ]
    _reseal_check(check)
    for gap in document["coverage_gaps"]:
        if gap["reason"].startswith(f"{check['check_id']}:"):
            gap["evidence_refs"] = [source_receipt_id, receipt["receipt_id"]]
            _reseal_gap(gap)


def _reseal_all_admitted_bindings(document, evidence_id):
    for check in document["checks"]:
        receipt = _validator_receipt(document, check["check_id"])
        receipt["detail"]["admitted_evidence_id"] = evidence_id
        _reseal_receipt(receipt)
        _replace_validator_binding(document, check, receipt)


def test_packet_is_byte_stable_and_digest_bound():
    first = packet_for()
    second = packet_for()
    assert first.serialize() == second.serialize()
    assert first.packet_digest == second.packet_digest


def test_corrected_input_creates_a_new_superseding_packet_without_editing_history():
    old = packet_for()
    corrected_contract = build_contract(supersedes_digest=old.packet_digest, predecessor_digest=old.packet_digest)
    new = packet_for(corrected_contract)
    assert new.packet_digest != old.packet_digest
    assert new.supersedes_digest == old.packet_digest
    assert old.human_state.acknowledgement_state == "not_requested"
    acknowledgement = PacketAcknowledgement(old.packet_digest, "independent-ds")
    invalidated = invalidate_acknowledgement(acknowledgement, new)
    assert acknowledgement.state == "acknowledged"
    assert invalidated.state == "invalidated"
    assert invalidated.invalidated_by == new.packet_digest


def test_packet_rejects_duplicate_or_missing_checks():
    packet = packet_for()
    with pytest.raises(PacketError, match="nineteen-check"):
        replace(packet, checks=packet.checks[:-1] + (packet.checks[0],))


def test_public_reconstruction_cannot_promote_a_blocked_packet():
    packet = packet_for(build_contract(arm_parity_consistent=False))
    with pytest.raises(PacketError, match="analysis_use must be derived"):
        replace(packet, analysis_use=AnalysisUse.DECISION_GRADE)


def test_digest_valid_tampered_serialized_packet_cannot_promote_readiness():
    packet = packet_for(build_contract(arm_parity_consistent=False))
    document = dict(packet.to_canonical())
    document["analysis_use"] = "decision_grade"
    identity = dict(document)
    identity.pop("packet_digest")
    document["packet_digest"] = content_digest(identity)
    with pytest.raises(PacketError, match="analysis_use is inconsistent"):
        FlightReadinessPacket.deserialize(
            canonical_encode(document), expected_packet_digest=packet.packet_digest,
        )


def test_serialized_packet_rejects_stale_nested_check_digest_even_when_readiness_and_outer_digest_are_resealed():
    packet = packet_for(build_contract(arm_parity_consistent=False))
    document = dict(packet.to_canonical())
    checks = [dict(item) for item in document["checks"]]
    checks[4]["outcome"] = "PASS"
    document["checks"] = checks
    document["analysis_use"] = "decision_grade"
    document["blockers"] = []
    document["next_safe_action"] = {
        "kind": "evidence_collection",
        "guidance": "route the sealed packet for human review",
        "reopen_condition": "a named human reviews this exact packet digest",
    }
    with pytest.raises(PacketError, match="check result digest"):
        FlightReadinessPacket.deserialize(
            _reseal_outer(document), expected_packet_digest=packet.packet_digest,
        )


@pytest.mark.parametrize(
    "mutate,error",
    [
        (lambda doc: doc["core_check_set"].__setitem__("digest", "sha256:" + "0" * 64), "core check set digest"),
        (lambda doc: doc["contract"].__setitem__("contract_digest", "sha256:" + "0" * 64), "contract digest"),
        (lambda doc: doc["source_receipts"][0].__setitem__("receipt_id", "rcpt_" + "0" * 24), "receipt identity"),
        (lambda doc: doc["source_receipts"][0].__setitem__("digest", "sha256:" + "0" * 64), "receipt identity"),
        (lambda doc: doc["coverage_gaps"][0].__setitem__("gap_id", "gap_" + "0" * 24), "Coverage Gap identity"),
    ],
)
def test_serialized_packet_rejects_stale_nested_identities(mutate, error):
    document = canonical_loads(packet_for().serialize().decode("utf-8"))
    mutate(document)
    with pytest.raises(PacketError, match=error):
        FlightReadinessPacket.deserialize(
            _reseal_outer(document), expected_packet_digest=packet_for().packet_digest,
        )


def test_serialized_packet_rejects_resealed_noncanonical_core_inventory():
    document = canonical_loads(packet_for().serialize().decode("utf-8"))
    document["core_check_set"]["check_ids"][-1] = "CHK-18"
    core_identity = dict(document["core_check_set"])
    core_identity.pop("digest")
    document["core_check_set"]["digest"] = content_digest(core_identity)
    with pytest.raises(PacketError, match="nineteen-check inventory"):
        FlightReadinessPacket.deserialize(
            _reseal_outer(document), expected_packet_digest=packet_for().packet_digest,
        )


def test_serialized_packet_rejects_resealed_frozen_binding_tamper():
    document = canonical_loads(packet_for().serialize().decode("utf-8"))
    document["contract"]["binding"]["architecture_digest"] = "sha256:" + "0" * 64
    contract_identity = dict(document["contract"])
    contract_identity.pop("contract_digest")
    document["contract"]["contract_digest"] = content_digest(contract_identity)
    document["frozen_binding"] = document["contract"]["binding"]
    with pytest.raises(PacketError, match="frozen binding"):
        FlightReadinessPacket.deserialize(
            _reseal_outer(document), expected_packet_digest=packet_for().packet_digest,
        )


def test_serialized_packet_rejects_check_receipt_and_evidence_rebinding():
    document = canonical_loads(packet_for().serialize().decode("utf-8"))
    document["checks"][0]["receipt_ids"] = ["rcpt_missing"]
    check_identity = dict(document["checks"][0])
    check_identity.pop("result_digest")
    document["checks"][0]["result_digest"] = content_digest(check_identity)
    with pytest.raises(PacketError, match="receipt binding"):
        FlightReadinessPacket.deserialize(
            _reseal_outer(document), expected_packet_digest=packet_for().packet_digest,
        )


def test_serialized_packet_requires_out_of_band_trusted_expected_digest():
    packet = packet_for()
    with pytest.raises(PacketError, match="trusted expected packet digest is required"):
        FlightReadinessPacket.deserialize(packet.serialize())
    with pytest.raises(PacketError, match="trusted expected packet digest mismatch"):
        FlightReadinessPacket.deserialize(
            packet.serialize(), expected_packet_digest="sha256:" + "0" * 64,
        )


def test_fully_resealed_chk05_promotion_is_rejected_by_trusted_expected_digest():
    packet = packet_for(build_contract(arm_parity_consistent=False))
    document = canonical_loads(packet.serialize().decode("utf-8"))
    check = document["checks"][4]
    receipt = _validator_receipt(document, "CHK-05")
    receipt["outcome"] = "CHK-05:PASS"
    receipt["detail"]["reason"] = "CHK-05 deterministic validator passed"
    _reseal_receipt(receipt)
    check["outcome"] = "PASS"
    check["reason"] = receipt["detail"]["reason"]
    _replace_validator_binding(document, check, receipt)
    document["coverage_gaps"] = [
        gap for gap in document["coverage_gaps"]
        if not gap["reason"].startswith("CHK-05:")
    ]
    document["analysis_use"] = "decision_grade"
    document["blockers"] = []
    document["next_safe_action"] = {
        "kind": "evidence_collection",
        "guidance": "route the sealed packet for human review",
        "reopen_condition": "a named human reviews this exact packet digest",
    }
    with pytest.raises(PacketError, match="trusted expected packet digest mismatch"):
        FlightReadinessPacket.deserialize(
            _reseal_outer(document), expected_packet_digest=packet.packet_digest,
        )


def test_present_but_wrong_fully_resealed_validator_receipt_is_rejected():
    packet = packet_for(build_contract(arm_parity_consistent=False))
    document = canonical_loads(packet.serialize().decode("utf-8"))
    check = document["checks"][4]
    wrong_receipt = _validator_receipt(document, "CHK-06")
    _replace_validator_binding(document, check, wrong_receipt)
    payload = _reseal_outer(document)
    with pytest.raises(PacketError, match="validator identity"):
        FlightReadinessPacket.deserialize(
            payload,
            expected_packet_digest=document["packet_digest"],
            trusted_source_body=reported_result().body,
        )


def test_changed_authoritative_body_value_is_rejected_against_the_source_receipt():
    packet = packet_for()
    changed_body = dict(reported_result().body)
    changed_body["value"] = 0.5
    with pytest.raises(PacketError, match="source body digest"):
        FlightReadinessPacket.deserialize(
            packet.serialize(),
            expected_packet_digest=packet.packet_digest,
            trusted_source_body=changed_body,
        )


def test_stale_authoritative_body_binding_is_rejected_even_when_metric_output_matches():
    packet = packet_for()
    stale_body = dict(reported_result().body)
    stale_body["experiment_id"] = "exp-stale-source-binding"
    with pytest.raises(PacketError, match="source body digest"):
        FlightReadinessPacket.deserialize(
            packet.serialize(),
            expected_packet_digest=packet.packet_digest,
            trusted_source_body=stale_body,
        )


def test_fully_resealed_stale_admitted_source_receipt_binding_is_rejected():
    document = canonical_loads(packet_for().serialize().decode("utf-8"))
    admitted = document["admitted_evidence"]
    admitted["source_receipt_id"] = "rcpt-" + "0" * 16
    admitted["evidence_id"] = content_digest({
        "source_receipt_id": admitted["source_receipt_id"],
        "contract_digest": admitted["contract_digest"],
        "output": admitted["output"],
        "observed": admitted["observed"],
    })
    _reseal_all_admitted_bindings(document, admitted["evidence_id"])
    payload = _reseal_outer(document)
    with pytest.raises(PacketError, match="source is not admitted"):
        FlightReadinessPacket.deserialize(
            payload,
            expected_packet_digest=document["packet_digest"],
            trusted_source_body=reported_result().body,
        )


def test_admitted_packet_requires_the_out_of_band_authoritative_source_body():
    packet = packet_for()
    with pytest.raises(PacketError, match="authoritative source body is required"):
        FlightReadinessPacket.deserialize(
            packet.serialize(), expected_packet_digest=packet.packet_digest,
        )


@pytest.mark.parametrize(
    "mutate,error",
    [
        (lambda receipt: receipt["actor"].__setitem__("actor_id", "m0-validator-wrong/v1"), "validator identity"),
        (lambda receipt: receipt["detail"].__setitem__("validator_id", "m0-wrong-validator/v1"), "validator identity"),
        (lambda receipt: receipt.__setitem__("outcome", "CHK-05:PASS"), "validator outcome"),
        (lambda receipt: receipt["detail"].__setitem__("reason", "wrong reason"), "validator reason"),
        (lambda receipt: receipt["detail"].__setitem__("contract_digest", "sha256:" + "0" * 64), "validator contract"),
        (lambda receipt: receipt["detail"].__setitem__("source_receipt_id", "rcpt-" + "0" * 16), "validator source"),
        (lambda receipt: receipt["detail"].__setitem__("source_body_digest", "sha256:" + "0" * 64), "source-body"),
        (lambda receipt: receipt["derivation_inputs"].__setitem__(0, "rcpt-" + "0" * 16), "derivation inputs"),
    ],
)
def test_resealed_validator_relation_mutations_are_rejected(mutate, error):
    packet = packet_for(build_contract(arm_parity_consistent=False))
    document = canonical_loads(packet.serialize().decode("utf-8"))
    check = document["checks"][4]
    receipt = _validator_receipt(document, "CHK-05")
    mutate(receipt)
    _reseal_receipt(receipt)
    _replace_validator_binding(document, check, receipt)
    payload = _reseal_outer(document)
    with pytest.raises(PacketError, match=error):
        FlightReadinessPacket.deserialize(
            payload, expected_packet_digest=document["packet_digest"],
        )


def test_resealed_arbitrary_evidence_lineage_is_rejected():
    packet = packet_for(build_contract(arm_parity_consistent=False))
    document = canonical_loads(packet.serialize().decode("utf-8"))
    check = document["checks"][4]
    check["evidence_ids"] = [content_digest({"attacker": "arbitrary-lineage"})]
    _reseal_check(check)
    payload = _reseal_outer(document)
    with pytest.raises(PacketError, match="evidence identity"):
        FlightReadinessPacket.deserialize(
            payload, expected_packet_digest=document["packet_digest"],
        )


def test_fully_resealed_arbitrary_admitted_evidence_id_is_rejected():
    document = canonical_loads(packet_for().serialize().decode("utf-8"))
    attacker_id = content_digest({"attacker": "arbitrary-admitted-evidence"})
    _reseal_all_admitted_bindings(document, attacker_id)
    payload = _reseal_outer(document)
    with pytest.raises(PacketError, match="admitted evidence"):
        FlightReadinessPacket.deserialize(
            payload, expected_packet_digest=document["packet_digest"],
        )


def test_resealed_admitted_payload_with_stale_id_is_rejected():
    document = canonical_loads(packet_for().serialize().decode("utf-8"))
    document["admitted_evidence"]["output"]["value"] = 999
    payload = _reseal_outer(document)
    with pytest.raises(PacketError, match="admitted evidence identity"):
        FlightReadinessPacket.deserialize(
            payload, expected_packet_digest=document["packet_digest"],
        )


def test_fully_resealed_metric_value_must_match_the_authoritative_source_body():
    document = canonical_loads(packet_for().serialize().decode("utf-8"))
    admitted = document["admitted_evidence"]
    admitted["output"]["value"] = 0.5
    admitted["evidence_id"] = content_digest({
        "source_receipt_id": admitted["source_receipt_id"],
        "contract_digest": admitted["contract_digest"],
        "output": admitted["output"],
        "observed": admitted["observed"],
    })
    _reseal_all_admitted_bindings(document, admitted["evidence_id"])
    payload = _reseal_outer(document)
    with pytest.raises(PacketError, match="authoritative source body"):
        FlightReadinessPacket.deserialize(
            payload,
            expected_packet_digest=document["packet_digest"],
            trusted_source_body=reported_result().body,
        )


@pytest.mark.parametrize("mutation", ["missing", "extra"])
def test_serialized_admitted_payload_requires_exact_schema(mutation):
    document = canonical_loads(packet_for().serialize().decode("utf-8"))
    if mutation == "missing":
        document["admitted_evidence"].pop("observed")
    else:
        document["admitted_evidence"]["attacker_field"] = "not-part-of-the-schema"
    payload = _reseal_outer(document)
    with pytest.raises(PacketError, match="admitted evidence schema mismatch"):
        FlightReadinessPacket.deserialize(
            payload, expected_packet_digest=document["packet_digest"],
        )


def test_fully_resealed_admitted_payload_with_wrong_output_relation_is_rejected():
    document = canonical_loads(packet_for().serialize().decode("utf-8"))
    admitted = document["admitted_evidence"]
    admitted["output"]["metric_id"] = "attacker_metric"
    admitted["evidence_id"] = content_digest({
        "source_receipt_id": admitted["source_receipt_id"],
        "contract_digest": admitted["contract_digest"],
        "output": admitted["output"],
        "observed": admitted["observed"],
    })
    _reseal_all_admitted_bindings(document, admitted["evidence_id"])
    payload = _reseal_outer(document)
    with pytest.raises(PacketError, match="admitted evidence output"):
        FlightReadinessPacket.deserialize(
            payload, expected_packet_digest=document["packet_digest"],
        )


def test_unadmitted_packet_rejects_fully_resealed_none_to_digest_promotion():
    document = canonical_loads(packet_for(
        build_contract(), reported=reported_result("m0-read-unauthorized-001"),
    ).serialize().decode("utf-8"))
    assert document["admitted_evidence"] is None
    attacker_id = content_digest({"attacker": "forged-unadmitted-evidence"})
    _reseal_all_admitted_bindings(document, attacker_id)
    payload = _reseal_outer(document)
    with pytest.raises(PacketError, match="unadmitted evidence"):
        FlightReadinessPacket.deserialize(
            payload, expected_packet_digest=document["packet_digest"],
        )


def test_unauthorized_packet_rejects_fully_resealed_forged_admitted_payload():
    document = canonical_loads(packet_for(
        build_contract(), reported=reported_result("m0-read-unauthorized-001"),
    ).serialize().decode("utf-8"))
    source = document["source_receipts"][0]
    output = {
        "metric_id": "synthetic_click_through_rate",
        "definition_version": "v3",
        "source_version": "fixture-source/v1",
        "cuped_mode": "unadjusted",
        "unit": "ratio",
        "value": 0.1278884462151394,
    }
    admitted = {
        "source_receipt_id": source["receipt_id"],
        "contract_digest": document["contract"]["contract_digest"],
        "output": output,
        "observed": True,
    }
    admitted["evidence_id"] = content_digest(admitted)
    document["admitted_evidence"] = admitted
    _reseal_all_admitted_bindings(document, admitted["evidence_id"])
    payload = _reseal_outer(document)
    with pytest.raises(PacketError, match="admitted evidence source"):
        FlightReadinessPacket.deserialize(
            payload, expected_packet_digest=document["packet_digest"],
        )


def test_resealed_gap_must_correspond_exactly_to_its_check():
    packet = packet_for(build_contract(arm_parity_consistent=False))
    document = canonical_loads(packet.serialize().decode("utf-8"))
    gap = next(item for item in document["coverage_gaps"] if item["reason"].startswith("CHK-05:"))
    gap["reason"] = "CHK-05: attacker-rewritten gap reason"
    _reseal_gap(gap)
    payload = _reseal_outer(document)
    with pytest.raises(PacketError, match="Coverage Gap/check correspondence"):
        FlightReadinessPacket.deserialize(
            payload, expected_packet_digest=document["packet_digest"],
        )


@pytest.mark.parametrize("forbidden", ["cause_claims", "recommendations", "win_loss_label", "candidate_diff", "m1_output", "m2_output"])
def test_packet_has_no_m1_m2_or_automation_contamination_surface(forbidden):
    packet = packet_for()
    assert forbidden not in packet.to_canonical()
    with pytest.raises(TypeError):
        FlightReadinessPacket(**(packet.__dict__ | {forbidden: "forbidden"}))


def test_unresolved_named_reviewer_conflict_remains_visible_and_blocked():
    disagreement = ({"reviewer": "reviewer-a", "position": "material"}, {"reviewer": "reviewer-b", "position": "non_material"})
    packet = packet_for(disagreements=disagreement)
    assert packet.analysis_use is AnalysisUse.NOT_PERMITTED
    assert tuple(item["reviewer"] for item in packet.disagreements) == ("reviewer-a", "reviewer-b")
