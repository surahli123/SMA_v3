# Freeze the Canonical Domain and Policy Contracts

Type: `wayfinder:grilling`  
Status: closed  
Claim: `019ff40c-ce33-7b71-83c6-61b6b24e5b8c`  
Blocked by: none

## Question

How should owner-confirmed language become one executable, non-conflicting contract in which lifecycle, stage, evidence state, claim state, Cause Verdict, Recommendation Readiness, human approval, and incident state remain independent while transitions, promotion ceilings, reopen behavior, and failures are explicit?

## Inputs

- [Planning decision packet](../planning-decision-packet.md)
- [Cross-research consistency audit](../cross-research-consistency-audit.md)
- [Fable adversarial audit](../fable-opus-audit.md)
- [RCA and SEV practices](../rca-sev-causal-confirmation-practices.md)

## Resolution requirements

- Canonical terms and forbidden aliases.
- `case_state` and `stage_state`, including pause/resume/close/reopen/new generation.
- Independent Evidence, Claim, Cause Verdict, and Recommendation Readiness enums and promotion matrix.
- Gate 0–7 inputs, executors, receipts, outcomes, ceilings, and reopen rules.
- `invalidated_by`, `supersedes`, and `recompute_from_stage` semantics.
- Separate human responsibility for causal ruling, action approval, and incident closure.

## Invariants

- An invalid experiment cannot produce a production proposal.
- HIGH risk, a material contradiction, or a material human gate fails closed.
- A model or worker cannot produce `confirmed` alone. No state authorizes mutation.
- Every verdict/readiness state cites evidence, counterevidence, scope, failed checks, and rationale.

## Decision

Adopt **orthogonal state dimensions with append-only revisions**.

Case lifecycle, stage execution, evidence usability, claim evaluation, Cause Verdict, Recommendation Readiness, human approval, and incident health answer eight different questions. No field implicitly changes another field.

Every transition creates an event or revision with actor, time, reason, input IDs, policy version, and receipt. Historical records are never overwritten. A closed generation and its packet are immutable; reopening creates a new generation.

This resolution freezes product semantics and policy behavior. JSON encoding, database, language, vendor, and framework remain engineering proposals.

## Canonical language

| Canonical term | Meaning | Do not conflate with |
| --- | --- | --- |
| `Case` | An investigation with a defined metric, scope, window, and scenario | ticket, incident, claim |
| `Case Generation` | One frozen-input investigation history for a Case | retry, overwritten Case |
| `Stage` | A unit of work that may pause, block, complete, or become invalid | Gate, verdict |
| `Evidence` | Material with source identity, locator, snapshot/time, scope, authorization, digest/receipt, freshness, and validation state | narration, tool log, model memory |
| `Observed Fact` | A directly evidenced, independently recomputable fact claim | root cause, confirmed cause |
| `Cause Claim` | A falsifiable explanation with change/actor, effect, mechanism, predictions, falsifiers, and alternatives | recent change, correlation, recommendation |
| `Cause Verdict` | The causal-assessment axis for a Cause Claim | actionability, approval, Case State |
| `Recommendation` | A proposal with exact target, delta, risk, verification, monitoring, and stop conditions | action, mutation, cause |
| `Recommendation Readiness` | The action-specific evidence maturity of a Recommendation | cause confidence, approval |
| `Human Causal Ruling` | Human review of whether causal-promotion evidence satisfies policy | action approval, preference |
| `Action Approval` | Human authorization for a particular immutable action packet to enter an external execution workflow | Agent execution, cause confirmation |
| `Incident State` | Human-owned operational health/response state | Case lifecycle, Cause Verdict |
| `Coverage Gap` | Missing authority, timeout, unavailable source, unknown mapping, or unchecked evidence plane | negative evidence, ruled out |
| `Abstain` | Output behavior when no conclusion is safe to publish | Cause Verdict, Case State |

Forbidden canonical usage:

- `observed` as Cause Verdict; it belongs to Evidence or Observed Fact state.
- `actionable`, `likely`, `probable`, `possible`, or `insufficient_evidence` as ambiguous verdict enums.
- `root cause` as an assumed single cause. Complex SEVs use `trigger | proximate_mechanism | contributing_factor | systemic_condition`.
- `approved`, `recovered`, `stable`, or `closed` as synonyms for `confirmed`.
- `confirmed` as a synonym for `action_ready` or `approved`.
- A confidence score as a substitute for a GateReceipt. Scores never override hard gates.
- `needs-human-ruling` as a verdict. It is a blocker/escalation reason.
- `invalid experiment` as lifecycle state. It is a validity result that activates policy ceilings.

