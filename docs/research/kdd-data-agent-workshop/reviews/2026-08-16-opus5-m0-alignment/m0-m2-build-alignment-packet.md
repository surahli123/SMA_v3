# M0-M2 Build Alignment Packet

Status: Owner-aligned post-review correction candidate; not frozen  
Date: 2026-08-16  
Scope: One authorized production Flight through M0, M1, and M2  
Authority: [`owner-alignment-record.md`](owner-alignment-record.md)  
Implementation authority: The completed `m0-codex-continuation-20260817` authorization covered one non-recurring local Phase A continuation and is exhausted. `M0-F1`–`M0-F5` require a new Owner authorization and start receipt binding the accepted packet path, revision label, SHA-256, active-time cap, run/read/tool cap, expiry, and halt owner. Production access and M1/M2 implementation are not granted.

## 1. Purpose

This packet is the proposed build contract among the Owner, Opus 5, and Codex. It prevents a technically plausible implementation from drifting away from the real post-experiment workflow. It also separates technical packet completion from Experiment Review Committee acceptance.

The three alignment parties are:

1. **Owner:** controls product meaning, workflow fit, milestone boundaries, staffing intent, and whether the result serves the real experiment job.
2. **Claude Code Opus 5:** independently challenges coverage, ambiguity, safety, feasibility, and fidelity to prior review findings.
3. **Codex:** maintains the evidence and conflict ledger, keeps the planning corpus consistent, and binds implementation to the applicable start authorization and frozen packet revision.

No alignment verdict authorizes production access, mutation, deployment, publication, or Committee Acceptance. The completed pre-alignment and continuation handoffs no longer grant a live implementation capability. `M0-F1`–`M0-F5` may start only under a new Owner authorization and start receipt that binds this packet's accepted path, revision, digest, bounded execution budget, expiry, and halt owner.

## 2. Product Outcome

Within four to six active engineering weeks, two builders should run one real, authorized Flight through three ordered milestones:

1. **M0 — Flight Readiness:** Can the Experiment setup and decision-metric read be trusted?
2. **M1 — Metric Movement and Production Grounding:** What explains the outcome, and which deployed production state could implement the supported mechanism?
3. **M2 — Win/Loss Evidence:** Which real queries or result examples make the supported movement concrete, and are they comparable?

M0 is the first gate and main deliverable. A correctly blocked real Flight remains non-decision-grade, but M1 investigation may continue under separate authority; every claim depending on failed or missing M0 evidence remains capped by the applicable publication ceiling. M2 cannot start until M1 has a review-ready supported mechanism or explicitly bounded candidate explanation. The slice ends with three review-ready packets for the same Flight. Committee Acceptance remains a separate human decision.

Scenario B SEV analysis, M3+ self-serve productization, generalized multi-source expansion, and autonomous action remain outside this slice.

The first planned implementation slice is fixture-backed M0 pre-production evidence. It is not M0 capability completion. No M0 unit is currently authorized: `M0-F1`-`M0-F5` require the new exact-digest bounded Owner receipt. The real-Flight capability run, M1, and M2 each retain their separate gates and authority.

## 3. Canonical Flight and Decision Metric Contract

A `Flight` is one A/B `Experiment`. Rollout, exposure, analysis window, and run attempts are revisions or observations within that Flight.

`ExperimentReadContract` must model a decision-metric set plus a frozen `DecisionMetricPolicy`:

- M0 defaults to one decision metric.
- Co-primary metrics require an approved, preregistered policy that defines their combination, conflict, and stop behavior.
- Monitoring and guardrail metrics do not silently become decision metrics.
- The policy must bind metric definition version, unit, estimator, assignment and analysis units, source, window, population, and owner.
- The policy must declare exactly one preregistered `sufficiency_rule.kind`: `runtime_only | runtime_and_sample`. The rule binds the preregistered runtime threshold and, for `runtime_and_sample`, the preregistered sample/unit threshold and inputs. M0 compares observed runtime and sample/units only to those declared inputs; it never computes or substitutes post-hoc or achieved power.

## 4. Human Responsibility Contract

