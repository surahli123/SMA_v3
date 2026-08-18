"""Receipt and Coverage Gap tests.

The load-bearing assertion here is the negative one: a Coverage Gap cannot be
called material without a named versioned rule, because M0 materiality policy
is not frozen and an engineering default would silently become product policy.
"""

from __future__ import annotations

import pytest

from kdd_data_agent.core.coverage_gap import (
    CoverageGap,
    CoverageGapKind,
    Materiality,
    MaterialityPolicyError,
    RULE_SOURCE_REGISTRY,
)
from kdd_data_agent.core.identity import (
    Actor,
    ActorKind,
    AuthorizationState,
    RedactionState,
    SourceIdentity,
    TimeInterval,
)
from kdd_data_agent.core.receipts import Receipt, ReceiptKind, record_receipt
from kdd_data_agent.core.revisions import RevisionLog
from kdd_data_agent.core.unknown import MISSING, UNKNOWN

T0 = "2026-08-16T00:00:00+00:00"
ACTOR = Actor(actor_id="test-validator", actor_kind=ActorKind.DETERMINISTIC_VALIDATOR)
SOURCE = SourceIdentity(source_id="fixture-metric-store", source_kind="synthetic_metric_store")


def make_receipt(**overrides) -> Receipt:
    defaults = dict(
        receipt_kind=ReceiptKind.SOURCE_READ,
        source=SOURCE,
        actor=ACTOR,
        authorization_state=AuthorizationState.AUTHORIZED,
        redaction_state=RedactionState.NOT_REQUIRED,
        observed_interval=TimeInterval(),
        recorded_at=T0,
        outcome="trusted",
    )
    defaults.update(overrides)
    return Receipt(**defaults)


def test_gap_defaults_to_unknown_materiality():
    gap = CoverageGap(kind=CoverageGapKind.TIMEOUT, reason="source did not respond")
    assert gap.materiality is Materiality.UNKNOWN
    assert gap.rule_source is UNKNOWN
    assert gap.next_safe_check is UNKNOWN


@pytest.mark.parametrize("materiality", [Materiality.MATERIAL, Materiality.NON_MATERIAL])
def test_classifying_materiality_without_a_named_rule_is_rejected(materiality):
    with pytest.raises(MaterialityPolicyError, match="registered"):
        CoverageGap(
            kind=CoverageGapKind.TIMEOUT,
            reason="source did not respond",
            materiality=materiality,
        )


def test_classifying_materiality_with_a_named_rule_is_accepted():
    gap = CoverageGap(
        kind=CoverageGapKind.TIMEOUT,
        reason="source did not respond",
        materiality=Materiality.MATERIAL,
        rule_source="m0-alignment-v1#materiality-rule",
    )
    assert gap.materiality is Materiality.MATERIAL


@pytest.mark.parametrize("bad", ["", "   ", "because I said so", 7, {"id": "x"}])
def test_classified_materiality_requires_a_registry_resolving_rule(bad):
    with pytest.raises(MaterialityPolicyError):
        CoverageGap(
            kind=CoverageGapKind.TIMEOUT,
            reason="source did not respond",
            materiality=Materiality.NON_MATERIAL,
            rule_source=bad,
        )


def test_rule_registry_is_explicit_versioned_and_closed():
    assert RULE_SOURCE_REGISTRY
    assert all(value.startswith("m0-alignment-v1#") for value in RULE_SOURCE_REGISTRY)


def test_gap_ids_are_content_addressed():
    first = CoverageGap(kind=CoverageGapKind.TIMEOUT, reason="same reason")
    second = CoverageGap(kind=CoverageGapKind.TIMEOUT, reason="same reason")
    third = CoverageGap(kind=CoverageGapKind.TIMEOUT, reason="different reason")
    assert first.gap_id == second.gap_id
    assert first.gap_id != third.gap_id


def test_gap_ids_are_derived_only():
    with pytest.raises(TypeError, match="gap_id"):
        CoverageGap(kind=CoverageGapKind.TIMEOUT, reason="r", gap_id="caller-chosen")


def test_gap_reason_is_required():
    with pytest.raises(ValueError, match="reason"):
        CoverageGap(kind=CoverageGapKind.TIMEOUT, reason="   ")


def test_receipt_digest_is_deterministic():
    assert make_receipt().digest == make_receipt().digest


def test_golden_receipt_content_address_locks_the_identity_vector():
    receipt = make_receipt()
    assert receipt.receipt_id == "rcpt-388e9a2561db107a"
    assert receipt.digest == "sha256:388e9a2561db107a3fe2e435a863249c7a269e79ddf6eaa3b4d4c731cd412fa0"


