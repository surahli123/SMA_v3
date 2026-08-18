# Greenfield Data Agent Evaluation and Acceptance Plan

Status: canonical evaluation design for the Owner-aligned M0-M2 Validation Slice; thresholds and production progression remain open human gates
Scope: local fixture-backed M0 evaluation is planned but not currently authorized; a new exact-digest Owner authorization and bounded start receipt are required before `M0-F1`-`M0-F5`; this document does not authorize production access, M1/M2 implementation, shadow-read, publication, or mutation

## 1. Acceptance Goal

The first planned evaluation goal is M0 Flight Readiness: determine whether a frozen `ExperimentReadContract` and decision-metric read produce a correct, reproducible, fail-closed `FlightReadinessPacket`. Execution requires the new digest-bound M0 start receipt. The packet must be useful to a human reviewer, reproducible from authorized Evidence, explicit about disagreements and Coverage Gaps, and contain no M1/M2 causal output.

The planned local M0 corpus is a hermetic fixture set covering trusted, invalid, materially unknown, conflicting, stale, partial, unavailable, redaction-failed, and unauthorized reads. It may execute only after the new M0 start receipt. It exercises Query Success union/component integrity, D1-D8 checks, D4/D6 recomputation independence, the D7 core floor, orthogonal authorization/redaction, versioned Coverage Gaps, and deterministic packet output. False readiness, hidden component guardrails, conflated authority/redaction, and security/ACL leakage are hard NO-GO.

The planned M1/M2 Scenario A evaluation corpus is:

- one blind historical experiment miss, adjudicated from the investigation-time snapshot; and
- de-identified fixtures covering invalid experiments, implementation/configuration defects, ACL/index/connector/pipeline failures, measurement bias, product-hypothesis failure, and correct abstention.

The local M0 fixtures prove only local Flight Readiness behavior. The later corpus tests broader workflow feasibility and exposes failure modes within the same validation program. Neither one historical case nor M0 completion proves general reliability, production authority, Committee Acceptance, or production readiness.

## 2. Authority and Non-Authority

The Owner-settled O1-O6 meanings come from the [M0-M2 alignment record](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md), and semantic implementation binds to the exact frozen revision and digest of the [M0-M2 Build Alignment Packet](reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md). The authoritative policy semantics come from the [closed canonical domain and policy ticket](wayfinder/freeze-canonical-domain-policy-contracts.md). The [final architecture specification](final-architecture-spec.md) is the canonical logical design. The detailed, threshold-free gold and calibration contract is [prepared but not yet adjudicated](wayfinder/evaluation-gold-calibration-contract.md). The implementation structure is proposed by the [CE implementation plan](../../plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md), subordinate to those product contracts.

Evaluation results never authorize the Agent to apply a diff, write production data, change a flag, deploy, roll back, commit, push, send a message, publish a document, approve an action, or change incident state.

## 3. Four Separate Evaluation Contracts

Each contract has its own inputs, authority, evidence, exit receipt, and failure boundary. Passing one contract does not imply passing the next.

The next local M0 slice, if approved, will use the de-identified fixture contract only. No such start receipt is live. Fixtures cannot demonstrate production-backed M0 capability. The first real Flight additionally requires a bounded start receipt plus the D8 laptop-scoped authorization or stricter applicable company policy; normalized production expansion requires P2; live reviewer acceptance requires P3; decision-bearing human judgment and blind/pilot exits require P4.

### 3.1 De-identified fixture contract

Purpose: test deterministic behavior, policy enforcement, planted defects, and safe failure without production access.

Required fixture properties:

- immutable version, digest, fixture author, planted truth, permitted sources, and expected Coverage Gaps;
- de-identification receipt and proof that no credential, tenant identifier, raw query, result, screenshot, or production secret is present;
- set-valued assertions: `required | acceptable | forbidden | unknown`;
- expected Evidence, counterevidence, falsifiers, canonical dual-axis ranges, applicable GateReceipts, and forbidden actions;
- perturbations for missing Evidence, strong counterevidence, current-main versus deployed-SHA conflict, name/order changes, adjacent-surface effects, source failure, stale receipts, and unsupported narration; and
- explicit answerability so correct abstention can be distinguished from excessive abstention;
- preregistered applicable trivial baselines: always-abstain for selective behavior and most-recent-deploy for change ranking;
- adversarial decoys that share names, timing, or surface adjacency without the planted mechanism; and
- a sealed record of fixture-author/evaluator independence or disclosed conflicts.

