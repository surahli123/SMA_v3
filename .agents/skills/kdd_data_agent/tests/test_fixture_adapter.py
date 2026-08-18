"""Fixture read-adapter tests.

Covers the eight typed read outcomes, the no-retained-body invariant, strict
fail-closed fixture validation, and the absence of any write, publish, or
execute path. No test writes a file: fixture-integrity failures are exercised
by calling the validators directly, which keeps "this package never writes"
true of the tests as well as the runtime.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import kdd_data_agent.adapters.fixture as fixture_module

from kdd_data_agent.adapters.base import ReadPolicyError, ReadRequest, ReadResult
from kdd_data_agent.adapters.fixture import (
    EXPECTED_READINESS_PLACEHOLDER,
    FixtureIntegrityError,
    FixtureNotFoundError,
    FixtureReadAdapter,
)
from kdd_data_agent.adapters.outcomes import (
    OUTCOMES_WITHOUT_RETAINED_BODY,
    ReadOutcome,
    parse_read_outcome,
)
from kdd_data_agent.core.capabilities import ALLOWED_CAPABILITIES, Capability
from kdd_data_agent.core.coverage_gap import CoverageGap, CoverageGapKind, Materiality
from kdd_data_agent.core.identity import AuthorizationState, RedactionState
from kdd_data_agent.core.receipts import ReceiptKind
from kdd_data_agent.core.unknown import MISSING

SOURCE_ID = "fixture-metric-store"


def read_case(adapter: FixtureReadAdapter, case_id: str) -> ReadResult:
    return adapter.read(
        ReadRequest(request_id=f"req-{case_id}", source_id=SOURCE_ID, locator=case_id)
    )


def test_manifest_covers_every_read_outcome(adapter):
    manifest = adapter.load_manifest()
    declared = {entry["expected_read_outcome"] for entry in manifest["cases"]}
    assert declared == {outcome.value for outcome in ReadOutcome}


def test_every_fixture_file_is_reachable_from_the_manifest(adapter):
    manifest_files = {f"{case_id}.json" for case_id in adapter.case_ids()}
    fixture_files = {path.name for path in adapter.root.glob("*.json")} - {"manifest.json", "sealed-corpus.json"}
    assert fixture_files == manifest_files


def test_case_id_validation_rejects_a_trailing_newline():
    with pytest.raises(FixtureIntegrityError, match="invalid fixture case id"):
        fixture_module.validate_case_id("m0-read-trusted-001\n")


def test_fixture_containment_backstop_rejects_a_resolved_escape():
    class EscapedPath:
        def resolve(self): return self
        def is_relative_to(self, _root): return False

    class FixtureRoot:
        def __truediv__(self, _name): return EscapedPath()

    adapter = object.__new__(FixtureReadAdapter)
    adapter._root = FixtureRoot()
    with pytest.raises(FixtureIntegrityError, match="outside the fixture root"):
        adapter._case_path("m0-read-trusted-001")


def test_every_manifest_case_reads_with_its_declared_outcome(adapter):
    for entry in adapter.load_manifest()["cases"]:
        result = read_case(adapter, entry["case_id"])
        assert result.outcome.value == entry["expected_read_outcome"], entry["case_id"]
        assert result.receipt.receipt_kind is ReceiptKind.SOURCE_READ
        assert result.receipt.outcome == result.outcome.value


def test_no_fixture_states_a_readiness_decision(adapter):
    for case_id in adapter.case_ids():
        raw = adapter.load_raw(case_id)
        assert raw["expected_final_readiness"] == EXPECTED_READINESS_PLACEHOLDER


@pytest.mark.parametrize(
    "mutation",
    [
        lambda document: document | {"schema_version": "wrong"},
        lambda document: {key: value for key, value in document.items() if key != "notes"},
        lambda document: document | {"unexpected": True},
        lambda document: document | {"case_id": "m0-read-stale-001"},
        lambda document: document | {"expected_final_readiness": "ready"},
    ],
)
def test_load_raw_rejects_malformed_documents_through_the_real_validator(
    adapter, monkeypatch, mutation
):
    original = dict(adapter.load_raw("m0-read-trusted-001"))
    monkeypatch.setattr(fixture_module, "canonical_loads", lambda text: mutation(original))

    with pytest.raises(FixtureIntegrityError):
        adapter.load_raw("m0-read-trusted-001")


@pytest.mark.parametrize("mutation", ["wrong_schema", "duplicate_case", "invalid_outcome"])
def test_load_manifest_rejects_malformed_documents_through_the_real_validator(
    adapter, monkeypatch, mutation
):
    original = dict(adapter.load_manifest())
    cases = [dict(entry) for entry in original["cases"]]
    if mutation == "wrong_schema":
        original["schema_version"] = "wrong"
    elif mutation == "duplicate_case":
        cases.append(dict(cases[0]))
        original["cases"] = cases
    else:
        cases[0]["expected_read_outcome"] = "not-an-outcome"
        original["cases"] = cases
    monkeypatch.setattr(fixture_module, "canonical_loads", lambda text: original)

    with pytest.raises((FixtureIntegrityError, ValueError)):
        adapter.load_manifest()


def test_outcomes_without_retained_body_carry_no_body(adapter):
    checked = set()
    for case_id in adapter.case_ids():
        result = read_case(adapter, case_id)
        if result.outcome in OUTCOMES_WITHOUT_RETAINED_BODY:
            checked.add(result.outcome)
            assert result.body is MISSING
            assert result.has_body() is False
            assert result.receipt.has_body() is False
            assert result.receipt.body_digest() is MISSING
    assert checked == set(OUTCOMES_WITHOUT_RETAINED_BODY)


def test_trusted_read_retains_a_body_and_no_coverage_gap(adapter):
    result = read_case(adapter, "m0-read-trusted-001")
    assert result.outcome is ReadOutcome.TRUSTED
    assert result.has_body() is True
    assert result.coverage_gaps == ()
    assert result.receipt.authorization_state is AuthorizationState.AUTHORIZED


def test_every_non_trusted_read_records_a_coverage_gap_with_unknown_materiality(adapter):
    for case_id in adapter.case_ids():
        result = read_case(adapter, case_id)
        if result.outcome is ReadOutcome.TRUSTED:
            continue
        assert result.coverage_gaps, case_id
        for gap in result.coverage_gaps:
            assert isinstance(gap.kind, CoverageGapKind)
            assert gap.materiality is Materiality.UNKNOWN
            assert gap.reason.strip()


def test_conflicting_read_preserves_both_sides(adapter):
    result = read_case(adapter, "m0-read-conflicting-001")
    assert result.outcome is ReadOutcome.CONFLICTING
    assert len(result.disagreements) == 1
    disagreement = result.disagreements[0]
    assert disagreement["left_value"] != disagreement["right_value"]
    assert disagreement["resolved"] is False


def test_unknown_fields_stay_unknown_rather_than_being_inferred(adapter):
    result = read_case(adapter, "m0-read-blocked-001")
    assert result.receipt.source.snapshot_id.name == "UNKNOWN"
    assert result.receipt.observed_interval.start.name == "UNKNOWN"


@pytest.mark.parametrize(
    "locator",
    ["../manifest", "../../sma/SKILL", "..", "a/b", "m0-read-trusted-001.json", "M0-READ-TRUSTED-001"],
)
def test_case_ids_that_could_name_a_path_are_rejected(adapter, locator):
    with pytest.raises(FixtureIntegrityError, match="invalid fixture case id"):
        read_case(adapter, locator)


def test_missing_case_raises_not_found(adapter):
    with pytest.raises(FixtureNotFoundError):
        read_case(adapter, "m0-read-does-not-exist-001")


def test_missing_fixture_root_raises_not_found(package_root: Path):
    # Deliberately not `tmp_path`: that fixture would have pytest create a
    # directory, and the claim this suite makes is that nothing in the package
    # or its tests writes to the filesystem at all.
    with pytest.raises(FixtureNotFoundError):
        FixtureReadAdapter(package_root / "evals" / "fixtures" / "does-not-exist")


def test_source_mismatch_between_request_and_fixture_is_rejected(adapter):
    with pytest.raises(FixtureIntegrityError, match="belongs to source"):
        adapter.read(
            ReadRequest(
                request_id="req-1", source_id="some-other-source", locator="m0-read-trusted-001"
            )
        )


def test_a_request_without_a_locator_is_rejected(adapter):
    with pytest.raises(FixtureIntegrityError, match="locator"):
        adapter.read(ReadRequest(request_id="req-1", source_id=SOURCE_ID))


@pytest.mark.parametrize("value", ["ready", "ok", "TRUSTED", "", "partial_read"])
def test_unknown_outcome_strings_fail_closed_with_no_alias_handling(value):
    with pytest.raises(ValueError, match="unknown read outcome"):
        parse_read_outcome(value)


def test_body_policy_rejects_a_retained_body_on_an_unauthorized_outcome():
    with pytest.raises(FixtureIntegrityError, match="no body may be retained"):
        FixtureReadAdapter._enforce_body_policy(
            "planted",
            ReadOutcome.UNAUTHORIZED,
            AuthorizationState.UNAUTHORIZED,
            RedactionState.UNKNOWN,
            {"value": 1},
        )


def test_body_policy_rejects_a_body_under_a_non_authorized_state():
    with pytest.raises(FixtureIntegrityError, match="only an explicit authorized state"):
        FixtureReadAdapter._enforce_body_policy(
            "planted", ReadOutcome.PARTIAL, AuthorizationState.UNKNOWN, RedactionState.APPLIED, {"value": 1}
        )


def test_body_policy_rejects_a_trusted_read_without_authorization_or_body():
    with pytest.raises(FixtureIntegrityError, match="trusted read under authorization state"):
        FixtureReadAdapter._enforce_body_policy(
            "planted", ReadOutcome.TRUSTED, AuthorizationState.UNKNOWN, RedactionState.UNKNOWN, MISSING
        )
    with pytest.raises(FixtureIntegrityError, match="trusted read with no body"):
        FixtureReadAdapter._enforce_body_policy(
            "planted", ReadOutcome.TRUSTED, AuthorizationState.AUTHORIZED, RedactionState.NOT_REQUIRED, MISSING
        )


def test_body_policy_requires_authorization_and_redaction_independently():
    with pytest.raises(FixtureIntegrityError, match="redaction state failed"):
        FixtureReadAdapter._enforce_body_policy(
            "planted",
            ReadOutcome.PARTIAL,
            AuthorizationState.AUTHORIZED,
            RedactionState.FAILED,
            {"value": 1},
        )


@pytest.mark.parametrize("bad", ["", "AUTHORIZED", " authorized", "authorised", "unknown-value", 7])
def test_authorization_parser_is_strict_and_fail_closed(bad):
    with pytest.raises(FixtureIntegrityError):
        FixtureReadAdapter._parse_authorization_state(bad, "planted")


def test_redaction_failure_preserves_the_authorization_axis(adapter):
    result = read_case(adapter, "m0-read-redaction-failure-001")
    assert result.receipt.authorization_state is AuthorizationState.AUTHORIZED
    assert result.receipt.redaction_state is RedactionState.FAILED


def test_a_non_trusted_outcome_with_no_coverage_gap_is_rejected():
    with pytest.raises(FixtureIntegrityError, match="no Coverage Gap"):
        FixtureReadAdapter._build_coverage_gaps([], ReadOutcome.STALE, "planted")


def test_a_trusted_outcome_that_also_carries_gaps_is_rejected():
    entry = [{"kind": "timeout", "reason": "r", "next_safe_check": "c"}]
    with pytest.raises(FixtureIntegrityError, match="trusted read that also carries"):
        FixtureReadAdapter._build_coverage_gaps(entry, ReadOutcome.TRUSTED, "planted")


def test_an_unrecognised_coverage_gap_kind_is_rejected():
    entry = [{"kind": "made_up_kind", "reason": "r", "next_safe_check": "c"}]
    with pytest.raises(FixtureIntegrityError, match="is not one of"):
        FixtureReadAdapter._build_coverage_gaps(entry, ReadOutcome.STALE, "planted")


# The three tests above prove the validators reject. They do not prove the
# validators are reached: silently unwiring a guard from `read()` leaves them
# all green. These drive a tampered document through the real read path, so the
# wiring is under test too. `monkeypatch` replaces the loader in memory; no
# hostile fixture is ever written to disk.


def test_the_read_path_itself_rejects_a_retained_body_on_a_no_body_outcome(adapter, monkeypatch):
    tampered = dict(adapter.load_raw("m0-read-unauthorized-001"))
    tampered["body"] = {"leaked_metric_value": 0.1234}
    monkeypatch.setattr(adapter, "load_raw", lambda case_id: tampered)

    with pytest.raises(FixtureIntegrityError, match="no body may be retained"):
        read_case(adapter, "m0-read-unauthorized-001")


def test_the_read_path_itself_rejects_a_body_under_a_non_authorized_state(adapter, monkeypatch):
    tampered = dict(adapter.load_raw("m0-read-partial-001"))
    tampered["authorization"] = dict(tampered["authorization"]) | {"state": "unknown"}
    monkeypatch.setattr(adapter, "load_raw", lambda case_id: tampered)

    with pytest.raises(FixtureIntegrityError, match="only an explicit authorized state"):
        read_case(adapter, "m0-read-partial-001")


def test_the_read_path_itself_requires_a_coverage_gap_for_a_non_trusted_outcome(adapter, monkeypatch):
    tampered = dict(adapter.load_raw("m0-read-stale-001"))
    tampered["coverage_gaps"] = []
    monkeypatch.setattr(adapter, "load_raw", lambda case_id: tampered)

    with pytest.raises(FixtureIntegrityError, match="no Coverage Gap"):
        read_case(adapter, "m0-read-stale-001")


def test_the_read_path_binds_fixture_outcome_to_the_manifest(adapter, monkeypatch):
    tampered = dict(adapter.load_raw("m0-read-trusted-001"))
    tampered["declared_outcome"] = "partial"
    monkeypatch.setattr(adapter, "load_raw", lambda case_id: tampered)

    with pytest.raises(FixtureIntegrityError, match="manifest.json.*expects"):
        read_case(adapter, "m0-read-trusted-001")


def test_the_read_path_rejects_a_fixture_absent_from_the_manifest(adapter, monkeypatch):
    manifest = dict(adapter.load_manifest())
    manifest["cases"] = tuple(
        entry for entry in manifest["cases"] if entry["case_id"] != "m0-read-trusted-001"
    )
    monkeypatch.setattr(adapter, "load_manifest", lambda: manifest)

    with pytest.raises(FixtureIntegrityError, match="not listed"):
        read_case(adapter, "m0-read-trusted-001")


def test_read_result_refuses_to_hold_a_body_for_a_no_body_outcome(adapter):
    blocked = read_case(adapter, "m0-read-blocked-001")
    with pytest.raises(ReadPolicyError, match="must not retain a source body"):
        ReadResult(
            request=blocked.request,
            outcome=ReadOutcome.BLOCKED,
            receipt=blocked.receipt,
            body={"leaked": True},
            coverage_gaps=blocked.coverage_gaps,
        )


def test_read_result_rejects_state_that_contradicts_its_receipt(adapter):
    trusted = read_case(adapter, "m0-read-trusted-001")
    with pytest.raises(ReadPolicyError, match="outcome must match"):
        ReadResult(
            request=trusted.request,
            outcome=ReadOutcome.STALE,
            receipt=trusted.receipt,
            body=trusted.body,
        )
    with pytest.raises(ReadPolicyError, match="Coverage Gaps must match"):
        ReadResult(
            request=trusted.request,
            outcome=trusted.outcome,
            receipt=trusted.receipt,
            body=trusted.body,
            coverage_gaps=(CoverageGap(kind=CoverageGapKind.TIMEOUT, reason="planted"),),
        )
    with pytest.raises(ReadPolicyError, match="body digest must match"):
        ReadResult(
            request=trusted.request,
            outcome=trusted.outcome,
            receipt=trusted.receipt,
            body={"different": True},
        )
    different_request = ReadRequest(
        request_id="different-request",
        source_id=trusted.request.source_id,
        locator=trusted.request.locator,
    )
    with pytest.raises(ReadPolicyError, match="request must match"):
        ReadResult(
            request=different_request,
            outcome=trusted.outcome,
            receipt=trusted.receipt,
            body=trusted.body,
        )


def test_adapter_capabilities_stay_inside_the_positive_allowlist(adapter):
    assert adapter.capabilities <= ALLOWED_CAPABILITIES
    assert Capability.FIXTURE_READ in adapter.capabilities


def test_adapter_exposes_no_write_publish_or_execute_surface(adapter):
    public = {name for name in dir(adapter) if not name.startswith("_")}
    assert public == {"capabilities", "case_ids", "load_manifest", "load_raw", "read", "root"}


def test_an_adapter_declaring_an_unknown_capability_cannot_be_constructed():
    class RogueAdapter(FixtureReadAdapter):
        capabilities = frozenset({Capability.FIXTURE_READ, "network"})

    with pytest.raises(PermissionError, match="non-capability values"):
        RogueAdapter(Path(__file__).resolve().parent.parent / "evals" / "fixtures" / "m0")
