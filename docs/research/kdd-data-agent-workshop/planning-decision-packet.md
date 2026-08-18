# Data Agent Redesign Planning Decision Packet

## Confirmed destination

- Deliver a requirements-first, problem-driven, deep, clear, implementation-ready greenfield redesign specification. Codex or Claude Code must be able to implement it directly or produce an implementation plan from it.
- The specification must select and explain logical architecture, contracts, interfaces, failure behavior, acceptance, and implementation sequence. It cannot stop at abstract principles.
- Scenario A: explain a post-experiment metric miss, tie it to deployed production code/config/flag/model/data/index/connector state, and identify what to inspect or change.
- Scenario B: find production changes matching a SEV metric-drop changepoint and affected scope, then produce a rollback-ready packet.
- The first gate and main deliverable is **M0 — Flight Readiness**. It produces an `ExperimentReadContract` and an immutable `FlightReadinessPacket` that decide whether one A/B Experiment, also called one Flight, and its decision-metric read are trustworthy.
- The first implementation program is one M0-M2 Validation Slice for one real authorized Flight. M1 Metric Movement and Production Grounding and M2 Win/Loss Evidence must run within the same four-to-six-active-week validation slice after their gates pass. Scenario B requires a separately approved later plan.
- The fixture-backed local M0 path is pre-production evidence, not M0 capability completion. The prior `M0-F0`–`M0-F5` continuation is exhausted. Any implementation requires a new exact-digest bounded Owner start receipt. Production-backed M0 capability additionally requires one real authorized Flight on the company laptop under the D8 receipt or a stricter applicable policy; production access, M1/M2 implementation, deployment, publication, commit, push, PR creation, and mutation remain unauthorized until their named gates and start decisions are satisfied.
- Old SMA, the KDD workshop, Champion, Fourth-place, Team 1286, and Team 1401 are Adopt/Adapt/Reject candidates only. Old SMA domain assets may be read and validated, but current production sources and named owners are authoritative. No source imposes a compatibility, migration, or target-architecture constraint.

## Success criteria

### M0 first gate, fixture evidence, and production-backed capability

- Freeze the Flight, decision-metric set and policy, population, assignment/exposure, window, source, estimator, unit, Experiment Owner, Independent DS Consultant, and Experiment Review Committee route in a versioned `ExperimentReadContract`.
- Default the first implementation to one decision metric without encoding singular cardinality as a permanent invariant. An approved preregistered policy may admit co-primary decision metrics.
- Read and independently recompute the decision metric through authorized read-only fixture or later approved source ports; preserve every source receipt, disagreement, failed check, and Coverage Gap.
- Evaluate identity/runtime, decision-metric registration/version/policy, assignment and analysis units, exposure, SRM/compositional SRM, scope, numerator/denominator/grain/join/unit/ratio/relative-percent/percentage-point handling, completeness/freshness/partial reads, estimator/variance method, CUPED identity, source/lineage/owner, primary-source versus scorecard/UI, independent recomputation, source-change revalidation, authorization/ACL/redaction/retention/load/halt, attribution, and disagreement/Coverage Gap closure without inventing missing authority or thresholds.
- Produce an immutable `FlightReadinessPacket` with `PASS | FAIL | MISSING | UNKNOWN | NOT_APPLICABLE` check outcomes and exactly one stored readiness state, `analysis_use = decision_grade | directional_only | not_permitted`. Renderers derive `post_analysis_eligibility = eligible | blocked`; it is never independently settable.
- Type every packet and receipt with `evidence_class = fixture | production_authorized`. A fixture packet cannot demonstrate M0 capability. A production start receipt preregisters and seals a versioned `core_check_set` whose fixed floor is CHK-01, CHK-03, the core assignment/exposure part of CHK-05, CHK-06, CHK-08, CHK-12, CHK-14, CHK-19, and CHK-16; the CHK-05 parity part and CHK-11 join the core only when their production sources were declared available before the read.
- Make the M0 first screen packet-, check-, and receipt-centered: show `evidence_class`, program `m0_capability_state`, per-Flight `analysis_use`, the derived eligibility projection, blockers, disagreements, Coverage Gaps, a typed `NextSafeAction`, and named `human_state` without implying a production cause. `m0_capability_state = not_demonstrated | demonstrated` is outcome-agnostic and changes to `demonstrated` only after one real authorized Flight executed every fixed core check, produced an auditable packet, and received independent adjudication that its eligible or correctly blocked result is correct. A correctly blocked first Flight remains non-decision-grade and records `positive_production_path_unverified`.
- For an invalid Flight, provide typed validity, instrumentation, or data-quality remediation guidance and a reopen condition. A correct unapplied remediation diff is allowed only after exact-target, authority, validation, and human-only delivery gates pass; guidance remains the permanent fallback.
- Prove the M0 path with hermetic fixtures for trusted, pre-runtime directional, invalid, materially unknown, conflicting, stale, partial, unauthorized, superseded, and reviewer-conflict reads. Preregister always-ready and always-blocked evaluators, adversarial metric-version/CUPED/source decoys, and fixture-author/evaluator independence or disclosed conflicts. False readiness, uncaught decoys, and security/ACL violations are hard NO-GO.