Fixture results may validate local behavior. They cannot establish production identity, external validity, source authority, or a production SLA.

### 3.2 Blind historical-case contract

Purpose: test an end-to-end investigation against a real historical experiment miss without leaking its later resolution.

Before the Agent runs:

1. Freeze the investigation-time snapshot, authorized source manifest, rubric version, policy version, Agent configuration, and budgets.
2. Remove the old RCA, final patch, PR title, later telemetry, owner conclusion, and other future-resolution evidence from Agent and initial-reviewer context.
3. Run exact-string, n-gram, symbol, filename, fixture-metadata, prompt, retrieval-index, cache, and prior-Trace leakage checks. Seal the prompt/configuration digest before case exposure. Exclude widely published incidents from clean MVP blind gold; retain them only as explicitly non-clean provenance if useful.
4. Obtain independent pre-labels from an experiment/domain reviewer and a production/code reviewer.
5. Establish production grounding through either closed P2 authority or a case-specific archival-snapshot authority receipt. The narrow receipt binds source and snapshot digests, permitted fields, deployment and mapping authority, tenant/ACL handling, named reviewers, retention/redaction/deletion, expiry, prohibited reuse, and no live adapter or broader production authority.
6. Seal a non-production `pilot_ranking_policy` before Agent output if the case will measure ranking. Bind it to the named rung and snapshot, fixed features and eligibility rules, normalization, deterministic ordering or pilot-only weights, stable tie-breaking, version/digest, expiry, and full-list retention.

After the output digest is sealed:

- the experiment owner adjudicates treatment intent, metric meaning, success criteria, and real-world product judgment;
- the production/code reviewer verifies runtime reachability, mechanism, deployed SHA, and exact repo/file/symbol/line or non-code artifact identity;
- production Evidence and GateReceipts ground the ruling;
- the old RCA and final patch may be reviewed as provenance-bearing Evidence, but never as the sole gold; and
- disagreements, unknowns, and later corrections remain append-only revisions.

If the archival receipt cannot establish exact deployed identity, the case may score abstention, evidence handling, and workflow behavior, but it cannot satisfy exact-target or production-grounding acceptance. Neither the archival receipt nor the pilot ranking policy authorizes a live adapter, production priority, production GO, or reuse outside the named case.

### 3.3 Production-like replay contract

Purpose: test read-only adapters and evaluation behavior under production-representative identity, scale, pagination, partial failures, authorization, freshness, and source-load conditions without affecting live decisions.

Replay cannot begin until the [production evidence authority ticket](wayfinder/establish-production-evidence-authority.md) is closed by the required humans. Its exit packet must include:

- approved authoritative sources and ownership;
- replay-fidelity receipts for production identity, scope, interval, rollout, scale, pagination, error/partial-result behavior, and freshness;
- tenant, role, ACL, retention, redaction, credential, cache, log, backup, and deletion controls;
- reproducible deterministic-validator results;
- accuracy, abstention, stability, human-utility, latency, token, source-load, and cost distributions; and
- safe partial-packet and Coverage-Gap behavior under timeout, budget, and source failure.

Unknown source authority, identity, authorization, fidelity, load containment, or provenance is NO-GO for progression to shadow-read.

### 3.4 Narrow shadow-read contract

Purpose: observe the read-only Agent on a bounded live scope while human triage continues independently.

Shadow-read requires all prior contracts plus explicit owner, Engineering, and security/privacy approval. The approval must name cases, tenants, surfaces, sources, reviewers, output channel, retention/redaction, load limits, stop conditions, expiry, and exit criteria. Output is evaluation material for named reviewers only. It cannot enter a formal experiment decision, incident workflow, Slack message, document, commit, PR, deployment, rollback, or other action path.