| Role | Owns | Must not own |
| --- | --- | --- |
| Experiment Owner | Experiment design and execution; contract inputs; evidence package; response to review questions | Final approval of their own production Flight |
| Independent DS Consultant | Independent challenge of methods, metric reads, evidence, uncertainty, and risk | Final approval or evidence substitution |
| Experiment Review Committee | Experimentation triage/review; pass, change, or block decision | Agent execution, evidence invention, or silent contract revision |
| Engineering / production owner | Source authority, deployed identity, mapping, runtime reachability, and operational constraints | Product-metric meaning or Committee Acceptance alone |
| Security/privacy reviewer | ACL, tenant, sensitive-field, retention, redaction, credential, and recipient boundaries | Causal or launch decision alone |
| Data Agent | Bounded read-only collection, validation, analysis, packet generation, and candidate preparation | Mutation, approval, deploy, rollback, message sending, or publication |

Fixture-only development may document a time-bounded role overlap. A real production Flight may not use that exception.

## 5. M0 — Flight Readiness

### 5.1 Required input

The frozen `ExperimentReadContract` must include or explicitly mark unknown:

- Flight identity, contract version, predecessor, and effective time;
- hypothesis and decision purpose;
- treatment and control identity;
- decision-metric set and `DecisionMetricPolicy`;
- production-bound online behavioral `Query Success = TraditionalResultSuccess OR AIAnswerSuccess`, with component definitions, common grain/population/window, overlap policy, and fixed-within-Flight thresholds; unresolved production values are typed `PRODUCTION_BINDING_REQUIRED`, and components are diagnostic rather than hidden guardrails;
- metric definition version, unit, estimator, ratio-variance method when applicable, and owner;
- population, eligibility, exclusions, tenant/surface/locale, assignment unit, analysis unit, exposure definition, and join keys;
- analysis window, timezone, ramp, planned runtime, and observed runtime;
- source identity, snapshot/version, lineage, freshness rule, and authoritative production owner;
- `evidence_class = fixture | production_authorized` on every packet and receipt;
- expected assignment/exposure and SRM or compositional-SRM plan;
- treatment/control arm-parity identities for index generation, serving alias, ACL snapshot, and effective pipeline;
- preregistered `sufficiency_rule.kind = runtime_only | runtime_and_sample`, its runtime threshold, and, when `runtime_and_sample`, its preregistered sample/unit threshold and inputs;
- legal readiness-combination policy;
- orthogonal authorization and redaction states; tenant/ACL, retention, recipient, load, halt, and export boundaries; and, for the first real Flight, the D8 laptop-scoped receipt or a stricter applicable policy;
- a versioned sealed `core_check_set` for production execution, preregistered before the read and immutable afterward;
- named Experiment Owner, Independent DS Consultant, and Experiment Review Committee route;
- contract digest, expiry, predecessor, and supersession link.

Missing authority, identity, metric meaning, or unit remains `UNKNOWN` or `MISSING`. The Agent must not infer it from old SMA, a dashboard label, or repository proximity.

### 5.2 Required checks

Each M0 check returns `PASS | FAIL | MISSING | UNKNOWN | NOT_APPLICABLE`, materiality, rule source, Evidence and receipt IDs, reason, and reopen condition.

The minimum check set covers:

1. Flight identity and contract version;
2. preregistered versus observed runtime;
3. decision-metric registration, definition version, role, and policy;
4. assignment-unit and analysis-unit consistency, including a named ratio-metric variance estimator when applicable;
5. treatment/control assignment, exposure integrity, and arm parity across index generation, serving alias, ACL snapshot, and effective pipeline;
6. SRM and applicable compositional SRM;
7. population, eligibility, exclusions, and scope consistency;
8. numerator, denominator, grain, join keys, unit arithmetic, ratio handling, and relative-percent versus percentage-point handling;
9. completeness, freshness, late arrival, pagination, and partial-read handling;
10. estimator and variance-method consistency;
11. CUPED-mode identity and non-interchangeability, including preservation of both adjusted and unadjusted values when they disagree;
12. source, lineage, metric-definition, and source-owner identity;
13. primary-source versus scorecard or UI reconciliation;
14. reported decision-metric read versus recomputation with `independence_class = independent_source | independent_transform | same_pipeline`, the same immutable authoritative source snapshot/interval/scope/receipt, an independently versioned deterministic transform, input manifest, transform and output digests, and the versioned comparison rule;
15. source-change revalidation for meaning, coverage, and attribution;
16. authorization, tenant/ACL, recipient, redaction, retention, load, and halt state;
17. attribution, freshness, and scope consistency across every source and derived read; and
18. disagreements, contradictions, and Coverage Gap closure state; and
19. preregistered sample/unit sufficiency for the decision metric when `sufficiency_rule.kind = runtime_and_sample`; this check is `NOT_APPLICABLE` only under a versioned `runtime_only` rule.

