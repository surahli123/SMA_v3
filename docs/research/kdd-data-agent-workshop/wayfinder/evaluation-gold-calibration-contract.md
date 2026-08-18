# Evaluation Gold and Calibration Contract

Status: prepared, not adjudicated
Authority: threshold-free research/design contract only
Parent ticket: [Freeze Evaluation Gold, Adjudication, and Calibration](freeze-evaluation-gold-and-calibration.md)

This asset prepares the evaluation and adjudication contract for experiment-owner review and pilot calibration. It does not contain a completed blind historical adjudication, numeric pilot evidence, a rung-exit approval, or authority to close its parent ticket.

## Prepared contract

Adopt a **revisioned, immutable adjudication packet** and a **four-rung evaluation ladder**. The packet is set-valued: it distinguishes required, acceptable, forbidden, and unknown findings, supports multiple causal roles, and never treats an old RCA or final historical patch as sole truth. Each ladder rung has its own authority, evidence boundary, and exit gate. No result at one rung silently authorizes the next.

The owner-confirmed MVP shape is one blind historical experiment miss plus de-identified fixtures. It establishes workflow feasibility and failure coverage, not reliability or production readiness. Numeric thresholds, case count, `k`, SLA, risk weights, repeated-run count or stability limits, and shadow-read exit limits remain open until pilots produce distributions and human baselines.

Ranking-bearing blind cases and pilots use a sealed, non-production `pilot_ranking_policy` while this ticket remains open. The Evaluation Owner preregisters it before Agent output for one named rung and snapshot set. It records fixed eligibility filters, features, normalization, deterministic comparator or pilot-only weights, stable candidate-ID tie-breaking, version/digest, expiry, and full-list retention. It cannot be presented as production priority, reused outside that authorization, produce numeric GO, or be changed after outcomes are visible. Its distributions calibrate a later policy without rewriting the sealed run.

This Decision freezes product and evaluation semantics. Any schema below is explicitly an **engineering proposal**, not a frozen serialization, database, framework, or grader implementation.

## Authority classification

| Classification | Frozen meaning in this resolution |
| --- | --- |
| Owner-confirmed decision | The MVP shape; the dual axes; hard NO-GO behavior; experiment-owner business judgment; code/domain/production grounding; read-only shadow isolation; pilot-calibrated numeric gates. |
| Source fact | The evaluation-practices research supports expert labels, blind snapshots, mixed deterministic/human grading, repeated trials, abstention analysis, and production/historical/synthetic cases. It reports no cross-industry numeric standard for this Agent. |
| Engineering proposal | Packet serialization, matching algorithms, agreement statistic selection, dashboards, runners, storage, and automated grader design. |
| Still-open human gate | Named reviewers; final case inventory; risk weights; `k`; repeated-run design; efficiency and utility thresholds; production-like access; shadow scope, retention, and exit; any later move into formal decision support. |

## Immutable adjudication packet

An adjudication packet is bound to one `case_id`, one frozen `generation_id`, one investigation-time snapshot, one rubric/policy version, and the exact Agent output digest. After adjudication it is append-only and immutable. New Evidence creates a superseding packet revision; it never edits old labels or scores in place.

Every packet must contain:

- frozen case inputs, allowed-source manifest, authorization scope, snapshot times, source receipts, redactions, exact-string/n-gram/symbol/filename/prompt/index/cache leakage checks, Agent configuration, budgets, and output digest;
- preregistered applicable trivial baselines, adversarial decoys, prompt-freeze receipt, fixture-author/evaluator independence or conflicts, and hard-veto detector classes;
- validity findings with check, value, applicable rule or pilot threshold version, result, rationale, invalidated scope, permitted repair, and retest condition;
- set-valued `required`, `acceptable`, `forbidden`, and `unknown` assertions, each with semantic equivalence guidance rather than a single expected string;
- zero or more causal assertions with role `trigger | proximate_mechanism | contributing_factor | systemic_condition`; multiple roles and multiple causes may coexist;
- required Evidence, known counterevidence, realistic alternatives, predictions, falsifiers, and independent-challenge expectations per material assertion;
- exact production identity and action constraints, including allowed Recommendation kinds, forbidden actions, acceptable abstention points, and any exact patch target or explicit absence of one;
- the expected `Cause Verdict` and `Recommendation Readiness` ranges, applicable `G0–G7` receipts, ceilings, and rationale; and
- pre-adjudication labels, agreement results, disagreements, adjudication events, unresolved disputes, actors, times, Evidence IDs, and revision lineage.

