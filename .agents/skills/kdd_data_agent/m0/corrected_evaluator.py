"""Correction-run evaluator: contract-bound evidence and explicit validators."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import erfc, sqrt
from typing import Any, Mapping

from ..adapters.base import ReadResult
from ..adapters.outcomes import ReadOutcome
from ..core.coverage_gap import CoverageGap, CoverageGapKind, Materiality
from ..core.digest import content_digest
from ..core.identity import Actor, ActorKind, AuthorizationState, RedactionState
from ..core.receipts import Receipt, ReceiptKind
from ..core.unknown import MISSING, is_sentinel
from .checks import CHECK_REGISTRY, CheckOutcome, CoreCheckSet, ValidatorResult, evaluate_checks
from .contracts import ExperimentReadContract, IndependenceClass, SufficiencyKind
from .packet import (
    AdmittedEvidenceIdentity,
    FlightReadinessPacket,
    HumanState,
    admitted_evidence_identity,
    decision_metric_output_from_source_body,
    derive_readiness,
    validator_evidence_identity,
)


class EvaluationHardVeto(str, Enum):
    FALSE_READINESS = "false_readiness"
    CROSS_CASE_OR_TENANT_LEAKAGE = "cross_case_or_tenant_leakage"
    SECRET_EXPOSURE = "secret_exposure"
    UNSAFE_REDACTION = "unsafe_redaction"
    WRITE_REACHABILITY = "write_reachability"
    UNAUTHORIZED_DELIVERY = "unauthorized_delivery"


@dataclass(frozen=True)
class DecisionMetricOutput:
    metric_id: str
    definition_version: str
    source_version: str
    cuped_mode: str
    unit: str
    value: int | float | str

    def __post_init__(self) -> None:
        values = {
            "metric_id": self.metric_id,
            "definition_version": self.definition_version,
            "source_version": self.source_version,
            "cuped_mode": self.cuped_mode,
            "unit": self.unit,
        }
        for name, value in values.items():
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} is required")
        if isinstance(self.value, bool) or not isinstance(self.value, (int, float, str)):
            raise TypeError("value must be an integer, float, or canonical string")

    def to_canonical(self) -> dict[str, Any]:
        return {
            "metric_id": self.metric_id,
            "definition_version": self.definition_version,
            "source_version": self.source_version,
            "cuped_mode": self.cuped_mode,
            "unit": self.unit,
            "value": self.value,
        }


@dataclass(frozen=True)
class EvidenceRecord:
    evidence_id: str
    receipt_id: str
    contract_digest: str
    output: DecisionMetricOutput
    observed: bool = True

    def __post_init__(self) -> None:
        expected = admitted_evidence_identity(
            self.receipt_id, self.contract_digest, self.output.to_canonical(), self.observed,
        )
        if self.evidence_id != expected:
            raise ValueError("evidence_id must match the canonical admitted evidence identity")

    def to_admitted_evidence(self) -> AdmittedEvidenceIdentity:
        return AdmittedEvidenceIdentity(
            self.receipt_id, self.contract_digest, self.output.to_canonical(), self.observed,
        )


def _output(result: ReadResult) -> DecisionMetricOutput | None:
    projected = decision_metric_output_from_source_body(result.body)
    if projected is None:
        return None
    try:
        return DecisionMetricOutput(**projected)
    except (TypeError, ValueError):
        return None


def _admission_failures(result: ReadResult, contract: ExperimentReadContract) -> tuple[str, ...]:
    receipt, metric, output = result.receipt, contract.metrics[0], _output(result)
    failures: list[str] = []
    if result.outcome is not ReadOutcome.TRUSTED or not result.has_body():
        failures.append("trusted retained body required")
    if result.request.source_id != contract.source.source_id or receipt.source != contract.source:
        failures.append("source or snapshot mismatch")
    if receipt.observed_interval != contract.analysis_window:
        failures.append("interval mismatch")
    if receipt.authorization_state is not contract.authorization_state or receipt.authorization_state is not AuthorizationState.AUTHORIZED:
        failures.append("authorization mismatch")
    if receipt.redaction_state is not contract.redaction_state or receipt.redaction_state not in {RedactionState.NOT_REQUIRED, RedactionState.APPLIED}:
        failures.append("redaction mismatch")
    if receipt.detail.get("recipient_scope") != contract.recipient_scope:
        failures.append("recipient mismatch")
    expected = (metric.metric_id, metric.definition_version, metric.source_version, metric.cuped_mode, metric.unit)
    actual = None if output is None else (
        output.metric_id, output.definition_version, output.source_version, output.cuped_mode, output.unit
    )
    if actual != expected:
        failures.append("metric or contract identity mismatch")
    return tuple(failures)


def admit_observed_evidence(result: ReadResult, contract: ExperimentReadContract | None = None) -> EvidenceRecord | None:
    if not isinstance(result, ReadResult):
        raise TypeError("result must be a ReadResult")
    output = _output(result)
    if output is None or result.outcome is not ReadOutcome.TRUSTED or not result.has_body():
        return None
    if result.receipt.authorization_state is not AuthorizationState.AUTHORIZED:
        return None
    if result.receipt.redaction_state not in {RedactionState.NOT_REQUIRED, RedactionState.APPLIED}:
        return None
    if contract is not None and _admission_failures(result, contract):
        return None
    contract_digest = "unbound" if contract is None else contract.contract_digest
    return EvidenceRecord(
        admitted_evidence_identity(
            result.receipt.receipt_id, contract_digest, output.to_canonical(), True,
        ),
        result.receipt.receipt_id,
        contract_digest,
        output,
    )


@dataclass(frozen=True)
class RecomputationEvidence:
    reported_result: ReadResult
    admitted_reported: EvidenceRecord | None
    reported_output: DecisionMetricOutput | None
    recomputed_output: DecisionMetricOutput
    recomputed_receipt: Receipt
    independence_class: IndependenceClass
    shared_source_gap: CoverageGap
    comparison_rule_id: str
    comparison_matches: bool
    comparator_digest: str
    admission_failures: tuple[str, ...]

    @property
    def reported_receipt(self) -> Receipt:
        return self.reported_result.receipt


def build_recomputation_evidence(
    contract: ExperimentReadContract,
    reported_result: ReadResult,
    *,
    recomputed_output: DecisionMetricOutput,
    independence_class: IndependenceClass = IndependenceClass.INDEPENDENT_TRANSFORM,
) -> RecomputationEvidence:
    if not isinstance(reported_result, ReadResult):
        raise TypeError("reported_result must be a typed ReadResult")
    if not isinstance(recomputed_output, DecisionMetricOutput):
        raise TypeError("recomputed_output must be typed")
    failures, reported = _admission_failures(reported_result, contract), _output(reported_result)
    rule_id = contract.decision_metric_policy.comparison_rule_id
    matches = rule_id == "m0-comparison-rule/v1" and reported is not None and reported.to_canonical() == recomputed_output.to_canonical()
    comparator_digest = content_digest({
        "comparator": "exact-typed-output/v1", "rule_id": rule_id,
        "reported": None if reported is None else reported.to_canonical(),
        "recomputed": recomputed_output.to_canonical(),
    })
    source_receipt = reported_result.receipt
    recomputed = Receipt(
        receipt_kind=ReceiptKind.DERIVATION,
        source=contract.source,
        actor=Actor("m0-independent-transform/v1", ActorKind.DETERMINISTIC_VALIDATOR),
        authorization_state=contract.authorization_state,
        redaction_state=contract.redaction_state,
        observed_interval=contract.analysis_window,
        recorded_at=contract.expiry,
        outcome="recomputed_decision_metric",
        derivation_inputs=(source_receipt.receipt_id, contract.contract_digest),
        detail={
            "independence_class": independence_class.value,
            "transform_id": "m0-independent-transform/v1",
            "input_manifest_digest": source_receipt.digest,
            "transform_digest": content_digest({"transform": "m0-independent-transform/v1"}),
            "reported_output_digest": None if reported is None else content_digest(reported.to_canonical()),
            "recomputed_output_digest": content_digest(recomputed_output.to_canonical()),
            "comparison_rule_id": rule_id,
            "comparator_digest": comparator_digest,
            "comparison_matches": matches,
            "contract_digest": contract.contract_digest,
            "decision_bindings": ["D4", "D6"],
        },
    )
    gap = CoverageGap(
        CoverageGapKind.SHARED_SOURCE_SNAPSHOT,
        "reported and recomputed values share the immutable authoritative snapshot",
        "an independently lineaged source remains optional behind P2",
        evidence_refs=(source_receipt.receipt_id, recomputed.receipt_id),
    )
    return RecomputationEvidence(
        reported_result, admit_observed_evidence(reported_result, contract), reported, recomputed_output,
        recomputed, independence_class, gap, rule_id, matches, comparator_digest, failures,
    )


@dataclass(frozen=True)
class RawCheckObservation:
    check_id: str
    payload: Mapping[str, Any]
    source_receipt_id: str
    source_body_digest: Any


@dataclass(frozen=True)
class ValidatorDecision:
    outcome: CheckOutcome
    reason: str
    materiality: Materiality = Materiality.MATERIAL
    rule_source: str | None = None


@dataclass(frozen=True)
class ValidatorContext:
    contract: ExperimentReadContract
    evidence: RecomputationEvidence
    body: Mapping[str, Any]
    disagreements: tuple[dict[str, Any], ...]


def _compare_observation(observation: RawCheckObservation, expected: Mapping[str, Any], reason: str) -> ValidatorDecision:
    if set(observation.payload) != set(expected):
        return ValidatorDecision(CheckOutcome.UNKNOWN, f"malformed observation schema for {observation.check_id}", Materiality.UNKNOWN)
    if content_digest(dict(observation.payload)) != content_digest(dict(expected)):
        return ValidatorDecision(CheckOutcome.FAIL, reason)
    return ValidatorDecision(CheckOutcome.PASS, f"{observation.check_id} deterministic validator passed")


def validate_chk_01(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    return _compare_observation(obs, {"flight_id": ctx.contract.flight_id, "contract_version": ctx.contract.contract_version}, "flight or contract identity mismatch")


def validate_chk_02(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    expected = {"observed_runtime_units": ctx.contract.observed_runtime_units}
    compared = _compare_observation(obs, expected, "observed runtime does not bind the contract")
    if compared.outcome is not CheckOutcome.PASS:
        return compared
    if ctx.contract.observed_runtime_units < ctx.contract.sufficiency_rule.runtime_threshold_units:
        return ValidatorDecision(CheckOutcome.FAIL, "runtime below preregistered threshold")
    return compared


def validate_chk_03(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    metric = ctx.contract.metrics[0]
    expected = {"metric_id": metric.metric_id, "definition_version": metric.definition_version, "role": metric.role.value, "policy_id": ctx.contract.decision_metric_policy.policy_id}
    compared = _compare_observation(obs, expected, "decision metric registration or policy mismatch")
    if ctx.evidence.reported_output is None or ctx.evidence.reported_output.definition_version != metric.definition_version:
        return ValidatorDecision(CheckOutcome.FAIL, "metric-definition version mismatch")
    return compared


def validate_chk_04(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    metric = ctx.contract.metrics[0]
    expected = {"assignment_unit": ctx.contract.assignment_unit, "analysis_unit": ctx.contract.analysis_unit, "metric_unit": metric.unit, "variance_method": metric.ratio_variance_method}
    if metric.unit == "ratio" and is_sentinel(metric.ratio_variance_method):
        return ValidatorDecision(CheckOutcome.FAIL, "ratio variance method missing")
    return _compare_observation(obs, expected, "assignment, analysis unit, or variance method mismatch")


def validate_chk_05(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    if ctx.contract.arm_parity_applicability_rule_id == "m0-alignment-v1#arm-parity-applicability":
        return ValidatorDecision(CheckOutcome.NOT_APPLICABLE, "arm parity versioned not applicable", Materiality.NON_MATERIAL, "m0-alignment-v1#arm-parity-applicability")
    if len(ctx.contract.arms) < 2 or not all(arm.complete for arm in ctx.contract.arms):
        return ValidatorDecision(CheckOutcome.MISSING, "required per-arm identity missing")
    exposure_counts = ctx.body.get("exposure_counts")
    expected = {"arm_ids": [arm.arm_id for arm in ctx.contract.arms], "exposure_counts": exposure_counts}
    compared = _compare_observation(obs, expected, "assignment, exposure, or arm identity mismatch")
    if ctx.contract.arm_parity_consistent is not True:
        return ValidatorDecision(CheckOutcome.FAIL, "applicable arm identities diverge")
    return compared


def validate_chk_06(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    payload = obs.payload
    required = {"observed_counts", "expected_proportions", "preregistered_alpha"}
    if set(payload) != required or not isinstance(payload.get("observed_counts"), Mapping) or not isinstance(payload.get("expected_proportions"), Mapping):
        return ValidatorDecision(CheckOutcome.UNKNOWN, "malformed SRM observation", Materiality.UNKNOWN)
    counts, proportions, alpha = payload["observed_counts"], payload["expected_proportions"], payload["preregistered_alpha"]
    if counts != ctx.body.get("exposure_counts") or set(counts) != set(proportions) or any(isinstance(v, bool) or not isinstance(v, int) or v < 0 for v in counts.values()):
        return ValidatorDecision(CheckOutcome.FAIL, "SRM counts do not bind the admitted exposure observations")
    if isinstance(alpha, bool) or not isinstance(alpha, (int, float)) or not 0 < alpha < 1 or abs(sum(proportions.values()) - 1.0) > 1e-12:
        return ValidatorDecision(CheckOutcome.UNKNOWN, "invalid preregistered SRM inputs", Materiality.UNKNOWN)
    total = sum(counts.values())
    expected_counts = {key: total * proportions[key] for key in counts}
    if any(value <= 0 for value in expected_counts.values()):
        return ValidatorDecision(CheckOutcome.UNKNOWN, "SRM expected counts must be positive", Materiality.UNKNOWN)
    chi_square = sum((counts[key] - expected_counts[key]) ** 2 / expected_counts[key] for key in counts)
    p_value = erfc(sqrt(chi_square / 2.0))
    return ValidatorDecision(CheckOutcome.PASS if p_value >= alpha else CheckOutcome.FAIL, "SRM calculation passed" if p_value >= alpha else "SRM calculation failed preregistered alpha")


def validate_chk_07(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    expected = {"population": ctx.contract.population, "eligibility": ctx.contract.eligibility, "exclusions": list(ctx.contract.exclusions), "tenant_scope": ctx.contract.tenant_scope, "surface": ctx.contract.surface, "locale": ctx.contract.locale}
    return _compare_observation(obs, expected, "population, eligibility, exclusions, or scope mismatch")


def validate_chk_08(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    payload = obs.payload
    required = {"numerator", "denominator", "value", "operation", "join_keys", "unit"}
    if set(payload) != required:
        return ValidatorDecision(CheckOutcome.UNKNOWN, "malformed arithmetic observation", Materiality.UNKNOWN)
    numerator, denominator, value = payload["numerator"], payload["denominator"], payload["value"]
    if any(isinstance(item, bool) or not isinstance(item, (int, float)) for item in (numerator, denominator, value)) or denominator == 0:
        return ValidatorDecision(CheckOutcome.UNKNOWN, "invalid arithmetic inputs", Materiality.UNKNOWN)
    expected = {
        "numerator": ctx.body.get("numerator"), "denominator": ctx.body.get("denominator"),
        "value": ctx.body.get("value"), "operation": "numerator_over_denominator",
        "join_keys": list(ctx.contract.join_keys), "unit": ctx.contract.metrics[0].unit,
    }
    if content_digest(dict(payload)) != content_digest(expected) or abs(value - numerator / denominator) > 1e-15:
        return ValidatorDecision(CheckOutcome.FAIL, "numerator, denominator, join, unit, or ratio arithmetic mismatch")
    return ValidatorDecision(CheckOutcome.PASS, "CHK-08 deterministic validator passed")


def validate_chk_09(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    expected = {"page_count": 1, "expected_page_count": 1, "partial_read": False, "late_arrival_count": 0, "snapshot_id": ctx.contract.source.snapshot_id}
    return _compare_observation(obs, expected, "completeness, pagination, freshness, or late-arrival failure")


def validate_chk_10(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    metric = ctx.contract.metrics[0]
    return _compare_observation(obs, {"estimator": metric.estimator, "variance_method": metric.ratio_variance_method}, "estimator or variance method mismatch")


def validate_chk_11(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    metric = ctx.contract.metrics[0]
    expected = {"reported_cuped_mode": metric.cuped_mode, "registered_cuped_mode": metric.cuped_mode}
    if ctx.evidence.reported_output is None or ctx.evidence.reported_output.cuped_mode != metric.cuped_mode:
        return ValidatorDecision(CheckOutcome.FAIL, "CUPED mode mismatch")
    return _compare_observation(obs, expected, "CUPED mode mismatch")


def validate_chk_12(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    metric, source = ctx.contract.metrics[0], ctx.contract.source
    expected = {"source_id": source.source_id, "snapshot_id": source.snapshot_id, "source_version": metric.source_version, "source_owner": source.owner, "metric_owner": metric.owner}
    if ctx.evidence.reported_output is None or ctx.evidence.reported_output.source_version != metric.source_version:
        return ValidatorDecision(CheckOutcome.FAIL, "source version mismatch")
    return _compare_observation(obs, expected, "source, snapshot, lineage, definition, or owner mismatch")


def validate_chk_13(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    expected = {"primary_value": ctx.body.get("value"), "scorecard_value": ctx.body.get("value"), "unit": ctx.contract.metrics[0].unit}
    return _compare_observation(obs, expected, "primary source and scorecard do not reconcile")


def validate_chk_14(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    expected = {"comparison_rule_id": ctx.contract.decision_metric_policy.comparison_rule_id, "independence_class": ctx.evidence.independence_class.value}
    compared = _compare_observation(obs, expected, "comparison rule or independence class mismatch")
    if compared.outcome is not CheckOutcome.PASS:
        return compared
    if ctx.evidence.independence_class is IndependenceClass.SAME_PIPELINE:
        return ValidatorDecision(CheckOutcome.UNKNOWN, "same_pipeline is not independent", Materiality.UNKNOWN)
    if not ctx.evidence.comparison_matches:
        return ValidatorDecision(CheckOutcome.FAIL, "typed outputs disagree")
    return compared


def validate_chk_15(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    version = ctx.contract.metrics[0].source_version
    expected = {"contract_source_version": version, "observed_source_version": version, "change_event_ids": []}
    return _compare_observation(obs, expected, "source change was not revalidated")


def validate_chk_16(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    if ctx.evidence.admission_failures:
        return ValidatorDecision(CheckOutcome.FAIL, "; ".join(ctx.evidence.admission_failures))
    expected = {"recipient_scope": ctx.contract.recipient_scope, "retention_rule_id": ctx.contract.retention_rule_id, "load_limit_rule_id": ctx.contract.load_limit_rule_id, "halt_rule_id": ctx.contract.halt_rule_id, "export_rule_id": ctx.contract.export_rule_id}
    return _compare_observation(obs, expected, "authorization boundary observation contradicts the contract")


def validate_chk_17(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    source = ctx.contract.source
    expected = {"source_id": source.source_id, "snapshot_id": source.snapshot_id, "window": ctx.contract.analysis_window.to_canonical(), "tenant_scope": ctx.contract.tenant_scope}
    return _compare_observation(obs, expected, "cross-read attribution, freshness, or scope mismatch")


def validate_chk_18(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    required = {"open_disagreement_ids", "open_gap_check_ids"}
    if set(obs.payload) != required or not all(isinstance(obs.payload[key], (list, tuple)) for key in required):
        return ValidatorDecision(CheckOutcome.UNKNOWN, "malformed closure observation", Materiality.UNKNOWN)
    if ctx.disagreements:
        return ValidatorDecision(CheckOutcome.UNKNOWN, "named reviewers disagree on materiality", Materiality.UNKNOWN)
    if obs.payload["open_disagreement_ids"] or obs.payload["open_gap_check_ids"]:
        return ValidatorDecision(CheckOutcome.FAIL, "declared disagreement or Coverage Gap remains open")
    return ValidatorDecision(CheckOutcome.PASS, "CHK-18 deterministic validator passed")


def validate_chk_19(ctx: ValidatorContext, obs: RawCheckObservation) -> ValidatorDecision:
    rule = ctx.contract.sufficiency_rule
    if rule.kind is SufficiencyKind.RUNTIME_ONLY:
        compared = _compare_observation(obs, {"sufficiency_kind": "runtime_only", "applicability_rule_id": "m0-alignment-v1#runtime-only-applicability"}, "sufficiency applicability contradicts the contract")
        if compared.outcome is not CheckOutcome.PASS:
            return compared
        return ValidatorDecision(CheckOutcome.NOT_APPLICABLE, "runtime_only applicability", Materiality.NON_MATERIAL, "m0-alignment-v1#runtime-only-applicability")
    if not isinstance(ctx.contract.observed_sample_units, int):
        return ValidatorDecision(CheckOutcome.MISSING, "observed sample units missing")
    expected = {"sufficiency_kind": "runtime_and_sample", "sample_units": ctx.contract.observed_sample_units, "sample_input_ids": list(rule.sample_input_ids)}
    compared = _compare_observation(obs, expected, "sample observation does not bind the preregistered contract")
    if compared.outcome is not CheckOutcome.PASS:
        return compared
    if ctx.contract.observed_sample_units < rule.sample_threshold_units:
        return ValidatorDecision(CheckOutcome.FAIL, "sample below preregistered threshold")
    return compared


_NAMED_VALIDATORS = {
    f"CHK-{index:02d}": validator for index, validator in enumerate((
        validate_chk_01, validate_chk_02, validate_chk_03, validate_chk_04, validate_chk_05,
        validate_chk_06, validate_chk_07, validate_chk_08, validate_chk_09, validate_chk_10,
        validate_chk_11, validate_chk_12, validate_chk_13, validate_chk_14, validate_chk_15,
        validate_chk_16, validate_chk_17, validate_chk_18, validate_chk_19,
    ), 1)
}


def _validators(
    contract: ExperimentReadContract,
    evidence: RecomputationEvidence,
    disagreements: tuple[dict[str, Any], ...],
) -> tuple[dict[str, ValidatorResult], tuple[Receipt, ...]]:
    body = evidence.reported_result.body if isinstance(evidence.reported_result.body, Mapping) else {}
    declared = body.get("check_observations") if isinstance(body, Mapping) else None
    context = ValidatorContext(contract, evidence, body, disagreements)
    results: dict[str, ValidatorResult] = {}
    validator_receipts: list[Receipt] = []
    admitted_payload = (
        None if evidence.admitted_reported is None
        else evidence.admitted_reported.to_admitted_evidence().to_canonical()
    )
    for definition in CHECK_REGISTRY:
        raw = None if not isinstance(declared, Mapping) else declared.get(definition.check_id, MISSING)
        if definition.check_id == "CHK-16" and evidence.admission_failures:
            decision = ValidatorDecision(CheckOutcome.FAIL, "; ".join(evidence.admission_failures))
            observation = None
        elif evidence.admitted_reported is None and definition.check_id not in {"CHK-03", "CHK-11", "CHK-12"}:
            decision = ValidatorDecision(CheckOutcome.UNKNOWN, "reported evidence was not admitted", Materiality.UNKNOWN)
            observation = None
        elif is_sentinel(raw):
            decision = ValidatorDecision(CheckOutcome.MISSING, "raw check observation is absent")
            observation = None
        elif not isinstance(raw, Mapping):
            decision = ValidatorDecision(CheckOutcome.UNKNOWN, "raw check observation is malformed", Materiality.UNKNOWN)
            observation = None
        else:
            observation = RawCheckObservation(
                definition.check_id, raw, evidence.reported_receipt.receipt_id,
                evidence.reported_receipt.body_digest(),
            )
            decision = _NAMED_VALIDATORS[definition.check_id](context, observation)
        observation_digest = content_digest({
            "check_id": definition.check_id,
            "observation": raw,
            "contract_digest": contract.contract_digest,
            "source_receipt_id": evidence.reported_receipt.receipt_id,
        })
        validator_receipt = Receipt(
            receipt_kind=ReceiptKind.DERIVATION,
            source=contract.source,
            actor=Actor(f"m0-validator-{definition.check_id.lower()}/v1", ActorKind.DETERMINISTIC_VALIDATOR),
            authorization_state=contract.authorization_state,
            redaction_state=contract.redaction_state,
            observed_interval=contract.analysis_window,
            recorded_at=contract.expiry,
            outcome=f"{definition.check_id}:{decision.outcome.value}",
            derivation_inputs=(evidence.reported_receipt.receipt_id, contract.contract_digest),
            detail={
                "validator_id": f"m0-{definition.check_id.lower()}-validator/v1",
                "contract_digest": contract.contract_digest,
                "source_receipt_id": evidence.reported_receipt.receipt_id,
                "observation_digest": observation_digest,
                "source_body_digest": evidence.reported_receipt.body_digest(),
                "admitted_evidence_id": None if evidence.admitted_reported is None else evidence.admitted_reported.evidence_id,
                "reason": decision.reason,
            },
        )
        validator_receipts.append(validator_receipt)
        evidence_ids = () if decision.outcome in {CheckOutcome.MISSING, CheckOutcome.UNKNOWN} else (
            validator_evidence_identity(
                definition.check_id, validator_receipt.to_canonical(), admitted_payload,
            ),
        )
        results[definition.check_id] = ValidatorResult(
            decision.outcome,
            evidence_ids,
            (evidence.reported_receipt.receipt_id, validator_receipt.receipt_id),
            decision.materiality,
            decision.reason,
            "supply corrected raw observations in a superseding admitted read",
            decision.rule_source,
        )
    return results, tuple(validator_receipts)


def evaluate_flight(
    contract: ExperimentReadContract,
    recomputation: RecomputationEvidence,
    *,
    disagreements: tuple[dict[str, Any], ...] = (),
    hard_vetoes: tuple[EvaluationHardVeto, ...] = (),
) -> FlightReadinessPacket:
    validators, validator_receipts = _validators(contract, recomputation, disagreements)
    if not all(isinstance(item, EvaluationHardVeto) for item in hard_vetoes):
        raise TypeError("hard vetoes must be typed EvaluationHardVeto values")
    if hard_vetoes:
        admitted_payload = (
            None if recomputation.admitted_reported is None
            else recomputation.admitted_reported.to_admitted_evidence().to_canonical()
        )
        veto_reason = "hard veto: " + ", ".join(item.value for item in hard_vetoes)
        observation_digest = content_digest({
            "check_id": "CHK-16",
            "hard_vetoes": [item.value for item in hard_vetoes],
            "contract_digest": contract.contract_digest,
            "source_receipt_id": recomputation.reported_receipt.receipt_id,
        })
        veto_receipt = Receipt(
            receipt_kind=ReceiptKind.DERIVATION,
            source=contract.source,
            actor=Actor("m0-validator-chk-16/v1", ActorKind.DETERMINISTIC_VALIDATOR),
            authorization_state=contract.authorization_state,
            redaction_state=contract.redaction_state,
            observed_interval=contract.analysis_window,
            recorded_at=contract.expiry,
            outcome="CHK-16:FAIL",
            derivation_inputs=(recomputation.reported_receipt.receipt_id, contract.contract_digest),
            detail={
                "validator_id": "m0-chk-16-validator/v1",
                "contract_digest": contract.contract_digest,
                "source_receipt_id": recomputation.reported_receipt.receipt_id,
                "observation_digest": observation_digest,
                "source_body_digest": recomputation.reported_receipt.body_digest(),
                "admitted_evidence_id": None if recomputation.admitted_reported is None else recomputation.admitted_reported.evidence_id,
                "reason": veto_reason,
            },
        )
        validator_receipts = tuple(
            veto_receipt if item.actor.actor_id == "m0-validator-chk-16/v1" else item
            for item in validator_receipts
        )
        validators["CHK-16"] = ValidatorResult(
            CheckOutcome.FAIL,
            (validator_evidence_identity("CHK-16", veto_receipt.to_canonical(), admitted_payload),),
            (recomputation.reported_receipt.receipt_id, veto_receipt.receipt_id),
            Materiality.MATERIAL,
            veto_reason,
            "remove the forbidden capability or boundary violation and rerun",
        )
    checks = evaluate_checks(contract, validator_results=validators)
    analysis_use, blockers, action = derive_readiness(checks)
    if not recomputation.comparison_matches:
        disagreements = (*disagreements, {
            "kind": "reported_vs_recomputed",
            "reported_receipt_id": recomputation.reported_receipt.receipt_id,
            "recomputed_receipt_id": recomputation.recomputed_receipt.receipt_id,
            "comparison_rule_id": recomputation.comparison_rule_id,
            "comparator_digest": recomputation.comparator_digest,
        })
    gaps = [recomputation.shared_source_gap]
    for item in checks:
        if item.outcome in {CheckOutcome.FAIL, CheckOutcome.MISSING, CheckOutcome.UNKNOWN}:
            gaps.append(CoverageGap(
                CoverageGapKind.UNCHECKED_PLANE,
                f"{item.check_id}: {item.reason}", item.reopen_condition,
                materiality=item.materiality,
                rule_source=item.materiality_rule_id if item.materiality is not Materiality.UNKNOWN else MISSING,
                evidence_refs=item.receipt_ids,
            ))
    roles = contract.roles
    admitted = (
        None if recomputation.admitted_reported is None
        else recomputation.admitted_reported.to_admitted_evidence()
    )
    return FlightReadinessPacket(
        contract=contract,
        core_check_set=CoreCheckSet(contract.core_check_set_revision),
        checks=checks,
        source_receipts=(recomputation.reported_receipt,),
        derivation_receipts=(recomputation.recomputed_receipt, *validator_receipts),
        coverage_gaps=tuple(gaps),
        disagreements=disagreements,
        analysis_use=analysis_use,
        blockers=blockers,
        next_safe_action=action,
        human_state=HumanState(
            roles.experiment_owner, roles.independent_ds_consultant, roles.committee_route,
            "not_requested",
        ),
        authorization_state=contract.authorization_state,
        redaction_state=contract.redaction_state,
        expiry=contract.expiry,
        admitted_evidence=admitted,
        predecessor_digest=contract.predecessor_digest,
        supersedes_digest=contract.supersedes_digest,
    )