def test_every_receipt_identity_field_changes_the_content_address():
    baseline = make_receipt()
    variants = (
        make_receipt(receipt_kind=ReceiptKind.DERIVATION),
        make_receipt(source=SourceIdentity(source_id="other")),
        make_receipt(actor=Actor(actor_id="other", actor_kind=ActorKind.FIXTURE)),
        make_receipt(authorization_state=AuthorizationState.UNKNOWN),
        make_receipt(redaction_state=RedactionState.APPLIED),
        make_receipt(observed_interval=TimeInterval(start=T0, end=T0)),
        make_receipt(recorded_at="2026-08-16T00:00:01+00:00"),
        make_receipt(outcome="partial"),
        make_receipt(derivation_inputs=("rcpt-input",)),
        make_receipt(coverage_gaps=(CoverageGap(CoverageGapKind.TIMEOUT, "timeout"),)),
        make_receipt(detail={"key": "value"}),
        make_receipt(body={"value": 1}),
    )
    assert len({item.receipt_id for item in (baseline, *variants)}) == len(variants) + 1
    assert len({item.digest for item in (baseline, *variants)}) == len(variants) + 1


def test_receipt_identity_excludes_the_body_but_records_its_digest():
    with_body = make_receipt(body={"value": 1})
    without_body = make_receipt()

    assert with_body.has_body() is True
    assert without_body.has_body() is False
    assert without_body.body_digest() is MISSING
    assert with_body.body_digest().startswith("sha256:")
    assert with_body.digest != without_body.digest


def test_two_receipts_differing_only_in_body_have_different_digests():
    assert make_receipt(body={"value": 1}).digest != make_receipt(body={"value": 2}).digest


def test_receipt_detaches_and_deeply_freezes_nested_identity_inputs():
    detail = {"nested": {"items": [1, 2]}}
    body = {"rows": [{"metric": 1}]}
    receipt = make_receipt(detail=detail, body=body)
    original_digest = receipt.digest

    detail["nested"]["items"].append(3)
    body["rows"][0]["metric"] = 99

    assert receipt.digest == original_digest
    assert receipt.detail["nested"]["items"] == (1, 2)
    assert receipt.body["rows"][0]["metric"] == 1
    with pytest.raises(TypeError):
        receipt.detail["nested"]["new"] = "mutation"


def test_receipt_detaches_mutable_objects_exposing_to_canonical():
    class MutableRecord:
        def __init__(self):
            self.value = 1

        def to_canonical(self):
            return {"value": self.value}

    source = MutableRecord()
    receipt = make_receipt(body=source)
    original_digest = receipt.body_digest()

    source.value = 99

    assert receipt.body["value"] == 1
    assert receipt.body_digest() == original_digest


def test_source_identity_rejects_mutable_or_empty_fields():
    with pytest.raises(TypeError, match="locator"):
        SourceIdentity(source_id="source", locator=[])
    with pytest.raises(ValueError, match="owner"):
        SourceIdentity(source_id="source", owner="  ")


def test_receipt_rejects_an_empty_outcome():
    with pytest.raises(ValueError, match="outcome"):
        make_receipt(outcome="  ")


def test_receipt_body_policy_is_reachable_without_the_fixture_adapter():
    with pytest.raises(ValueError, match="explicit authorization"):
        make_receipt(body={"value": 1}, authorization_state=AuthorizationState.UNKNOWN)
    with pytest.raises(ValueError, match="redaction"):
        make_receipt(body={"value": 1}, redaction_state=RedactionState.FAILED)


def test_receipt_rejects_non_coverage_gap_entries():
    with pytest.raises(TypeError, match="CoverageGap"):
        make_receipt(coverage_gaps=({"kind": "timeout"},))


def test_recording_a_receipt_appends_one_revision():
    log = RevisionLog()
    receipt = make_receipt()
    revision = record_receipt(log, receipt)

    assert len(log) == 1
    assert revision.entity_id == receipt.receipt_id
    assert revision.entity_kind == "receipt"
    assert revision.payload["digest"] == receipt.digest
    log.verify_chain()


def test_an_identical_receipt_cannot_be_logged_as_its_own_correction():
    log = RevisionLog()
    first = make_receipt()
    record_receipt(log, first)
    with pytest.raises(Exception, match="identical payload"):
        record_receipt(log, first)
    assert len(log) == 1