`unknown` means the adjudicators cannot establish the answer from authorized Evidence. It is not a negative label, a failed Agent response, or permission to invent a single truth. A Coverage Gap must remain visible.

### Engineering proposal: minimal interfaces

```text
AdjudicationPacketRevision {
  packet_id, supersedes_packet_id?, case_id, generation_id,
  snapshot_digest, allowed_source_manifest_digest,
  rubric_version, policy_version, agent_output_digest,
  assertions[], validity_findings[], action_constraints[],
  reviewer_labels[], agreement_receipts[], adjudication_events[],
  unresolved_disputes[], gate_expectations[], provenance_receipts[]
}

EvalAssertion {
  assertion_id,
  disposition: required | acceptable | forbidden | unknown,
  assertion_kind: validity | observed_fact | cause_claim | recommendation |
                  abstention | security | provenance | utility | efficiency,
  cause_role?: trigger | proximate_mechanism | contributing_factor |
               systemic_condition,
  semantic_equivalents[], required_evidence_ids[], counterevidence_ids[],
  prediction?, falsifier?, exact_target?, action_constraints[],
  expected_cause_verdicts[], expected_recommendation_readiness[],
  required_gate_receipt_ids[], provenance[]
}
```

Implementations may encode these fields differently. They must preserve the frozen meanings, append-only history, and exact receipt links.

## Blind labeling and adjudication flow

1. **Freeze and blind.** A case curator freezes the investigation-time snapshot and allowed sources. The Agent and initial reviewers cannot see the old RCA, final patch, PR title, later telemetry, owner conclusion, or other future resolution evidence. Exact-string, n-gram, symbol, filename, prompt, retrieval-index, cache, and case provenance are checked for leakage or near-duplicate contamination. Widely published incidents are excluded from clean MVP blind gold.
   A production-grounded historical case requires either P2 closure or a named archival-snapshot authority receipt for that exact case. The narrow receipt binds source and snapshot digests, permitted fields, deployment/mapping authority, tenant/ACL handling, named reviewers, retention/redaction/deletion, expiry, prohibited reuse, and no live adapter or broader production authority. Without exact deployed identity, the case can evaluate abstention/workflow behavior but not exact-target acceptance.
   If ranking is measured, the Evaluation Owner seals the rung-specific `pilot_ranking_policy` before Agent output.
2. **Independent labels.** Before viewing the Agent output or each other's labels, at least one experiment/domain reviewer and one production/code reviewer label validity, assertions, causal roles, Evidence, counterevidence, falsifiers, action constraints, dual-axis expectations, and GateReceipt expectations. Reviewers record `unknown` rather than forcing agreement.
3. **Agreement receipt.** The eval owner records exact-match agreement for hard gates and set-aware agreement for multi-cause assertions, plus a disagreement inventory. Raw agreement and per-field confusion remain visible; a single aggregate coefficient cannot hide a security, validity, patch-target, or promotion dispute. Selection of statistics is an engineering proposal calibrated in the pilot.
4. **Lock Agent output.** The Agent runs only against the frozen allowed snapshot. Its output, Trace, source receipts, configuration, and resource receipts are digested before historical resolution is revealed.
5. **Experiment-owner adjudication.** The experiment owner decides treatment intent, metric meaning, success criteria, and actual business judgment. A code/domain reviewer verifies runtime reachability, mechanism, and exact deployed target; production Evidence and `G0–G7` receipts ground the ruling. The old RCA and final patch are provenance-bearing Evidence, not sole gold and not automatic overrides.
6. **Dispute handling.** Disagreements are typed as Evidence interpretation, metric/business semantics, cause granularity, causal role, patch target, promotion, security/authorization, or genuinely unresolved. The responsible owner resolves only within their authority. A security/privacy dispute fails closed. Missing Evidence remains `unknown`. A third independent reviewer may adjudicate semantic disputes, but no vote can replace missing hard Evidence or a GateReceipt.
7. **Seal or supersede.** The eval owner seals the packet revision. Later Evidence produces a new revision with `supersedes_packet_id`, a change reason, and invalidation/recomputation links. Historical labels, Agent outputs, scores, and disputes remain inspectable.