## Independent state contracts

### 1. Case lifecycle

Canonical `case_state`:

`draft | active | paused | blocked | review_ready | handed_off | closed`

| Transition | Required receipt |
| --- | --- |
| create → `draft` | creator, scenario, initial question |
| `draft` → `active` | frozen-input digest, scope/window, authorization, new `generation_id` |
| `active` → `paused` | actor and pause reason; a pause is not a blocker |
| `paused` → `active` | actor and resume reason; continue the same generation |
| `active` → `blocked` | blocker type, affected stages, owner/escalation, next safe check |
| `blocked` → `active` | blocker-resolution receipt; timeout is not resolution |
| `active` → `review_ready` | policy result, candidate packet digest, no open publish blocker |
| `review_ready` → `active` | reviewer request and reason for more investigation |
| `review_ready` → `handed_off` | immutable packet revision, named recipient, expiry, acknowledgement requirement |
| `handed_off` → `closed` | required acknowledgement and authorized human close receipt |

Rules:

- Handoff expiry makes the packet `stale` and the Case `blocked`. Re-handoff requires a superseding packet.
- A `closed` generation never returns to `active`. `reopen` creates a new `generation_id` referencing, but not overwriting, frozen inputs and packets.
- Closing a Case only ends that generation's investigation/delivery flow. It does not promote Cause Verdict or change Incident State.

### 2. Stage execution

Canonical `stage_state`:

`not_started | running | paused | blocked | completed | invalidated | skipped`

Canonical Scenario A stages:

1. `intake_and_freeze`
2. `validity_and_observation`
3. `production_identity_and_scope`
4. `candidate_discovery_and_mapping`
5. `claim_construction`
6. `causal_challenge`
7. `recommendation_and_risk`
8. `review_packet_and_handoff`

Rules:

- Normal flow is `not_started → running → completed`.
- `running ↔ paused` requires pause/resume events.
- `running → blocked → running` requires blocker and resolution receipts.
- `completed → invalidated` only through a new invalidation event; the completion record remains.
- `skipped` requires a deterministic applicability receipt and cannot bypass a hard gate.
- Re-entry recomputes only the dependency closure. Stages are not a one-pass waterfall.
- Pausing a Case pauses running stages without marking them failed.

### 3. Evidence usability

Canonical `evidence_state`:

`observed | validated | stale | invalidated | superseded`

- `observed`: successful nonzero source read; not yet independently validated.
- `validated`: identity, digest, scope/time, query/read set, and applicable rules passed validators.
- `stale`: freshness or expiry exceeded; the historical observation remains true but cannot support current promotion.
- `invalidated`: authorization, identity, scope, derivation, or source correction makes it unusable for the original claim.
- `superseded`: a new revision is current; the old Evidence remains auditable and is not necessarily false.

Timeout, no authority, and zero reads create a Coverage Gap, not observed Evidence. A numeric or identity fact with an empty source-read set fails Gate 1.

### 4. Claim evaluation

Canonical `claim_state`:

`draft | testable | observed | supported | contradicted | falsified | invalidated | superseded`

- `observed` is valid only for `claim_kind=observed_fact` with validated direct Evidence.
- A Cause Claim moves from `draft` to `testable` through Gate 0 and can never be `observed`.
- `supported` means Evidence matches predictions; it does not mean Cause Verdict=`confirmed`.
- `contradicted` means material counterevidence exists but a declared falsifier has not necessarily passed.
- `falsified` requires a validated falsifier receipt.
- `invalidated` means dependencies changed and recomputation is required.
- `superseded` means a new claim revision replaces wording or scope while history remains.

### 5. Cause Verdict

Owner-confirmed enum:

`unassessed | suspected | confirmed | ruled_out | inconclusive`