### M1 and M2 within the first validation slice

- Narrow a broad metric miss into ranked production candidates, grounded to deployed SHA, repo/file/symbol/line, or an exact config/flag/model/data artifact. Scenario A may produce an unapplied candidate diff.
- Include all shareable evidence and an auditable reasoning path: metric phenomenon → observed facts → typed production changes → mapping/association → cause claim → confidence/gaps/counterevidence → verify/falsify → recommendation. This is not hidden chain-of-thought.
- When evidence is insufficient, return ranked suspected directions or abstain. Never disguise them as a confirmed root cause.
- A blocked or critically invalid Flight may be investigated only under separate M1 authority, but every claim depending on failed or missing M0 evidence inherits the applicable publication ceiling. It cannot produce a promoted production-cause claim or product-logic recommendation from invalid evidence. Any validity/instrumentation/data-quality remediation remains separately gated.
- Keep Cause Verdict and Recommendation Readiness independent. Every state includes evidence, counterevidence, failed checks, scope, and policy-matrix rationale. No state authorizes mutation.
- Publish M1's non-binding conclusion as an append-only `FlightAdvisoryRevision` with `recommend_pass | recommend_change | recommend_block | insufficient_evidence`. It is separate from Cause Verdict, Recommendation Readiness, Action Approval, and Incident State, and records the official Query Success result, evidence IDs and lineage classes, counterevidence, falsifier and execution state, `query_evidence_state`, selection timing, independent-confirmation receipt, DS challenge record, and supersession.
- Challenge evidence declares `independent_instrumentation | shared_logs_independent_definition | derived_from_decision_metric_inputs`; the last class is not independent. Human judgment is decision-bearing only under a preregistered blind rubric and P4 authority; otherwise it remains exploratory. Post-unblinding evidence may trigger `urgent_investigation` but cannot alone carry `recommend_change` or `recommend_block`; until an independent confirmation receipt exists the advisory is `insufficient_evidence`, with selection timing and the tested-analysis inventory preserved.
- Candidate-diff generation has a separate `candidate_diff_eligibility` state. It requires exact deployed identity/SHA, reliable file/symbol attribution, runtime and scope reachability, a supported mechanism, alternative/counterevidence challenge, independent code-domain review, and LOW or MEDIUM risk. HIGH risk or large blast radius fails closed. M2 query/result corroboration is mandatory for user-visible search semantics; a versioned rule may mark it not applicable only for deterministic technical corrections whose evidence does not depend on query-level user value.
- False `confirmed`, an incorrect patch target, or a security/ACL violation is a hard NO-GO.
- MVP uses multiple cases: one real blind historical experiment miss plus de-identified fixtures for invalid experiments, implementation/config bugs, ACL/index/pipeline failures, measurement bias, product-hypothesis failure, and correct abstention.
- The Experiment Owner runs the Flight and prepares evidence. The Independent DS Consultant challenges methods and evidence without approval authority. The Experiment Review Committee alone decides pass, change, or block for a real production Flight. The old RCA is not the sole gold label.
- The first screen combines a conclusion summary with a local evidence graph for the primary claim, with access to full coverage, competing claims, the full graph, Trace, timeline, code, diff, and receipts.
- Graphs exist only for observability and reviewability. Use a table, timeline, diff, or receipt when it is clearer.
- Every node or edge affecting verdict/readiness has an explicit type and expandable trust detail. Conflicts, stale or invalidated evidence, supersession, and human overrides retain history.
- Human causal reviewer and action approver are separate where M1 action readiness applies. Material gates fail closed. The Agent is always read-only and no verdict authorizes mutation.
- Technical completion means review-ready M0, M1, and M2 packets for one authorized Flight. It does not imply Experiment Review Committee acceptance.
- Two builders have four to six active engineering weeks for the validation slice. The primary builder's leave from 2026-08-24 through 2026-09-14 is excluded from active time, and a reproducible Continuity Checkpoint is required before leave.
- Calibrate latency, tokens, cost, top-k, case count, stability, and shadow-read thresholds with production-complexity pilots rather than guesses.

