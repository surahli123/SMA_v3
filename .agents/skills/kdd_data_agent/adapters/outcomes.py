"""Typed read outcomes.

These eight outcomes are the vocabulary M0 needs to describe what a read
actually produced, and they are invariant across the open alignment decisions:
whatever the frozen packet decides about readiness, a read that hit an ACL wall
is still `unauthorized` and a read that returned half a window is still
`partial`.

What is deliberately absent: any mapping from an outcome to a readiness
decision. `trusted` does not mean ready, and `stale` does not mean blocked.
That mapping is `SEAM-M0-01-READINESS-OUTCOME`.
"""

from __future__ import annotations

from enum import Enum

from ..core.coverage_gap import CoverageGapKind


class ReadOutcome(str, Enum):
    """What happened when a source was read."""

    TRUSTED = "trusted"
    BLOCKED = "blocked"
    PARTIAL = "partial"
    STALE = "stale"
    CONFLICTING = "conflicting"
    UNAUTHORIZED = "unauthorized"
    UNAVAILABLE = "unavailable"
    REDACTION_FAILURE = "redaction_failure"


OUTCOMES_WITHOUT_RETAINED_BODY = frozenset(
    {
        ReadOutcome.BLOCKED,
        ReadOutcome.UNAUTHORIZED,
        ReadOutcome.UNAVAILABLE,
        ReadOutcome.REDACTION_FAILURE,
    }
)
"""Outcomes where no source body may be retained or rendered.

Security invariant bound to packet §5.4 and sole-owner scenario `VAL-SEC-001`.
The typed receipt still exists; only the body is gone.
"""

OUTCOMES_REQUIRING_COVERAGE_GAP = frozenset(
    {
        ReadOutcome.BLOCKED,
        ReadOutcome.PARTIAL,
        ReadOutcome.STALE,
        ReadOutcome.CONFLICTING,
        ReadOutcome.UNAUTHORIZED,
        ReadOutcome.UNAVAILABLE,
        ReadOutcome.REDACTION_FAILURE,
    }
)
"""Every non-trusted outcome must record why coverage is incomplete.

This encodes the P1 rule that absence, timeout, and no-authority produce a
Coverage Gap rather than negative evidence. It records the gap; it does not
classify its materiality.
"""

DEFAULT_GAP_KIND_BY_OUTCOME: dict[ReadOutcome, CoverageGapKind] = {
    ReadOutcome.BLOCKED: CoverageGapKind.UNCHECKED_PLANE,
    ReadOutcome.PARTIAL: CoverageGapKind.UNCHECKED_PLANE,
    ReadOutcome.STALE: CoverageGapKind.UNCHECKED_PLANE,
    ReadOutcome.CONFLICTING: CoverageGapKind.UNKNOWN_MAPPING,
    ReadOutcome.UNAUTHORIZED: CoverageGapKind.MISSING_AUTHORITY,
    ReadOutcome.UNAVAILABLE: CoverageGapKind.UNAVAILABLE_SOURCE,
    ReadOutcome.REDACTION_FAILURE: CoverageGapKind.UNCHECKED_PLANE,
}
"""Gap kind implied by an outcome when the fixture does not state one.

This is a classification of the same fact in two vocabularies, not an inferred
judgement: an `unavailable` read is an unavailable source by definition.
"""


def parse_read_outcome(value: str) -> ReadOutcome:
    """Parse a declared outcome string, failing closed on an unknown value.

    No alias handling and no default branch: an unrecognised outcome is an
    error, because guessing one here is exactly how a fail-closed default gets
    bypassed.
    """
    if not isinstance(value, str):
        raise TypeError(f"read outcome must be a string, got {type(value).__name__}")
    try:
        return ReadOutcome(value)
    except ValueError:
        allowed = ", ".join(item.value for item in ReadOutcome)
        raise ValueError(f"unknown read outcome {value!r}; allowed: {allowed}") from None
