"""Deep immutability helpers for content-addressed records.

``dataclass(frozen=True)`` only protects top-level attributes. A nested list or
dictionary can otherwise change after its digest is computed, leaving the
record's visible content out of sync with its identity. ``deep_freeze`` makes a
detached immutable value before any digest is sealed.
"""

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import Any


def deep_freeze(value: Any) -> Any:
    """Return a recursively detached, immutable representation of ``value``."""
    if isinstance(value, Mapping):
        return MappingProxyType({key: deep_freeze(item) for key, item in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(deep_freeze(item) for item in value)
    to_canonical = getattr(value, "to_canonical", None)
    if callable(to_canonical):
        return deep_freeze(to_canonical())
    return value


__all__ = ["deep_freeze"]
