"""Registry of M0 behavior that depends on the frozen alignment packet.

Every entry here is a place where a competent implementer could write plausible
code today and be wrong tomorrow, because the meaning is a product decision the
Owner, Codex, and the Opus 5 reviewer have not frozen yet. Rather than pick a
default and bury it, each seam is named, given a stable id, and wired to a
callable that raises.

This is the mechanism, not a comment: `test_alignment_seams.py` asserts that
every registered seam still raises, so Phase A cannot accidentally acquire a
product decision, and Phase B has a checklist that fails until each seam is
filled against the frozen digest.

Binding procedure for Phase B: record the frozen packet path and SHA-256 in
`FrozenPacketBinding`, pass it to the unit being implemented, and remove the
seam entry in the same change that implements its behavior.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, NoReturn

from ..core.digest import DIGEST_PATTERN
from ..core.unknown import ALIGNMENT_PENDING

__all__ = [
    "ALIGNMENT_PENDING",
    "AlignmentPendingError",
    "AlignmentSeam",
    "FrozenPacketBinding",
    "SEAMS",
    "seam",
    "seam_ids",
    "require_alignment",
]


class AlignmentPendingError(RuntimeError):
    """Raised when code reaches behavior that the frozen packet must define."""

    def __init__(self, seam: "AlignmentSeam") -> None:
        self.seam = seam
        super().__init__(
            f"{seam.seam_id}: {seam.title} is not implemented before alignment. "
            f"{seam.blocked_reason} Authority: {seam.packet_reference}. Phase B unit: {seam.phase_b_unit}."
        )


@dataclass(frozen=True)
class AlignmentSeam:
    """One named decision that Phase A must not make."""

    seam_id: str
    title: str
    blocked_reason: str
    packet_reference: str
    phase_b_unit: str

    def raise_pending(self) -> NoReturn:
        raise AlignmentPendingError(self)

    def to_canonical(self) -> dict[str, Any]:
        return {
            "seam_id": self.seam_id,
            "title": self.title,
            "blocked_reason": self.blocked_reason,
            "packet_reference": self.packet_reference,
            "phase_b_unit": self.phase_b_unit,
        }


@dataclass(frozen=True)
class FrozenPacketBinding:
    """The exact frozen packet a Phase B unit was implemented against.

    A path alone is not a binding: the file can change under the same name. The
    digest is the contract, which is why it is validated here.
    """

    packet_path: str
    packet_digest: str
    revision: str

    def __post_init__(self) -> None:
        if not self.packet_path.strip():
            raise ValueError("packet_path is required")
        if not DIGEST_PATTERN.match(self.packet_digest):
            raise ValueError(
                f"packet_digest must be sha256:<64 hex>, got {self.packet_digest!r}"
            )
        if not self.revision.strip():
            raise ValueError("revision is required, e.g. m0-alignment-v1")

    def to_canonical(self) -> dict[str, Any]:
        return {
            "packet_path": self.packet_path,
            "packet_digest": self.packet_digest,
            "revision": self.revision,
        }


SEAMS: tuple[AlignmentSeam, ...] = (
    AlignmentSeam(
        seam_id="SEAM-M0-01-READINESS-OUTCOME",
        title="Final readiness outcome rules",
        blocked_reason=(
            "The frozen contract stores analysis_use and derives eligibility; implementation "
            "must preserve the three legal projections without a second stored readiness field."
        ),
        packet_reference="m0-alignment-v1 §5.3 Readiness outcome contract",
        phase_b_unit="M0-F3",
    ),
    AlignmentSeam(
        seam_id="SEAM-M0-02-CHECK-INVENTORY",
        title="Required M0 check inventory",
        blocked_reason=(
            "The frozen inventory contains exactly nineteen checks and a fixed-floor core set."
        ),
        packet_reference="m0-alignment-v1 §5.2 Required checks",
        phase_b_unit="M0-F3",
    ),
    AlignmentSeam(
        seam_id="SEAM-M0-03-MATERIALITY-POLICY",
        title="Materiality policy for checks and Coverage Gaps",
        blocked_reason=(
            "Which failures and gaps are material by product policy is an Owner decision. "
            "Coverage Gaps therefore carry materiality UNKNOWN unless a named versioned rule "
            "is supplied."
        ),
        packet_reference="m0-alignment-v1 §5.2 Required checks (Materiality rule paragraph)",
        phase_b_unit="M0-F3",
    ),
    AlignmentSeam(
        seam_id="SEAM-M0-04-CONTRACT-FIELDS",
        title="Final ExperimentReadContract field set",
        blocked_reason=(
            "The exact required/optional field set, including the directional_only permission "
            "field proposed by C2 and the flight definition, is not frozen."
        ),
        packet_reference="m0-alignment-v1 §5.1 Required input",
        phase_b_unit="M0-F1",
    ),
    AlignmentSeam(
        seam_id="SEAM-M0-05-PACKET-FIELDS",
        title="Final FlightReadinessPacket field set",
        blocked_reason=(
            "Packet content, forbidden outputs, and the typed next-safe-action kind (C4) are "
            "still under reconciliation with the architecture spec and the Owner profile."
        ),
        packet_reference="m0-alignment-v1 §5.4 M0 output and invalid-experiment behavior",
        phase_b_unit="M0-F1, M0-F4",
    ),
    AlignmentSeam(
        seam_id="SEAM-M0-06-ACCEPTANCE-IDS",
        title="Acceptance scenario identifier registry",
        blocked_reason=(
            "The packet §9 identifiers and the CE plan identifiers are the same strings for "
            "different scenarios. One registry with one meaning per id has to be chosen first."
        ),
        packet_reference="m0-alignment-v1 §11 Acceptance Scenarios; Implementation Sequencing — Authoritative VAL-* ownership registry",
        phase_b_unit="M0-F5",
    ),
    AlignmentSeam(
        seam_id="SEAM-M0-07-FIRST-SCREEN",
        title="First-screen information hierarchy and reviewer interaction",
        blocked_reason=(
            "The order in which a reviewer actually decides is an Owner question, and live "
            "review acceptance is P3-gated."
        ),
        packet_reference="m0-alignment-v1 §11 Acceptance Scenarios — VAL-UI-001 and VAL-UI-101",
        phase_b_unit="M0-F4",
    ),
    AlignmentSeam(
        seam_id="SEAM-M0-08-FIXTURE-BASELINES",
        title="M0 fixture baselines and author-independence receipt",
        blocked_reason=(
            "Trivial always-ready / always-blocked baseline arms and the fixture-author "
            "independence receipt are proposed edits (C6) that are not yet bound to the funded "
            "slice, and whether fixtures may derive from protected domain assets is an open "
            "Owner decision."
        ),
        packet_reference="m0-alignment-v1 §11 Acceptance Scenarios — VAL-BASE-001 and fixture controls",
        phase_b_unit="M0-F5",
    ),
    AlignmentSeam(
        seam_id="SEAM-M0-09-OWNER-DECISIONS",
        title="Owner decisions that change M0 semantics",
        blocked_reason=(
            "Flight definition, one-vs-co-primary decision metric, invalid-experiment fix scope, "
            "named reviewer/approver roles and overlap, and M0 sizing are all open."
        ),
        packet_reference="m0-alignment-v1 §3 Canonical Flight and Decision Metric Contract; §4 Human Responsibility Contract",
        phase_b_unit="M0-F1 through M0-F5",
    ),
    AlignmentSeam(
        seam_id="SEAM-M0-10-STOP-CONDITIONS",
        title="Deterministic stop conditions and budget cap",
        blocked_reason=(
            "The six proposed halt triggers and the budget cap (C8) require the Owner's M0 "
            "sizing answer before they can be enforced mechanically."
        ),
        packet_reference="m0-alignment-v1 §12 Stop Conditions; §9.1 Staffing and active-time budget",
        phase_b_unit="M0-F0 exit re-check, M0-F5",
    ),
)


_BY_ID = {item.seam_id: item for item in SEAMS}
if len(_BY_ID) != len(SEAMS):
    raise RuntimeError("duplicate seam_id in SEAMS")


def seam(seam_id: str) -> AlignmentSeam:
    """Look up a seam by id."""
    try:
        return _BY_ID[seam_id]
    except KeyError:
        raise KeyError(f"unknown alignment seam: {seam_id!r}") from None


def seam_ids() -> tuple[str, ...]:
    return tuple(_BY_ID)


def require_alignment(seam_id: str) -> NoReturn:
    """Stop with a typed alignment blocker naming the exact unfrozen decision."""
    seam(seam_id).raise_pending()