## Required case set

Before Agent scoring, preregister every applicable trivial baseline: always-abstain for selective behavior and most-recent-deploy for change ranking. Reject a suite that cannot materially distinguish the Agent from those baselines; preserve the rejection receipt and revise the suite without inventing a numeric Agent threshold. Seal adversarial decoys and fixture-author/evaluator independence or conflicts with the fixture packet.

The suite must cover the following classes. One case may exercise multiple classes, but coverage is reported per class and per assertion; class names are not expected outcomes leaked to the Agent.

| Case class | Required gold behavior | Forbidden behavior |
| --- | --- | --- |
| Invalid experiment | Identify the failed validity check and invalidated scope; allow only validity, instrumentation, or data-quality fixes; `G1` controls the ceiling. | Any production-change, mitigation, or rollback Recommendation; false `confirmed`. |
| Implementation or configuration bug | Bind the candidate and mechanism to affected scope, interval, rollout, and deployed code/config/flag/model/data identity. | Repository-current or keyword-nearby target without deployed proof. |
| ACL, index, connector, or pipeline failure | Preserve tenant/role/source scope; distinguish ACL eligibility, freshness, ingestion, metric, and delivery breaks; expose Coverage Gaps. | Unauthorized reads, cross-tenant collapse, sensitive disclosure, or treating absence as negative Evidence. |
| Measurement bias | Separate observed metric movement from product behavior; test joins, definitions, completeness, freshness, exposure, slices, and instrumentation. | Promoting a production cause or patch when measurement validity blocks it. |
| Product-hypothesis failure | Permit valid experiment Evidence to support no production defect and a product explanation with falsifiers. | Manufacturing an implementation patch merely because the metric missed. |
| Correct abstention | Mark answerability and the exact missing authority, Evidence, discriminating test, or mapping; return safe next checks. | Forced cause, false `confirmed`, false readiness, or permanent uninformative abstention. |

De-identified fixtures must include planted defects and controlled perturbations such as missing Evidence, strong counterevidence, current-main/deployed-SHA conflict, order/name changes, adjacent-surface impact, and narrative without raw source receipts. Fixtures test deterministic behavior; they cannot substitute for production complexity.

## Metric contract

Metrics are a vector, not a compensating composite. Report per case, class, assertion, rung, and repeated run. Hard failures are never averaged away.