- `unassessed`: the claim/evidence contract is not yet evaluable.
- `suspected`: scope-grounded support exists, but at least one confirmation gate is incomplete.
- `confirmed`: every applicable Gate 0–7 passes, no open material contradiction or HIGH promotion blocker remains, and an independent human causal reviewer rules explicitly.
- `ruled_out`: a validated falsifier or identity/scope/time impossibility excludes the Cause Claim.
- `inconclusive`: all feasible work within current authority and budget is complete, but a key gate remains inconclusive.

Legal transitions:

- `unassessed → suspected | ruled_out | inconclusive`
- `suspected → confirmed | ruled_out | inconclusive`
- `inconclusive → suspected | ruled_out` only with new Evidence or a reopened generation
- New Evidence never overwrites `confirmed` or `ruled_out`; it creates a new claim/verdict revision that may become `suspected | inconclusive | ruled_out`.

An Agent, semantic worker, vote, or consensus cannot produce `confirmed` alone.

### 6. Recommendation Readiness

Owner-confirmed enum:

`not_applicable | blocked | proposal_ready | action_ready | rejected`

- `not_applicable`: the Recommendation class is not allowed or needed, such as a production-change Recommendation for an invalid experiment.
- `blocked`: exact target, action-specific evidence, risk/recovery/monitoring, or another hard requirement is missing.
- `proposal_ready`: exact target, delta, Evidence, and verification plan are ready for review, but action conditions are incomplete.
- `action_ready`: exact target, bounded blast radius, recoverability, independent operational Evidence, monitoring, and stop conditions are complete; no HIGH risk or action-changing material contradiction remains.
- `rejected`: a human or deterministic policy rejects the current Recommendation revision with a reason.

Compute readiness per Recommendation item. `kind` distinguishes at least `validity_fix | instrumentation_fix | data_quality_fix | production_change | mitigation | rollback`.

No readiness authorizes mutation or equals Action Approval. Scenario A candidate diffs are always `not_applied`; Scenario B rollback packets are human-facing only.

### 7. Action approval

Canonical `action_approval_state`:

`not_requested | pending | approved | rejected | expired | revoked`

- Only an independent human action approver may set `approved`.
- Approval binds immutable recommendation/packet digest, target, scope, expiry, and actor.
- Any packet or Evidence revision expires the old approval.
- Approval still does not authorize this Agent to mutate. External execution is outside this design's authority.

### 8. Incident health

Canonical `incident_state`:

`not_applicable | investigating | mitigating | recovered | monitoring | stable | closed`

- Only a human IC/on-call/action owner may set `recovered | stable | closed`.
- Recovery verification and continuing RCA run in parallel after mitigation or rollback.
- Incident recovery, stability, or closure does not alter Case State or Cause Verdict.
- An action approver may also be incident owner, but causal reviewer and action approver must be different people for the same Case.

## Deterministic two-axis policy matrix

This matrix applies to claim-linked production Recommendations. Validity/data-quality fixes are separate Recommendation items.

| Cause Verdict | `not_applicable` | `blocked` | `proposal_ready` | `action_ready` | `rejected` |
| --- | --- | --- | --- | --- | --- |
| `unassessed` | legal | legal | illegal | illegal | legal |
| `suspected` | legal | legal | legal | conditional | legal |
| `confirmed` | legal | legal | legal | conditional | legal |
| `ruled_out` | legal | legal | illegal when it is the sole supporting claim | illegal when it is the sole supporting claim | legal |
| `inconclusive` | legal | legal | legal | conditional | legal |

Conditional `action_ready` requires all of the following:

1. exact deployed target and delta/parameter;
2. bounded, non-HIGH blast radius;
3. recoverability and rollback/undo path;
4. independent action-specific operational Evidence;
5. monitoring, success, stop, and escalation conditions;
6. no open material contradiction that changes action or risk;
7. experiment validity permits the Recommendation kind;
8. a policy receipt listing all source Evidence IDs.

Required legal examples:

- Cause=`suspected`, Readiness=`action_ready`: a low-risk, recoverable mitigation has independent operational Evidence although causation is unconfirmed.
- Cause=`confirmed`, Readiness=`blocked`: causation is established, but target, blast radius, rollback, or monitoring is incomplete.
- Cause=`inconclusive`, Readiness=`not_applicable`: no production Recommendation is safe.

Illegal combinations remain visible. The Policy Engine returns `policy_fail`, violated predicates, Evidence IDs, and the forced readiness ceiling.

