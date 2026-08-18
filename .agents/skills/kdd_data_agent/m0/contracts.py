"""Frozen M0 ExperimentReadContract and supporting typed policy inputs."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any

from ..alignment.seams import FrozenPacketBinding
from ..core.digest import content_digest
from ..core.digest import DIGEST_PATTERN
from ..core.identity import (
    AuthorizationState,
    RedactionState,
    SourceIdentity,
    TimeInterval,
    validate_maybe_str,
    validate_timestamp,
)
from ..core.immutability import deep_freeze
from ..core.unknown import MISSING, UNKNOWN, Sentinel, is_sentinel

PACKET_PATH = "docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md"
PACKET_REVISION = "m0-alignment-v1"
PACKET_SHA256 = "sha256:82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19"
ARCHITECTURE_PATH = "docs/research/kdd-data-agent-workshop/final-architecture-spec.md"
ARCHITECTURE_REVISION = "kdd-data-agent-architecture-v1"
ARCHITECTURE_SHA256 = "sha256:9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1"


class ContractError(ValueError):
    pass


class EvidenceClass(str, Enum):
    FIXTURE = "fixture"
    PRODUCTION_AUTHORIZED = "production_authorized"


class MetricRole(str, Enum):
    DECISION = "decision"
    CO_PRIMARY = "co_primary"


class SufficiencyKind(str, Enum):
    RUNTIME_ONLY = "runtime_only"
    RUNTIME_AND_SAMPLE = "runtime_and_sample"


class IndependenceClass(str, Enum):
    INDEPENDENT_SOURCE = "independent_source"
    INDEPENDENT_TRANSFORM = "independent_transform"
    SAME_PIPELINE = "same_pipeline"


@dataclass(frozen=True)
class FrozenM0Binding:
    packet: FrozenPacketBinding = field(
        default_factory=lambda: FrozenPacketBinding(PACKET_PATH, PACKET_SHA256, PACKET_REVISION)
    )
    architecture_path: str = ARCHITECTURE_PATH
    architecture_revision: str = ARCHITECTURE_REVISION
    architecture_digest: str = ARCHITECTURE_SHA256

    def __post_init__(self) -> None:
        if self.packet.to_canonical() != FrozenPacketBinding(
            PACKET_PATH, PACKET_SHA256, PACKET_REVISION
        ).to_canonical():
            raise ContractError("M0 implementation requires the exact frozen packet binding")
        if (
            self.architecture_path,
            self.architecture_revision,
            self.architecture_digest,
        ) != (ARCHITECTURE_PATH, ARCHITECTURE_REVISION, ARCHITECTURE_SHA256):
            raise ContractError("M0 implementation requires the exact frozen architecture binding")

    def to_canonical(self) -> dict[str, Any]:
        return {
            "packet": self.packet.to_canonical(),
            "architecture_path": self.architecture_path,
            "architecture_revision": self.architecture_revision,
            "architecture_digest": self.architecture_digest,
        }


@dataclass(frozen=True)
class QuerySuccessDefinition:
    traditional_component_id: str
    ai_answer_component_id: str
    common_grain: str
    common_population: str
    common_window: str
    overlap_policy_id: str
    fixed_threshold_rule_id: str

    def __post_init__(self) -> None:
        for name, value in (
            ("traditional_component_id", self.traditional_component_id),
            ("ai_answer_component_id", self.ai_answer_component_id),
            ("common_grain", self.common_grain),
            ("common_population", self.common_population),
            ("common_window", self.common_window),
            ("overlap_policy_id", self.overlap_policy_id),
            ("fixed_threshold_rule_id", self.fixed_threshold_rule_id),
        ):
            validate_maybe_str(value, name)
        if self.traditional_component_id == self.ai_answer_component_id:
            raise ContractError("Query Success union components must be distinct")

    def to_canonical(self) -> dict[str, Any]:
        return {
            "formula": "TraditionalResultSuccess OR AIAnswerSuccess",
            "traditional_component_id": self.traditional_component_id,
            "ai_answer_component_id": self.ai_answer_component_id,
            "common_grain": self.common_grain,
            "common_population": self.common_population,
            "common_window": self.common_window,
            "overlap_policy_id": self.overlap_policy_id,
            "fixed_threshold_rule_id": self.fixed_threshold_rule_id,
        }


@dataclass(frozen=True)
class DecisionMetricPolicy:
    policy_id: str
    metric_cardinality: str
    conflict_rule_id: str
    comparison_rule_id: str
    query_success: QuerySuccessDefinition

    def __post_init__(self) -> None:
        for name, value in (
            ("policy_id", self.policy_id),
            ("conflict_rule_id", self.conflict_rule_id),
            ("comparison_rule_id", self.comparison_rule_id),
        ):
            validate_maybe_str(value, name)
        if self.metric_cardinality not in {"one", "co_primary"}:
            raise ContractError("metric_cardinality must be one or co_primary")
        if not isinstance(self.query_success, QuerySuccessDefinition):
            raise TypeError("query_success must be a QuerySuccessDefinition")

    def to_canonical(self) -> dict[str, Any]:
        return {
            "policy_id": self.policy_id,
            "metric_cardinality": self.metric_cardinality,
            "conflict_rule_id": self.conflict_rule_id,
            "comparison_rule_id": self.comparison_rule_id,
            "query_success": self.query_success.to_canonical(),
        }


@dataclass(frozen=True)
class MetricDefinition:
    metric_id: str
    definition_version: str
    role: MetricRole
    unit: str
    estimator: str
    source_version: str
    owner: str
    cuped_mode: str
    ratio_variance_method: str | Sentinel = MISSING

    def __post_init__(self) -> None:
        for name, value in (
            ("metric_id", self.metric_id), ("definition_version", self.definition_version),
            ("unit", self.unit), ("estimator", self.estimator),
            ("source_version", self.source_version), ("owner", self.owner),
            ("cuped_mode", self.cuped_mode),
        ):
            validate_maybe_str(value, name)
        if not isinstance(self.role, MetricRole):
            raise TypeError("role must be a MetricRole")
        if not is_sentinel(self.ratio_variance_method):
            validate_maybe_str(self.ratio_variance_method, "ratio_variance_method")

    def to_canonical(self) -> dict[str, Any]:
        return {
            "metric_id": self.metric_id,
            "definition_version": self.definition_version,
            "role": self.role.value,
            "unit": self.unit,
            "estimator": self.estimator,
            "source_version": self.source_version,
            "owner": self.owner,
            "cuped_mode": self.cuped_mode,
            "ratio_variance_method": self.ratio_variance_method,
        }


@dataclass(frozen=True)
class SufficiencyRule:
    kind: SufficiencyKind
    rule_id: str
    runtime_threshold_units: int
    sample_threshold_units: int | Sentinel = MISSING
    sample_input_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not isinstance(self.kind, SufficiencyKind):
            raise TypeError("kind must be a SufficiencyKind")
        validate_maybe_str(self.rule_id, "sufficiency.rule_id")
        if not isinstance(self.runtime_threshold_units, int) or self.runtime_threshold_units <= 0:
            raise ContractError("runtime threshold must be a positive preregistered integer")
        object.__setattr__(self, "sample_input_ids", tuple(self.sample_input_ids))
        if self.kind is SufficiencyKind.RUNTIME_AND_SAMPLE:
            if not isinstance(self.sample_threshold_units, int) or self.sample_threshold_units <= 0:
                raise ContractError("runtime_and_sample requires a positive preregistered sample threshold")
            if not self.sample_input_ids:
                raise ContractError("runtime_and_sample requires preregistered sample input ids")
        elif not is_sentinel(self.sample_threshold_units) or self.sample_input_ids:
            raise ContractError("runtime_only cannot carry sample thresholds or sample inputs")

    def to_canonical(self) -> dict[str, Any]:
        return {
            "kind": self.kind.value,
            "rule_id": self.rule_id,
            "runtime_threshold_units": self.runtime_threshold_units,
            "sample_threshold_units": self.sample_threshold_units,
            "sample_input_ids": list(self.sample_input_ids),
        }


@dataclass(frozen=True)
class ArmIdentity:
    arm_id: str
    index_generation: str | Sentinel
    serving_alias: str | Sentinel
    acl_snapshot: str | Sentinel
    effective_pipeline: str | Sentinel

    def __post_init__(self) -> None:
        for name, value in (
            ("arm_id", self.arm_id), ("index_generation", self.index_generation),
            ("serving_alias", self.serving_alias), ("acl_snapshot", self.acl_snapshot),
            ("effective_pipeline", self.effective_pipeline),
        ):
            validate_maybe_str(value, name)

    @property
    def complete(self) -> bool:
        return not any(is_sentinel(value) for value in (
            self.index_generation, self.serving_alias, self.acl_snapshot, self.effective_pipeline
        ))

    def to_canonical(self) -> dict[str, Any]:
        return {
            "arm_id": self.arm_id,
            "index_generation": self.index_generation,
            "serving_alias": self.serving_alias,
            "acl_snapshot": self.acl_snapshot,
            "effective_pipeline": self.effective_pipeline,
        }


@dataclass(frozen=True)
class HumanRoles:
    experiment_owner: str
    independent_ds_consultant: str
    committee_route: str

    def __post_init__(self) -> None:
        for name, value in (
            ("experiment_owner", self.experiment_owner),
            ("independent_ds_consultant", self.independent_ds_consultant),
            ("committee_route", self.committee_route),
        ):
            validate_maybe_str(value, name)

    def to_canonical(self) -> dict[str, Any]:
        return {
            "experiment_owner": self.experiment_owner,
            "independent_ds_consultant": self.independent_ds_consultant,
            "committee_route": self.committee_route,
        }


@dataclass(frozen=True)
class ExperimentReadContract:
    flight_id: str
    contract_version: str
    binding: FrozenM0Binding
    evidence_class: EvidenceClass
    metrics: tuple[MetricDefinition, ...]
    decision_metric_policy: DecisionMetricPolicy
    assignment_unit: str
    analysis_unit: str
    population: str
    eligibility: str
    exclusions: tuple[str, ...]
    tenant_scope: str
    surface: str
    locale: str
    exposure_definition: str
    join_keys: tuple[str, ...]
    analysis_window: TimeInterval
    timezone: str
    planned_runtime_units: int
    observed_runtime_units: int
    observed_sample_units: int | Sentinel
    source: SourceIdentity
    authorization_state: AuthorizationState
    redaction_state: RedactionState
    recipient_scope: str
    retention_rule_id: str
    load_limit_rule_id: str
    halt_rule_id: str
    export_rule_id: str
    sufficiency_rule: SufficiencyRule
    arms: tuple[ArmIdentity, ...]
    arm_parity_consistent: bool | Sentinel
    arm_parity_applicability_rule_id: str | Sentinel
    core_check_set_revision: str
    roles: HumanRoles
    expiry: str
    predecessor_digest: str | Sentinel = MISSING
    supersedes_digest: str | Sentinel = MISSING
    metadata: Mapping[str, Any] = field(default_factory=dict)
    contract_digest: str = field(init=False)

    def __post_init__(self) -> None:
        for name, value in (
            ("flight_id", self.flight_id), ("contract_version", self.contract_version),
            ("assignment_unit", self.assignment_unit), ("analysis_unit", self.analysis_unit),
            ("population", self.population), ("eligibility", self.eligibility),
            ("tenant_scope", self.tenant_scope), ("surface", self.surface), ("locale", self.locale),
            ("exposure_definition", self.exposure_definition), ("timezone", self.timezone),
            ("recipient_scope", self.recipient_scope), ("retention_rule_id", self.retention_rule_id),
            ("load_limit_rule_id", self.load_limit_rule_id), ("halt_rule_id", self.halt_rule_id),
            ("export_rule_id", self.export_rule_id), ("core_check_set_revision", self.core_check_set_revision),
        ):
            validate_maybe_str(value, name)
        if not isinstance(self.binding, FrozenM0Binding):
            raise TypeError("binding must be FrozenM0Binding")
        if not isinstance(self.evidence_class, EvidenceClass):
            raise TypeError("evidence_class must be EvidenceClass")
        if self.evidence_class is not EvidenceClass.FIXTURE:
            raise ContractError("this local M0 implementation accepts fixture evidence only")
        object.__setattr__(self, "metrics", tuple(self.metrics))
        object.__setattr__(self, "exclusions", tuple(self.exclusions))
        object.__setattr__(self, "join_keys", tuple(self.join_keys))
        object.__setattr__(self, "arms", tuple(self.arms))
        object.__setattr__(self, "metadata", deep_freeze(self.metadata))
        if not self.metrics or not all(isinstance(item, MetricDefinition) for item in self.metrics):
            raise ContractError("at least one typed decision metric is required")
        expected_count = 1 if self.decision_metric_policy.metric_cardinality == "one" else 2
        if len(self.metrics) != expected_count:
            raise ContractError("metric count does not match the preregistered cardinality policy")
        if not self.join_keys:
            raise ContractError("join_keys are required")
        if not isinstance(self.analysis_window, TimeInterval):
            raise TypeError("analysis_window must be a TimeInterval")
        if not isinstance(self.source, SourceIdentity):
            raise TypeError("source must be SourceIdentity")
        if not isinstance(self.authorization_state, AuthorizationState):
            raise TypeError("authorization_state must be AuthorizationState")
        if not isinstance(self.redaction_state, RedactionState):
            raise TypeError("redaction_state must be RedactionState")
        if not isinstance(self.sufficiency_rule, SufficiencyRule):
            raise TypeError("sufficiency_rule must be SufficiencyRule")
        if not isinstance(self.roles, HumanRoles):
            raise TypeError("roles must be HumanRoles")
        if not isinstance(self.arm_parity_consistent, bool) and not is_sentinel(self.arm_parity_consistent):
            raise TypeError("arm_parity_consistent must be bool or explicit sentinel")
        if not isinstance(self.planned_runtime_units, int) or self.planned_runtime_units <= 0:
            raise ContractError("planned_runtime_units must be positive")
        if not isinstance(self.observed_runtime_units, int) or self.observed_runtime_units < 0:
            raise ContractError("observed_runtime_units must be non-negative")
        if not is_sentinel(self.observed_sample_units) and (
            not isinstance(self.observed_sample_units, int) or self.observed_sample_units < 0
        ):
            raise ContractError("observed_sample_units must be non-negative or explicit MISSING")
        validate_timestamp(self.expiry, "contract.expiry")
        if self.observed_runtime_units < self.sufficiency_rule.runtime_threshold_units:
            if is_sentinel(self.analysis_window.end):
                raise ContractError("a pre-runtime contract requires the preregistered runtime end")
            if datetime.fromisoformat(self.expiry) > datetime.fromisoformat(str(self.analysis_window.end)):
                raise ContractError("a pre-runtime packet expiry cannot exceed the preregistered runtime end")
        for name, value in (("predecessor_digest", self.predecessor_digest), ("supersedes_digest", self.supersedes_digest)):
            if not is_sentinel(value) and (not isinstance(value, str) or DIGEST_PATTERN.fullmatch(value) is None):
                raise ContractError(f"{name} must be sha256:<64 hex> or an explicit sentinel")
        object.__setattr__(self, "contract_digest", content_digest(self._identity_payload()))

    def _identity_payload(self) -> dict[str, Any]:
        return {
            "flight_id": self.flight_id,
            "contract_version": self.contract_version,
            "binding": self.binding.to_canonical(),
            "evidence_class": self.evidence_class.value,
            "metrics": [item.to_canonical() for item in self.metrics],
            "decision_metric_policy": self.decision_metric_policy.to_canonical(),
            "assignment_unit": self.assignment_unit,
            "analysis_unit": self.analysis_unit,
            "population": self.population,
            "eligibility": self.eligibility,
            "exclusions": list(self.exclusions),
            "tenant_scope": self.tenant_scope,
            "surface": self.surface,
            "locale": self.locale,
            "exposure_definition": self.exposure_definition,
            "join_keys": list(self.join_keys),
            "analysis_window": self.analysis_window.to_canonical(),
            "timezone": self.timezone,
            "planned_runtime_units": self.planned_runtime_units,
            "observed_runtime_units": self.observed_runtime_units,
            "observed_sample_units": self.observed_sample_units,
            "source": self.source.to_canonical(),
            "authorization_state": self.authorization_state.value,
            "redaction_state": self.redaction_state.value,
            "recipient_scope": self.recipient_scope,
            "retention_rule_id": self.retention_rule_id,
            "load_limit_rule_id": self.load_limit_rule_id,
            "halt_rule_id": self.halt_rule_id,
            "export_rule_id": self.export_rule_id,
            "sufficiency_rule": self.sufficiency_rule.to_canonical(),
            "arms": [item.to_canonical() for item in self.arms],
            "arm_parity_consistent": self.arm_parity_consistent,
            "arm_parity_applicability_rule_id": self.arm_parity_applicability_rule_id,
            "core_check_set_revision": self.core_check_set_revision,
            "roles": self.roles.to_canonical(),
            "expiry": self.expiry,
            "predecessor_digest": self.predecessor_digest,
            "supersedes_digest": self.supersedes_digest,
            "metadata": dict(self.metadata),
        }

    def to_canonical(self) -> dict[str, Any]:
        payload = self._identity_payload()
        payload["contract_digest"] = self.contract_digest
        return payload
