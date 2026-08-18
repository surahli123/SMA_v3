# Owner Steelman Alignment — Final Record

Status: `OWNER_CONFIRMED_COMPLETE`

Closed: `2026-08-18`  
Discussion language: Chinese  
Durable record language: English

## Authority and source records

This record consolidates the Owner decisions from:

- `steelman-owner-alignment-handoff.md` — S1 through S8;
- `steelman-owner-alignment-codex-continuation.md` — S9 through S11; and
- `architecture-decision-ledger.md` — D1 through D8 and their source attributions.

Where a facilitator proposal conflicts with S1-S11 or D1-D8, the confirmed Owner decision controls. This record closes the product steelman discussion; it does not itself freeze implementation bytes.

## Confirmed product decisions

| ID | Confirmed decision |
| --- | --- |
| S1 | M0 capability requires one real authorized production Flight on the company laptop; fixtures are pre-production evidence only. |
| S2 | Production metric definitions, schemas, catalog identities, business-table routing, ACLs, owners, retention, and source bindings come from the company environment, never old SMA assumptions. |
| S3 | The decision metric is online behavioral `Query Success = TraditionalResultSuccess OR AIAnswerSuccess`; thresholds are fixed within a Flight and production values remain `PRODUCTION_BINDING_REQUIRED`. |
| S4 | M0 validates registration, instrumentation, read integrity, common grain/population/window, overlap handling, source authority, and reproducibility. M1 explains component movement, substitution, mix shift, and user-value meaning. |
| S5 | Query Success is the decision metric. Its components are diagnostic, and the Agent may not invent post-hoc component guardrails. |
| S6 | M1 publishes a separate, explicit, non-binding `FlightAdvisory`: `recommend_pass | recommend_change | recommend_block | insufficient_evidence`. The Committee retains final authority. |
| S7 | Component divergence alone cannot justify `recommend_change` or `recommend_block`; at least one valid, scope-matched outcome stream not mechanically derived from the same union metric is required. |
| S8 | M1 need not wait for M2 query examples when its evidence floor is met. M2 may strengthen or falsify the advisory. |
| S9 | A post-unblinding evidence stream may trigger urgent investigation, but it needs independent confirmation before it can carry `recommend_change` or `recommend_block`. Until then the advisory is `insufficient_evidence`. |
| S10 | A correctly blocked real Flight may establish `M0 capability demonstrated` after independent adjudication, while that Flight remains non-decision-grade and the positive production path remains unverified. |
| S11 | Candidate-diff generation has an independent evidence- and change-type-driven gate. M2 corroboration is mandatory for user-visible search semantics but may be not applicable for deterministic technical corrections under a versioned rule. |

## Resulting architecture boundaries

1. Program capability, per-Flight `analysis_use`, production authorization, M1 advisory readiness, and Committee Acceptance are separate state dimensions.
2. M0 blocking constrains dependent claims; it does not prevent M1 investigation.
3. A validity-based `recommend_block` targets only `use_of_this_flight_as_decision_evidence`. It never blocks product launch, rollback, deployment, or mutation.
4. `FlightAdvisory` is separate from Cause Verdict, Recommendation Readiness, Action Approval, and Incident State.
5. The official metric result and the Agent advisory render together, with evidence lineage, counterevidence, falsifier state, and typed Coverage Gaps.
6. Candidate diffs remain syntactically valid, unapplied, human-only, capability-isolated, and unavailable to automation consumers.
7. A new exact-digest candidate, independent review, and bounded implementation handoff are required before M0-F1 through M0-F5.

## Explicit non-decisions and remaining gates

This alignment does not decide or close:

- production table names, schema fields, metric threshold values, or timer implementations;
- P2 evidence authority and access boundaries;
- P3 live review-surface acceptance;
- P4 evaluation calibration and numeric thresholds;
- production deployment or write authority;
- Committee Acceptance; or
- any real Flight's outcome.

## Closure receipt

The Owner explicitly confirmed closure of the steelman discussion and authorized the following sequence: reconcile the architecture, perform independent exact-byte review, complete and independently verify the M0 prototype, package the research and design artifacts, verify the exact user-owned GitHub repository, then commit and push the intended package.