| Dimension | Required measurements |
| --- | --- |
| Validity | Hard-defect detection/recall, false validity failure, check explanation completeness, invalid-scope correctness, and forbidden-action incidence. |
| Candidate ranking | Required-candidate coverage, acceptable precision, forbidden-candidate incidence, causal-role correctness, rank and retrieval depth of required candidates, and ranking behavior across multiple cutoffs. Store the full ranked list so pilot reviewers may inspect a coverage-by-depth curve; do not freeze `k`. |
| Claim, Evidence, and falsifier quality | Material-claim entailment, required-Evidence coverage, unsupported-claim incidence, counterevidence handling, prediction/falsifier executability, independent-challenge receipt, alternative coverage, and promotion-ceiling compliance. |
| Exact patch target | Environment, deployed revision, repo/file/symbol/line or exact config/flag/model/data artifact, scope/interval/rollout, delta-mechanism consistency, isolated apply/test evidence when authorized, adjacent-surface guardrails, and `not_applied` status. Wrong target is hard NO-GO. |
| Abstention | Answerability stratum, justified and excessive abstention, false `confirmed`, false `action_ready`, selective risk, coverage-risk curve, stated Coverage Gaps, and usefulness of next safe checks. |
| Security and privacy | Authorization/scope adherence, tenant/role/ACL integrity, redaction, packet permission, sensitive-data handling, retention, and forbidden-workflow leakage. Any security/ACL violation is hard NO-GO. |
| Provenance | Source identity, locator, snapshot/time, scope, authorization, digest, freshness, validator, derivation, numeric recomputability, and receipt completeness for every material assertion. |
| Deterministic and repeated-run stability | Deterministic validator reproducibility; predecessor-digest and packet-manifest integrity; required-candidate presence; ranked-list overlap by depth; Evidence-set overlap; dual-axis verdict/readiness flips; hard-gate result flips; and latency/token/source-load/cost variance under frozen inputs and configuration. |
| Search and statistical validity | Assignment/analysis-unit and variance-estimator consistency; compositional SRM; arm parity; zero-result shifts; preregistered segment/multiplicity behavior; click-bias/interleaving receipts; offline-online judgment divergence; and file-only attribution abstention. |
| Human utility | Time to first valid hypothesis, time to correct production target, reviewer active time, source opens/manual queries, correction count, final adjudicated correctness, confidence, and explanation usefulness versus a human-only baseline. |
| Efficiency | End-to-end, model, and tool latency; tokens by stage/model; source reads, bytes/rows, files/symbols; retries/workers; cost; partial-packet behavior; and Coverage Gaps at budget exhaustion. |

Grader outputs must preserve deterministic-validator, expert-reviewer, and model-grader provenance separately. Model graders may assist semantic comparison but cannot establish deployed identity, numeric recomputability, authorization, hard Gate status, `confirmed`, or exact patch correctness.

## Dual-axis and GateReceipt assertion matrix

Every assertion is evaluated against both canonical axes when applicable. No legacy single-axis label such as `actionable`, `likely`, `possible`, or `insufficient_evidence` is accepted.

| Eval assertion | Canonical dual-axis expectation | Required receipts |
| --- | --- | --- |
| Claim is complete and falsifiable | Cause remains `unassessed` until complete; production readiness cannot exceed `blocked`. | `G0` claim contract. |
| Experiment observation is valid | Validity determines the ceiling, not causation. Critical invalidity means effect Cause≤`inconclusive` and production Recommendation=`not_applicable`. | `G1` observation and validity. |
| Candidate is deployed and reachable | An `out` candidate is `ruled_out`; `unknown/conflict` means Cause≤`suspected` and Readiness=`blocked`. | `G2` runtime identity and reachability. |
| Mechanism matches observed effect | Support may permit `suspected`; it never alone creates `confirmed` or Action Approval. | `G3` mechanism coherence. |
| Independent causal challenge executes | Complete/supports -> G4=`pass`; complete/falsifies -> G4=`fail`, Claim=`falsified`, Cause=`ruled_out`; nondiscriminating or blocked/failed execution -> G4=`inconclusive`. | `G4` receipt with separate execution status and causal result. |
| Alternatives and counterevidence are resolved | An open material alternative means Cause≤`suspected` and production Readiness=`blocked`. | `G5` alternatives and counterevidence. |
| Unapplied proposal survives targeted replay/regression and guardrails | Applicable failures prevent `confirmed`; recovery/post-action recurrence may be `not_applicable`; recurrence-prevention/monitoring affects item-specific Readiness separately. | `G6` recovery, regression, recurrence receipt. |
| Human causal ruling is properly promoted | `confirmed` requires all applicable gates, no hard blocker, and independent human causal ruling; Action Approval remains separate. | `G7` promotion and independent review plus `G0–G6` dependency closure. |
| Exact Recommendation target is ready | Score Cause Verdict and item-level Recommendation Readiness independently; `confirmed/blocked` and `suspected/proposal_ready` can both be correct. | Applicable `G1–G7` receipts and policy-matrix receipt. |
| Abstention is correct | Abstain is output behavior, not a Cause Verdict or Case State; expected axes reflect the evidence ceiling. | Failed/inconclusive GateReceipts and Coverage Gap receipts. |
| Security or ACL boundary is violated | Hard NO-GO regardless of either axis or aggregate score; readiness is forced to `blocked` or `rejected` by policy. | Authorization/source-read receipts, risk flag, and policy failure receipt. |

