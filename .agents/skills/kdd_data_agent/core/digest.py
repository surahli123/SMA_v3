"""Deterministic content digests for immutable revisions.

A digest is the identity of a frozen value in M0: revisions, receipts, and (in
Phase B) the sealed packet are addressed by content, not by filename or
insertion order. Digests are computed over `canonical_json` bytes only, so
digest stability is exactly canonicalization stability.

Replacement boundary: the algorithm name is carried in the digest string
(`sha256:<hex>`), so a later milestone can introduce a second algorithm without
making old digests ambiguous.
"""

from __future__ import annotations

import hashlib
import hmac
import re
from collections.abc import Iterable, Mapping
from typing import Any

from .canonical_json import canonical_encode

DIGEST_ALGORITHM = "sha256"
DIGEST_PREFIX = f"{DIGEST_ALGORITHM}:"
DIGEST_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")


class DigestError(ValueError):
    """Raised for a malformed digest string."""


def digest_bytes(data: bytes) -> str:
    """Return the prefixed digest of raw bytes."""
    return DIGEST_PREFIX + hashlib.sha256(data).hexdigest()


def content_digest(value: Any) -> str:
    """Return the prefixed digest of the canonical encoding of `value`."""
    return digest_bytes(canonical_encode(value))


def content_digest_excluding(mapping: Mapping[str, Any], exclude: Iterable[str]) -> str:
    """Digest a mapping while omitting self-referential fields.

    A record cannot contain its own digest and also hash to it, so the digest
    field (and any field derived from it) is removed before hashing.
    """
    excluded = frozenset(exclude)
    return content_digest({key: item for key, item in mapping.items() if key not in excluded})


def verify_content_digest(value: Any, expected: str) -> bool:
    """Constant-time comparison of a recomputed digest against `expected`."""
    parse_digest(expected)
    return hmac.compare_digest(content_digest(value), expected)


def parse_digest(digest: str) -> str:
    """Validate a digest string and return its hex body."""
    if not isinstance(digest, str) or not DIGEST_PATTERN.match(digest):
        raise DigestError(f"malformed digest: {digest!r}")
    return digest[len(DIGEST_PREFIX):]


def is_digest(value: object) -> bool:
    return isinstance(value, str) and bool(DIGEST_PATTERN.match(value))


def stable_id(prefix: str, value: Any, length: int = 16) -> str:
    """Derive a deterministic identifier from content.

    Random UUIDs would make replay non-deterministic, so every generated
    identifier in this package is a truncated content digest instead.
    """
    if length < 8 or length > 64:
        raise ValueError("stable_id length must be between 8 and 64 hex characters")
    if not prefix:
        raise ValueError("stable_id requires a non-empty prefix")
    return f"{prefix}-{parse_digest(content_digest(value))[:length]}"
