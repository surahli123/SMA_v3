"""Threshold-free fixture matrix, baselines, decoys, provenance, and hard vetoes."""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from pathlib import Path
from typing import Callable

from ..adapters.base import ReadRequest
from ..adapters.fixture import FixtureReadAdapter
from ..core.digest import content_digest
from .evaluator import DecisionMetricOutput, EvaluationHardVeto, build_recomputation_evidence, evaluate_flight
from .contracts import ExperimentReadContract
from .packet import AnalysisUse


class ValidationError(ValueError):
    pass


@dataclass(frozen=True)
class ReviewerProvenance:
    fixture_author: str
    evaluator: str
    independence: str
    disclosed_conflict: str | None = None

    def __post_init__(self) -> None:
        if self.independence not in {"independent", "conflict_disclosed"}:
            raise ValidationError("reviewer independence must be explicit")
        if self.fixture_author == self.evaluator and self.independence != "conflict_disclosed":
            raise ValidationError("same author and evaluator requires a disclosed conflict")
        if self.independence == "conflict_disclosed" and not self.disclosed_conflict:
            raise ValidationError("conflict_disclosed requires the conflict text")


@dataclass(frozen=True)
class FixtureTruth:
    case_id: str
    scenario: str
    expected_analysis_use: AnalysisUse
    provenance: ReviewerProvenance
    decoy_kind: str | None = None
    fixture_digest: str = ""

    def __post_init__(self) -> None:
        if not self.case_id.startswith("m0-"):
            raise ValidationError("fixture case id must be M0-scoped")
        if self.decoy_kind not in {None, "metric_definition_version", "cuped_mode", "source_identity"}:
            raise ValidationError("unregistered adversarial decoy")
        identity = {
            "case_id": self.case_id,
            "scenario": self.scenario,
            "expected_analysis_use": self.expected_analysis_use.value,
            "fixture_author": self.provenance.fixture_author,
            "evaluator": self.provenance.evaluator,
            "independence": self.provenance.independence,
            "disclosed_conflict": self.provenance.disclosed_conflict,
            "decoy_kind": self.decoy_kind,
        }
        object.__setattr__(self, "fixture_digest", content_digest(identity))


INDEPENDENT = ReviewerProvenance("fixture-author-a", "fixture-reviewer-b", "independent")
CONFLICT = ReviewerProvenance(
    "fixture-author-a", "fixture-author-a", "conflict_disclosed", "author also evaluates this case"
)

FIXTURE_MATRIX = (
    FixtureTruth("m0-trusted", "trusted", AnalysisUse.DECISION_GRADE, INDEPENDENT),
    FixtureTruth("m0-directional", "pre-runtime directional", AnalysisUse.DIRECTIONAL_ONLY, INDEPENDENT),
    FixtureTruth("m0-invalid", "material validity failure", AnalysisUse.NOT_PERMITTED, INDEPENDENT),
    FixtureTruth("m0-materially-unknown", "materiality unknown", AnalysisUse.NOT_PERMITTED, INDEPENDENT),
    FixtureTruth("m0-conflicting", "conflicting reads", AnalysisUse.NOT_PERMITTED, INDEPENDENT),
    FixtureTruth("m0-stale", "stale read", AnalysisUse.NOT_PERMITTED, INDEPENDENT),
    FixtureTruth("m0-partial", "partial read", AnalysisUse.NOT_PERMITTED, INDEPENDENT),
    FixtureTruth("m0-unauthorized", "unauthorized read", AnalysisUse.NOT_PERMITTED, INDEPENDENT),
    FixtureTruth("m0-superseded", "superseded packet", AnalysisUse.NOT_PERMITTED, INDEPENDENT),
    FixtureTruth("m0-reviewer-conflict", "reviewer materiality conflict", AnalysisUse.NOT_PERMITTED, CONFLICT),
    FixtureTruth("m0-decoy-metric-version", "metric version decoy", AnalysisUse.NOT_PERMITTED, INDEPENDENT, "metric_definition_version"),
    FixtureTruth("m0-decoy-cuped", "CUPED mode decoy", AnalysisUse.NOT_PERMITTED, INDEPENDENT, "cuped_mode"),
    FixtureTruth("m0-decoy-source", "source identity decoy", AnalysisUse.NOT_PERMITTED, INDEPENDENT, "source_identity"),
)

if len({item.case_id for item in FIXTURE_MATRIX}) != len(FIXTURE_MATRIX):
    raise RuntimeError("fixture case ids must be unique")


def validate_trivial_baselines() -> tuple[str, ...]:
    """Both trivial evaluators must contradict sealed planted truth."""
    always_ready_wrong = any(item.expected_analysis_use is not AnalysisUse.DECISION_GRADE for item in FIXTURE_MATRIX)
    always_blocked_wrong = any(item.expected_analysis_use is AnalysisUse.DECISION_GRADE for item in FIXTURE_MATRIX)
    if not always_ready_wrong or not always_blocked_wrong:
        raise ValidationError("VAL-BASE-001 rejects the fixture suite before Agent scoring")
    return ("always_ready:contradicted", "always_blocked:contradicted")


class HardVetoKind(str, Enum):
    FALSE_READINESS = "false_readiness"
    CROSS_CASE_OR_TENANT_LEAKAGE = "cross_case_or_tenant_leakage"
    SECRET_EXPOSURE = "secret_exposure"
    UNSAFE_REDACTION = "unsafe_redaction"
    WRITE_REACHABILITY = "write_reachability"
    UNAUTHORIZED_DELIVERY = "unauthorized_delivery"


@dataclass(frozen=True)
class HardVetoResult:
    no_go: bool
    reasons: tuple[HardVetoKind, ...]


