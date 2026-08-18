"""Receipt primitives.

A receipt is the auditable trace of one act: a source read, a derivation, an
authorization evaluation, a redaction evaluation, or a build run. Every visible
conclusion in M0 must resolve to one, so a receipt carries source identity,
authorization state, the observed interval, the exact derivation inputs, the
typed outcome, and any Coverage Gaps — before anyone decides what the outcome
means.

The outcome vocabulary lives with the layer that produces it (read outcomes in
`adapters.outcomes`). This module stores whatever typed outcome string it is
given and refuses to interpret it. Interpretation is the readiness decision,
which is an alignment seam.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Union

from .coverage_gap import CoverageGap
from .digest import content_digest, stable_id
from .identity import (
    Actor,
    AUTHORIZATION_STATES_PERMITTING_BODY,
    AuthorizationState,
    REDACTION_STATES_PERMITTING_BODY,
    RedactionState,
    SourceIdentity,
    TimeInterval,
    validate_timestamp,
)
from .immutability import deep_freeze
from .revisions import Revision, RevisionLog
from .unknown import MISSING, Sentinel, is_sentinel

MaybeStr = Union[str, Sentinel]


class ReceiptKind(str, Enum):
    """What act the receipt records."""

    SOURCE_READ = "source_read"
    DERIVATION = "derivation"
    AUTHORIZATION = "authorization"
    REDACTION = "redaction"
    BUILD = "build"


@dataclass(frozen=True)
class Receipt:
    """An immutable record of one act, addressed by content digest."""

    receipt_kind: ReceiptKind
    source: SourceIdentity
    actor: Actor
    authorization_state: AuthorizationState
    observed_interval: TimeInterval
    recorded_at: MaybeStr
    outcome: str
    redaction_state: RedactionState = RedactionState.UNKNOWN
    derivation_inputs: tuple[str, ...] = field(default_factory=tuple)
    coverage_gaps: tuple[CoverageGap, ...] = field(default_factory=tuple)
    detail: Mapping[str, Any] = field(default_factory=dict)
    body: Any = MISSING
    receipt_id: str = ""
    digest: str = ""

    def __post_init__(self) -> None:
        if not isinstance(self.receipt_kind, ReceiptKind):
            raise TypeError("receipt_kind must be a ReceiptKind")
        if not isinstance(self.source, SourceIdentity):
            raise TypeError("source must be a SourceIdentity")
        if not isinstance(self.actor, Actor):
            raise TypeError("actor must be an Actor")
        if not isinstance(self.authorization_state, AuthorizationState):
            raise TypeError("authorization_state must be an AuthorizationState")
        if not isinstance(self.observed_interval, TimeInterval):
            raise TypeError("observed_interval must be a TimeInterval")
        if not isinstance(self.outcome, str) or not self.outcome.strip():
            raise ValueError("outcome must be a non-empty typed string")
        if not isinstance(self.redaction_state, RedactionState):
            raise TypeError("redaction_state must be a RedactionState")
        validate_timestamp(self.recorded_at, "recorded_at")

        if isinstance(self.coverage_gaps, CoverageGap) or not isinstance(self.coverage_gaps, Sequence):
            raise TypeError("coverage_gaps must be a sequence of CoverageGap")
        for gap in self.coverage_gaps:
            if not isinstance(gap, CoverageGap):
                raise TypeError("coverage_gaps must contain only CoverageGap values")

        object.__setattr__(self, "derivation_inputs", tuple(self.derivation_inputs))
        object.__setattr__(self, "coverage_gaps", tuple(self.coverage_gaps))
        object.__setattr__(self, "detail", deep_freeze(self.detail))
        object.__setattr__(self, "body", deep_freeze(self.body))
        if not is_sentinel(self.body):
            if self.authorization_state not in AUTHORIZATION_STATES_PERMITTING_BODY:
                raise ValueError("a retained receipt body requires explicit authorization")
            if self.redaction_state not in REDACTION_STATES_PERMITTING_BODY:
                raise ValueError("a retained receipt body requires applied or not-required redaction")

        identity = self._identity_payload()
        object.__setattr__(self, "receipt_id", stable_id("rcpt", identity))
        object.__setattr__(self, "digest", content_digest(identity))

    def _identity_payload(self) -> dict[str, Any]:
        # Nested values are handed over un-normalized on purpose: canonical
        # serialization happens exactly once, at the top level.
        return {
            "receipt_kind": self.receipt_kind.value,
            "source": self.source,
            "actor": self.actor,
            "authorization_state": self.authorization_state.value,
            "redaction_state": self.redaction_state.value,
            "observed_interval": self.observed_interval,
            "recorded_at": self.recorded_at,
            "outcome": self.outcome,
            "derivation_inputs": list(self.derivation_inputs),
            "coverage_gaps": list(self.coverage_gaps),
            "detail": dict(self.detail),
            "body_digest": self.body_digest(),
        }

    def body_digest(self) -> Any:
        """Digest of the retained body, or the sentinel when nothing is retained.

        The body itself is never part of the receipt identity: a receipt must
        stay quotable even when policy forbids retaining what was read.
        """
        if is_sentinel(self.body):
            return self.body
        return content_digest(self.body)

    def has_body(self) -> bool:
        return not is_sentinel(self.body)

    def to_canonical(self) -> dict[str, Any]:
        record = self._identity_payload()
        record["receipt_id"] = self.receipt_id
        record["digest"] = self.digest
        return record

    def verify(self) -> None:
        """Recompute and verify the receipt's content address."""
        identity = self._identity_payload()
        if self.receipt_id != stable_id("rcpt", identity) or self.digest != content_digest(identity):
            raise ValueError(f"receipt {self.receipt_id!r} content address mismatch")


def record_receipt(
    log: RevisionLog,
    receipt: Receipt,
    *,
    entity_kind: str = "receipt",
) -> Revision:
    """Append a receipt to the append-only log as its own entity revision."""
    receipt.verify()
    return log.append(
        entity_id=receipt.receipt_id,
        entity_kind=entity_kind,
        actor=receipt.actor,
        authorization_state=receipt.authorization_state,
        recorded_at=receipt.recorded_at,
        payload=receipt.to_canonical(),
        derivation_inputs=receipt.derivation_inputs,
    )
