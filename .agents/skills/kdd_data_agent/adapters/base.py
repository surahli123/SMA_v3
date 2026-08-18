"""The read-adapter interface.

One method, `read`, returning a typed `ReadResult` that always carries a
receipt. There is no `write`, no `publish`, no `execute`, and no way to add one
without also adding a capability that does not exist in
`core.capabilities.Capability`.

The interface is the replacement seam for sources: a P2-authorized production
adapter would implement this same protocol, which is why the interface carries
authorization state and Coverage Gaps rather than assuming a happy fixture.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Union

from ..core.capabilities import Capability, assert_capabilities
from ..core.coverage_gap import CoverageGap
from ..core.digest import content_digest
from ..core.identity import TimeInterval
from ..core.immutability import deep_freeze
from ..core.receipts import Receipt
from ..core.unknown import MISSING, UNKNOWN, Sentinel, is_sentinel
from .outcomes import OUTCOMES_WITHOUT_RETAINED_BODY, ReadOutcome

MaybeStr = Union[str, Sentinel]


class ReadPolicyError(RuntimeError):
    """Raised when a read result violates a read-layer invariant."""


@dataclass(frozen=True)
class ReadRequest:
    """What was asked for. Frozen so the request itself is digestible."""

    request_id: str
    source_id: str
    locator: MaybeStr = UNKNOWN
    requested_interval: TimeInterval = field(default_factory=TimeInterval)
    requested_fields: tuple[str, ...] = field(default_factory=tuple)
    purpose: MaybeStr = UNKNOWN

    def __post_init__(self) -> None:
        if not isinstance(self.request_id, str) or not self.request_id.strip():
            raise ValueError("request_id must be a non-empty string")
        if not isinstance(self.source_id, str) or not self.source_id.strip():
            raise ValueError("source_id must be a non-empty string")
        if not isinstance(self.requested_interval, TimeInterval):
            raise TypeError("requested_interval must be a TimeInterval")
        object.__setattr__(self, "requested_fields", tuple(self.requested_fields))

    def to_canonical(self) -> dict[str, Any]:
        return {
            "request_id": self.request_id,
            "source_id": self.source_id,
            "locator": self.locator,
            "requested_interval": self.requested_interval.to_canonical(),
            "requested_fields": list(self.requested_fields),
            "purpose": self.purpose,
        }


@dataclass(frozen=True)
class ReadResult:
    """A typed read outcome plus the receipt that proves it."""

    request: ReadRequest
    outcome: ReadOutcome
    receipt: Receipt
    body: Any = MISSING
    coverage_gaps: tuple[CoverageGap, ...] = field(default_factory=tuple)
    disagreements: tuple[dict[str, Any], ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if not isinstance(self.request, ReadRequest):
            raise TypeError("request must be a ReadRequest")
        if not isinstance(self.outcome, ReadOutcome):
            raise TypeError("outcome must be a ReadOutcome")
        if not isinstance(self.receipt, Receipt):
            raise TypeError("receipt must be a Receipt")
        object.__setattr__(self, "body", deep_freeze(self.body))
        object.__setattr__(self, "coverage_gaps", tuple(self.coverage_gaps))
        object.__setattr__(self, "disagreements", deep_freeze(self.disagreements))
        if self.outcome in OUTCOMES_WITHOUT_RETAINED_BODY and not is_sentinel(self.body):
            raise ReadPolicyError(
                f"outcome {self.outcome.value} must not retain a source body"
            )
        if self.receipt.outcome != self.outcome.value:
            raise ReadPolicyError("read outcome must match the proving receipt")
        receipt_request = self.receipt.detail.get("request")
        if receipt_request is None or content_digest(receipt_request) != content_digest(
            self.request.to_canonical()
        ):
            raise ReadPolicyError("read request must match the proving receipt")
        if self.receipt.coverage_gaps != self.coverage_gaps:
            raise ReadPolicyError("read Coverage Gaps must match the proving receipt")
        if is_sentinel(self.body):
            if self.receipt.body_digest() is not self.body:
                raise ReadPolicyError("read body absence must match the proving receipt")
        elif self.receipt.body_digest() != content_digest(self.body):
            raise ReadPolicyError("read body digest must match the proving receipt")

    def has_body(self) -> bool:
        return not is_sentinel(self.body)

    def to_canonical(self) -> dict[str, Any]:
        return {
            "request": self.request.to_canonical(),
            "outcome": self.outcome.value,
            "receipt": self.receipt.to_canonical(),
            "body": self.body,
            "coverage_gaps": [gap.to_canonical() for gap in self.coverage_gaps],
            "disagreements": list(self.disagreements),
        }


class ReadAdapter:
    """Base class for every M0 read adapter.

    Subclasses declare their capabilities, which are checked against the
    positive allowlist at construction. A subclass that needs network or
    credentials has no capability to declare, so it cannot be built.
    """

    capabilities: frozenset[Capability] = frozenset()

    def __init__(self) -> None:
        assert_capabilities(self.capabilities, type(self).__name__)

    def read(self, request: ReadRequest) -> ReadResult:
        raise NotImplementedError("read adapters must implement read()")