**Check-14 independence rule.** D4/D6 require at least `independent_transform`; `same_pipeline` yields `UNKNOWN`, applies the material ceiling, and reopens through `evidence_collection`. Sharing the immutable primary source snapshot is explicit and always records the versioned Coverage Gap `shared_source_snapshot`; it does not make evidence independently sourced. A second independently lineaged source remains optional behind P2. No comparison tolerance is invented: `DecisionMetricPolicy.comparison_rule_id` owns it.

**Production core rule.** The sealed `core_check_set` has a fixed floor: CHK-01, CHK-03, the core assignment/exposure part of CHK-05, CHK-06, CHK-08, CHK-12, CHK-14, CHK-19, and CHK-16. The parity part of CHK-05 and CHK-11 enter the core only when their production source was declared available before the read. Non-core checks still execute or emit typed Coverage Gaps. Any core `MISSING` or `UNKNOWN` leaves production-backed M0 capability unproven even when `analysis_use = not_permitted` is correct.

**Check-outcome rule.** Each check stores exactly one outcome from `PASS | FAIL | MISSING | UNKNOWN | NOT_APPLICABLE`. `NOT_APPLICABLE` requires a versioned applicability rule and rationale; without both, the stored check outcome is `UNKNOWN`.

For arm parity, missing required per-arm index-generation, serving-alias, ACL-snapshot, or effective-pipeline identity yields `MISSING` and, under the fail-closed materiality rule, `blocked + not_permitted` with `next_safe_action.kind = evidence_collection`. A versioned `DecisionMetricPolicy` applicability rule may declare the check `NOT_APPLICABLE`, for example for a single-index non-search Flight; divergent applicable arms are a material `FAIL`.

For sufficiency, check 2 compares observed runtime with the preregistered runtime threshold. Check 19 compares observed sample/units with preregistered inputs only when `sufficiency_rule.kind = runtime_and_sample`; it never computes post-hoc or achieved power. Under `runtime_only`, check 19 is `NOT_APPLICABLE` by that versioned rule. Under `runtime_and_sample`, missing declared sample fields yields `MISSING`, making the contract incomplete and producing `blocked + not_permitted` with `next_safe_action.kind = contract_correction`.

**Materiality rule.** Each check separately stores `materiality = material | non_material | unknown`, `materiality_rule_id`, affected decision metric/scope/window, and ruling actor or deterministic rule. A result is material when it can change decision-metric meaning, value, uncertainty, eligibility, population, attribution, authority, coverage, or security/privacy handling. Flight identity, decision-metric identity/policy, assignment/exposure, population/scope, numerator/denominator/join/unit, estimator/CUPED, authoritative source identity, and authorization/isolation failures are always material. Preregistered runtime or sample/unit insufficiency is material but maps specifically to `directional_only` when all other validity checks permit the read. `non_material` requires a preregistered versioned rule and evidence that the affected field cannot change the decision; reviewer convenience is not a rule. `unknown` and unclassified values remain stored as `unknown`, preserving the reviewable classification gap, while the applied decision ceiling treats them as material until a versioned ruling supersedes them.

Adjusted and unadjusted reads are never silently substituted, and a scorecard/UI value is a reconciliation surface rather than production authority.

### 5.3 Readiness outcome contract

M0 stores exactly one readiness state:

- `analysis_use = decision_grade | directional_only | not_permitted`.

`post_analysis_eligibility = eligible | blocked` is a render-time projection derived only from `analysis_use`; it is never stored or independently settable:

| Stored `analysis_use` | Derived `post_analysis_eligibility` | Meaning |
| --- | --- | --- |
| `decision_grade` | `eligible` | The frozen M0 checks permit decision-grade post-analysis. This does not itself start M1 or imply Committee Acceptance. |
| `directional_only` | `blocked` | The read is valid enough to inspect but the declared preregistered sufficiency rule is incomplete. It cannot pass the decision metric or enter M1 causal promotion. |
| `not_permitted` | `blocked` | A material validity, authority, isolation, contract-completeness, or evidence failure forbids post-analysis. |

Scenario and review wording may retain `eligible + decision_grade`, `blocked + directional_only`, and `blocked + not_permitted` as shorthand for these three projections. `directional_only` is not a softer form of M1 authorization, and it cannot be promoted by a renderer, reviewer preference, or Committee outcome. Review triage keys on the stored `analysis_use` together with `next_safe_action.kind`, never on the derived eligibility projection alone.

