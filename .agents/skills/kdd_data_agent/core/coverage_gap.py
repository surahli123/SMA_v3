"""Coverage Gaps: recorded absence of authority, source, or coverage.

Canonical rule this encodes (P1, `freeze-canonical-domain-policy-contracts.md`):
absence, timeout, and no-authority are Coverage Gaps, never negative evidence.
A gap says "this was not established", not "this is false".

What this module deliberately does NOT decide: whether a given gap is material.
Materiality policy is one of the open M0 alignment decisions, so `Materiality`
defaults to `UNKNOWN` and a classified materiality is only accepted together
with a named, versioned `rule_source`. That makes an invented policy fail at
construction time instead of quietly shipping.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Union

from .digest import stable_id
from .unknown import UNKNOWN, Sentinel, is_sentinel

MaybeStr = Union[str, Sentinel]


class CoverageGapKind(str, Enum):
    """Typed representation; the versioned registry below is authoritative."""

    MISSING_AUTHORITY = "missing_authority"
    UNAVAILABLE_SOURCE = "unavailable_source"
    TIMEOUT = "timeout"
    UNKNOWN_MAPPING = "unknown_mapping"
    UNCHECKED_PLANE = "unchecked_plane"
    SHARED_SOURCE_SNAPSHOT = "shared_source_snapshot"


COVERAGE_GAP_REGISTRY_VERSION = "m0-alignment-v1#coverage-gap-registry"
COVERAGE_GAP_KIND_REGISTRY = {
    item.value: item
    for item in (
        CoverageGapKind.MISSING_AUTHORITY,
        CoverageGapKind.UNAVAILABLE_SOURCE,
        CoverageGapKind.TIMEOUT,
        CoverageGapKind.UNKNOWN_MAPPING,
        CoverageGapKind.UNCHECKED_PLANE,
        CoverageGapKind.SHARED_SOURCE_SNAPSHOT,
    )
}
"""Closed registry from the canonical five plus packet §5.2's named shared-snapshot gap."""


def resolve_coverage_gap_kind(value: str) -> CoverageGapKind:
    if not isinstance(value, str):
        raise TypeError("coverage gap kind must be a string")
    try:
        return COVERAGE_GAP_KIND_REGISTRY[value]
    except KeyError:
        raise ValueError(
            f"coverage gap kind {value!r} is not registered in {COVERAGE_GAP_REGISTRY_VERSION}"
        ) from None


class Materiality(str, Enum):
    """Whether a gap blocks a decision. `UNKNOWN` until a named rule says."""

    MATERIAL = "material"
    NON_MATERIAL = "non_material"
    UNKNOWN = "unknown"


class MaterialityPolicyError(ValueError):
    """Raised when a gap is classified without a named versioned rule."""


RULE_REGISTRY_VERSION = "m0-alignment-v1#rule-registry"
RULE_SOURCE_REGISTRY = frozenset(
    {
        "m0-alignment-v1#materiality-rule",
        "m0-alignment-v1#always-material-fields",
        "m0-alignment-v1#runtime-only-applicability",
        "m0-alignment-v1#arm-parity-applicability",
        "m0-alignment-v1#check-outcome-applicability",
        *(f"m0-alignment-v1#CHK-{index:02d}" for index in range(1, 20)),
    }
)


def require_registered_rule_source(value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise MaterialityPolicyError("rule_source must be a non-empty registered string")
    if value not in RULE_SOURCE_REGISTRY:
        raise MaterialityPolicyError(
            f"rule_source {value!r} does not resolve in {RULE_REGISTRY_VERSION}"
        )
    return value


@dataclass(frozen=True)
class CoverageGap:
    """One recorded absence, with the next safe check that would close it."""

    kind: CoverageGapKind
    reason: str
    next_safe_check: MaybeStr = UNKNOWN
    materiality: Materiality = Materiality.UNKNOWN
    rule_source: MaybeStr = UNKNOWN
    evidence_refs: tuple[str, ...] = field(default_factory=tuple)
    gap_id: str = field(init=False)

    def __post_init__(self) -> None:
        if not isinstance(self.kind, CoverageGapKind):
            raise TypeError("kind must be a CoverageGapKind")
        if not isinstance(self.materiality, Materiality):
            raise TypeError("materiality must be a Materiality")
        if not isinstance(self.reason, str) or not self.reason.strip():
            raise ValueError("reason must be a non-empty string")
        if self.kind.value not in COVERAGE_GAP_KIND_REGISTRY:
            raise ValueError(f"kind {self.kind.value!r} is outside {COVERAGE_GAP_REGISTRY_VERSION}")
        if self.materiality is not Materiality.UNKNOWN:
            require_registered_rule_source(self.rule_source)
        object.__setattr__(self, "evidence_refs", tuple(self.evidence_refs))
        object.__setattr__(self, "gap_id", stable_id("gap", self._identity_payload()))

    def _identity_payload(self) -> dict[str, Any]:
        return {
            "kind": self.kind.value,
            "reason": self.reason,
            "next_safe_check": self.next_safe_check,
            "materiality": self.materiality.value,
            "rule_source": self.rule_source,
            "evidence_refs": list(self.evidence_refs),
        }

    def to_canonical(self) -> dict[str, Any]:
        payload = self._identity_payload()
        payload["gap_id"] = self.gap_id
        return payload