Any unauthorized expansion, source or ACL violation, sensitive-data leakage, loss of provenance, unsafe load, or workflow leakage stops shadow-read immediately and preserves an immutable failure receipt.

## 4. Gold and Adjudication Contract

Each case uses an immutable, revisioned adjudication packet bound to one `case_id`, `generation_id`, snapshot digest, allowed-source manifest digest, rubric/policy version, Agent-output digest, and reviewer set.

The packet must contain:

- validity findings with check, value, applicable rule, result, reason, invalidated scope, allowed repair, and retest condition;
- `required | acceptable | forbidden | unknown` assertions with semantic equivalence guidance;
- zero or more causes with role `trigger | proximate_mechanism | contributing_factor | systemic_condition`;
- required Evidence, counterevidence, alternatives, predictions, falsifiers, and independent-challenge expectations;
- expected Cause Verdict and Recommendation Readiness ranges with applicable `G0-G7` receipts and ceilings;
- exact production identity and permitted/forbidden Recommendation kinds;
- acceptable abstention points and useful next safe checks;
- independent labels, agreement receipts, typed disagreements, adjudication events, unresolved disputes, actors, times, and Evidence IDs; and
- `supersedes`, invalidation, predecessor-digest, packet-manifest, and recomputation lineage for later corrections; and
- applicable baseline definitions, adversarial decoys, fixture-author/evaluator independence or conflicts, prompt-freeze receipt, leakage results, and hard-veto detector ownership.

Missing Evidence stays `unknown`; it is not converted to negative Evidence or a guessed label. A security/privacy disagreement fails closed. A third reviewer may resolve semantic disputes, but no vote can replace a missing hard receipt.

## 5. Canonical Policy Assertions

Every material assertion is evaluated against both independent axes:

- Cause Verdict: `unassessed | suspected | confirmed | ruled_out | inconclusive`.
- Recommendation Readiness: `not_applicable | blocked | proposal_ready | action_ready | rejected`.

`observed` is an Evidence or Observed Fact state, not a Cause Verdict. `actionable`, `likely`, `possible`, and `insufficient_evidence` are not accepted substitutes.

The evaluation must verify:

| Contract | Required behavior |
| --- | --- |
| G0 — claim contract | Incomplete or unfalsifiable claims remain `unassessed`; production readiness cannot exceed `blocked`. |
| G1 — observation and validity | Critical invalidity caps the effect Cause at `inconclusive`, makes production Recommendations `not_applicable`, and permits only validity/instrumentation/data-quality fixes. |
| G2 — runtime identity and reachability | `out` is `ruled_out`; `unknown/conflict` caps Cause at `suspected` and readiness at `blocked`. |
| G3 — mechanism coherence | Mechanism support may justify `suspected`; it cannot alone produce `confirmed`. |
| G4 — independent causal challenge | Record execution separately from result. Complete/supports -> `pass`; complete/falsifies -> `fail`, Claim=`falsified`, Cause=`ruled_out`; nondiscriminating or blocked/failed execution -> `inconclusive`. G7 requires the supporting pass. |
| G5 — alternatives and counterevidence | A material unresolved alternative caps Cause at `suspected` and production readiness at `blocked`. |
| G6 — recovery, regression, recurrence | For an unapplied Scenario A proposal, targeted pre-action replay/regression and guardrails may pass while recovery and post-action recurrence are `not_applicable`. Failed applicable causal checks block confirmation; recurrence-prevention/monitoring plans affect readiness separately. |
| G7 — promotion and independent review | `confirmed` requires every applicable gate, no hard blocker, and an independent human causal ruling. Action Approval remains separate. |

The deterministic policy-matrix receipt must explain every accepted or rejected Cause Verdict × Recommendation Readiness pair. No state grants mutation authority.

## 6. Required Measurements

Metrics remain a vector. Report them per case, class, assertion, evaluation contract, and repeated run. Do not collapse them into one compensating score.

### Correctness and grounding