## Gate 0–7 executable contract

Every `GateReceipt` contains at least `gate_id`, `gate_version`, `claim_id`, `generation_id`, `input_ids`, `executor_kind`, `executor_id`, `started_at`, `completed_at`, `status`, `checks`, `failed_checks`, `coverage_gaps`, `risk_flags`, `output_digest`, `ceiling`, and `reopen_condition`. A G4 receipt additionally records `challenge_execution_status` and, only after a completed challenge, `challenge_result`.

Canonical status: `pending | pass | fail | inconclusive | not_applicable`.

- `fail`: Evidence violates a hard predicate.
- `inconclusive`: required Evidence, authority, or coverage is missing, or a material conflict cannot be resolved.
- `not_applicable`: a deterministic applicability rule creates a receipt. It is not a pass and cannot bypass confirmation. Gate 7 counts it only when policy explicitly accepts the reason.

G4 keeps execution from causal outcome:

- `challenge_execution_status = pending | complete | blocked | failed` records whether the predeclared challenge actually ran under its frozen contract.
- `challenge_result = supports | falsifies | nondiscriminating` exists only when `challenge_execution_status=complete`.
- `complete + supports` maps to G4=`pass`.
- `complete + falsifies` maps to G4=`fail`, Claim=`falsified`, and Cause=`ruled_out`.
- `complete + nondiscriminating`, `blocked`, or failed execution maps to G4=`inconclusive`; operational failure is not causal falsification.
- G7 requires a current G4=`pass` with `challenge_result=supports`; a syntactically complete or merely executed receipt cannot satisfy promotion.

| Gate | Inputs and executor | Pass | Failure ceiling and reopen |
| --- | --- | --- | --- |
| **G0 Claim contract** | Change/actor, effect, scope/window, mechanism, predictions, falsifiers, alternatives. Deterministic schema validator; semantic worker only drafts. | Complete, falsifiable, no forbidden shortcut. | Fail/inconclusive: Cause=`unassessed`, production readiness≤`blocked`. Reopen on claim/scope revision. |
| **G1 Observation and validity** | Metric/version, reads, freshness/completeness, effect interval; A adds assignment, SRM, exposure, trigger/ramp/power, join, interference, guardrails. Deterministic numeric/data-quality validators; experiment owner rules only on business semantics. | Nonzero read set; every critical check passes with value, threshold, result, and reason. | Critical invalidity: effect Cause≤`inconclusive`; production Recommendation=`not_applicable`; only validity/instrumentation/data-quality fixes. Reopen with repaired data and a refrozen snapshot, normally a new generation. |
| **G2 Runtime identity and reachability** | Environment, tenant/role/surface, deployed versions, interval, rollout, mapping. Deterministic `scope × interval × rollout` matcher and mapping resolver. | `in`, or policy-accepted `partial`, with exact identity and locator; conflicts resolved. | `out`: candidate `ruled_out`. `unknown/conflict`: Cause≤`suspected`, readiness=`blocked`. Reopen with new runtime/mapping receipt or a human semantic ruling. |
| **G3 Mechanism coherence** | Code/config/data path, effect direction/shape, intermediate metrics/logs, candidate group. Deterministic identity/numeric validators; semantic worker drafts mechanism. | At least one runtime observation matches a prediction; no validated impossibility. | Fail: `ruled_out` or claim revision. Inconclusive: Cause≤`suspected`; causally linked production action≤`proposal_ready`. Reopen with mechanism Evidence, replay, or claim revision. |
| **G4 Independent causal challenge** | Predeclared prediction, scope/window, and criterion for replay, rollback pair, control/holdout, negative control, or discriminating test. Deterministic receipt validator; any real action comes from an authorized external human/system. | At least one independent challenge is `complete`, has `challenge_result=supports`, and has a valid supporting receipt. | `complete + falsifies`: G4=`fail`, Claim=`falsified`, Cause=`ruled_out`. `complete + nondiscriminating`, blocked, or failed execution: G4=`inconclusive`, Cause≤`suspected`; independently justified safe mitigation may still be `action_ready`. Reopen with a new predeclared test; never reinterpret the old result. |
| **G5 Alternatives and counterevidence** | Concurrent changes, dependencies, traffic/load/cache, metric pipeline, recovery confounders, and eight-plane coverage. Deterministic coverage registry; workers submit Evidence/claims only. | No open realistic material alternative that changes action; search scope has a receipt. | Open material alternative/contradiction: Cause≤`suspected`, production readiness=`blocked`. Reopen with conflict-resolving Evidence or human semantic ruling; humans cannot waive hard Evidence. |
| **G6 Recovery, regression, recurrence** | Applicable recovery window; primary/guardrail/error/latency/availability/dependency health; targeted regression or replay; and action-specific recurrence-prevention/monitoring plan. Deterministic monitoring/regression validators; human IC/on-call owns SEV health. | All applicable causal-verification checks pass. For an unapplied Scenario A proposal, recovery and post-action recurrence are deterministically `not_applicable`; targeted pre-action replay/regression and guardrail checks may satisfy G6. | Failed or inconclusive applicable replay/regression/guardrail Evidence prevents Cause=`confirmed`. A missing recurrence-prevention/monitoring plan lowers Recommendation Readiness separately; it does not falsify the Cause. Post-action recovery or recurrence Evidence creates later superseding receipts. Incident `recovered` is not a pass. |
| **G7 Promotion and independent review** | G0–G6 receipts, dependency closure, risk/contradiction registry, policy result, packet digest. Policy Engine evaluates first; independent human causal reviewer rules second. | Applicable G0–G6 pass; no HIGH/open material contradiction; reviewer cites Evidence in an explicit ruling. | Timeout, denial, or missing reviewer: Case=`blocked`, Cause≤`suspected`, no publication. Action Approval is separate. Reopen after ruling, new Evidence and rerun, or a new generation. |