## Canonical domain terms

**Query Success**: the production-bound online behavioral decision metric `TraditionalResultSuccess OR AIAnswerSuccess`. The component definitions, overlap handling, grain, population, window, and thresholds are fixed within a Flight and remain `PRODUCTION_BINDING_REQUIRED` until bound on the company laptop. Components are diagnostic; no hidden or post-hoc component guardrail is permitted.

**Flight Advisory**: a non-binding append-only M1 assessment `recommend_pass | recommend_change | recommend_block | insufficient_evidence`. It never grants action, mutation, launch, rollback, or Committee authority.

**Metric Question**: A question with a frozen metric, population, window, surface/component, and experiment or incident context.

**Experiment Miss**: An experiment that did not meet its expected metric outcome, subject to validity checks. It does not itself prove product-hypothesis failure or an implementation bug.

**Production Code Tie**: Evidence-backed mapping from a metric phenomenon or mechanism through runtime/deploy identity to an exact deployed repo/file/symbol/line or exact config/flag/model/data artifact. Keyword proximity is not a tie.

**Production Change Candidate**: A typed `code | config | flag | model | data` change that is reachable in affected scope, interval, and rollout and has a source receipt. A candidate is not automatically a cause.

**Cause Claim**: A falsifiable explanation of how a trigger, proximate mechanism, contributing factor, or systemic condition produced an observed metric effect.

**Recommendation**: An exact inspection, validation, modification, mitigation, or rollback proposal supported by action-specific evidence. It grants no execution authority.

**Evidence**: Reviewable material with stable identity, source locator, snapshot/time, scope, authorization, digest/receipt, freshness, and validation state.

**Cause Verdict**: The independent causal-assessment axis: `unassessed | suspected | confirmed | ruled_out | inconclusive`. `observed` belongs to evidence or claim state, not Cause Verdict.

**Recommendation Readiness**: The independent action-evidence axis: `not_applicable | blocked | proposal_ready | action_ready | rejected`. It derives from action-specific evidence, not cause confidence.

**Agent Autonomy**: The Agent may select and repeat allowlisted read-only tools and start bounded workers within an authorized dependency graph, subject to concurrency, scope, token/cost, timeout, and evidence-submission limits.

**Human Gate**: A fail-closed gate requiring a named human decision based on visible evidence. Timeout is not approval, and human opinion cannot replace missing evidence.

**Evidence Graph**: A typed projection for reviewing relationships among evidence, derived facts, mappings, claims, verification, contradictions, and recommendations. It is not an architecture diagram, execution trace, or hidden reasoning.

**Trace**: Agent/worker tool calls, retries, errors, and execution order. It is a separate linked view and does not automatically constitute claim evidence.