- validity-defect detection, false validity failure, invalidated-scope correctness, and forbidden-action incidence;
- required-candidate coverage by inspected depth, acceptable precision, forbidden-candidate incidence, rank, and causal-role correctness;
- exact deployed target: environment, SHA or artifact version, repo/file/symbol/line where applicable, scope/interval/rollout, and proposed-delta consistency;
- material-claim entailment, Evidence coverage, unsupported-claim incidence, counterevidence handling, alternative coverage, and executable falsifiers;
- provenance completeness and numeric reproducibility through D4/D6 recomputation receipts, including independence class, shared immutable snapshot, transform/input/output digests, comparison-rule ID, and the `shared_source_snapshot` Coverage Gap; and
- dual-axis, GateReceipt, ceiling, and policy-matrix correctness;
- experiment assignment/analysis-unit, ratio-metric variance, compositional-SRM, arm-parity, zero-result, segment/multiplicity, click-bias/interleaving, and offline-online judgment correctness;
- symbol-attribution provenance and correct G2 inconclusive behavior for file-only identity; and
- predecessor-digest and packet-manifest chain integrity.

### Abstention and selective risk

- justified versus excessive abstention by answerability stratum;
- false `confirmed` and false `action_ready` incidence;
- stated Coverage Gaps and usefulness of proposed next safe checks; and
- coverage-risk curves without preselecting a favorable candidate depth.

### Stability and reproducibility

- deterministic validator reproducibility under identical inputs;
- required-candidate and Evidence-set overlap by depth;
- Cause Verdict, Recommendation Readiness, and hard-gate flips;
- ranking variation under frozen inputs and configuration; and
- latency, token, source-read, source-load, and cost variation.

### Human utility and cost

- time to first valid hypothesis and correct production target;
- reviewer active time, source opens, manual queries, and correction count;
- final adjudicated correctness, reviewer confidence, and explanation usefulness;
- comparison with a human-only baseline and preregistered applicable trivial baselines; and
- end-to-end/model/tool latency, tokens by stage/model, source reads/bytes/rows/files/symbols, workers/retries, and cost.

Deterministic validators, expert reviewers, and model graders retain separate provenance. Model graders may assist semantic comparison; they cannot establish authorization, deployed identity, numeric recomputability, exact patch correctness, hard-gate status, or `confirmed`.

## 7. Non-Compensable Vetoes and Stop Conditions

Each stop condition records its detector as `deterministic | human | not_yet_implemented`, its accountable owner, and its Evidence or Coverage Gap. A missing detector remains an explicit acceptance blocker; it is never treated as a pass.

The owner-confirmed hard NO-GO conditions are:

- false `confirmed`;
- wrong exact patch target;
- security, privacy, tenant, ACL, or authorization violation.

None can be offset by an aggregate score. The following additional contract failures also stop advancement at the current evaluation stage:

- a critically invalid experiment that still produces a production Recommendation;
- production mutation or an output that falsely claims a diff was applied;
- gold leakage or post-resolution contamination presented as a clean blind result;
- a material claim without source provenance or a numeric conclusion without source-read and derivation receipts;
- unresolved deployed identity promoted as an exact target;
- a hidden material contradiction or alternative;
- deterministic checks disagreeing under identical inputs, or repeated runs flipping a hard gate or `confirmed`; or
- budget/source-load failure that cannot return a safe partial packet and Coverage Gap;
- forbidden-workflow leakage from an evaluation or shadow output.

Failures remain evaluation Evidence. They are not deleted or averaged away.

## 8. Threshold-Free Acceptance Sequence

### M0. Planned local Flight Readiness acceptance after a new start receipt

Before any M1/M2 evaluation, the M0 suite must prove:

