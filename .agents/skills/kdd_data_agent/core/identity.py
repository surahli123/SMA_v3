"""Source identity, actor identity, authorization state, and time intervals.

These are the "who said it, from where, under what authority, over what
window" fields that every M0 revision and receipt must carry. They are
invariant across the open alignment decisions: whatever the final check
inventory turns out to be, a read still has a source, an actor, an
authorization state, and an observed interval.

No value here is inferred. Any field the fixture does not establish stays
`UNKNOWN` or `MISSING`.

Timestamps are inputs, never wall-clock reads. `datetime.now()` appears nowhere
in this package: a hermetic replay must produce identical bytes, and a clock
read would break that immediately.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Union

from .unknown import MISSING, UNKNOWN, Sentinel, is_sentinel

MaybeStr = Union[str, Sentinel]


class TimestampError(ValueError):
    """Raised for a timestamp that is not an explicit, timezone-aware instant."""


def validate_maybe_str(value: MaybeStr, field: str) -> MaybeStr:
    """Require a non-empty string or an explicit absence sentinel."""
    if is_sentinel(value):
        return value
    if not isinstance(value, str):
        raise TypeError(f"{field} must be a string or explicit sentinel, got {type(value).__name__}")
    if not value.strip():
        raise ValueError(f"{field} must be non-empty or an explicit sentinel")
    return value


class ActorKind(str, Enum):
    """Who produced a record. `AGENT` output never carries human authority."""

    HUMAN = "human"
    AGENT = "agent"
    DETERMINISTIC_VALIDATOR = "deterministic_validator"
    FIXTURE = "fixture"


class AuthorizationState(str, Enum):
    """Authorization status of a read or record.

    `NOT_EVALUATED` and `UNKNOWN` are distinct on purpose: the first means no
    authorization check ran, the second means one ran and could not conclude.
    Neither is a pass.
    """

    AUTHORIZED = "authorized"
    UNAUTHORIZED = "unauthorized"
    UNKNOWN = "unknown"
    NOT_EVALUATED = "not_evaluated"


class RedactionState(str, Enum):
    """Orthogonal redaction status; it never overwrites authorization."""

    NOT_REQUIRED = "not_required"
    APPLIED = "applied"
    FAILED = "failed"
    UNKNOWN = "unknown"
    NOT_EVALUATED = "not_evaluated"


AUTHORIZATION_STATES_PERMITTING_BODY = frozenset({AuthorizationState.AUTHORIZED})
REDACTION_STATES_PERMITTING_BODY = frozenset(
    {RedactionState.NOT_REQUIRED, RedactionState.APPLIED}
)
"""Only an explicit `authorized` state may carry a source body.

    Bound to packet §5.4 and the sole-owner `VAL-SEC-001` scenario. Authorization
    and redaction are evaluated independently; both must permit retention.
"""


def validate_timestamp(value: MaybeStr, field: str = "timestamp") -> MaybeStr:
    """Validate an ISO-8601 timezone-aware timestamp string, or pass a sentinel.

    A naive timestamp is rejected: without an offset, two records cannot be
    ordered or compared across sources without guessing a timezone.
    """
    if is_sentinel(value):
        return value
    if not isinstance(value, str):
        raise TimestampError(f"{field} must be an ISO-8601 string, got {type(value).__name__}")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as error:
        raise TimestampError(f"{field} is not ISO-8601: {value!r}") from error
    if parsed.tzinfo is None:
        raise TimestampError(f"{field} must carry a UTC offset: {value!r}")
    return value


def _timestamp_order_key(value: MaybeStr) -> datetime | None:
    if is_sentinel(value):
        return None
    return datetime.fromisoformat(str(value))


@dataclass(frozen=True)
class Actor:
    """The identified producer of a record."""

    actor_id: MaybeStr
    actor_kind: ActorKind

    def __post_init__(self) -> None:
        validate_maybe_str(self.actor_id, "actor_id")
        if not isinstance(self.actor_kind, ActorKind):
            raise TypeError("actor_kind must be an ActorKind")

    def to_canonical(self) -> dict[str, Any]:
        return {"actor_id": self.actor_id, "actor_kind": self.actor_kind.value}


@dataclass(frozen=True)
class SourceIdentity:
    """Where a read came from, at which snapshot, owned by whom."""

    source_id: MaybeStr
    source_kind: MaybeStr = UNKNOWN
    locator: MaybeStr = UNKNOWN
    snapshot_id: MaybeStr = UNKNOWN
    owner: MaybeStr = UNKNOWN

    def __post_init__(self) -> None:
        validate_maybe_str(self.source_id, "source_id")
        validate_maybe_str(self.source_kind, "source_kind")
        validate_maybe_str(self.locator, "locator")
        validate_maybe_str(self.snapshot_id, "snapshot_id")
        validate_maybe_str(self.owner, "owner")

    def to_canonical(self) -> dict[str, Any]:
        return {
            "source_id": self.source_id,
            "source_kind": self.source_kind,
            "locator": self.locator,
            "snapshot_id": self.snapshot_id,
            "owner": self.owner,
        }


@dataclass(frozen=True)
class TimeInterval:
    """A closed observation window. Either endpoint may be explicitly absent."""

    start: MaybeStr = UNKNOWN
    end: MaybeStr = UNKNOWN

    def __post_init__(self) -> None:
        validate_timestamp(self.start, "interval.start")
        validate_timestamp(self.end, "interval.end")
        start_key = _timestamp_order_key(self.start)
        end_key = _timestamp_order_key(self.end)
        if start_key is not None and end_key is not None and start_key > end_key:
            raise TimestampError(f"interval start {self.start!r} is after end {self.end!r}")

    def to_canonical(self) -> dict[str, Any]:
        return {"start": self.start, "end": self.end}


UNKNOWN_SOURCE = SourceIdentity(source_id=UNKNOWN)
UNKNOWN_INTERVAL = TimeInterval()

__all__ = [
    "ActorKind",
    "Actor",
    "AuthorizationState",
    "AUTHORIZATION_STATES_PERMITTING_BODY",
    "RedactionState",
    "REDACTION_STATES_PERMITTING_BODY",
    "SourceIdentity",
    "TimeInterval",
    "TimestampError",
    "UNKNOWN_INTERVAL",
    "UNKNOWN_SOURCE",
    "MISSING",
    "UNKNOWN",
    "validate_maybe_str",
    "validate_timestamp",
]
