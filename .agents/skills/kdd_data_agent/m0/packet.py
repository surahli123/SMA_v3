"""Immutable fixture-class FlightReadinessPacket and synthetic projection."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from ..core.canonical_json import canonical_encode, canonical_loads
from ..core.coverage_gap import (
    COVERAGE_GAP_KIND_REGISTRY,
    CoverageGap,
    CoverageGapKind,
    Materiality,
    require_registered_rule_source,
)
from ..core.digest import content_digest, is_digest, stable_id
from ..core.identity import AuthorizationState, RedactionState, validate_timestamp
from ..core.immutability import deep_freeze
from ..core.receipts import Receipt, ReceiptKind
from ..core.unknown import MISSING, Sentinel
from .checks import CHECK_REGISTRY, CheckOutcome, CheckResult, CoreCheckSet
from .contracts import EvidenceClass, ExperimentReadContract, FrozenM0Binding


class PacketError(ValueError):
    pass


class AnalysisUse(str, Enum):
    DECISION_GRADE = "decision_grade"
    DIRECTIONAL_ONLY = "directional_only"
    NOT_PERMITTED = "not_permitted"


class PostAnalysisEligibility(str, Enum):
    ELIGIBLE = "eligible"
    BLOCKED = "blocked"


class NextSafeActionKind(str, Enum):
    EVIDENCE_COLLECTION = "evidence_collection"
    CONTRACT_CORRECTION = "contract_correction"
    VALIDITY_FIX = "validity_fix"
    INSTRUMENTATION_FIX = "instrumentation_fix"
    DATA_QUALITY_FIX = "data_quality_fix"


def derive_readiness(
    checks: tuple[CheckResult, ...],
) -> tuple[AnalysisUse, tuple[str, ...], "NextSafeAction"]:
    """Derive the only legal readiness fields from sealed check results."""
    issues = tuple(
        item for item in checks
        if item.outcome in {CheckOutcome.FAIL, CheckOutcome.MISSING, CheckOutcome.UNKNOWN}
        and item.materiality in {Materiality.MATERIAL, Materiality.UNKNOWN}
    )
    issue_ids = {item.check_id for item in issues}
    directional_reasons = {
        "CHK-02": "runtime below preregistered threshold",
        "CHK-19": "sample below preregistered threshold",
    }
    if issues and issue_ids.issubset({"CHK-02", "CHK-19"}) and all(
        item.outcome is CheckOutcome.FAIL and item.reason == directional_reasons[item.check_id]
        for item in issues
    ):
        return (
            AnalysisUse.DIRECTIONAL_ONLY,
            tuple(item.check_id for item in issues),
            NextSafeAction(
                NextSafeActionKind.EVIDENCE_COLLECTION,
                "collect the preregistered runtime or sample units",
                "new read after the preregistered threshold",
            ),
        )
    if issues:
        kind = (
            NextSafeActionKind.CONTRACT_CORRECTION
            if any(item.check_id == "CHK-19" and item.outcome is CheckOutcome.MISSING for item in issues)
            else NextSafeActionKind.EVIDENCE_COLLECTION
            if any(item.outcome in {CheckOutcome.MISSING, CheckOutcome.UNKNOWN} for item in issues)
            else NextSafeActionKind.VALIDITY_FIX
        )
        return (
            AnalysisUse.NOT_PERMITTED,
            tuple(item.check_id for item in issues),
            NextSafeAction(
                kind,
                "resolve the recorded material blockers without changing history",
                "superseding evidence and a new sealed packet",
            ),
        )
    return (
        AnalysisUse.DECISION_GRADE,
        (),
        NextSafeAction(
            NextSafeActionKind.EVIDENCE_COLLECTION,
            "route the sealed packet for human review",
            "a named human reviews this exact packet digest",
        ),
    )


@dataclass(frozen=True)
class NextSafeAction:
    kind: NextSafeActionKind
    guidance: str
    reopen_condition: str

    def __post_init__(self) -> None:
        if not isinstance(self.kind, NextSafeActionKind):
            raise TypeError("kind must be NextSafeActionKind")
        for name, value in (("guidance", self.guidance), ("reopen_condition", self.reopen_condition)):
            if not isinstance(value, str) or not value.strip():
                raise PacketError(f"{name} is required")
        forbidden = ("diff --git", "production_target", "apply_patch", "automation_consumer")
        if any(token in self.guidance for token in forbidden):
            raise PacketError("next safe action cannot carry an exact production target or diff")

    def to_canonical(self) -> dict[str, str]:
        return {"kind": self.kind.value, "guidance": self.guidance, "reopen_condition": self.reopen_condition}


@dataclass(frozen=True)
class HumanState:
    experiment_owner: str
    independent_ds_consultant: str
    committee_route: str
    acknowledgement_state: str

    def __post_init__(self) -> None:
        if self.acknowledgement_state not in {"not_requested", "pending", "acknowledged", "invalidated"}:
            raise PacketError("invalid acknowledgement_state")

    def to_canonical(self) -> dict[str, str]:
        return {
            "experiment_owner": self.experiment_owner,
            "independent_ds_consultant": self.independent_ds_consultant,
            "committee_route": self.committee_route,
            "acknowledgement_state": self.acknowledgement_state,
        }


@dataclass(frozen=True)
class PacketAcknowledgement:
    packet_digest: str
    reviewer: str
    state: str = "acknowledged"
    invalidated_by: str | Sentinel = MISSING

    def __post_init__(self) -> None:
        if self.state not in {"acknowledged", "invalidated"}:
            raise PacketError("acknowledgement state must be acknowledged or invalidated")


def _mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise PacketError(f"serialized {label} must be an object")
    return value


def _exact_keys(value: Mapping[str, Any], expected: set[str], label: str) -> None:
    if set(value) != expected:
        raise PacketError(f"serialized {label} schema mismatch")


def _verify_content_address(
    value: Mapping[str, Any], *, identity_field: str, label: str, stable_prefix: str | None = None,
) -> None:
    identity = dict(value)
    stated = identity.pop(identity_field, None)
    expected = stable_id(stable_prefix, identity) if stable_prefix else content_digest(identity)
    if stated != expected:
        raise PacketError(f"serialized {label} identity mismatch")


def _verify_serialized_contract(document: Mapping[str, Any]) -> None:
    expected_fields = {
        "flight_id", "contract_version", "binding", "evidence_class", "metrics",
        "decision_metric_policy", "assignment_unit", "analysis_unit", "population",
        "eligibility", "exclusions", "tenant_scope", "surface", "locale",
        "exposure_definition", "join_keys", "analysis_window", "timezone",
        "planned_runtime_units", "observed_runtime_units", "observed_sample_units", "source",
        "authorization_state", "redaction_state", "recipient_scope", "retention_rule_id",
        "load_limit_rule_id", "halt_rule_id", "export_rule_id", "sufficiency_rule", "arms",
        "arm_parity_consistent", "arm_parity_applicability_rule_id", "core_check_set_revision",
        "roles", "expiry", "predecessor_digest", "supersedes_digest", "metadata",
        "contract_digest",
    }
    _exact_keys(document, expected_fields, "contract")
    _verify_content_address(document, identity_field="contract_digest", label="contract digest")
    binding = _mapping(document.get("binding"), "contract frozen binding")
    if binding != FrozenM0Binding().to_canonical():
        raise PacketError("serialized frozen binding does not match the canonical freeze")
    if document.get("evidence_class") != EvidenceClass.FIXTURE.value:
        raise PacketError("serialized contract must remain fixture evidence")
    if document.get("authorization_state") not in {item.value for item in AuthorizationState}:
        raise PacketError("serialized contract authorization state is invalid")
    if document.get("redaction_state") not in {item.value for item in RedactionState}:
        raise PacketError("serialized contract redaction state is invalid")
    if document.get("core_check_set_revision") != "m0-core-check-set/v1":
        raise PacketError("serialized contract core check set revision mismatch")
    _exact_keys(_mapping(document.get("source"), "contract source"), {"source_id", "source_kind", "locator", "snapshot_id", "owner"}, "contract source")
    _exact_keys(_mapping(document.get("analysis_window"), "contract analysis window"), {"start", "end"}, "contract analysis window")
    metrics = document.get("metrics")
    if not isinstance(metrics, list) or not metrics:
        raise PacketError("serialized contract requires typed metrics")
    metric_fields = {"metric_id", "definition_version", "role", "unit", "estimator", "source_version", "owner", "cuped_mode", "ratio_variance_method"}
    for metric in metrics:
        _exact_keys(_mapping(metric, "contract metric"), metric_fields, "contract metric")
        if metric["role"] not in {"decision", "co_primary"}:
            raise PacketError("serialized contract metric role is invalid")
    policy = _mapping(document.get("decision_metric_policy"), "decision metric policy")
    _exact_keys(policy, {"policy_id", "metric_cardinality", "conflict_rule_id", "comparison_rule_id", "query_success"}, "decision metric policy")
    if policy["metric_cardinality"] not in {"one", "co_primary"}:
        raise PacketError("serialized metric cardinality is invalid")
    expected_metric_count = 1 if policy["metric_cardinality"] == "one" else 2
    if len(metrics) != expected_metric_count:
        raise PacketError("serialized metric inventory contradicts its cardinality policy")
    _exact_keys(
        _mapping(policy["query_success"], "Query Success definition"),
        {"formula", "traditional_component_id", "ai_answer_component_id", "common_grain", "common_population", "common_window", "overlap_policy_id", "fixed_threshold_rule_id"},
        "Query Success definition",
    )
    sufficiency = _mapping(document.get("sufficiency_rule"), "sufficiency rule")
    _exact_keys(sufficiency, {"kind", "rule_id", "runtime_threshold_units", "sample_threshold_units", "sample_input_ids"}, "sufficiency rule")
    if sufficiency["kind"] not in {"runtime_only", "runtime_and_sample"}:
        raise PacketError("serialized sufficiency kind is invalid")
    arms = document.get("arms")
    if not isinstance(arms, list):
        raise PacketError("serialized contract arms must be a list")
    for arm in arms:
        _exact_keys(_mapping(arm, "contract arm"), {"arm_id", "index_generation", "serving_alias", "acl_snapshot", "effective_pipeline"}, "contract arm")
    _exact_keys(_mapping(document.get("roles"), "contract roles"), {"experiment_owner", "independent_ds_consultant", "committee_route"}, "contract roles")
    if not isinstance(document.get("metadata"), dict):
        raise PacketError("serialized contract metadata must be an object")
    if not isinstance(document.get("exclusions"), list) or not isinstance(document.get("join_keys"), list):
        raise PacketError("serialized contract exclusions and join keys must be lists")
    validate_timestamp(document.get("expiry"), "serialized contract.expiry")


def _verify_serialized_core_set(document: Mapping[str, Any]) -> None:
    _exact_keys(document, {"revision", "check_ids", "digest"}, "core check set")
    identity = dict(document)
    stated = identity.pop("digest", None)
    if stated != content_digest(identity):
        raise PacketError("serialized core check set digest mismatch")
    expected = [item.check_id for item in CHECK_REGISTRY]
    if document.get("revision") != "m0-core-check-set/v1" or document.get("check_ids") != expected:
        raise PacketError("serialized core check set must preserve the exact nineteen-check inventory")


def _verify_serialized_receipt(document: Mapping[str, Any]) -> None:
    fields = {
        "receipt_kind", "source", "actor", "authorization_state", "redaction_state",
        "observed_interval", "recorded_at", "outcome", "derivation_inputs", "coverage_gaps",
        "detail", "body_digest", "receipt_id", "digest",
    }
    _exact_keys(document, fields, "receipt")
    if document["receipt_kind"] not in {item.value for item in ReceiptKind}:
        raise PacketError("serialized receipt kind is invalid")
    if document["authorization_state"] not in {item.value for item in AuthorizationState}:
        raise PacketError("serialized receipt authorization state is invalid")
    if document["redaction_state"] not in {item.value for item in RedactionState}:
        raise PacketError("serialized receipt redaction state is invalid")
    _exact_keys(_mapping(document["source"], "receipt source"), {"source_id", "source_kind", "locator", "snapshot_id", "owner"}, "receipt source")
    _exact_keys(_mapping(document["actor"], "receipt actor"), {"actor_id", "actor_kind"}, "receipt actor")
    _exact_keys(_mapping(document["observed_interval"], "receipt interval"), {"start", "end"}, "receipt interval")
    if not isinstance(document["detail"], dict):
        raise PacketError("serialized receipt detail must be an object")
    validate_timestamp(document["recorded_at"], "serialized receipt.recorded_at")
    identity = dict(document)
    stated_id = identity.pop("receipt_id", None)
    stated_digest = identity.pop("digest", None)
    if stated_id != stable_id("rcpt", identity) or stated_digest != content_digest(identity):
        raise PacketError("serialized receipt identity mismatch")
    if not isinstance(document["derivation_inputs"], list) or not all(
        isinstance(item, str) for item in document["derivation_inputs"]
    ):
        raise PacketError("serialized receipt derivation inputs are invalid")
    if not isinstance(document["coverage_gaps"], list):
        raise PacketError("serialized receipt Coverage Gaps must be a list")
    for raw_gap in document["coverage_gaps"]:
        _verify_serialized_gap(_mapping(raw_gap, "receipt Coverage Gap"))


def _verify_serialized_gap(document: Mapping[str, Any]) -> None:
    _exact_keys(
        document,
        {"kind", "reason", "next_safe_check", "materiality", "rule_source", "evidence_refs", "gap_id"},
        "Coverage Gap",
    )
    _verify_content_address(
        document, identity_field="gap_id", label="Coverage Gap identity", stable_prefix="gap",
    )
    if document["kind"] not in COVERAGE_GAP_KIND_REGISTRY:
        raise PacketError("serialized Coverage Gap kind is invalid")
    if document["materiality"] not in {item.value for item in Materiality}:
        raise PacketError("serialized Coverage Gap materiality is invalid")
    if not isinstance(document["reason"], str) or not document["reason"].strip():
        raise PacketError("serialized Coverage Gap reason is invalid")
    if document["materiality"] != Materiality.UNKNOWN.value:
        try:
            require_registered_rule_source(document["rule_source"])
        except (TypeError, ValueError) as error:
            raise PacketError("serialized Coverage Gap rule source is invalid") from error
    if not isinstance(document["evidence_refs"], list) or not all(
        isinstance(item, str) for item in document["evidence_refs"]
    ):
        raise PacketError("serialized Coverage Gap evidence references are invalid")


_ADMITTED_OUTPUT_FIELDS = {
    "metric_id", "definition_version", "source_version", "cuped_mode", "unit", "value",
}
_SOURCE_OUTPUT_FIELDS = {
    "metric_id": "metric_name",
    "definition_version": "metric_definition_version",
    "source_version": "source_version",
    "cuped_mode": "cuped_mode",
    "unit": "unit",
    "value": "value",
}


def decision_metric_output_from_source_body(body: Any) -> dict[str, Any] | None:
    """Project the typed decision-metric fact from one canonical source body."""
    if not isinstance(body, Mapping) or not set(_SOURCE_OUTPUT_FIELDS.values()).issubset(body):
        return None
    output = {target: body[source] for target, source in _SOURCE_OUTPUT_FIELDS.items()}
    for name in _ADMITTED_OUTPUT_FIELDS - {"value"}:
        if not isinstance(output[name], str) or not output[name].strip():
            return None
    if isinstance(output["value"], bool) or not isinstance(output["value"], (int, float, str)):
        return None
    return output


def admitted_evidence_identity(
    source_receipt_id: str,
    contract_digest: str,
    output: Mapping[str, Any],
    observed: bool,
) -> str:
    """Canonical local identity for one admitted typed decision-metric observation."""
    return content_digest({
        "source_receipt_id": source_receipt_id,
        "contract_digest": contract_digest,
        "output": dict(output),
        "observed": observed,
    })


@dataclass(frozen=True)
class AdmittedEvidenceIdentity:
    source_receipt_id: str
    contract_digest: str
    output: Mapping[str, Any]
    observed: bool
    evidence_id: str = field(init=False)

    def __post_init__(self) -> None:
        if not isinstance(self.source_receipt_id, str) or not self.source_receipt_id:
            raise PacketError("admitted evidence source receipt ID is required")
        if not is_digest(self.contract_digest):
            raise PacketError("admitted evidence contract digest is invalid")
        output = _mapping(self.output, "admitted evidence output")
        _exact_keys(output, _ADMITTED_OUTPUT_FIELDS, "admitted evidence output")
        for name in _ADMITTED_OUTPUT_FIELDS - {"value"}:
            if not isinstance(output[name], str) or not output[name].strip():
                raise PacketError("admitted evidence output is invalid")
        if isinstance(output["value"], bool) or not isinstance(output["value"], (int, float, str)):
            raise PacketError("admitted evidence output value is invalid")
        if self.observed is not True:
            raise PacketError("admitted evidence must be observed")
        object.__setattr__(self, "output", deep_freeze(output))
        object.__setattr__(self, "evidence_id", admitted_evidence_identity(
            self.source_receipt_id, self.contract_digest, output, self.observed,
        ))

    def to_canonical(self) -> dict[str, Any]:
        return {
            "source_receipt_id": self.source_receipt_id,
            "contract_digest": self.contract_digest,
            "output": dict(self.output),
            "observed": self.observed,
            "evidence_id": self.evidence_id,
        }


def _verify_serialized_admitted_evidence(
    document: Any,
    source_receipts: list[Mapping[str, Any]],
    contract: Mapping[str, Any],
) -> str | None:
    if document is None:
        return None
    admitted = _mapping(document, "admitted evidence")
    _exact_keys(
        admitted,
        {"source_receipt_id", "contract_digest", "output", "observed", "evidence_id"},
        "admitted evidence",
    )
    output = _mapping(admitted["output"], "admitted evidence output")
    _exact_keys(output, _ADMITTED_OUTPUT_FIELDS, "admitted evidence output")
    for name in _ADMITTED_OUTPUT_FIELDS - {"value"}:
        if not isinstance(output[name], str) or not output[name].strip():
            raise PacketError("serialized admitted evidence output is invalid")
    if isinstance(output["value"], bool) or not isinstance(output["value"], (int, float, str)):
        raise PacketError("serialized admitted evidence output is invalid")
    if admitted["observed"] is not True:
        raise PacketError("serialized admitted evidence observed state is invalid")
    if admitted["contract_digest"] != contract["contract_digest"]:
        raise PacketError("serialized admitted evidence contract does not match the frozen contract")
    source = next(
        (item for item in source_receipts if item["receipt_id"] == admitted["source_receipt_id"]),
        None,
    )
    if source is None or not (
        source["source"] == contract["source"]
        and source["observed_interval"] == contract["analysis_window"]
        and source["authorization_state"] == contract["authorization_state"] == "authorized"
        and source["redaction_state"] == contract["redaction_state"]
        and source["redaction_state"] in {"not_required", "applied"}
        and source["outcome"] == "trusted"
        and isinstance(source["body_digest"], str)
        and is_digest(source["body_digest"])
    ):
        raise PacketError("serialized admitted evidence source is not admitted under the contract")
    metric = contract["metrics"][0]
    expected_output = {
        "metric_id": metric["metric_id"],
        "definition_version": metric["definition_version"],
        "source_version": metric["source_version"],
        "cuped_mode": metric["cuped_mode"],
        "unit": metric["unit"],
        "value": output["value"],
    }
    if output != expected_output:
        raise PacketError("serialized admitted evidence output does not match the frozen contract")
    expected_id = admitted_evidence_identity(
        admitted["source_receipt_id"], admitted["contract_digest"], output, admitted["observed"],
    )
    if admitted["evidence_id"] != expected_id:
        raise PacketError("serialized admitted evidence identity mismatch")
    return expected_id


def _verify_authoritative_source_body(
    admitted_evidence: Mapping[str, Any] | None,
    source_receipts: list[Mapping[str, Any]],
    trusted_source_body: Mapping[str, Any] | None,
) -> None:
    """Bind admitted output to a transient out-of-band authoritative body."""
    if admitted_evidence is None:
        if trusted_source_body is not None:
            raise PacketError("unadmitted evidence cannot receive a trusted source body")
        return
    if trusted_source_body is None:
        raise PacketError("trusted authoritative source body is required for admitted evidence")
    if not isinstance(trusted_source_body, Mapping):
        raise PacketError("trusted authoritative source body must be a canonical object")
    try:
        canonical_body = canonical_loads(canonical_encode(trusted_source_body).decode("utf-8"))
    except (TypeError, ValueError) as error:
        raise PacketError("trusted authoritative source body is not canonical") from error
    if not isinstance(canonical_body, dict):
        raise PacketError("trusted authoritative source body must be a canonical object")
    source = next(
        (
            item for item in source_receipts
            if item["receipt_id"] == admitted_evidence["source_receipt_id"]
        ),
        None,
    )
    if source is None:
        raise PacketError("admitted evidence has a stale authoritative source binding")
    if source["body_digest"] != content_digest(canonical_body):
        raise PacketError("trusted authoritative source body digest does not match its receipt")
    derived_output = decision_metric_output_from_source_body(canonical_body)
    if derived_output is None:
        raise PacketError("trusted authoritative source body cannot derive the decision metric")
    if derived_output != admitted_evidence["output"]:
        raise PacketError("admitted metric output does not match the authoritative source body")


def validator_evidence_identity(
    check_id: str,
    validator_receipt: Mapping[str, Any],
    admitted_evidence: Mapping[str, Any] | None,
) -> str:
    """Bind one check to the exact typed validator and source lineage fields."""
    detail = _mapping(validator_receipt.get("detail"), "validator receipt detail")
    return content_digest({
        "check_id": check_id,
        "validator_actor": validator_receipt.get("actor"),
        "validator_id": detail.get("validator_id"),
        "outcome": validator_receipt.get("outcome"),
        "reason": detail.get("reason"),
        "contract_digest": detail.get("contract_digest"),
        "source_receipt_id": detail.get("source_receipt_id"),
        "source_body_digest": detail.get("source_body_digest"),
        "observation_digest": detail.get("observation_digest"),
        "derivation_inputs": validator_receipt.get("derivation_inputs"),
        "admitted_evidence": admitted_evidence,
    })


def _verify_serialized_checks(
    documents: list[Any],
    source_receipts: list[Mapping[str, Any]],
    derivation_receipts: list[Mapping[str, Any]],
    contract_digest: str,
    admitted_evidence: Mapping[str, Any] | None,
    admitted_evidence_id: str | None,
) -> None:
    expected_ids = [item.check_id for item in CHECK_REGISTRY]
    if len(documents) != 19:
        raise PacketError("serialized packet requires nineteen checks")
    seen_evidence: set[str] = set()
    observed_ids: list[str] = []
    source_by_id = {item["receipt_id"]: item for item in source_receipts}
    derivation_by_id = {item["receipt_id"]: item for item in derivation_receipts}
    bound_validator_ids: set[str] = set()
    fields = {
        "check_id", "outcome", "materiality", "rule_source", "materiality_rule_id",
        "evidence_ids", "receipt_ids", "reason", "reopen_condition", "affected_scope",
        "ruling_actor", "result_digest",
    }
    for raw in documents:
        check = _mapping(raw, "check result")
        _exact_keys(check, fields, "check result")
        identity = dict(check)
        stated = identity.pop("result_digest", None)
        if stated != content_digest(identity):
            raise PacketError("serialized check result digest mismatch")
        observed_ids.append(check.get("check_id"))
        if check.get("outcome") not in {item.value for item in CheckOutcome}:
            raise PacketError("serialized check outcome is invalid")
        if check.get("materiality") not in {item.value for item in Materiality}:
            raise PacketError("serialized check materiality is invalid")
        try:
            require_registered_rule_source(check.get("rule_source"))
            require_registered_rule_source(check.get("materiality_rule_id"))
        except (TypeError, ValueError) as error:
            raise PacketError("serialized check rule source is invalid") from error
        if check.get("outcome") == CheckOutcome.NOT_APPLICABLE.value and "applicability" not in check["rule_source"]:
            raise PacketError("serialized NOT_APPLICABLE check lacks an applicability rule")
        if any(
            not isinstance(check.get(field), str) or not check[field].strip()
            for field in ("reason", "reopen_condition", "affected_scope", "ruling_actor")
        ):
            raise PacketError("serialized check descriptive fields are invalid")
        evidence_ids = check.get("evidence_ids")
        bound_receipts = check.get("receipt_ids")
        if not isinstance(evidence_ids, list) or not isinstance(bound_receipts, list):
            raise PacketError("serialized check evidence and receipt bindings must be lists")
        if check.get("outcome") == CheckOutcome.PASS.value and (not evidence_ids or not bound_receipts):
            raise PacketError("serialized PASS requires check-specific evidence and receipt bindings")
        if any(not isinstance(item, str) or not is_digest(item) for item in evidence_ids):
            raise PacketError("serialized check evidence binding is invalid")
        if len(bound_receipts) != 2:
            raise PacketError("serialized check receipt binding must be the exact source and validator pair")
        source_receipt = source_by_id.get(bound_receipts[0])
        validator_receipt = derivation_by_id.get(bound_receipts[1])
        if source_receipt is None or validator_receipt is None:
            raise PacketError("serialized check receipt binding is not present in the packet")
        detail = _mapping(validator_receipt.get("detail"), "validator receipt detail")
        _exact_keys(
            detail,
            {
                "validator_id", "contract_digest", "source_receipt_id",
                "observation_digest", "source_body_digest", "admitted_evidence_id", "reason",
            },
            "validator receipt detail",
        )
        check_id = check["check_id"]
        expected_actor = {
            "actor_id": f"m0-validator-{check_id.lower()}/v1",
            "actor_kind": "deterministic_validator",
        }
        if validator_receipt["actor"] != expected_actor or detail["validator_id"] != f"m0-{check_id.lower()}-validator/v1":
            raise PacketError("serialized validator identity does not match its check")
        if validator_receipt["outcome"] != f"{check_id}:{check['outcome']}":
            raise PacketError("serialized validator outcome does not match its check")
        if detail["reason"] != check["reason"]:
            raise PacketError("serialized validator reason does not match its check")
        if detail["contract_digest"] != contract_digest:
            raise PacketError("serialized validator contract digest does not match the frozen contract")
        if detail["source_receipt_id"] != source_receipt["receipt_id"]:
            raise PacketError("serialized validator source receipt does not match its check")
        if detail["source_body_digest"] != source_receipt["body_digest"]:
            raise PacketError("serialized validator source-body digest does not match its source receipt")
        if not is_digest(detail["observation_digest"]):
            raise PacketError("serialized validator observation digest is invalid")
        if detail["admitted_evidence_id"] != admitted_evidence_id:
            label = "unadmitted evidence" if admitted_evidence_id is None else "admitted evidence"
            raise PacketError(f"serialized validator {label} identity mismatch")
        if validator_receipt["derivation_inputs"] != [source_receipt["receipt_id"], contract_digest]:
            raise PacketError("serialized validator derivation inputs do not match the source and contract")
        expected_evidence = validator_evidence_identity(check_id, validator_receipt, admitted_evidence)
        if check["outcome"] in {CheckOutcome.MISSING.value, CheckOutcome.UNKNOWN.value}:
            if evidence_ids:
                raise PacketError("serialized unresolved check cannot claim evidence identity")
        elif evidence_ids != [expected_evidence]:
            raise PacketError("serialized check evidence identity does not match its validator lineage")
        if check["ruling_actor"] != "m0-deterministic-validator":
            raise PacketError("serialized check ruling actor does not match its validator")
        if validator_receipt["receipt_id"] in bound_validator_ids:
            raise PacketError("serialized validator receipt cannot prove more than one check")
        bound_validator_ids.add(validator_receipt["receipt_id"])
        if seen_evidence.intersection(evidence_ids):
            raise PacketError("serialized check evidence binding is not check-specific")
        seen_evidence.update(evidence_ids)
    if observed_ids != expected_ids:
        raise PacketError("serialized checks must preserve the exact nineteen-check inventory")
    validator_receipt_ids = {
        item["receipt_id"] for item in derivation_receipts
        if isinstance(item.get("actor"), dict)
        and isinstance(item["actor"].get("actor_id"), str)
        and item["actor"]["actor_id"].startswith("m0-validator-chk-")
    }
    if bound_validator_ids != validator_receipt_ids or len(bound_validator_ids) != 19:
        raise PacketError("serialized packet must bind exactly one validator receipt per check")


def _verify_gap_check_correspondence(
    gaps: list[Mapping[str, Any]], checks: list[Mapping[str, Any]],
) -> None:
    issues = {
        item["check_id"]: item for item in checks
        if item["outcome"] in {
            CheckOutcome.FAIL.value, CheckOutcome.MISSING.value, CheckOutcome.UNKNOWN.value,
        }
    }
    matched: set[str] = set()
    for gap in gaps:
        if gap["kind"] == CoverageGapKind.SHARED_SOURCE_SNAPSHOT.value:
            continue
        reason = gap["reason"]
        check_id = reason.split(":", 1)[0] if ":" in reason else ""
        check = issues.get(check_id)
        expected_rule = check["materiality_rule_id"] if check and check["materiality"] != Materiality.UNKNOWN.value else MISSING
        if (
            check is None
            or check_id in matched
            or gap["kind"] != CoverageGapKind.UNCHECKED_PLANE.value
            or reason != f"{check_id}: {check['reason']}"
            or gap["next_safe_check"] != check["reopen_condition"]
            or gap["materiality"] != check["materiality"]
            or gap["rule_source"] != expected_rule
            or gap["evidence_refs"] != check["receipt_ids"]
        ):
            raise PacketError("serialized Coverage Gap/check correspondence is not exact")
        matched.add(check_id)
    if matched != set(issues):
        raise PacketError("serialized Coverage Gap/check correspondence is not exact")


def invalidate_acknowledgement(
    acknowledgement: PacketAcknowledgement,
    superseding_packet: "FlightReadinessPacket",
) -> PacketAcknowledgement:
    if superseding_packet.supersedes_digest != acknowledgement.packet_digest:
        raise PacketError("superseding packet does not name the acknowledged packet")
    return PacketAcknowledgement(
        packet_digest=acknowledgement.packet_digest,
        reviewer=acknowledgement.reviewer,
        state="invalidated",
        invalidated_by=superseding_packet.packet_digest,
    )


@dataclass(frozen=True)
class FlightReadinessPacket:
    contract: ExperimentReadContract
    core_check_set: CoreCheckSet
    checks: tuple[CheckResult, ...]
    source_receipts: tuple[Receipt, ...]
    derivation_receipts: tuple[Receipt, ...]
    coverage_gaps: tuple[CoverageGap, ...]
    disagreements: tuple[Mapping[str, Any], ...]
    analysis_use: AnalysisUse
    blockers: tuple[str, ...]
    next_safe_action: NextSafeAction
    human_state: HumanState
    authorization_state: AuthorizationState
    redaction_state: RedactionState
    expiry: str
    admitted_evidence: AdmittedEvidenceIdentity | None = None
    predecessor_digest: str | Sentinel = MISSING
    supersedes_digest: str | Sentinel = MISSING
    packet_digest: str = field(init=False)

    def __post_init__(self) -> None:
        if not isinstance(self.contract, ExperimentReadContract):
            raise TypeError("contract must be ExperimentReadContract")
        if not isinstance(self.core_check_set, CoreCheckSet):
            raise TypeError("core_check_set must be CoreCheckSet")
        if not isinstance(self.analysis_use, AnalysisUse):
            raise TypeError("analysis_use must be AnalysisUse")
        if self.admitted_evidence is not None and not isinstance(
            self.admitted_evidence, AdmittedEvidenceIdentity,
        ):
            raise TypeError("admitted_evidence must be typed AdmittedEvidenceIdentity or None")
        if self.contract.evidence_class is not EvidenceClass.FIXTURE:
            raise PacketError("local packet must be fixture class")
        object.__setattr__(self, "checks", tuple(self.checks))
        object.__setattr__(self, "source_receipts", tuple(self.source_receipts))
        object.__setattr__(self, "derivation_receipts", tuple(self.derivation_receipts))
        object.__setattr__(self, "coverage_gaps", tuple(self.coverage_gaps))
        object.__setattr__(self, "disagreements", deep_freeze(self.disagreements))
        object.__setattr__(self, "blockers", tuple(self.blockers))
        if tuple(item.check_id for item in self.checks) != self.core_check_set.check_ids:
            raise PacketError("packet checks must match the sealed nineteen-check set exactly once")
        if len({item.check_id for item in self.checks}) != 19:
            raise PacketError("packet checks contain a duplicate or omission")
        if not self.source_receipts or not self.derivation_receipts:
            raise PacketError("packet requires source and independent derivation receipts")
        if {item.receipt_id for item in self.source_receipts} & {item.receipt_id for item in self.derivation_receipts}:
            raise PacketError("source and derivation receipts must be distinct")
        check_outcomes = {item.check_id: item.outcome for item in self.checks}
        for receipt in self.source_receipts:
            receipt_not_admitted = (
                receipt.source != self.contract.source
                or receipt.observed_interval != self.contract.analysis_window
                or receipt.authorization_state is not self.contract.authorization_state
                or receipt.redaction_state is not self.contract.redaction_state
                or receipt.outcome != "trusted"
                or not receipt.has_body()
            )
            if receipt_not_admitted and check_outcomes.get("CHK-16") not in {
                CheckOutcome.FAIL, CheckOutcome.MISSING, CheckOutcome.UNKNOWN
            }:
                raise PacketError("source receipts must be admitted under the sealed contract")
        for receipt in self.derivation_receipts:
            if (
                receipt.source != self.contract.source
                or receipt.observed_interval != self.contract.analysis_window
                or self.contract.contract_digest not in receipt.derivation_inputs
            ):
                raise PacketError("derivation receipts must bind the sealed contract source and interval")
        admitted_document = (
            None if self.admitted_evidence is None else self.admitted_evidence.to_canonical()
        )
        canonical_contract = canonical_loads(
            canonical_encode(self.contract.to_canonical()).decode("utf-8")
        )
        canonical_sources = canonical_loads(canonical_encode(
            [item.to_canonical() for item in self.source_receipts]
        ).decode("utf-8"))
        canonical_derivations = canonical_loads(canonical_encode(
            [item.to_canonical() for item in self.derivation_receipts]
        ).decode("utf-8"))
        admitted_id = _verify_serialized_admitted_evidence(
            admitted_document,
            canonical_sources,
            canonical_contract,
        )
        trusted_source_body = None
        if self.admitted_evidence is not None:
            admitted_source = next(
                (
                    item for item in self.source_receipts
                    if item.receipt_id == self.admitted_evidence.source_receipt_id
                ),
                None,
            )
            if admitted_source is not None and admitted_source.has_body():
                trusted_source_body = admitted_source.body
        _verify_authoritative_source_body(
            admitted_document, canonical_sources, trusted_source_body,
        )
        _verify_serialized_checks(
            canonical_loads(canonical_encode(
                [item.to_canonical() for item in self.checks]
            ).decode("utf-8")),
            canonical_sources,
            canonical_derivations,
            self.contract.contract_digest,
            admitted_document,
            admitted_id,
        )
        if self.authorization_state is not self.contract.authorization_state:
            raise PacketError("packet authorization must match the sealed contract")
        if self.redaction_state is not self.contract.redaction_state:
            raise PacketError("packet redaction must match the sealed contract")
        expected_use, expected_blockers, expected_action = derive_readiness(self.checks)
        if self.analysis_use is not expected_use:
            raise PacketError("analysis_use must be derived exactly from the sealed checks")
        if self.blockers != expected_blockers:
            raise PacketError("blockers must be derived exactly from the sealed checks")
        if self.next_safe_action != expected_action:
            raise PacketError("next_safe_action must be derived exactly from the sealed checks")
        issue_ids = {
            item.check_id for item in self.checks
            if item.outcome in {CheckOutcome.FAIL, CheckOutcome.MISSING, CheckOutcome.UNKNOWN}
        }
        gap_ids = {
            item.reason.split(":", 1)[0]
            for item in self.coverage_gaps
            if isinstance(item.reason, str) and ":" in item.reason
        }
        if not issue_ids.issubset(gap_ids):
            raise PacketError("every failed, missing, or unknown check requires a matching Coverage Gap")
        if any(
            gap.kind is not CoverageGapKind.SHARED_SOURCE_SNAPSHOT
            and gap.reason.split(":", 1)[0] not in issue_ids
            for gap in self.coverage_gaps
        ):
            raise PacketError("Coverage Gaps cannot contradict the sealed check outcomes")
        validate_timestamp(self.expiry, "packet.expiry")
        object.__setattr__(self, "packet_digest", content_digest(self._identity_payload()))

    @property
    def post_analysis_eligibility(self) -> PostAnalysisEligibility:
        return (
            PostAnalysisEligibility.ELIGIBLE
            if self.analysis_use is AnalysisUse.DECISION_GRADE
            else PostAnalysisEligibility.BLOCKED
        )

    def _identity_payload(self) -> dict[str, Any]:
        return {
            "schema_version": "flight-readiness-packet/v1",
            "evidence_class": self.contract.evidence_class.value,
            "frozen_binding": self.contract.binding.to_canonical(),
            "contract": self.contract.to_canonical(),
            "core_check_set": self.core_check_set.to_canonical(),
            "checks": [item.to_canonical() for item in self.checks],
            "source_receipts": [item.to_canonical() for item in self.source_receipts],
            "derivation_receipts": [item.to_canonical() for item in self.derivation_receipts],
            "admitted_evidence": None if self.admitted_evidence is None else self.admitted_evidence.to_canonical(),
            "coverage_gaps": [item.to_canonical() for item in self.coverage_gaps],
            "disagreements": list(self.disagreements),
            "analysis_use": self.analysis_use.value,
            "blockers": list(self.blockers),
            "next_safe_action": self.next_safe_action.to_canonical(),
            "human_state": self.human_state.to_canonical(),
            "authorization_state": self.authorization_state.value,
            "redaction_state": self.redaction_state.value,
            "expiry": self.expiry,
            "predecessor_digest": self.predecessor_digest,
            "supersedes_digest": self.supersedes_digest,
        }

    def to_canonical(self) -> dict[str, Any]:
        payload = self._identity_payload()
        payload["packet_digest"] = self.packet_digest
        return payload

    def serialize(self) -> bytes:
        return canonical_encode(self.to_canonical())

    @classmethod
    def deserialize(
        cls,
        payload: bytes,
        *,
        expected_packet_digest: str | None = None,
        trusted_source_body: Mapping[str, Any] | None = None,
    ) -> Mapping[str, Any]:
        """Verify the complete sealed identity graph before exposing a document."""
        if not isinstance(payload, bytes):
            raise TypeError("serialized packet payload must be bytes")
        if expected_packet_digest is None:
            raise PacketError("trusted expected packet digest is required")
        if not is_digest(expected_packet_digest):
            raise PacketError("trusted expected packet digest mismatch")
        document = canonical_loads(payload.decode("utf-8"))
        if not isinstance(document, dict):
            raise PacketError("serialized packet must be an object")
        _exact_keys(
            document,
            {
                "schema_version", "evidence_class", "frozen_binding", "contract",
                "core_check_set", "checks", "source_receipts", "derivation_receipts",
                "admitted_evidence",
                "coverage_gaps", "disagreements", "analysis_use", "blockers",
                "next_safe_action", "human_state", "authorization_state", "redaction_state",
                "expiry", "predecessor_digest", "supersedes_digest", "packet_digest",
            },
            "packet",
        )
        if document.get("schema_version") != "flight-readiness-packet/v1":
            raise PacketError("serialized packet schema version mismatch")
        human_state = _mapping(document.get("human_state"), "human state")
        _exact_keys(
            human_state,
            {"experiment_owner", "independent_ds_consultant", "committee_route", "acknowledgement_state"},
            "human state",
        )
        if human_state["acknowledgement_state"] not in {"not_requested", "pending", "acknowledged", "invalidated"}:
            raise PacketError("serialized acknowledgement state is invalid")
        if not isinstance(document.get("disagreements"), list) or not all(
            isinstance(item, dict) for item in document["disagreements"]
        ):
            raise PacketError("serialized disagreements must be object records")
        if not isinstance(document.get("blockers"), list) or not all(
            isinstance(item, str) for item in document["blockers"]
        ):
            raise PacketError("serialized blockers must be check IDs")
        validate_timestamp(document.get("expiry"), "serialized packet.expiry")
        stated_digest = document.get("packet_digest")
        identity = dict(document)
        identity.pop("packet_digest", None)
        if stated_digest != content_digest(identity):
            raise PacketError("serialized packet digest mismatch")
        contract = _mapping(document.get("contract"), "contract")
        _verify_serialized_contract(contract)
        if document.get("frozen_binding") != contract.get("binding"):
            raise PacketError("serialized packet and contract frozen binding mismatch")
        if document.get("evidence_class") != contract.get("evidence_class"):
            raise PacketError("serialized packet evidence class mismatch")
        _verify_serialized_core_set(_mapping(document.get("core_check_set"), "core check set"))
        source_receipts = document.get("source_receipts")
        derivation_receipts = document.get("derivation_receipts")
        if not isinstance(source_receipts, list) or not source_receipts:
            raise PacketError("serialized packet requires source receipts")
        if not isinstance(derivation_receipts, list) or not derivation_receipts:
            raise PacketError("serialized packet requires derivation receipts")
        receipts = source_receipts + derivation_receipts
        for raw in receipts:
            _verify_serialized_receipt(_mapping(raw, "receipt"))
        receipt_ids = {item["receipt_id"] for item in receipts}
        if len(receipt_ids) != len(receipts):
            raise PacketError("serialized packet receipt identities must be unique")
        if set(item["receipt_id"] for item in source_receipts) & set(
            item["receipt_id"] for item in derivation_receipts
        ):
            raise PacketError("serialized source and derivation receipts must be distinct")
        contract_digest = contract["contract_digest"]
        if any(contract_digest not in item["derivation_inputs"] for item in derivation_receipts):
            raise PacketError("serialized derivation receipt must bind the contract digest")
        gaps = document.get("coverage_gaps")
        if not isinstance(gaps, list):
            raise PacketError("serialized Coverage Gaps must be a list")
        for raw in gaps:
            gap = _mapping(raw, "Coverage Gap")
            _verify_serialized_gap(gap)
            if any(reference not in receipt_ids for reference in gap["evidence_refs"]):
                raise PacketError("serialized Coverage Gap evidence binding is not present in the packet")
        raw_checks = document.get("checks")
        if not isinstance(raw_checks, list):
            raise PacketError("serialized packet checks must be a list")
        admitted_document = document.get("admitted_evidence")
        admitted_id = _verify_serialized_admitted_evidence(
            admitted_document, source_receipts, contract,
        )
        _verify_serialized_checks(
            raw_checks, source_receipts, derivation_receipts, contract_digest,
            admitted_document, admitted_id,
        )
        check_outcomes = {item["check_id"]: item["outcome"] for item in raw_checks}
        for receipt in source_receipts:
            admitted = (
                receipt["source"] == contract["source"]
                and receipt["observed_interval"] == contract["analysis_window"]
                and receipt["authorization_state"] == contract["authorization_state"] == "authorized"
                and receipt["redaction_state"] == contract["redaction_state"]
                and receipt["outcome"] == "trusted"
                and isinstance(receipt["body_digest"], str)
                and is_digest(receipt["body_digest"])
            )
            if not admitted and check_outcomes.get("CHK-16") not in {"FAIL", "MISSING", "UNKNOWN"}:
                raise PacketError("serialized source receipt is not admitted under the contract")
        for receipt in derivation_receipts:
            if (
                receipt["source"] != contract["source"]
                or receipt["observed_interval"] != contract["analysis_window"]
                or receipt["authorization_state"] != contract["authorization_state"]
                or receipt["redaction_state"] != contract["redaction_state"]
            ):
                raise PacketError("serialized derivation receipt does not bind the contract")
        issues = [
            item for item in raw_checks
            if item.get("outcome") in {"FAIL", "MISSING", "UNKNOWN"}
            and item.get("materiality") in {"material", "unknown"}
        ]
        issue_ids = {item.get("check_id") for item in issues}
        directional_reasons = {
            "CHK-02": "runtime below preregistered threshold",
            "CHK-19": "sample below preregistered threshold",
        }
        if issues and issue_ids.issubset({"CHK-02", "CHK-19"}) and all(
            item.get("outcome") == "FAIL"
            and item.get("reason") == directional_reasons.get(item.get("check_id"))
            for item in issues
        ):
            expected_use = "directional_only"
            expected_action = {
                "kind": "evidence_collection",
                "guidance": "collect the preregistered runtime or sample units",
                "reopen_condition": "new read after the preregistered threshold",
            }
        elif issues:
            expected_use = "not_permitted"
            kind = (
                "contract_correction"
                if any(item.get("check_id") == "CHK-19" and item.get("outcome") == "MISSING" for item in issues)
                else "evidence_collection"
                if any(item.get("outcome") in {"MISSING", "UNKNOWN"} for item in issues)
                else "validity_fix"
            )
            expected_action = {
                "kind": kind,
                "guidance": "resolve the recorded material blockers without changing history",
                "reopen_condition": "superseding evidence and a new sealed packet",
            }
        else:
            expected_use = "decision_grade"
            expected_action = {
                "kind": "evidence_collection",
                "guidance": "route the sealed packet for human review",
                "reopen_condition": "a named human reviews this exact packet digest",
            }
        if document.get("analysis_use") != expected_use:
            raise PacketError("serialized analysis_use is inconsistent with checks")
        if document.get("blockers") != [item.get("check_id") for item in issues]:
            raise PacketError("serialized blockers are inconsistent with checks")
        if document.get("next_safe_action") != expected_action:
            raise PacketError("serialized next_safe_action is inconsistent with checks")
        _verify_gap_check_correspondence(gaps, raw_checks)
        if document.get("authorization_state") != contract.get("authorization_state"):
            raise PacketError("serialized packet authorization state mismatch")
        if document.get("redaction_state") != contract.get("redaction_state"):
            raise PacketError("serialized packet redaction state mismatch")
        if stated_digest != expected_packet_digest:
            raise PacketError("trusted expected packet digest mismatch")
        _verify_authoritative_source_body(
            admitted_document, source_receipts, trusted_source_body,
        )
        return deep_freeze(document)


def synthetic_review_projection(packet: FlightReadinessPacket) -> Mapping[str, Any]:
    """Packet-centered pre-P3 view; it has no cause, recommendation, or diff field."""
    return deep_freeze(
        {
            "scenario_id": "VAL-UI-001",
            "projection_class": "synthetic_packet_projection",
            "packet_digest": packet.packet_digest,
            "analysis_use": packet.analysis_use.value,
            "post_analysis_eligibility": packet.post_analysis_eligibility.value,
            "blockers": list(packet.blockers),
            "coverage_gaps": [gap.to_canonical() for gap in packet.coverage_gaps],
            "disagreements": list(packet.disagreements),
            "source_receipt_ids": [item.receipt_id for item in packet.source_receipts],
            "derivation_receipt_ids": [item.receipt_id for item in packet.derivation_receipts],
            "check_receipt_ids": [receipt_id for check in packet.checks for receipt_id in check.receipt_ids],
            "next_safe_action": packet.next_safe_action.to_canonical(),
            "human_state": packet.human_state.to_canonical(),
            "live_review_scenario": "VAL-UI-101:open_external_P3_gate",
        }
    )