- each required `ExperimentReadContract` field is frozen and validated;
- every readiness check records inputs, rule source, result, `material | non_material | unknown`, materiality rule, receipt, affected decision metric/scope/window, and reopen condition;
- identity/policy, assignment/exposure, population/scope, numerator/denominator/join/unit, estimator/CUPED, authoritative source, and authorization/isolation failures are always material; stored unknown/unclassified materiality remains visible while applying a material ceiling; `non_material` and `NOT_APPLICABLE` each require their own versioned rule and rationale;
- `analysis_use = decision_grade | directional_only | not_permitted` is the single stored readiness state; `post_analysis_eligibility` is derived only at render time (`decision_grade -> eligible`; otherwise `blocked`) and is never persisted or independently set; scenario assertions may retain the three familiar pair forms;
- `DecisionMetricPolicy` declares `sufficiency_rule.kind = runtime_only | runtime_and_sample`; observed runtime and, when declared, sample/units are compared only with preregistered thresholds and inputs, never with post-hoc or achieved power;
- failure of a declared runtime or sample/unit threshold is exactly `blocked + directional_only` when no other material blocker applies, cannot pass the decision metric, and cannot enter M1 causal promotion; missing required `runtime_and_sample` inputs is `blocked + not_permitted` with `contract_correction`;
- treatment/control arm parity across index generation, serving alias, ACL snapshot, and effective pipeline is checked before decision-grade use; missing required evidence is `MISSING` and `blocked + not_permitted` with `evidence_collection`, a versioned applicability rule may yield `NOT_APPLICABLE`, and divergent applicable arms are a material `FAIL`;
- CUPED-adjusted and unadjusted reads are never substituted, and a mismatch preserves both values and returns `blocked + not_permitted`;
- numerator, denominator, grain, join keys, unit, ratio estimator, relative-percent, and percentage-point interpretation are checked explicitly;
- primary-source, scorecard/UI, reported, and recomputation values retain separate identities and receipts; `same_pipeline` yields `UNKNOWN`, at least `independent_transform` is required, and shared source snapshots emit `shared_source_snapshot`;
- source changes trigger versioned revalidation of meaning, coverage, owner, and attribution;
- primary and recomputation disagreement remains visible and is evaluated only under the versioned comparison rule; no tolerance is invented;
- trusted, pre-runtime directional, invalid, materially unknown, conflicting, stale, partial, unauthorized, superseded, and reviewer-conflict fixtures produce the expected deterministic packet;
- every packet/receipt declares `evidence_class = fixture | production_authorized`; `FlightReadinessPacket` contains the sealed core-set revision, stored `analysis_use`, blockers, disagreements, versioned Coverage Gaps, typed `NextSafeAction`, `human_state`, orthogonal authorization/redaction states, and applicable laptop export/redaction receipts; its renderer derives eligibility and cannot imply production capability;
- Query Success is tested as `TraditionalResultSuccess OR AIAnswerSuccess` with frozen within-Flight bindings, common grain/population/window/overlap policy, component labels, and no hidden or post-hoc component guardrail; unresolved production values remain `PRODUCTION_BINDING_REQUIRED`;
- the D7 core floor is immutable after the production read; any core `MISSING`/`UNKNOWN` leaves capability unproven; a correctly blocked production Flight can set program `m0_capability_state = demonstrated` only after independent adjudication while its `analysis_use` remains unchanged and `positive_production_path_unverified` is recorded;
- authorization and redaction failures are independently reachable and tested; an implementation Coverage Gap enum cannot add canonical kinds without a versioned registry decision;
- `NextSafeAction.kind` is exactly one of `evidence_collection | contract_correction | validity_fix | instrumentation_fix | data_quality_fix`, has a reopen condition, and carries no exact production target or diff;
- an invalid Experiment returns typed validity/instrumentation/data-quality guidance and a reopen condition; a correct syntactically valid `not_applied` remediation diff is permitted only when the frozen exact-target, authority, validator, risk, recipient, and no-write gates all pass, and guidance remains the fallback;
- preregistered always-ready and always-blocked evaluators are each contradicted by at least one sealed planted-truth fixture; otherwise the suite is rejected before Agent scoring;
- adversarial metric-definition-version, CUPED-mode, and source-identity decoys are caught by their exact validators;
- every sealed fixture records author and evaluator/reviewer identity plus independence or a disclosed conflict;
- false readiness and security/ACL leakage trigger a hard NO-GO; and
- identical frozen inputs reproduce identical check and packet digests.