`confirmed` has one path: all applicable G0–G7 conditions are satisfied and G7 passes. Gate 6 cannot be wholly N/A merely because a Scenario A proposal is unapplied: applicable pre-action replay/regression and guardrail validation must still pass. Recovery and post-action recurrence are not required before an unapplied proposal can receive causal confirmation; they enter later superseding receipts if a separately authorized external actor applies a change. Prevention and monitoring obligations affect Recommendation Readiness, not the historical Cause Verdict.

## Invalidation, supersession, and recomputation

Canonical edge direction:

- `new_revision --supersedes--> old_revision`
- `affected_node --invalidated_by--> invalidation_event_or_evidence`
- `derived_node --depends_on--> input_node`

Rules:

1. Evidence, derived facts, Claims, GateReceipts, Recommendations, VerdictEvents, Approvals, and Packets are append-only.
2. Human override requires new code-grounded Evidence and a `supersedes` or `invalidated_by` relation. Old records remain.
3. An invalidation event records reason, actor, scope, effective time, targets, source receipt, and `recompute_from_stage`.
4. The Policy Engine follows reverse `depends_on` edges and invalidates only the affected dependency closure.
5. `recompute_from_stage` is the earliest affected stage in that closure, not a manual full-rerun switch. Runtime/mapping invalidation starts at `production_identity_and_scope`; renderer invalidation does not recompute Evidence or Claims.
6. Stale/invalidated support, open HIGH risk, contradictions, verdicts, and readiness propagate to the publish gate.
7. Closed packets remain immutable. Recomputation creates a new packet with `supersedes_packet_id`.

## Human responsibility split

| Decision | Agent output | Required human | Prohibited conflation |
| --- | --- | --- | --- |
| Causal promotion | Evidence graph, GateReceipts, counterevidence, policy result | Independent causal reviewer | Cannot approve action or replace missing hard Evidence with opinion |
| Action approval | Immutable Recommendation/rollback packet, blast radius, monitoring/stop/undo | Separate action approver | Cannot turn approval into Cause=`confirmed` or expand packet scope |
| Experiment adjudication/eval | Blind output, triage Evidence, code grounding | Experiment owner assisted by code/domain reviewer | Old RCA is not automatically sole gold |
| Operational recovery/closure | Read-only health Evidence, continuing-RCA state | IC/on-call/action owner | Agent cannot set recovered/stable/closed |

The causal reviewer and action approver must be different humans for the same Case. The action approver may also be incident owner. A material human timeout stays `pending/blocked`, triggers escalation, and never defaults to continue.

## Fail-closed behavior

