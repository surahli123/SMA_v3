"""Explicit absence sentinels.

M0 must preserve "we do not know" rather than guess. Python's `None` cannot
carry that meaning safely: it is already used for "this field is legitimately
null", it is falsy, and it disappears into default branches. So unknown state
gets its own singleton type.

Three sentinels exist:

- `UNKNOWN`  - the value may exist but this slice has not established it.
- `MISSING`  - the value is absent from the source or was never provided.
- `ALIGNMENT_PENDING` - the value is a product decision owned by the frozen M0
  Build Alignment Packet and must not be computed before Phase B.

`__bool__` deliberately raises. Any `if value:` written against a sentinel is a
silent guess, so the sentinel turns it into a loud failure at the exact line
that tried to guess.
"""

from __future__ import annotations

RESERVED_KEY = "__kdd__"
"""Reserved object key used to encode sentinels in canonical JSON.

Application payloads may not use this key; canonical serialization rejects it.
"""


class SentinelTruthError(TypeError):
    """Raised when code asks a sentinel for a truth value."""


class UnknownValueError(ValueError):
    """Raised when a known value is required but a sentinel was supplied."""


class Sentinel:
    """A named singleton standing for an explicitly absent value."""

    __slots__ = ("_name",)
    _registry: dict[str, "Sentinel"] = {}

    def __init__(self, name: str) -> None:
        if name in Sentinel._registry:
            raise ValueError(f"sentinel already defined: {name}")
        self._name = name
        Sentinel._registry[name] = self

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f"<{self._name}>"

    def __bool__(self) -> bool:
        raise SentinelTruthError(
            f"{self._name} has no truth value; handle it explicitly "
            "(compare with `is`) instead of relying on truthiness"
        )

    def __reduce__(self):  # keeps the singleton identity across copy/pickle
        return (sentinel_from_name, (self._name,))


UNKNOWN = Sentinel("UNKNOWN")
MISSING = Sentinel("MISSING")
ALIGNMENT_PENDING = Sentinel("ALIGNMENT_PENDING")

SENTINEL_NAMES = ("UNKNOWN", "MISSING", "ALIGNMENT_PENDING")


def sentinel_from_name(name: str) -> Sentinel:
    """Return the singleton for `name`, or raise for an unregistered name."""
    try:
        return Sentinel._registry[name]
    except KeyError:
        raise ValueError(f"unknown sentinel: {name!r}") from None


def is_sentinel(value: object) -> bool:
    return isinstance(value, Sentinel)


def is_known(value: object) -> bool:
    """True when `value` carries an established value rather than absence."""
    return not isinstance(value, Sentinel)


def require_known(value: object, field: str) -> object:
    """Return `value`, or raise when it is an absence sentinel.

    Used at the boundary where a downstream computation genuinely cannot
    proceed without the value. It never substitutes a default.
    """
    if isinstance(value, Sentinel):
        raise UnknownValueError(f"{field} is {value.name}; M0 must not infer it")
    return value