Passing this sequence supports only fixture-backed pre-production evidence. It does not demonstrate production-backed M0 capability, authorize production reads, start M1/M2, close P2/P3/P4, establish production GO, or replace the Committee.

### M1 advisory and candidate-diff contract acceptance

Before any M1 advisory or candidate diff is treated as review-ready, sealed cases must prove:

- `FlightAdvisoryRevision` is append-only and separate from Cause Verdict, Recommendation Readiness, Action Approval, and Incident State; it preserves official metric result, evidence IDs/lineage, counterevidence, falsifier/execution state, `query_evidence_state`, selection timing, tested-analysis inventory, independent-confirmation receipt, DS challenge record, and supersession;
- challenge lineage accepts only `independent_instrumentation | shared_logs_independent_definition | derived_from_decision_metric_inputs`, and the last never satisfies independence;
- component divergence alone and post-unblinding evidence without independent confirmation both yield `insufficient_evidence`; the latter also emits `urgent_investigation` while preserving the discovered signal and analysis-selection history;
- blind/preregistered reproduction, independently versioned reproduction, or named independent DS/Committee challenge can supply the required confirmation receipt; human judgment without a preregistered blind rubric remains exploratory and P4-gated;
- `candidate_diff_eligibility` is evaluated independently of advisory publication and fails unless deployed artifact/SHA, attribution, reachability, mechanism, alternatives/counterevidence, independent code-domain review, and LOW/MEDIUM risk all pass;
- HIGH risk and large blast radius always fail closed; user-visible search semantics require M2 query/result corroboration; versioned N/A is accepted only for deterministic technical corrections not dependent on query-level user value; and
- every diff is syntactically valid, `not_applied`, generated outside a source worktree, human-only, and unreachable from automation or apply/commit/PR/deploy/rollback interfaces.

These are planned contract checks, not authority to execute M1 or M2.

### A. Contract acceptance before pilot

Before Agent scoring, preregister every applicable trivial baseline and run the sealed suite against it. Reject a suite that cannot materially distinguish the Agent from always abstaining or, for change ranking, selecting the most recent deploy. This is a suite-validity decision, not a numeric Agent threshold. Preserve the rejection receipt, revise the cases, and rerun baseline validation before scoring.

Implementation may begin with only threshold-free fixtures, schemas, hard-veto receipts, blind-isolation controls, and calibration hooks when explicitly authorized by the owner. Acceptance requires:

- every fixture class and hard NO-GO path is represented;
- all canonical enums, state transitions, GateReceipts, and ceilings are validated fail-closed;
- the harness cannot emit a numeric GO decision while thresholds are unset;
- correct abstention and safe partial packets are testable;
- output remains read-only and hermetic; and
- gold, Trace, grader, reviewer, and source provenance remain separate; and
- adversarial decoys, leakage checks, prompt-freeze receipt, fixture-author/evaluator independence or conflicts, and detector classes are sealed before output review.

This permits implementation of the evaluation substrate only. It does not close the evaluation Wayfinder ticket or establish reliability.

### B. Planned historical full Scenario A acceptance

The one blind historical case must complete end to end with a sealed adjudication packet, preserved disagreement, no hard NO-GO, explicit human baseline, and an experiment-owner ruling grounded by code/domain/production Evidence. It still does not establish general reliability.

### C. Pilot calibration

Before outcomes are reviewed, preregister case strata, answerability strata, metric definitions, segmentation and multiplicity method, assignment and analysis units, variance estimator, trivial baselines, adversarial decoys, comparisons, candidate-depth curves, repeated-run factors, resource measurements, hard NO-GO detector classes, leakage controls, and a sealed `pilot_ranking_policy` for each ranking-bearing rung. The policy is explicitly non-production and binds the named rung/snapshots, fixed features, normalization, deterministic comparator or pilot-only weights, stable tie rule, version/digest, expiry, and full ranked-list retention. Run fixtures and the blind case first; later contracts require separate authority.