### 5.4 M0 output and invalid-experiment behavior

`FlightReadinessPacket` contains `evidence_class`, the frozen contract revision, source and derivation receipts, the sealed core-check-set revision, all checks, disagreements, Coverage Gaps, the stored `analysis_use` state, blockers, typed next safe action, `human_state`, orthogonal authorization/redaction states, laptop export manifest and redaction receipt where applicable, digest, expiry, and supersession link. Renderers derive `post_analysis_eligibility` from `analysis_use` without persisting a second readiness field.

A trusted Flight may proceed to M1 only after its separate implementation-start and production gates also pass. A Flight that fails the preregistered runtime threshold or, under `runtime_and_sample`, the preregistered sample/unit threshold is `blocked + directional_only` when no other material blocker applies. A pre-runtime packet's reopen condition names the preregistered runtime end as its trigger, and its `expiry` must not exceed that time; reaching the trigger requires a new read and superseding packet rather than mutating the sealed packet. Missing required `runtime_and_sample` inputs is contract-incomplete rather than directional: it is `blocked + not_permitted` with `contract_correction`. A materially invalid, unauthorized, or isolated Flight is `blocked + not_permitted`. A critically invalid Flight cannot produce a production-cause Claim, product-logic recommendation, production-change candidate, or M1/M2 output.

`next_safe_action` is a typed guidance field with exactly one kind:

`evidence_collection | contract_correction | validity_fix | instrumentation_fix | data_quality_fix`.

It names the missing or corrective work and reopen condition, but carries no exact production target and no diff. Any optional exact candidate diff lives only in the separately typed `InvalidExperimentRemediation` artifact and must pass the O3 gates below.

An invalid Flight may receive an `InvalidExperimentRemediation`:

- The first vertical path returns typed guidance and a reopen condition.
- A later M0 increment may attach a correct, reviewable, unapplied diff limited to validity, instrumentation, or data-quality remediation after exact-target, authority, validator, and no-write delivery gates pass.
- When any gate is incomplete, guidance remains the required fallback.
- The Agent never applies the diff or exposes it to an automation consumer.

### 5.5 Program capability is not Flight readiness

The program stores `m0_capability_state = not_demonstrated | demonstrated` separately from every Flight's `analysis_use`. It becomes `demonstrated` only when one real authorized production Flight runs the sealed fixed-floor core set on the company laptop, produces a reviewer-auditable packet, and independent adjudication confirms that its eligible or correctly blocked outcome is correct. A correctly blocked Flight remains non-decision-grade, unavailable as Committee decision evidence, and carries `positive_production_path_unverified`; fixture coverage of the positive path is never represented as production validation. Capability demonstration is not P2 closure, production authorization, launch approval, or Committee Acceptance.

The D8 first-Flight receipt names the Flight, existing sources and owners, the Owner's existing read-only entitlement, write-denial attestation, laptop-local raw-evidence boundary and retention period, Owner halt authority, and security/privacy notification. Exports are limited to the packet, receipts, and a redaction manifest with digests, and packets carry `authorization_scope = laptop_owner_entitlement`. If company policy requires formal approval for automated reads, the receipt is void and full P2 applies.

## 6. M1 — Metric Movement and Production Grounding

M1 investigation may proceed under its separate authority even when a Flight is blocked, but every dependent claim remains under the applicable publication ceiling. Its output is an immutable `MetricMovementPacket` containing:

- the observed result across the decision metric, related metrics, preregistered segments, and named trade-offs;
- source reads, derivations, units, uncertainty, contradictions, and Coverage Gaps;
- a ranked set of falsifiable mechanism Claims with predictions, falsifiers, alternatives, and counterevidence;
- exact production grounding through scope, interval, rollout, runtime/deploy identity, and symbol or non-code artifact attribution;
- typed candidates spanning at least `code | config | flag | model | data`, with other subtypes admitted only through an accepted domain contract;
- Cause Verdict and Recommendation Readiness as independent states;
- verification and falsification steps;
- an optional syntactically valid `not_applied` candidate diff only after exact-target, causal, action-evidence, risk, review, and delivery gates pass.

M1 also appends a `FlightAdvisoryRevision` with `recommend_pass | recommend_change | recommend_block | insufficient_evidence`. The revision is separate from Cause Verdict, Recommendation Readiness, Action Approval, and Incident State and records the official Query Success result, evidence IDs, lineage classes, counterevidence, falsifier and execution state, `query_evidence_state`, selection timing, tested-analysis inventory, independent-confirmation receipt, Independent DS challenge record, and supersession. It is non-binding and never authorizes action.

