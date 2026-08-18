"""Canonical JSON serialization for immutable M0 revisions.

Every immutable revision, receipt, and packet in M0 is identified by a content
digest. A digest only means something if the same logical value always produces
the same bytes, so serialization has to be canonical, not merely valid JSON.

Canonical form:

- UTF-8 bytes, no byte-order mark.
- Object keys sorted ascending by Unicode code point.
- No insignificant whitespace: separators are `,` and `:`.
- `NaN`, `Infinity`, and `-Infinity` are rejected rather than emitted.
- Absence sentinels are encoded under the single reserved key `__kdd__`, so
  "unknown" is never confused with `null`, `""`, or `0`.

Replacement boundary: this module is the only canonicalization seam in the
package. If a later milestone needs cross-language digest agreement, replace
this file with an RFC 8785 (JCS) implementation and re-pin the golden byte
vectors in `tests/test_canonical_json.py`. Nothing else changes.

Known deviation from RFC 8785 today: keys are sorted by Unicode code point
rather than UTF-16 code unit. The two orders agree for every key in the M0
schema boundary (ASCII identifiers); they can differ only for keys containing
characters above U+FFFF, which `require_ascii_keys` can reject outright.
"""

from __future__ import annotations

import json
import math
from collections.abc import Mapping, Sequence
from enum import Enum
from typing import Any, NoReturn

from .unknown import RESERVED_KEY, SENTINEL_NAMES, Sentinel, sentinel_from_name


class CanonicalJSONError(ValueError):
    """Raised when a value cannot be canonically serialized."""


_SEPARATORS = (",", ":")


class _NormalizedSentinel(dict[str, str]):
    """Marks sentinel objects produced by this normalizer, not application data."""


def to_canonical_value(value: Any, path: str = "$") -> Any:
    """Normalize `value` into the restricted JSON model this package allows.

    Accepted inputs: sentinels, `None`, `str`, `bool`, `int`, finite `float`,
    `Enum` (its value), any object exposing `to_canonical()`, mappings with
    string keys, and sequences. Everything else is a serialization error rather
    than a silent `str()`.
    """
    if isinstance(value, Sentinel):
        return _NormalizedSentinel({RESERVED_KEY: value.name})
    if isinstance(value, Enum):
        # Checked before `str`: the enums in this package subclass `str`, and
        # only `.value` is part of the wire format.
        return to_canonical_value(value.value, path)
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise CanonicalJSONError(f"{path}: non-finite float is not canonical")
        return value

    to_canonical = getattr(value, "to_canonical", None)
    if callable(to_canonical):
        return to_canonical_value(to_canonical(), path)

    if isinstance(value, Mapping):
        if RESERVED_KEY in value:
            # Only a sentinel object produced by this module may survive a
            # second normalization pass. A plain application mapping with the
            # same bytes must be rejected or it would decode as absence.
            if (
                isinstance(value, _NormalizedSentinel)
                and len(value) == 1
                and value[RESERVED_KEY] in SENTINEL_NAMES
            ):
                return _NormalizedSentinel({RESERVED_KEY: value[RESERVED_KEY]})
            raise CanonicalJSONError(
                f"{path}: key {RESERVED_KEY!r} is reserved for absence sentinels"
            )
        out: dict[str, Any] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise CanonicalJSONError(f"{path}: object keys must be strings, got {type(key).__name__}")
            out[key] = to_canonical_value(item, f"{path}.{key}")
        return out

    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [to_canonical_value(item, f"{path}[{index}]") for index, item in enumerate(value)]

    if isinstance(value, (set, frozenset)):
        raise CanonicalJSONError(
            f"{path}: sets have no canonical order; pass an explicitly ordered sequence"
        )

    raise CanonicalJSONError(f"{path}: {type(value).__name__} is not canonically serializable")


def canonical_dumps(value: Any) -> str:
    """Return the canonical JSON text for `value`."""
    return json.dumps(
        to_canonical_value(value),
        sort_keys=True,
        ensure_ascii=False,
        separators=_SEPARATORS,
        allow_nan=False,
    )


def canonical_encode(value: Any) -> bytes:
    """Return the canonical UTF-8 bytes for `value`. This is what gets hashed."""
    return canonical_dumps(value).encode("utf-8")


def from_canonical_value(value: Any) -> Any:
    """Rebuild sentinels from decoded JSON. Structure is otherwise unchanged."""
    if isinstance(value, dict):
        if len(value) == 1 and RESERVED_KEY in value:
            return sentinel_from_name(value[RESERVED_KEY])
        return {key: from_canonical_value(item) for key, item in value.items()}
    if isinstance(value, list):
        return [from_canonical_value(item) for item in value]
    return value


def canonical_loads(text: str) -> Any:
    """Parse canonical JSON text, restoring absence sentinels."""
    try:
        decoded = json.loads(
            text,
            object_pairs_hook=_object_without_duplicate_keys,
            parse_constant=_reject_non_finite_constant,
        )
    except CanonicalJSONError:
        raise
    return from_canonical_value(decoded)


def _object_without_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CanonicalJSONError(f"duplicate object key {key!r}")
        result[key] = value
    return result


def _reject_non_finite_constant(value: str) -> NoReturn:
    raise CanonicalJSONError(f"non-finite numeric constant {value!r} is not canonical")


def canonical_decode(data: bytes) -> Any:
    """Parse canonical JSON bytes, restoring absence sentinels."""
    return canonical_loads(data.decode("utf-8"))


def require_ascii_keys(value: Any, path: str = "$") -> None:
    """Raise unless every object key is ASCII.

    Optional guard for callers that want the code-point vs UTF-16 sort
    deviation to be structurally impossible rather than merely documented.
    """
    normalized = to_canonical_value(value, path)
    _walk_ascii(normalized, path)


def _walk_ascii(value: Any, path: str) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if not key.isascii():
                raise CanonicalJSONError(f"{path}: non-ASCII object key {key!r}")
            _walk_ascii(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _walk_ascii(item, f"{path}[{index}]")