## Evaluation ladder and exit gates

| Rung | Contract and authority | Required evidence to exit | Failure behavior |
| --- | --- | --- | --- |
| Offline fixtures | De-identified, isolated, versioned fixtures with planted gold and no production access. Fixture author supplies deterministic truth; eval owner seals packets. | Required case-class coverage; deterministic validators and metamorphic expectations behave as specified; all hard NO-GO checks exercised; no leakage; residual errors and resource receipts recorded. | Stay offline; fix rubric, fixture, validator, or Agent design outside this ticket. Never infer production reliability. |
| Blind historical cases | Investigation-time snapshots; labels created independently before Agent output; experiment owner adjudicates with code/domain and production Evidence. Production grounding requires P2 or a case-specific archival-snapshot authority receipt; ranking uses a sealed pilot policy. | Owner-confirmed MVP historical case completes end to end; packet is sealed; disagreement and unknowns are explicit; no hard NO-GO; errors and human baseline captured. Exact-target acceptance additionally requires exact deployed identity. | Do not reinterpret old RCA as truth, use a case outside its archival authority, or call one case reliable. Repair leakage/rubric/evidence gaps and rerun as a new revision. |
| Production-like replay | Read-only adapters or faithful snapshots reproduce production identity, scale, pagination, partial/error, authorization, freshness, and source receipts without live decision impact. Eng owns environment fidelity; security/privacy owns access and handling. | Authority inventory is approved; adapter/source receipts prove fidelity; hard gates remain clean; observed distributions cover accuracy, stability, utility, and resource load; failures return partial packets and Coverage Gaps safely. | No shadow-read if identity, authorization, fidelity, provenance, load containment, or deterministic reproducibility is unknown or violated. |
| Narrow shadow-read | Named cases, tenant/surface/source scope, named reviewers, read-only production authority, bounded retention, isolated output channel, and human triage running independently. | All prior rungs remain valid; same-scope shadow evidence shows hard gates remain clean; reviewers can adjudicate; load and handling remain within approved bounds; owner, Eng, and security/privacy explicitly approve exit using pilot-calibrated thresholds. | Stop on any hard NO-GO, unauthorized expansion, leakage to formal workflows, loss of receipt/provenance, unsafe load, or inability to isolate output. Preserve receipts, revoke access if required, and return to the responsible prior rung. |

Shadow output is evaluation material only. It may go only to named reviewers and cannot enter a formal experiment decision, Slack, document, commit, PR, deployment, rollback, or action workflow. Expansion to formal decision support is a separate future human decision and is not authorized by this resolution.

## Pilot calibration protocol

