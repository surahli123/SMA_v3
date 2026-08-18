"""Digest tests.

The anchors are pinned SHA-256 values of literal byte strings, computed outside
this package with stdlib `hashlib`. That keeps the lock independent: if the
canonicalizer ever changes what bytes a value produces, these fail, because the
expected value was never derived from the code under test.
"""

from __future__ import annotations

import pytest

from kdd_data_agent.core.digest import (
    DigestError,
    content_digest,
    content_digest_excluding,
    digest_bytes,
    is_digest,
    parse_digest,
    stable_id,
    verify_content_digest,
)
from kdd_data_agent.core.unknown import UNKNOWN

SHA256_OF_A_1 = "sha256:015abd7f5cc57a2dd94b7590f04ad8084273905ee33ec5cebeae62276a97f862"
SHA256_OF_UNKNOWN_SENTINEL = "sha256:5e5f4f8a56b0d17185095e9680ebd9ff46e4b4b3d68aab238faa9c72c8005d68"


def test_digest_of_a_literal_byte_string_is_pinned():
    assert digest_bytes(b'{"a":1}') == SHA256_OF_A_1


def test_content_digest_hashes_the_canonical_bytes():
    assert content_digest({"a": 1}) == SHA256_OF_A_1
    assert content_digest(UNKNOWN) == SHA256_OF_UNKNOWN_SENTINEL


def test_content_digest_ignores_key_insertion_order():
    assert content_digest({"a": 1, "b": 2}) == content_digest({"b": 2, "a": 1})


def test_content_digest_excluding_drops_self_referential_fields():
    record = {"a": 1, "digest": "sha256:" + "0" * 64}
    assert content_digest_excluding(record, ["digest"]) == SHA256_OF_A_1


def test_verify_content_digest_accepts_and_rejects():
    assert verify_content_digest({"a": 1}, SHA256_OF_A_1) is True
    assert verify_content_digest({"a": 2}, SHA256_OF_A_1) is False


@pytest.mark.parametrize(
    "bad",
    ["", "sha256:", "sha1:" + "a" * 40, "sha256:" + "A" * 64, "sha256:" + "a" * 63, "a" * 64],
)
def test_malformed_digests_are_rejected(bad):
    assert is_digest(bad) is False
    with pytest.raises(DigestError):
        parse_digest(bad)


def test_stable_id_is_deterministic_and_content_addressed():
    first = stable_id("rev", {"a": 1})
    second = stable_id("rev", {"a": 1})
    assert first == second
    assert first == "rev-" + SHA256_OF_A_1.removeprefix("sha256:")[:16]
    assert stable_id("rev", {"a": 2}) != first


@pytest.mark.parametrize("length", [7, 65])
def test_stable_id_rejects_out_of_range_lengths(length):
    with pytest.raises(ValueError):
        stable_id("rev", {"a": 1}, length=length)


def test_stable_id_requires_a_prefix():
    with pytest.raises(ValueError):
        stable_id("", {"a": 1})
