# Owner Steelman Alignment — Codex Continuation

Status: `CLOSED_OWNER_CONFIRMED`

Facilitator: Codex main orchestrator  
Started: `2026-08-18`  
Predecessor: `steelman-owner-alignment-handoff.md`  
Fable draft custody receipt: `fable5-architecture-custody-receipt.md`

This record continues the Owner steelman discussion after the Fable 5 architecture session reached its rate limit. It records Owner decisions only after explicit confirmation. It does not freeze the architecture, authorize implementation, or transfer any review verdict across changed bytes.

## Confirmed continuation decisions

### S9 — Post-unblinding evidence cannot alone carry a change/block advisory

An independently lineaged outcome-evidence stream discovered only after outcome unblinding may trigger mandatory urgent investigation, but it cannot by itself support `recommend_change` or `recommend_block`, even when the signal is strong and reproducible within the discovered analysis.

Before such a stream can carry `recommend_change` or `recommend_block`, it requires at least one independent confirmation step, such as:

- a blind or preregistered reproduction;
- reproduction through an independently versioned data or transformation path; or
- a named independent DS or Committee reviewer challenge confirmation with evidence citations.

Until that confirmation exists, the Agent emits `insufficient_evidence` with an `urgent_investigation` next safe action. The Agent preserves the discovered signal, selection timing, tested-analysis inventory, counterevidence, and falsifier in the Evidence record. This rule prevents post-hoc metric shopping without making unexpected harm invisible.

Owner confirmation: agreed in the main orchestrator discussion on `2026-08-18`.

### S10 — M0 capability completion is separate from Flight decision-grade status

The program does not store or present a single ambiguous `M0 complete` boolean.

`M0 capability demonstrated` may be reached by one real, authorized production Flight whose fixed core checks executed, whose blocking or eligibility result was independently adjudicated as correct, and whose reviewer-auditable `FlightReadinessPacket` was produced. A correctly blocked `not_permitted` Flight may therefore satisfy the M0 capability milestone; the milestone is outcome-agnostic and does not require waiting for a second eligible Flight.

This does not make that Flight `decision_grade`. When the first real Flight is correctly blocked:

- the Flight remains unavailable as Committee decision evidence;
- M1 investigation may continue, but every claim depending on failed or missing M0 evidence remains capped by the applicable publication ceiling;
- the packet records `positive_production_path_unverified` as a typed Coverage Gap; and
- local fixtures must cover the positive `decision_grade` path without being represented as production validation.

The review surface must show at least two distinct states: program capability status and per-Flight `analysis_use`. It must never render `M0 capability demonstrated` as equivalent to production gate passage, product launch approval, production authorization, or Committee Acceptance.

Owner confirmation: agreed to the dual-state principle in the main orchestrator discussion on `2026-08-18`.

### S11 — Candidate diffs use an evidence- and change-type-driven gate

`FlightAdvisory` publication and candidate-diff generation are separate state dimensions. An M1 advisory does not automatically authorize or imply a candidate diff.

A syntactically valid, unapplied candidate diff may be generated only after a separate `candidate_diff_eligibility` gate verifies, at minimum:

- exact deployed artifact identity and deployed SHA binding;
- file and symbol attribution, with line attribution when the available provenance makes it reliable;
- runtime and scope reachability;
- a supported causal mechanism;
- material-alternative and counterevidence challenge;
- an independent code-domain review; and
- LOW or MEDIUM action risk. HIGH risk or large blast radius cannot pass this gate.

M2 query/result-level corroboration is mandatory when the proposed change affects relevance, ranking, AI-answer behavior, result presentation, or another user-visible search semantic. A versioned applicability rule may mark M2 corroboration not applicable for deterministic instrumentation, assignment, configuration, flag, ACL, or pipeline-wiring corrections when the evidence supporting the correction does not depend on query-level user-value interpretation.

Every candidate diff remains `not_applied`, is generated outside a source worktree, is delivered only through an authorized human review surface, and is unavailable to automation consumers or apply/commit/PR/deploy/rollback interfaces.

Owner confirmation: agreed to an evidence- and change-type-driven independent candidate-diff gate in the main orchestrator discussion on `2026-08-18`.

## Closure summary

The continuation resolved the three remaining high-value steelman disputes:

1. Post-unblinding evidence can trigger urgent investigation but needs an independent confirmation step before it can carry `recommend_change` or `recommend_block`.
2. A correctly blocked real Flight may demonstrate M0 program capability while the Flight remains non-decision-grade and the positive production path remains unverified.
3. Candidate-diff generation is controlled by a separate evidence/change-type gate; M2 corroboration is conditional on the proposed change's semantics rather than universally mandatory.

No new production authority, mutation authority, Committee authority, numeric threshold, source identity, schema binding, retention value, or P2/P3/P4 closure was granted.

## Still open

- Exact-digest architecture reconciliation and independent review after closure.

Owner closure confirmation: the Owner explicitly closed the steelman discussion and authorized the proposed reconciliation, independent-review, M0-prototype, packaging, commit, and push sequence on `2026-08-18`.