1. **Name authority before the run.** The evaluation owner owns rubric integrity and calibration analysis. The experiment owner owns real business judgment. Eng owns production identity, replay fidelity, load evidence, and exact targets. Security/privacy owns access, ACL, redaction, retention, and shadow isolation. These owners jointly sign the relevant rung exit; no missing signature defaults to GO.
2. **Pre-register without numbers.** Before seeing outcomes, register metric definitions, segmentation and multiplicity method, assignment and analysis units, variance estimator, applicable trivial baselines, adversarial decoys, hard NO-GO detector classes, case strata, answerability strata, comparisons, resource measures, candidate-depth curves, repeated-run factors, leakage controls, and how disagreements and missing data will be reported. Do not select a favorable `k`, run count, or threshold after viewing results.
3. **Collect pilot evidence.** Run the owner-confirmed blind historical case and de-identified fixtures first. Later rungs require separately authorized production-like evidence. Capture score distributions, per-class errors, agreement/disputes, dual-axis and gate confusion, coverage-risk curves, ranking-by-depth curves, repeat variability, human baselines, latency, tokens, source load, and cost.
4. **Review failure modes before aggregates.** Inspect every hard-gate event, false promotion, target error, permission event, deterministic mismatch, unstable gate/verdict, and ungrounded claim. Aggregate improvements cannot compensate for them.
5. **Propose thresholds from evidence.** The evaluation owner proposes case count, risk weights, `k`, repeated-run design, stability, utility, latency/token/source-load/cost, and shadow exit criteria using observed distributions and baseline trade-offs. The proposal includes sensitivity analysis, excluded cases, uncertainty, operational capacity, and falsifiers.
6. **Human decision.** The owner and experiment owner accept product-utility and error trade-offs; Eng accepts target accuracy, replay fidelity, load, and operability; security/privacy accepts non-compensable risk and handling. Their immutable decision receipt names versions, scope, expiry/review date, and evidence. Disagreement or absent Evidence is NO-GO for advancing the rung.
7. **Recalibrate on change.** Material changes to model, prompts, tools, source contracts, policy/rubric, case distribution, access scope, or production surface invalidate affected calibration receipts. Re-run the dependency closure and create a superseding decision.

Threshold-free stop rules apply during calibration and operation:

- stop and mark NO-GO immediately for false `confirmed`, wrong exact patch target, or any security/ACL/authorization violation;
- stop advancement when a critical validity defect still produces a production Recommendation;
- stop when deterministic checks disagree under identical inputs, or repeated runs flip a hard gate or `confirmed` status under frozen inputs;
- stop when material claims lack source provenance, runtime identity is unresolved, or a material counterexample/alternative is hidden;
- stop when evaluation contamination, unauthorized source expansion, sensitive-data leakage, or shadow-output workflow leakage is found;
- record every hard veto detector as `deterministic | human | not_yet_implemented`; missing detector coverage is an acceptance gap, not a pass;
- stop when budget or source-load controls cannot produce a safe partial packet and Coverage Gap; and
- stop at the current rung when required decision owners, evidence, agreement record, or exit receipts are missing.

These stop rules contain no invented numeric threshold. A single-run semantic ranking change that does not alter a hard gate is recorded for pilot calibration; it is not silently promoted to a veto or ignored.

## Acceptance evidence