Challenge evidence declares `independent_instrumentation | shared_logs_independent_definition | derived_from_decision_metric_inputs`; the last is not independent. Human judgment is decision-bearing only under a preregistered blind rubric and applicable P4 authority, otherwise it remains exploratory. Component divergence or evidence mechanically derived from Query Success inputs cannot alone carry `recommend_change` or `recommend_block`. Post-unblinding evidence may trigger `urgent_investigation`, but until an independent confirmation receipt exists the advisory remains `insufficient_evidence`.

`candidate_diff_eligibility` is a separate gate from the advisory. It requires exact deployed artifact/SHA, reliable file/symbol attribution, runtime/scope reachability, supported causal mechanism, material-alternative and counterevidence challenge, independent code-domain review, and LOW or MEDIUM risk. HIGH risk or large blast radius fails closed. M2 corroboration is mandatory for user-visible search semantics; a versioned applicability rule may mark it not applicable only for deterministic technical corrections whose support does not depend on query-level user value. Every diff remains `not_applied`, generated outside a source worktree, delivered only to an authorized human review surface, and unreachable by automation or apply/commit/PR/deploy/rollback interfaces.

Repository similarity, commit timing, or an unverified graph edge cannot establish production grounding. Missing exact mapping keeps the Claim `suspected` or `inconclusive` and blocks an exact recommendation.

## 7. M2 — Win/Loss Evidence

M2 starts only after M1 identifies a supported mechanism or bounded candidate explanation. Its immutable `WinLossEvidencePacket` contains:

- the linked M1 Claim and predicted direction;
- candidate-query discovery method and coverage;
- exact query or trace identity through an authorized opaque locator;
- treatment and counterfactual/control result identities;
- replay/SBS configuration, source, corpus/index snapshot, ACL/tenant scope, and comparability receipts;
- side-by-side evidence or an explicit counterfactual gap;
- `win | loss | unclear | not_comparable` judgment with named human review;
- counterexamples, coverage limits, disagreement, and artifact digest.

Examples make an aggregate mechanism concrete; they do not independently prove the aggregate cause. Missing replay, authorization, counterfactual, or comparability remains visible and cannot be converted into a win or loss.

## 8. Production Authority and Old SMA

The validation slice uses exactly one P2-authorized production path before any expansion. The production authority must bind source owners, deployed identity and mapping owners, credential scope, tenant/ACL boundary, sensitive fields, retention/redaction, load ceilings, halt authority, recipient scope, expiry, and failure behavior.

Old SMA metric definitions, schema catalogs, business-table routing, and fixtures are discovery candidates only. Each adopted fact must be checked against current production sources and named owners for the Flight's scope and effective time. The transferred contract records its old source, production validator, validation receipt, observed drift, and adopted revision.

The new package does not import or depend on old SMA runtime or architecture. Direct code reuse is a separate gated decision and requires interface, provenance, test, security, and license evidence.

## 9. Build Envelope and Continuity

### 9.1 Staffing and active-time budget

- Two builders.
- Four to six active engineering weeks for M0 through M2.
- Part-time Experiment Owner, Independent DS Consultant, Experiment Review Committee, production/Engineering owner, and security/privacy support when their gate requires it.
- Primary builder leave from 2026-08-24 through 2026-09-14 does not count as active engineering time.
- End of September is a stretch target. It is not a promise of technical completion or Committee Acceptance.
- Every implementation start receipt must also bind a slice-specific active-time cap, run/read/tool cap, expiry, and halt owner. An unset or exceeded cap halts that slice; it is never converted into silent extra scope. Handoff `m0-codex-continuation-20260817` was a one-run, non-recurring continuation and is exhausted; it supplies no current execution budget. The next `M0-F1`-`M0-F5` start receipt must bind the accepted packet path, revision, SHA-256, active-time cap, run/read/tool cap, expiry, and halt owner. The four-to-six-week active-time envelope governs the complete M0-M2 validation program but is not itself a start budget.

### 9.2 Continuity Checkpoint due before 2026-08-24

The checkpoint must include:

- a clean-checkout branch and immutable revision identifier after implementation authorization;
- locked dependencies and environment prerequisites;
- one documented command that runs the current hermetic path and verification suite;
- fixture/source manifests with no secrets;
- completed, partial, blocked, and next work mapped to stable unit and scenario IDs;
- expected outputs, current receipts, known failures, Coverage Gaps, gate state, and named owners;
- a fresh-context handoff rehearsal in which a builder or coding-agent session runs the project and completes the next bounded task without oral context;
- a return runbook that restores effective work within half a day on or after 2026-09-15.

