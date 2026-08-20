"""Project accepted-package M0 packets into the review surface's render model.

What this does
--------------
It imports the independently accepted local M0 package read-only, evaluates
seven fixture-class Flights through the accepted evaluator, and writes the
resulting `FlightReadinessPacket` values into a single render model that a
static page can display without any dependency, build step, or server.

What this does not do
---------------------
It does not modify the accepted package, read production data, reach the
network, invent a check outcome, or promote a fixture packet into evidence of
production capability. Every scenario below is emitted by the accepted
evaluator; nothing is hand-authored into a readiness field.

Determinism
-----------
No clock, no randomness, no dictionary-iteration dependence. The emitted bytes
are a pure function of the accepted package and this file, so repeated runs
under different `PYTHONHASHSEED` values produce identical output.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from bindings import (
    ACCEPTED_PACKAGE_AGGREGATE,
    ACCEPTED_PACKAGE_VERDICT,
    FILE_BINDINGS,
    PROTOTYPE_ROOT,
    SKILLS_ROOT,
    verify_bindings,
)

if str(SKILLS_ROOT) not in sys.path:
    sys.path.insert(0, str(SKILLS_ROOT))

from kdd_data_agent.core.canonical_json import canonical_encode  # noqa: E402
from kdd_data_agent.core.identity import AuthorizationState, RedactionState  # noqa: E402
from kdd_data_agent.core.unknown import RESERVED_KEY  # noqa: E402
from kdd_data_agent.m0.checks import CHECK_REGISTRY  # noqa: E402
from kdd_data_agent.m0.contracts import IndependenceClass  # noqa: E402
from kdd_data_agent.m0.evaluator import DecisionMetricOutput  # noqa: E402
from kdd_data_agent.m0.packet import (  # noqa: E402
    PacketAcknowledgement,
    invalidate_acknowledgement,
    synthetic_review_projection,
)
from kdd_data_agent.tests._m0_fixtures import (  # noqa: E402
    build_contract,
    packet_for,
    reported_result,
    result_with_body,
)

SCHEMA_VERSION = "m0-review-surface-projection/v1"
CHECK_TITLES = {item.check_id: item.title for item in CHECK_REGISTRY}
CHECK_CORE_FLOOR = {item.check_id: item.core_floor for item in CHECK_REGISTRY}

OUTCOME_ORDER = {"FAIL": 0, "MISSING": 1, "UNKNOWN": 2, "NOT_APPLICABLE": 3, "PASS": 4}
"""First-screen ordering fixed by the architecture: blocking work before passes."""

BOUNDARIES = (
    "Fixture-only. Every packet on this page has evidence_class = fixture and was "
    "emitted by the local accepted M0 package against synthetic reads.",
    "No production capability. Nothing here demonstrates that the Agent can read, "
    "authenticate against, or evaluate a production source.",
    "No cause. M0 evaluates experiment and metric-read integrity; it does not "
    "explain metric movement.",
    "No M1 or M2 recommendation. No candidate diff, remediation, or ranking is "
    "produced or implied.",
    "No win or loss. No query-level outcome judgement is present.",
    "No P3 closure. Live review-surface acceptance remains an open external gate "
    "(VAL-UI-101).",
    "No Committee decision. The Experiment Review Committee owns Acceptance; this "
    "page carries none of it.",
    "Read-only. No control on this page writes, mutates, applies, approves, "
    "acknowledges, or re-evaluates anything.",
)

AUTHORITY_NOTE = (
    "A validity-based block advises against using this Flight as decision evidence. "
    "It does not block, approve, roll back, or otherwise gate a product launch."
)


def _plain(value: Any) -> Any:
    """Normalize package output through the package's own canonical encoder.

    `to_canonical()` deliberately hands nested values over un-normalized, since
    the package canonicalizes exactly once at the top level. Round-tripping
    through that same encoder is therefore the only correct way to obtain plain
    JSON values, and it guarantees the surface reads the same bytes the packet
    digest is computed over.

    Absence stays encoded under the reserved `__kdd__` key, so the surface can
    render `UNKNOWN` and `MISSING` as the distinct typed states they are, never
    as `null` or an empty string. `json.loads` rather than the package's
    `canonical_loads` is deliberate here: the latter reconstructs live
    `Sentinel` objects, and this projection needs inert JSON.
    """
    return json.loads(canonical_encode(value).decode("utf-8"))


def _sentinel_name(value: Any) -> str | None:
    """Return `UNKNOWN` / `MISSING` when a canonical value encodes absence."""
    if isinstance(value, dict) and set(value) == {RESERVED_KEY}:
        return str(value[RESERVED_KEY])
    return None


def _absent(value: Any) -> bool:
    return _sentinel_name(value) is not None


def _receipt_view(document: dict[str, Any], role: str) -> dict[str, Any]:
    """Flatten one canonical receipt into the fields a reviewer reads first."""
    detail = document.get("detail") or {}
    return {
        "role": role,
        "receipt_id": document["receipt_id"],
        "receipt_kind": document["receipt_kind"],
        "digest": document["digest"],
        "outcome": document["outcome"],
        "actor_id": (document.get("actor") or {}).get("actor_id"),
        "actor_kind": (document.get("actor") or {}).get("actor_kind"),
        "authorization_state": document["authorization_state"],
        "redaction_state": document["redaction_state"],
        "recorded_at": document["recorded_at"],
        "observed_interval": document["observed_interval"],
        "source": document["source"],
        "body_digest": document["body_digest"],
        "body_retained": not _absent(document["body_digest"]),
        "derivation_inputs": document.get("derivation_inputs") or [],
        "decision_bindings": detail.get("decision_bindings") or [],
        "detail": detail,
    }


def _why_limited(analysis_use: str, blocking: list[dict[str, Any]]) -> str:
    """State the limit from the sealed checks. Nothing is added to them."""
    if analysis_use == "decision_grade":
        return (
            "No material check failed, is missing, or is unknown, so the sealed "
            "checks place no limit on this Flight's use as decision evidence."
        )
    lead = blocking[0]
    head = f"{lead['check_id']} ({CHECK_TITLES[lead['check_id']]}) is {lead['outcome']}: {lead['reason']}."
    if len(blocking) > 1:
        head += f" {len(blocking) - 1} further check(s) are also unresolved."
    if analysis_use == "directional_only":
        return head + " Direction may be read; the decision metric may not be concluded from it."
    return head + " This Flight may not be used as decision evidence."


def _state_view(packet: Any, document: dict[str, Any], source_views: list[dict[str, Any]]) -> dict[str, Any]:
    """Derive staleness, invalidation, supersession and incompleteness.

    Every field is read off the emitted packet. None of it is asserted by this
    tool: a claim the packet does not carry is reported as `not_recorded`.
    """
    window = document["contract"]["analysis_window"]
    stale_reads = [
        item for item in source_views
        if item["outcome"] != "trusted" or item["observed_interval"] != window
    ]
    incomplete = [
        item for item in document["checks"] if item["outcome"] in {"MISSING", "UNKNOWN"}
    ]
    supersedes = document["supersedes_digest"]
    predecessor = document["predecessor_digest"]
    return {
        "authorization_state": document["authorization_state"],
        "redaction_state": document["redaction_state"],
        "body_retention": (
            "no source body is retained under this authorization and redaction state"
            if not any(item["body_retained"] for item in source_views)
            else "a source body is retained; only its digest is exposed by the packet"
        ),
        "staleness": {
            "state": "stale" if stale_reads else "current",
            "contract_analysis_window": window,
            "detail": [
                {
                    "receipt_id": item["receipt_id"],
                    "outcome": item["outcome"],
                    "observed_interval": item["observed_interval"],
                }
                for item in stale_reads
            ],
        },
        "incompleteness": {
            "state": "incomplete" if incomplete else "complete",
            "unresolved_checks": [
                {"check_id": item["check_id"], "outcome": item["outcome"], "reason": item["reason"]}
                for item in incomplete
            ],
        },
        "supersession": {
            "state": "supersedes_an_earlier_packet" if not _absent(supersedes) else "not_recorded",
            "supersedes_digest": supersedes,
            "predecessor_digest": predecessor,
        },
    }


def _acknowledgement_view(packet: Any, acknowledged: Any | None) -> dict[str, Any]:
    """Project the packet's human state and, where present, its invalidation.

    `PacketAcknowledgement` and `invalidate_acknowledgement` are the accepted
    package's own acknowledgement lifecycle. They are separate objects from the
    packet, and are labelled as such so the surface never presents an
    acknowledgement as a packet field. `acknowledged` is the earlier packet a
    reviewer had acknowledged, which `packet` supersedes.
    """
    view = {
        "packet_human_state": _plain(packet.human_state.to_canonical()),
        "acknowledgement_record": None,
    }
    if acknowledged is None:
        return view
    acknowledgement = PacketAcknowledgement(acknowledged.packet_digest, "independent-ds")
    invalidated = invalidate_acknowledgement(acknowledgement, packet)
    view["acknowledgement_record"] = {
        "object": "PacketAcknowledgement (separate from the packet)",
        "acknowledged_packet_digest": acknowledgement.packet_digest,
        "reviewer": acknowledgement.reviewer,
        "state_before": acknowledgement.state,
        "state_after": invalidated.state,
        "invalidated_by_packet_digest": _plain(invalidated.invalidated_by),
    }
    return view


def project(
    *,
    scenario_id: str,
    title: str,
    review_question: str,
    packet: Any,
    acknowledged_packet: Any | None = None,
    projection_note: str | None = None,
) -> dict[str, Any]:
    document = _plain(packet.to_canonical())
    checks = list(document["checks"])
    for item in checks:
        item["title"] = CHECK_TITLES[item["check_id"]]
        item["core_floor"] = CHECK_CORE_FLOOR[item["check_id"]]
    checks.sort(key=lambda item: (OUTCOME_ORDER[item["outcome"]], item["check_id"]))
    blocking = [item for item in checks if item["check_id"] in document["blockers"]]

    source_views = [_receipt_view(item, "source_read") for item in document["source_receipts"]]
    derivation_views = [_receipt_view(item, "derivation") for item in document["derivation_receipts"]]
    recomputation = [item for item in derivation_views if item["decision_bindings"]]
    validators = [item for item in derivation_views if not item["decision_bindings"]]

    return {
        "scenario_id": scenario_id,
        "title": title,
        "review_question": review_question,
        "projection_class": "emitted_fixture_packet",
        "emitted_by": "kdd_data_agent.m0.evaluator.evaluate_flight",
        "projection_note": projection_note,
        "flight": {
            "flight_id": document["contract"]["flight_id"],
            "evidence_class": document["evidence_class"],
            "contract_version": document["contract"]["contract_version"],
            "tenant_scope": document["contract"]["tenant_scope"],
            "surface": document["contract"]["surface"],
            "locale": document["contract"]["locale"],
            "population": document["contract"]["population"],
            "analysis_window": document["contract"]["analysis_window"],
            "timezone": document["contract"]["timezone"],
            "planned_runtime_units": document["contract"]["planned_runtime_units"],
            "observed_runtime_units": document["contract"]["observed_runtime_units"],
            "decision_metric": document["contract"]["metrics"][0],
            "decision_metric_policy": document["contract"]["decision_metric_policy"],
            "source": document["contract"]["source"],
            "roles": document["contract"]["roles"],
        },
        "decision": {
            "analysis_use": {
                "value": document["analysis_use"],
                "storage": "stored on the packet",
                "derived_by": "derive_readiness() over the sealed nineteen checks",
            },
            "post_analysis_eligibility": {
                "value": packet.post_analysis_eligibility.value,
                "storage": "derived at render time; never stored on the packet",
                "rule": "decision_grade -> eligible; directional_only or not_permitted -> blocked",
            },
            "why_limited": _why_limited(document["analysis_use"], blocking),
            "blockers": document["blockers"],
            "authority_note": AUTHORITY_NOTE,
        },
        "next_safe_action": document["next_safe_action"],
        "checks": checks,
        "coverage_gaps": document["coverage_gaps"],
        "disagreements": document["disagreements"],
        "state": _state_view(packet, document, source_views),
        "human": _acknowledgement_view(packet, acknowledged_packet),
        "receipts": {
            "source_read": source_views,
            "recomputation_d4_d6": recomputation,
            "validator": validators,
        },
        "identity": {
            "packet_digest": document["packet_digest"],
            "contract_digest": document["contract"]["contract_digest"],
            "frozen_binding": document["frozen_binding"],
            "architecture_revision": document["contract"]["binding"]["architecture_revision"]
            if "binding" in document["contract"] else None,
            "core_check_set": document["core_check_set"],
            "expiry": document["expiry"],
            "predecessor_digest": document["predecessor_digest"],
            "supersedes_digest": document["supersedes_digest"],
        },
        "accepted_package_projection": _plain(dict(synthetic_review_projection(packet))),
    }


def _observations(**overrides: Any) -> Any:
    """Rebuild the trusted read with adjusted raw check observations."""
    base = reported_result()
    observations = {key: dict(value) for key, value in base.body["check_observations"].items()}
    for key, value in overrides.items():
        check_id = key.replace("_", "-").upper()
        if value is None:
            observations.pop(check_id, None)
        else:
            observations[check_id] = value
    return result_with_body(check_observations=observations)


def build_scenarios() -> list[dict[str, Any]]:
    trusted = packet_for()

    directional_contract = build_contract(observed_runtime_units=4)
    directional = packet_for(directional_contract)

    disagreement = packet_for(
        recomputed_output=DecisionMetricOutput(
            "synthetic_click_through_rate", "v3", "fixture-source/v1", "unadjusted", "ratio", 0.1301,
        )
    )

    unauthorized = packet_for(
        build_contract(authorization_state=AuthorizationState.UNAUTHORIZED),
        reported=reported_result("m0-read-unauthorized-001"),
    )

    redaction_blocked = packet_for(
        build_contract(redaction_state=RedactionState.FAILED),
        reported=reported_result("m0-read-redaction-failure-001"),
    )

    stale = packet_for(
        build_contract(
            supersedes_digest=trusted.packet_digest,
            predecessor_digest=trusted.packet_digest,
        ),
        reported=reported_result("m0-read-stale-001"),
    )

    incomplete = packet_for(
        build_contract(),
        independence_class=IndependenceClass.SAME_PIPELINE,
        reported=_observations(
            chk_02={"observed_runtime_units": 10},
            chk_14={"comparison_rule_id": "m0-comparison-rule/v1", "independence_class": "same_pipeline"},
            chk_09=None,
            chk_17=None,
        ),
    )

    return [
        project(
            scenario_id="trusted-decision-grade",
            title="Trusted read, decision grade",
            review_question="Is this Flight usable as decision evidence, and what proves it?",
            packet=trusted,
        ),
        project(
            scenario_id="pre-runtime-directional",
            title="Pre-runtime read, directional only",
            review_question="Why is direction readable here while the decision metric is not?",
            packet=directional,
        ),
        project(
            scenario_id="recomputation-disagreement",
            title="Recomputation disagreement, not permitted",
            review_question="Where do the reported and independently recomputed values disagree?",
            packet=disagreement,
        ),
        project(
            scenario_id="unauthorized-read",
            title="Unauthorized read, not permitted",
            review_question="What was refused, and what would reopen the read?",
            packet=unauthorized,
        ),
        project(
            scenario_id="redaction-blocked-read",
            title="Redaction failure, not permitted",
            review_question="What did redaction block, and what is still safe to show?",
            packet=redaction_blocked,
        ),
        project(
            scenario_id="stale-superseded-read",
            title="Stale read, superseded packet",
            review_question="Which packet is current, and what happened to the earlier acknowledgement?",
            packet=stale,
            acknowledged_packet=trusted,
            projection_note=(
                "This packet supersedes the trusted packet by digest. The acknowledgement "
                "record beside it is a separate PacketAcknowledgement object, not a packet field."
            ),
        ),
        project(
            scenario_id="incomplete-observations",
            title="Incomplete observations, typed Coverage Gaps",
            review_question="Which planes were never checked, and what closes each gap?",
            packet=incomplete,
        ),
    ]


def build_model() -> dict[str, Any]:
    binding_report = verify_bindings()
    scenarios = build_scenarios()
    return {
        "schema_version": SCHEMA_VERSION,
        "surface": {
            "name": "M0 Flight Readiness review surface",
            "class": "local, static, dependency-free, read-only, pre-P3 review artifact",
            "live_review_scenario": "VAL-UI-101:open_external_P3_gate",
            "projection_scenario": "VAL-UI-001",
        },
        "boundaries": list(BOUNDARIES),
        "provenance": {
            "accepted_package_aggregate_sha256": ACCEPTED_PACKAGE_AGGREGATE,
            "accepted_package_verdict": ACCEPTED_PACKAGE_VERDICT,
            "accepted_package_file_count": binding_report["package_file_count"],
            "aggregate_recipe": binding_report["recipe"],
            "file_bindings": [
                {
                    "role": item.role,
                    "path": item.path,
                    "revision": item.revision,
                    "sha256": item.sha256,
                }
                for item in FILE_BINDINGS
            ],
        },
        "check_registry": [
            {
                "check_id": item.check_id,
                "title": item.title,
                "core_floor": item.core_floor,
                "rule_source": item.rule_source,
            }
            for item in CHECK_REGISTRY
        ],
        "scenarios": scenarios,
    }


def render_bytes(model: dict[str, Any]) -> tuple[bytes, bytes]:
    """Serialize the model once, for the JSON record and the file:// loader."""
    payload = json.dumps(model, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    loader = (
        "/* Generated by tools/build_fixtures.py. Do not edit by hand. */\n"
        "/* Static data only: no executable statement is embedded in this payload. */\n"
        "window.__M0_REVIEW_MODEL__ = "
        + json.dumps(model, indent=2, sort_keys=True, ensure_ascii=False)
        + ";\n"
    )
    return payload.encode("utf-8"), loader.encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        type=Path,
        default=PROTOTYPE_ROOT / "data",
        help="directory that receives fixtures.json and fixtures.js",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify the committed files match a fresh build instead of writing",
    )
    args = parser.parse_args()

    model = build_model()
    payload, loader = render_bytes(model)
    json_path = args.out / "fixtures.json"
    js_path = args.out / "fixtures.js"

    if args.check:
        for path, expected in ((json_path, payload), (js_path, loader)):
            if not path.is_file():
                print(f"MISSING {path}", file=sys.stderr)
                return 1
            if path.read_bytes() != expected:
                print(f"DRIFT {path}", file=sys.stderr)
                return 1
        print(f"fixtures match a fresh build; model sha256 {hashlib.sha256(payload).hexdigest()}")
        return 0

    args.out.mkdir(parents=True, exist_ok=True)
    json_path.write_bytes(payload)
    js_path.write_bytes(loader)
    print(f"wrote {json_path} ({len(payload)} bytes, sha256 {hashlib.sha256(payload).hexdigest()})")
    print(f"wrote {js_path} ({len(loader)} bytes, sha256 {hashlib.sha256(loader).hexdigest()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