**Search Surface / SERP Component**: A production-observable delivery boundary such as quick find or SERP, and traditional results, AI search, or a mixed component. Unobservable `search_task` labels are not canonical.

**Declared / Reachable / Observed Impact**: What a change says it targets, what the dependency graph says it can affect, and what evidence shows it affected. These remain distinct.

## Adopt / Adapt / Reject criteria

- **Adopt**: A source-backed practice directly satisfies an A/B requirement, has clear responsibility, failure boundary, and evidence obligation, and does not weaken read-only behavior, causal discipline, tenant/ACL controls, human gates, or auditability.
- **Adapt**: A useful mechanism comes from a competition/file-analysis context without production metric, runtime/deploy/change, permission, or causal proof. Add typed receipts, scope, authorization, validators, falsifiers, and failure ceilings before use.
- **Reject**: A practice depends on legacy compatibility; treats heuristics, consensus, narration, or traces as fact or causation; permits arbitrary execution, forced submission, fail-open gates, hidden evidence gaps, or expanded authority; or cannot be justified by A/B problems and acceptance fixtures.
- Learn directly from Team 1286 source graphs, node/group detail, question-specific paths, re-layout, and `rests on` affordances. Its paper generation chain is an author claim without a public repo SHA.
- Learn directly from Team 1401 schema/PDF graphs, typed relations, clusters, filters, collapse/expand, locators, and exact-receipt affordances. Its generation implementation was not observed.
- Neither team proves the complete production causal chain. This is an Adapt gap, not a denial that their graph UIs exist.
- Champion/Fourth-place provide bounded-stage, allowlist, validation, and trace-visibility ideas. Their graph UI was not observed, and debug/static artifacts are not evidence graphs.

## Wayfinder status and current frontier

- Resolved: [Freeze the Canonical Domain and Policy Contracts](wayfinder/freeze-canonical-domain-policy-contracts.md) — canonical orthogonal states and fail-closed policy are frozen.
- Current frontier:
- [Establish Production Evidence Authority and Access Boundaries](wayfinder/establish-production-evidence-authority.md) — requires production owner, Eng, and security/privacy source ownership.
- [Prototype the Observability-First Review Surface](wayfinder/prototype-observability-first-review-surface.md) — build a rough prototype from Team 1286/1401 UI evidence and review it with humans.
- [Freeze Evaluation Gold, Adjudication, and Calibration](wayfinder/freeze-evaluation-gold-and-calibration.md) — freeze the threshold-free evaluation contract, then calibrate numbers with pilots.

## Owner-confirmed decisions and remaining gates

- **Resolved on 2026-08-16:** one Flight is one A/B Experiment; M0 is the first gate and main deliverable; M1 and M2 run in the same one-Flight validation slice; the first M0 path defaults to one decision metric while the target supports an approved co-primary policy; invalid Flights may receive gated unapplied validity/instrumentation/data-quality remediation; production roles separate the Experiment Owner, Independent DS Consultant, and Experiment Review Committee; old SMA assets are candidates rather than production authority; and the four-to-six-week budget counts active engineering time only.
- **Current session boundary:** no implementation receipt is live. Fixture work, the first real-Flight laptop run, M1/M2, and production work must not start from this packet alone.
- Before 2026-08-24, the Continuity Checkpoint must make the current build runnable and resumable from a clean context without oral history. If no builder works during leave, calendar progress pauses.
- After a real source inventory exists, the owner must join production owner, Eng, and security/privacy to confirm authoritative sources, mapping ownership, sensitive raw evidence, retention/redaction, and tenant-expansion boundaries.
- After blind cases and production-complexity pilots, the owner must confirm case set, risk weights, top-k, stability, latency/token/cost, and shadow-read GO/NO-GO thresholds.
- After the observability prototype, the owner must confirm that its interactions reduce review time and expose conflict and failure rather than merely looking complete.
- Any later ticket that changes confirmed product meaning must return to an owner gate. Engineering choices such as schema encoding, storage, language, vendor, and framework must not masquerade as owner decisions.