If no builder continues during leave, calendar progress pauses. The checkpoint preserves usability and limits restart cost; it does not claim progress that did not occur.

## 10. Implementation Slices

| Slice | Outcome | Exit evidence |
| --- | --- | --- |
| V0 — Continuity-ready foundation | Isolated package, frozen contracts, fixture read, deterministic receipts, and pre-leave checkpoint | Clean-context rehearsal runs the hermetic path and names the next task |
| V1 — M0 Flight Readiness | Trusted and blocked fixtures plus one authorized Flight produce a `FlightReadinessPacket` | Every material check and gap resolves to a receipt; false readiness fails hard |
| V2 — One production-grounding path | One least-privilege source and deployed-identity path is authorized and reproducible | Read/write-denial, scope, mapping, freshness, and halt receipts pass |
| V3 — M1 Metric Movement | The Flight produces ranked, falsifiable, production-grounded explanations | Exact mappings are proven or remain explicitly blocked; no inferred authority |
| V4 — M2 Win/Loss Evidence | The linked mechanism produces reviewable query-level examples and counterexamples | Comparability, replay/SBS, ACL, coverage, and human-review receipts are explicit |
| V5 — Review-ready handoff | M0, M1, and M2 packets share one Flight identity and are ready for Committee review | Owner and independent reviewer can trace every conclusion to Evidence and state remaining gaps |

V0 and V1 precede V3. V2 must close before a real M1 or M2 production claim. V4 depends on M1. V5 does not imply Committee Acceptance.

## 11. Acceptance Scenarios

