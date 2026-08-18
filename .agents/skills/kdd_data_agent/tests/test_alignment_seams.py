"""Alignment-seam tests.

These assert the absence of work: every seam still raises, no fixture states a
readiness decision, and the run result reports `ALIGNMENT_PENDING` instead of
an outcome. If Phase A ever quietly acquires a product decision, one of these
fails.
"""

from __future__ import annotations

import pytest

from kdd_data_agent.alignment.seams import (
    ALIGNMENT_PENDING,
    AlignmentPendingError,
    AlignmentSeam,
    FrozenPacketBinding,
    SEAMS,
    require_alignment,
    seam,
    seam_ids,
)
from kdd_data_agent.runner.hermetic import decide_readiness

EXPECTED_SEAM_IDS = {
    "SEAM-M0-01-READINESS-OUTCOME",
    "SEAM-M0-02-CHECK-INVENTORY",
    "SEAM-M0-03-MATERIALITY-POLICY",
    "SEAM-M0-04-CONTRACT-FIELDS",
    "SEAM-M0-05-PACKET-FIELDS",
    "SEAM-M0-06-ACCEPTANCE-IDS",
    "SEAM-M0-07-FIRST-SCREEN",
    "SEAM-M0-08-FIXTURE-BASELINES",
    "SEAM-M0-09-OWNER-DECISIONS",
    "SEAM-M0-10-STOP-CONDITIONS",
}

CURRENT_AUTHORITY_ANCHORS = {
    "m0-alignment-v1 §5.3 Readiness outcome contract",
    "m0-alignment-v1 §5.2 Required checks",
    "m0-alignment-v1 §5.2 Required checks (Materiality rule paragraph)",
    "m0-alignment-v1 §5.1 Required input",
    "m0-alignment-v1 §5.4 M0 output and invalid-experiment behavior",
    "m0-alignment-v1 §11 Acceptance Scenarios; Implementation Sequencing — Authoritative VAL-* ownership registry",
    "m0-alignment-v1 §11 Acceptance Scenarios — VAL-UI-001 and VAL-UI-101",
    "m0-alignment-v1 §11 Acceptance Scenarios — VAL-BASE-001 and fixture controls",
    "m0-alignment-v1 §3 Canonical Flight and Decision Metric Contract; §4 Human Responsibility Contract",
    "m0-alignment-v1 §12 Stop Conditions; §9.1 Staffing and active-time budget",
}


def test_the_registered_seam_set_is_the_expected_one():
    assert set(seam_ids()) == EXPECTED_SEAM_IDS
    assert len(SEAMS) == len(EXPECTED_SEAM_IDS)


@pytest.mark.parametrize("seam_id", sorted(EXPECTED_SEAM_IDS))
def test_every_seam_still_raises(seam_id: str):
    with pytest.raises(AlignmentPendingError) as caught:
        require_alignment(seam_id)
    assert caught.value.seam.seam_id == seam_id
    assert "not implemented before alignment" in str(caught.value)


@pytest.mark.parametrize("entry", SEAMS, ids=lambda item: item.seam_id)
def test_every_seam_names_its_reason_authority_and_phase_b_unit(entry: AlignmentSeam):
    assert entry.title.strip()
    assert entry.blocked_reason.strip()
    assert entry.packet_reference.strip()
    assert entry.phase_b_unit.strip()
    assert entry.packet_reference in CURRENT_AUTHORITY_ANCHORS
    assert "draft" not in entry.packet_reference.lower()
    assert "open Owner" not in entry.packet_reference


def test_current_packet_headings_and_val_authority_are_mechanically_reachable(package_root):
    repository_root = package_root.parents[2]
    packet = (
        repository_root
        / "docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md"
    ).read_text(encoding="utf-8")
    for heading in (
        "### 5.1 Required input",
        "### 5.2 Required checks",
        "### 5.3 Readiness outcome contract",
        "### 5.4 M0 output and invalid-experiment behavior",
        "## 11. Acceptance Scenarios",
        "## 12. Stop Conditions",
    ):
        assert heading in packet
    assert "`VAL-SEC-001`" in packet


def test_security_warrants_name_current_sole_owner_val_ids(package_root):
    outcomes = (package_root / "adapters/outcomes.py").read_text(encoding="utf-8")
    identity = (package_root / "core/identity.py").read_text(encoding="utf-8")
    combined = outcomes + identity
    assert "VAL-SEC-001" in combined
    assert "M0-SEC-001" not in combined
    assert "M0-READ-001" not in combined


def test_looking_up_an_unregistered_seam_fails_loudly():
    with pytest.raises(KeyError, match="unknown alignment seam"):
        seam("SEAM-M0-99-INVENTED")


def test_the_readiness_decision_is_not_implemented():
    with pytest.raises(AlignmentPendingError, match="SEAM-M0-01-READINESS-OUTCOME"):
        decide_readiness([])


def test_a_run_reports_alignment_pending_rather_than_a_decision(frozen_run_input, adapter):
    from kdd_data_agent.runner.hermetic import run_foundation

    result = run_foundation(frozen_run_input, adapter)
    assert result.readiness is ALIGNMENT_PENDING
    assert result.to_canonical()["readiness"] is ALIGNMENT_PENDING
    assert b'"readiness":{"__kdd__":"ALIGNMENT_PENDING"}' in result.serialize()


def test_a_frozen_packet_binding_requires_a_real_digest():
    binding = FrozenPacketBinding(
        packet_path="docs/.../m0-build-alignment-packet-draft.md",
        packet_digest="sha256:" + "a" * 64,
        revision="m0-alignment-v1",
    )
    assert binding.revision == "m0-alignment-v1"

    for bad in ("", "sha256:short", "m0-alignment-v1", "sha1:" + "a" * 40):
        with pytest.raises(ValueError):
            FrozenPacketBinding(
                packet_path="p", packet_digest=bad, revision="m0-alignment-v1"
            )


def test_a_frozen_packet_binding_requires_a_path_and_revision():
    for path, revision in ((" ", "m0-alignment-v1"), ("p", " ")):
        with pytest.raises(ValueError):
            FrozenPacketBinding(
                packet_path=path, packet_digest="sha256:" + "a" * 64, revision=revision
            )


def test_the_alignment_pending_sentinel_has_no_truth_value():
    with pytest.raises(TypeError, match="no truth value"):
        bool(ALIGNMENT_PENDING)