- **Invalid experiment**: production-change/mitigation/rollback Recommendation=`not_applicable`; discovered system hypotheses may be retained only as non-ranked, non-publishable blocked leads and are excluded from production candidate output; only validity, instrumentation, and data-quality fixes are publishable. Every failed check explains cause and retest.
- **HIGH risk / large blast radius**: Recommendation≤`blocked`, even when Cause=`confirmed`. Security regression, ACL bypass, cross-tenant leakage, unauthorized exposure, and critical over-filtering are launch NO-GO.
- **Material contradiction**: retain both sides with `contradicts`. If it changes verdict, rank, action, or risk, Cause cannot be `confirmed` and Recommendation cannot be `action_ready`.
- **Human timeout/absence**: remain `pending/blocked`, record escalation and expiry, and never default approve/publish/continue.
- **Missing authority/coverage**: emit a Coverage Gap; absence, timeout, or no authority is not negative Evidence.
- **Budget exhaustion**: preserve Evidence and cost/latency receipts plus the next safe check; never promote merely to return an answer.

## Acceptance evidence

| Scenario | Expected deterministic result |
| --- | --- |
| Cause=`suspected`; low-risk recoverable mitigation has independent operational Evidence and monitor/stop plan | Readiness may be `action_ready`; Action Approval remains `not_requested/pending`; Cause does not promote |
| Cause=`confirmed`; rollback, blast radius, or monitoring is incomplete | Readiness=`blocked`; Cause remains `confirmed` |
| Critical SRM failure | G1=`fail`; effect Cause≤`inconclusive`; production Recommendation=`not_applicable`; no candidate diff |
| Candidate rollout follows the effect | G2=`fail/out`; candidate Cause=`ruled_out` |
| Independent challenge executes and supports the Claim | `challenge_execution_status=complete`, `challenge_result=supports`, G4=`pass`; promotion still requires G5–G7 |
| Independent challenge executes and falsifies the Claim | `challenge_execution_status=complete`, `challenge_result=falsifies`, G4=`fail`, Claim=`falsified`, Cause=`ruled_out` |
| Independent challenge is nondiscriminating or cannot execute | G4=`inconclusive`; Cause≤`suspected`; operational failure is not falsification |
| Unapplied Scenario A proposal passes targeted replay/regression and guardrails | G6 may pass with recovery and post-action recurrence=`not_applicable`; prevention/monitoring plan is evaluated on Recommendation Readiness |
| Runtime mapping unknown | G2=`inconclusive`; Cause≤`suspected`; Readiness=`blocked`; Coverage Gap emitted |
| Strong alternative unresolved | G5=`inconclusive`; Cause≤`suspected`; Readiness=`blocked` |
| Causal review times out | G7=`inconclusive`; Case=`blocked`; no publish or default continue |
| HIGH security-regression proposal | Even with Cause=`confirmed`, Readiness=`blocked`; escalate to action approver/IC/security |
| Human code-grounded override | New Evidence supersedes old; dependency closure invalidates; history and old packet remain |
| Closed Case reopens | New generation and superseding packet; old generation remains closed and immutable |
| Metric recovers after incident rollback | Human may set Incident=`recovered/monitoring`; Cause does not auto-confirm; RCA continues |
| Renderer or Trace is wrong | Rebuild projection/trace only; Evidence, Claim, Verdict, and Readiness do not change |

## Authority and conflicts resolved

- Owner authority: [planning decision packet](../planning-decision-packet.md), especially the two enums, evidence obligations, human separation, invalid/high-risk ceilings, and append-only override.
- Conflict inventory: [cross-research consistency audit](../cross-research-consistency-audit.md), especially P0-1, P0-2, P0-4, P1-3, and P1-4.
- Architecture/risk input: [Fable adversarial audit](../fable-opus-audit.md). Its old single-axis vocabulary is superseded here.
- Research basis: [RCA and SEV practices](../rca-sev-causal-confirmation-practices.md). Gate rationale is research support, not owner authority.

## Resolution gist

The canonical policy is now orthogonal and append-only: eight state dimensions remain independent; owner-confirmed two-axis enums are preserved; Gates 0–7 have inputs, executors, receipts, ceilings, and reopen rules; invalid experiments, HIGH risk, material contradictions, and human timeouts fail closed; and causal ruling, action approval, and incident closure have separate human responsibility.
