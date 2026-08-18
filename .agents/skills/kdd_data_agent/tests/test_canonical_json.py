"""Canonical JSON is the foundation of every digest, so its byte output is
pinned to hand-written golden vectors rather than to whatever the code happens
to produce today.
"""

from __future__ import annotations

import pytest

from kdd_data_agent.core.canonical_json import (
    CanonicalJSONError,
    canonical_decode,
    canonical_dumps,
    canonical_encode,
    canonical_loads,
    require_ascii_keys,
    to_canonical_value,
)
from kdd_data_agent.core.identity import AuthorizationState
from kdd_data_agent.core.unknown import ALIGNMENT_PENDING, MISSING, UNKNOWN

GOLDEN_VECTORS = (
    ({"b": 1, "a": 2}, '{"a":2,"b":1}'),
    ({"a": {"d": True, "c": None}}, '{"a":{"c":null,"d":true}}'),
    ([1, "two", None, False], '[1,"two",null,false]'),
    ({"z": [], "y": {}}, '{"y":{},"z":[]}'),
    ({"n": 1.5}, '{"n":1.5}'),
    ({"unicode": "café"}, '{"unicode":"café"}'),
    (UNKNOWN, '{"__kdd__":"UNKNOWN"}'),
    (MISSING, '{"__kdd__":"MISSING"}'),
    (ALIGNMENT_PENDING, '{"__kdd__":"ALIGNMENT_PENDING"}'),
    ({"state": AuthorizationState.UNAUTHORIZED}, '{"state":"unauthorized"}'),
    ({"outer": {"inner": UNKNOWN}}, '{"outer":{"inner":{"__kdd__":"UNKNOWN"}}}'),
)


@pytest.mark.parametrize("value,expected", GOLDEN_VECTORS)
def test_canonical_form_matches_golden_bytes(value, expected):
    assert canonical_dumps(value) == expected
    assert canonical_encode(value) == expected.encode("utf-8")


def test_key_order_is_independent_of_insertion_order():
    first = canonical_dumps({"a": 1, "b": 2, "c": 3})
    second = canonical_dumps({"c": 3, "b": 2, "a": 1})
    assert first == second == '{"a":1,"b":2,"c":3}'


def test_sentinels_round_trip_to_the_same_singleton():
    payload = {"authority": UNKNOWN, "body": MISSING, "readiness": ALIGNMENT_PENDING}
    restored = canonical_decode(canonical_encode(payload))
    assert restored["authority"] is UNKNOWN
    assert restored["body"] is MISSING
    assert restored["readiness"] is ALIGNMENT_PENDING


def test_reencoding_a_decoded_document_is_byte_identical():
    payload = {"b": [1, {"a": UNKNOWN}], "a": "x"}
    encoded = canonical_encode(payload)
    assert canonical_encode(canonical_loads(encoded.decode("utf-8"))) == encoded


def test_decoding_rejects_duplicate_object_keys_instead_of_silently_overwriting():
    with pytest.raises(CanonicalJSONError, match="duplicate object key"):
        canonical_loads('{"metric":1,"metric":2}')


@pytest.mark.parametrize("constant", ["NaN", "Infinity", "-Infinity"])
def test_decoding_rejects_non_json_numeric_constants(constant):
    with pytest.raises(CanonicalJSONError, match="non-finite"):
        canonical_loads('{"metric":' + constant + '}')


def test_normalization_is_idempotent():
    """A `to_canonical()` result must survive a second normalization pass.

    Without this, embedding one already-normalized record inside another would
    trip the reserved-key guard on the encoded sentinel.
    """
    payload = {"outer": {"inner": UNKNOWN}, "list": [MISSING]}
    once = to_canonical_value(payload)
    assert to_canonical_value(once) == once
    assert canonical_dumps(once) == canonical_dumps(payload)


def test_reserved_key_is_rejected_in_application_payloads():
    with pytest.raises(CanonicalJSONError, match="reserved"):
        canonical_dumps({"__kdd__": "UNKNOWN"})
    with pytest.raises(CanonicalJSONError, match="reserved"):
        canonical_dumps({"__kdd__": "not-a-sentinel-name"})
    with pytest.raises(CanonicalJSONError, match="reserved"):
        canonical_dumps({"__kdd__": "UNKNOWN", "extra": 1})


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_non_finite_floats_are_rejected(value):
    with pytest.raises(CanonicalJSONError, match="non-finite"):
        canonical_dumps({"metric": value})


def test_sets_are_rejected_because_they_have_no_canonical_order():
    with pytest.raises(CanonicalJSONError, match="no canonical order"):
        canonical_dumps({"ids": {"a", "b"}})


def test_non_string_keys_are_rejected():
    with pytest.raises(CanonicalJSONError, match="keys must be strings"):
        canonical_dumps({1: "one"})


@pytest.mark.parametrize("value", [object(), b"bytes", bytearray(b"x"), 1j])
def test_unsupported_types_are_rejected_rather_than_stringified(value):
    with pytest.raises(CanonicalJSONError):
        canonical_dumps({"field": value})


def test_objects_exposing_to_canonical_are_serialized_through_it():
    class Record:
        def to_canonical(self):
            return {"kind": "record", "value": UNKNOWN}

    assert canonical_dumps(Record()) == '{"kind":"record","value":{"__kdd__":"UNKNOWN"}}'


def test_require_ascii_keys_flags_the_documented_sort_deviation():
    require_ascii_keys({"plain": 1})
    with pytest.raises(CanonicalJSONError, match="non-ASCII object key"):
        require_ascii_keys({"clé": 1})


def test_tuples_normalize_to_lists():
    assert to_canonical_value(("a", "b")) == ["a", "b"]