def hard_veto(*reasons: HardVetoKind) -> HardVetoResult:
    if not all(isinstance(item, HardVetoKind) for item in reasons):
        raise TypeError("hard-veto reasons must be typed")
    return HardVetoResult(bool(reasons), tuple(dict.fromkeys(reasons)))


@dataclass(frozen=True)
class SealedFixtureTruth:
    case_id: str
    base_fixture: str
    mutation: str
    scenario: str
    expected_analysis_use: AnalysisUse
    provenance: ReviewerProvenance
    decoy_kind: str | None
    fixture_digest: str


_CORPUS_ROOT = Path(__file__).resolve().parent.parent / "evals" / "fixtures" / "m0"


def _load_sealed_matrix() -> tuple[SealedFixtureTruth, ...]:
    adapter = FixtureReadAdapter(_CORPUS_ROOT)
    document = adapter._load_sealed_corpus()
    if document.get("schema_version") != "m0-executable-corpus/v1":
        raise ValidationError("unsupported executable corpus schema")
    records = []
    for entry in document.get("cases", []):
        byte_digest = adapter._fixture_byte_sha256(entry["base_fixture"])
        if document["fixture_byte_sha256"].get(entry["base_fixture"]) != byte_digest:
            raise ValidationError(f"fixture bytes drifted for {entry['base_fixture']}")
        provenance = CONFLICT if entry["provenance"] == "conflict_disclosed" else INDEPENDENT
        records.append(SealedFixtureTruth(
            entry["case_id"], entry["base_fixture"], entry["mutation"], entry["scenario"],
            AnalysisUse(entry["expected_analysis_use"]), provenance, entry.get("decoy_kind"),
            content_digest({"corpus_entry": entry, "fixture_byte_sha256": byte_digest}),
        ))
    if len(records) != len({item.case_id for item in records}):
        raise ValidationError("sealed corpus case ids must be unique")
    return tuple(records)


# This shadows the rejected metadata-only matrix with byte-bound executable cases.
FIXTURE_MATRIX = _load_sealed_matrix()


def execute_fixture_corpus(
    contract_factory: Callable[..., ExperimentReadContract],
) -> dict[str, AnalysisUse]:
    """Run every planted-truth case through the public evaluator and veto path."""
    adapter = FixtureReadAdapter(_CORPUS_ROOT)
    observed: dict[str, AnalysisUse] = {}
    for truth in FIXTURE_MATRIX:
        contract = contract_factory()
        result = adapter.read(ReadRequest(f"corpus-{truth.case_id}", "fixture-metric-store", truth.base_fixture))
        disagreements: tuple[dict[str, str], ...] = ()
        vetoes: tuple[EvaluationHardVeto, ...] = ()
        mutation = truth.mutation
        if mutation == "pre_runtime":
            contract = replace(contract, observed_runtime_units=9)
            body = dict(result.body)
            observations = dict(body["check_observations"])
            observations["CHK-02"] = {"observed_runtime_units": 9}
            body["check_observations"] = observations
            result = replace(result, body=body, receipt=replace(result.receipt, body=body, receipt_id="", digest=""))
        elif mutation == "arm_divergence":
            contract = replace(contract, arm_parity_consistent=False)
        elif mutation == "source_mismatch":
            contract = replace(contract, source=replace(contract.source, snapshot_id="superseded-snapshot"))
        elif mutation == "reviewer_conflict":
            disagreements = ({"reviewer": "fixture-author-a", "position": "material"}, {"reviewer": "fixture-reviewer-b", "position": "non_material"})
        elif mutation in {"missing_check_evidence", "decoy_metric_version", "decoy_cuped", "decoy_source"}:
            body = dict(result.body)
            if mutation == "missing_check_evidence":
                observations = dict(body["check_observations"])
                observations.pop("CHK-06")
                body["check_observations"] = observations
            elif mutation == "decoy_metric_version":
                body["metric_definition_version"] = "decoy-version"
            elif mutation == "decoy_cuped":
                body["cuped_mode"] = "adjusted"
            else:
                body["source_version"] = "decoy-source"
            result = replace(result, body=body, receipt=replace(result.receipt, body=body, receipt_id="", digest=""))
        elif mutation.startswith("veto:"):
            vetoes = (EvaluationHardVeto(mutation.split(":", 1)[1]),)
        output = DecisionMetricOutput(
            "synthetic_click_through_rate", "v3", "fixture-source/v1", "unadjusted", "ratio", 0.1278884462151394
        )
        recomputation = build_recomputation_evidence(contract, result, recomputed_output=output)
        packet = evaluate_flight(contract, recomputation, disagreements=disagreements, hard_vetoes=vetoes)
        observed[truth.case_id] = packet.analysis_use
    return observed


def validate_trivial_baselines(observed: dict[str, AnalysisUse] | None = None) -> tuple[str, ...]:
    """Score trivial baselines against actual evaluator outcomes when supplied."""
    values = observed or {item.case_id: item.expected_analysis_use for item in FIXTURE_MATRIX}
    if set(values) != {item.case_id for item in FIXTURE_MATRIX}:
        raise ValidationError("baseline scoring requires every sealed corpus case")
    for item in FIXTURE_MATRIX:
        if values[item.case_id] is not item.expected_analysis_use:
            raise ValidationError(f"real evaluator contradicted planted truth for {item.case_id}")
    if not any(value is not AnalysisUse.DECISION_GRADE for value in values.values()):
        raise ValidationError("always-ready baseline was not contradicted")
    if not any(value is AnalysisUse.DECISION_GRADE for value in values.values()):
        raise ValidationError("always-blocked baseline was not contradicted")
    return ("always_ready:contradicted", "always_blocked:contradicted")