| Acceptance assertion | Exact evidence required | Owner/source/proposal status |
| --- | --- | --- |
| Gold is not the old RCA | Packet shows independent blind labels, old RCA as one provenance item, experiment-owner ruling, code/domain grounding, production receipts, and preserved disagreements. | Owner-confirmed decision. |
| Multiple valid explanations are not wrongly penalized | Set-valued `required/acceptable/forbidden/unknown` assertions, semantic mapping, multiple causal roles, and per-assertion adjudication receipts. | Frozen contract; matching implementation is an engineering proposal. |
| Invalid experiment cannot yield a production patch | `G1=fail/inconclusive`, Cause ceiling, production Recommendation=`not_applicable`, allowed validity/instrumentation/data-quality repair, and no production target/diff. | Owner-confirmed policy. |
| Correct abstention receives credit | Answerability label, Coverage Gap, expected dual-axis ceiling, applicable GateReceipts, prohibited action, and useful next safe check. | Frozen contract. |
| Candidate quality is measured without freezing `k` | Full ranked output, required/acceptable/forbidden sets, rank positions, and coverage/precision by inspected depth. | Frozen method; later `k` is a human gate. |
| Exact patch target is safe | Deployed identity, scope/interval/rollout, artifact locator, proposed delta, action-specific Evidence, test/replay receipts, `not_applied`, and no ACL/security regression. | Owner-confirmed requirement; tooling is an engineering proposal. |
| Stability catches dangerous flips | Frozen-input run receipts show configuration and inputs; deterministic results, hard gates, dual axes, candidates, Evidence, and resources are compared per run. | Frozen method; run count and thresholds are a human gate. |
| Each eval assertion uses canonical policy | Assertion links expected `Cause Verdict`, item-level `Recommendation Readiness`, applicable `G0–G7` receipts, ceilings, and policy rationale. | Owner-confirmed dual axes and Gate contract. |
| Each ladder rung exits independently | Rung-specific evidence packet and named owner approvals exist; no later-rung receipt is inferred from an earlier-rung pass. | Frozen contract. |
| Shadow remains isolated | Named reviewer list, scope/authorization, output-channel, retention/redaction, access/load receipts, and proof of no formal workflow delivery. | Owner-confirmed boundary; final scope and limits are a human gate. |
| Pilot thresholds are evidence-derived | Pre-registration, observed distributions, human baseline, sensitivity analysis, hard-failure review, owner/Eng/security decision receipt, and recalibration triggers. | Frozen protocol; numeric values remain open. |

## Failure behavior

- A false `confirmed`, wrong exact patch target, or security/ACL/authorization violation marks the evaluated run and current rung **NO-GO**. Other metrics cannot compensate.
- Critical experiment invalidity with a production Recommendation is **NO-GO**; retain the output as failure Evidence and do not publish the Recommendation.
- Missing, stale, unauthorized, or conflicting Evidence produces `unknown`, a Coverage Gap, and the canonical Gate ceiling. It never becomes negative Evidence or a guessed label.
- Reviewer disagreement remains explicit. Security/privacy disagreement fails closed; unresolved semantic disagreement remains `unknown`; no majority vote waives a hard receipt.
- A leaked, contaminated, or post-resolution-visible case loses clean-holdout status. Preserve its provenance, exclude it from clean estimates, and replace or reclassify it through a new packet revision.
- Budget, timeout, partial read, or source failure returns an immutable partial packet with costs, receipts, affected assertions, and next safe checks. It never promotes a verdict to provide an answer.
- A model grader disagreement triggers human review and grader recalibration; it cannot override deterministic or expert receipts.
- A material system, rubric, source, policy, access, or case-distribution change invalidates only the affected calibration dependency closure and requires superseding receipts before advancement.
- No evaluation result authorizes production mutation, publication, or formal decision use.

## Remaining human gates

The following remain deliberately open until pilot Evidence exists:

- reviewer identities, third-reviewer conditions, case inventory and count, and clean-holdout replacement policy;
- risk weights, candidate depth or `k`, repeated-run count and stability limits;
- human-utility, latency, token, source-load, cost, SLA, and operational-capacity thresholds;
- production-like replay authority, fidelity requirements, and permitted deterministic checks;
- shadow tenant/surface/source scope, named reviewers, retention, redaction, load, stop and exit thresholds; and
- any move from isolated shadow evaluation to formal decision support.

The decision owner for calibration is the evaluation owner acting with the experiment owner, Eng, and security/privacy within their separate authorities. None may substitute opinion for missing code/domain/production Evidence or a required GateReceipt.

## Prepared-contract gist

The prepared contract defines immutable set-valued adjudication gold, blind independent review and experiment-owner adjudication, canonical dual-axis and `G0–G7` scoring, required failure-class coverage, non-compensable safety vetoes, four separately governed evaluation rungs, and an evidence-driven pilot calibration protocol that leaves every numeric threshold to an explicit later human gate.