Use observed distributions, per-class errors, coverage-risk curves, ranking-by-depth curves, repeat variability, human baselines, latency, tokens, source load, cost, and operational capacity to propose:

- final case inventory and count;
- risk weights and candidate depth or `k`;
- repeated-run count and stability limits;
- human-utility and reviewer-cost requirements;
- latency, token, source-load, cost, and SLA limits; and
- replay and shadow-read stop/exit criteria.

Every proposed number requires sensitivity analysis, uncertainty, excluded cases, trade-offs, and a falsifier. The evaluation owner, experiment owner, Engineering, and security/privacy approve only within their separate authority. Missing approval or Evidence is NO-GO.

### D. Recalibration

A material change to model, prompts, tools, source contract, policy/rubric, case distribution, access scope, or production surface invalidates the affected calibration dependency closure. The prior receipt remains; a superseding pilot and decision receipt are required.

## 9. Open Human and Pilot Gates

The following remain intentionally unset:

- reviewer identities, third-reviewer conditions, final case inventory/count, and clean-holdout replacement policy;
- risk weights, candidate depth/`k`, repeated-run count, and stability limits;
- utility, reviewer-cost, latency, token, source-load, cost, SLA, and operational-capacity thresholds;
- production-like replay authority and fidelity requirements;
- shadow tenant/surface/source scope, named reviewers, retention/redaction, load, stop, and exit limits; and
- any transition from isolated evaluation to formal decision support.

These gates must be closed with evidence-backed human receipts. This plan intentionally invents no numeric threshold.

## 10. Acceptance Evidence Checklist

- [ ] Immutable case, snapshot, source-manifest, policy, rubric, configuration, and output digests exist.
- [ ] Fixture truth or blind adjudication provenance exists and no clean-holdout leakage is found.
- [ ] Applicable trivial baselines were preregistered and the suite materially distinguishes the Agent before scoring.
- [ ] Adversarial decoys, prompt-freeze receipt, and fixture-author/evaluator independence or conflicts are sealed.
- [ ] Each hard veto names a deterministic, human, or not-yet-implemented detector and exposes any coverage gap.
- [ ] Gold is set-valued and the old RCA is not the sole label.
- [ ] Experiment-owner judgment is grounded by independent code/domain and production Evidence.
- [ ] Cause Verdict and Recommendation Readiness are scored independently with `G0-G7` and policy receipts.
- [ ] Exact targets bind deployed identity, scope, interval, rollout, and `not_applied` status.
- [ ] Correct abstention, Coverage Gaps, stability, human utility, and efficiency are reported separately.
- [ ] No hard NO-GO occurred or was hidden by an aggregate.
- [ ] Required human owners signed only within their authority.
- [ ] Numeric decisions cite a named pilot receipt; unset values remain explicit.
- [ ] Output and evaluation infrastructure retain no mutation or publication path.
- [ ] Optional diagnostic Trace absence is visible but is neither negative Evidence nor a global packet block; only a predeclared Trace-dependent operational assertion or view requires a matching capture/pin receipt.

## 11. Dependencies

- Owner-settled O1-O6: [M0-M2 alignment record](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md)
- Digest-bound semantic implementation contract: [M0-M2 Build Alignment Packet](reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md)
- Product intent and boundaries: [planning decision packet](planning-decision-packet.md)
- Canonical states and Gates: [closed policy ticket](wayfinder/freeze-canonical-domain-policy-contracts.md)
- Canonical logical design: [final architecture specification](final-architecture-spec.md)
- Prepared gold/calibration detail: [evaluation gold and calibration contract](wayfinder/evaluation-gold-calibration-contract.md)
- Open evaluation gate: [evaluation Wayfinder ticket](wayfinder/freeze-evaluation-gold-and-calibration.md)
- Production authority gate: [production evidence authority ticket](wayfinder/establish-production-evidence-authority.md)
- Evaluation research basis: [experiment-analysis evaluation practices](experiment-analysis-agent-evaluation-practices.md)
- Implementation plan: [CE implementation plan](../../plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md)