The `VAL-*` entries below define scenario meaning only. The single authoritative ownership registry is [Implementation Sequencing, "Authoritative `VAL-*` ownership registry"](../../implementation-sequencing.md#authoritative-val--ownership-registry). That table assigns every active ID exactly once to an `M0-F*` unit, later `U*` unit, or explicit external gate and names its proving test/receipt or open-gate evidence. This packet does not duplicate ownership; an identifier has one meaning and may not be reused by another plan, fixture, or test.

| ID | Scenario | Required result |
| --- | --- | --- |
| `VAL-FLT-001` | One Experiment has multiple rollout/run/window observations | All observations remain under one Flight identity |
| `VAL-MET-001` | Default one-metric policy | Contract is accepted without hard-coding singular cardinality |
| `VAL-MET-002` | Approved co-primary policy | Combination/conflict rule is frozen before the read; an unapproved second metric cannot gate the decision |
| `VAL-M0-001` | Trusted complete Flight read | M0 packet is review-ready with stable receipts and digest |
| `VAL-M0-002` | Preregistered runtime/sample insufficiency or a material validity, source, ACL, isolation, evidence, or contract-completeness failure | Failure of the preregistered runtime threshold or, under `runtime_and_sample`, the preregistered sample/unit threshold with no other material blocker is exactly `blocked + directional_only`. Missing required `runtime_and_sample` fields is `blocked + not_permitted` with `contract_correction`; any other material validity, source, ACL, isolation, or evidence failure is `blocked + not_permitted`. No post-hoc or achieved-power computation is permitted, and neither state produces M1/M2 output. |
| `VAL-PRE-001` | Observed runtime is shorter than the preregistered runtime | Packet is `blocked + directional_only`; the decision metric cannot pass and M1 causal promotion cannot start |
| `VAL-CUP-001` | Reported and recomputed reads use different CUPED modes | Packet is `blocked + not_permitted`; both values and modes remain visible and no substitution occurs |
| `VAL-UNIT-001` | Assignment and analysis units differ for a ratio metric without a named valid variance estimator | The applicable unit/estimator check fails materially and the packet is `blocked + not_permitted` |
| `VAL-SRC-001` | Contract is internally consistent but the registered metric-definition version differs from the computed source version | The decoy is caught by check 3 or 15 and cannot become eligible |
| `VAL-SUP-001` | Corrected source read arrives after packet sealing | A new packet supersedes the old packet with a new digest; the prior acknowledgement is invalidated and history is not edited |
| `VAL-CONF-001` | Two named reviewers disagree on materiality | Both positions remain visible and the packet stays blocked until a versioned ruling resolves the conflict |
| `VAL-REM-001` | Invalid Flight without exact remediation target | Typed guidance, Coverage Gap, and reopen condition; no diff |
| `VAL-REM-002` | Exact bounded validity/instrumentation/data-quality remediation passes all gates | Correct syntactically valid diff is attached as `not_applied` and has no automation consumer |
| `VAL-M1-001` | Valid Flight with exact deployed mapping | Ranked mechanism Claims link to deployed SHA and repo/file/symbol/line or exact non-code artifact |
| `VAL-M1-002` | Valid Flight with unresolved production mapping | Claim remains suspected/inconclusive and exact recommendation is blocked |
| `VAL-M2-001` | Comparable treatment/control query evidence | Packet records win/loss/unclear with exact receipts, coverage, and linked M1 prediction |
| `VAL-M2-002` | Missing ACL, replay, counterfactual, or comparability | Judgment is `not_comparable` or a typed Coverage Gap, never inferred win/loss |
| `VAL-ROL-001` | Real production Flight reaches review | Owner prepares, DS independently challenges, Committee alone decides pass/change/block |
| `VAL-OLD-001` | Old SMA definition conflicts with current production authority | Production definition wins; drift and provenance remain visible |
| `VAL-CON-001` | Fresh context checks out the implementation before leave | It runs the current path, explains state, and starts the next bounded task without oral context |
| `VAL-APR-001` | All technical packets are review-ready but Committee has not ruled | Technical state is complete/review-ready; Committee Acceptance remains pending |
| `VAL-SEC-001` | Any write, cross-tenant, secret, unsafe-redaction, or unauthorized delivery path is reachable | Hard NO-GO; no packet promotion or external action |
| `VAL-UI-001` | Pre-P3 synthetic packet projection | A reviewer reaches exact source and D4/D6 recomputation receipts without any implied production capability or cause; this is mechanical projection proof only |
| `VAL-UI-101` | Post-P3 named-reviewer interaction | The accepted first-screen hierarchy and review behavior are bound to a named live-review receipt; this cannot pass before P3 |
| `VAL-BASE-001` | Always-ready and always-blocked evaluators run against the M0 fixture suite | Each trivial evaluator is contradicted by at least one sealed planted-truth fixture; otherwise the suite is rejected before Agent scoring |
| `VAL-DECOY-001` | Adversarial metric-version, CUPED-mode, or source-identity decoy | The planted mismatch remains hidden from superficial consistency checks but is caught by the exact required validator |

Numeric thresholds, final case count, production expansion, and Committee outcome must not be invented.

### 11.1 M0 fixture controls

Before the real evaluator is scored, M0 fixtures must preregister and run both an always-ready and an always-blocked evaluator. The fixture set must contain planted truth that makes each trivial evaluator wrong on at least one case; otherwise the suite is rejected. The set must also contain adversarial decoys for metric-definition version, CUPED mode, and source identity.

Every sealed fixture receipt records the fixture author, evaluator or reviewer, and either independence or a disclosed conflict. Independence is preferred but different humans are not mandatory for a small team. A conflict never disappears by seniority or timeout; it stays visible and is routed through the P4 adjudication contract when the fixture is used for a formal blind or pilot claim.

### 11.2 Gate map

| Contract or scenario | Local fixture-backed M0 | Additional gate for broader claim |
| --- | --- | --- |
| Checks 1-12, 14-15, 17-19 | Synthetic, de-identified receipts may exercise deterministic behavior only after the new M0 start receipt; check 14 uses D4/D6 independence classes and always exposes shared-snapshot limits | D8 laptop receipt or stricter applicable policy for the first real Flight; P2 for normalized expansion; P4 before blind/pilot exit claims |
| Check 13, primary-source versus scorecard/UI | Synthetic primary and presentation surfaces may be reconciled only after the new M0 start receipt | P2 before reading or trusting a real source or enterprise UI |
| Check 16, authorization/ACL/redaction/retention/load/halt | Synthetic allow/deny principals and no-body failures only after the new M0 start receipt | P2 must name real credentials, tenants, ACLs, retention, redaction, load ceilings, and halt owner |
| `VAL-FLT-*`, `VAL-MET-*`, `VAL-M0-*`, `VAL-PRE-*`, `VAL-CUP-*`, `VAL-UNIT-*`, `VAL-SRC-*`, `VAL-SUP-*`, `VAL-CONF-*`, `VAL-REM-*`, `VAL-CON-*`, `VAL-SEC-*`, `VAL-BASE-*`, `VAL-DECOY-*` | May run against hermetic fixtures only after the new exact-digest M0 start receipt | P2 for any production input; P4 for sealed blind/pilot acceptance |
| `VAL-UI-001` | May run as a synthetic technology-neutral projection only after the new M0 start receipt | It does not close P3 |
| `VAL-UI-101` | Cannot pass locally without named live-review evidence | P3 required |
| `VAL-M1-*`, `VAL-M2-*`, `VAL-ROL-*`, `VAL-OLD-*` | Contract planning may exist, but no M1/M2 or production claim has a current receipt | Separate implementation start plus P2; P3/P4 where the scenario depends on live review or calibrated evaluation |
| `VAL-APR-001` | May prove technical-state separation | Committee Acceptance is an external human ruling, not a P2/P3/P4 substitute |

Fixture authorization means only that the case is synthetic or de-identified, contains no secret or production credential, stays inside the isolated package, names its fixture owner and recipient, and passes the no-network/no-write boundary. It is not evidence of a real production ACL.

## 12. Stop Conditions

Stop the affected slice and return to the named owner when any of the following occurs:

1. a fail-closed default is bypassed by an enum alias, unenumerated value, or permissive default branch;
2. any file appears under `adapters/production/` before P2 and a separate start receipt;
3. any local M0 test requires a network socket, secret, production credential, or path outside the isolated package and its declared fixture roots;
4. packet bytes or digest differ across two clean runs with identical frozen inputs;
5. the fixture set cannot produce a failing case for each of SRM, CUPED-mode mismatch, unregistered or mismatched decision metric, and pre-runtime invocation;
6. the slice-specific budget cap or expiry is missing or exceeded without a green hermetic command and reviewable partial packet;
7. production source or mapping authority is missing or contradicted;
8. a material validity, ACL, redaction, credential, load, or write-denial control fails;
9. two competent implementers cannot map a requirement to the same contract or scenario meaning;
10. the packet or UI implies a cause, recommendation, win/loss, approval, or authority that its evidence does not support;
11. a candidate diff is stale, not exact, not independently reviewable, or exposed to an automation consumer;
12. the continuity rehearsal cannot run from a clean context; or
13. an Owner decision, gate receipt, or Committee ruling is absent and the implementation would need to guess.

For conditions 1-6, the local halt owner is the M0 implementation lead named in the start receipt. Conditions 7-13 route to the authority named by the affected contract. A halt preserves immutable receipts, emits the applicable Coverage Gap, and never expands scope to make the check green.

## 13. Three-Party Review and Freeze

O1-O6 in `owner-alignment-record.md` are resolved product authority, including Flight identity, decision-metric policy, invalid-Experiment remediation, production role separation, the M0-M2 active-time envelope, and legacy-asset treatment. They are not open seams. Remaining P2/P3/P4 decisions block only the production, live-interaction, or calibrated claims mapped above; they do not authorize an implementation to invent the answer.

Each alignment party records:

- `accept | accept_with_changes | reject`;
- reviewed sections and content digest;
- required changes and rationale;
- unresolved gates or implementation ambiguities;
- conflicts of interpretation;
- timestamp and reviewer identity.

Freeze requires:

1. the Owner confirms fidelity to O1-O6 and the real post-experiment workflow;
2. Opus 5 finds no unresolved ambiguity that would produce materially different M0-M2 behavior;
3. Codex maps every active requirement to a startable unit and acceptance scenario;
4. P2/P3/P4 and Committee Acceptance remain explicit gates rather than guessed outcomes;
5. the accepted packet digest is bound into the implementation plan and Continuity Checkpoint.

The freeze record also binds the controlling [`final-architecture-spec.md`](../../final-architecture-spec.md) revision label and exact SHA-256. The packet and controlling-spec bindings are independent: changing either file's bytes invalidates the freeze and requires a superseding review record.

Any change to milestone questions, input authority, packet meaning, role authority, legacy reuse, first-screen hierarchy, acceptance scenarios, schedule accounting, or continuity behavior creates a new packet revision and requires renewed alignment.

## 14. Explicit Non-Authorization

This packet itself grants no implementation authority. The prior continuation authorization is exhausted, and any future local fixture-backed M0 slice requires a new exact-digest Owner start receipt. It does not grant production access, start M1/M2 implementation, approve a source, close P2/P3/P4, approve a Flight, establish a deadline, commit code, push a branch, open a PR, deploy, roll back, send a message, publish a document, or apply a candidate diff.
