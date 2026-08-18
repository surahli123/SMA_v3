# SEV / RCA and Experimental Causal Confirmation: Primary-Source Practice Research

Date: 2026-08-11
Scope: research-only. This document is not an owner decision or an architecture spec. No agent, production system, or tracker was modified.

> [!IMPORTANT]
> **Current-authority boundary.** This file preserves primary-source research and a pre-contract policy proposal. Its `observed / suspected / action-ready / confirmed` promotion language and the Gates 0–7 formulation below are historical research recommendations, not the current product contract. Current implementation meaning comes from the [`planning-decision-packet.md`](planning-decision-packet.md), the closed [`freeze-canonical-domain-policy-contracts.md`](wayfinder/freeze-canonical-domain-policy-contracts.md) resolution, and the [`final-architecture-spec.md`](final-architecture-spec.md). Those artifacts separate Cause Verdict (`unassessed | suspected | confirmed | ruled_out | inconclusive`) from Recommendation Readiness (`not_applicable | blocked | proposal_ready | action_ready | rejected`) and define canonical G0–G7 receipts and ceilings. No state authorizes mutation. Production authority, calibrated evaluation, and live review-surface acceptance remain open gates.

## Conclusions Up Front

The previously proposed confirmation conditions have directional support, but they were not copied directly from a single industry standard. Mature primary sources support a stricter conclusion:

1. Temporal proximity, matching scope, matching runtime, and a recent change are only screening conditions, not causal proof.
2. A high-quality investigation must express a hypothesis as a falsifiable claim and actively seek both confirming **and** disconfirming evidence.
3. Metric recovery after a rollback is strong evidence, but it may still be inconclusive when concurrent changes, natural recovery, cache behavior, traffic shifts, or similar factors are present.
4. Complex incidents often have a trigger, a direct mechanism, and multiple contributing factors. Forcing the system to report only one root cause omits preventable systemic conditions.
5. People can approve actions, rule on business semantics, and review evidence; human confirmation cannot turn missing evidence into a causal fact.
6. An experiment conclusion must first pass gates for assignment, SRM, data quality, treatment/control, interference, and metric definition. When a critical validity gate fails, promotion of a causal claim about a production change should stop.
7. At this research stage, when coverage was insufficient, strong alternative explanations could not be excluded, or critical facts conflicted, the proposed behavior was `suspected`, `action-ready`, or `abstain` rather than a forced `confirmed` verdict. In the current contract, `action_ready` belongs only to Recommendation Readiness and must not be used as a Cause Verdict.

This document ends with a set of **research-recommended gates** for this Data Agent. At the time of writing, they still required a separate owner decision before they could become a product contract. That later decision is now recorded in the closed canonical policy ticket; the historical proposal below is not the resulting contract.

## Research Method and Evidence Labels

Only official books, materials from official engineering or research teams, and official standards definitions were used. SEO summaries, consulting-company blogs, and secondary RCA templates were excluded.

- **Strong support**: The source states the principle directly or demonstrates the mechanism through an official case.
- **Reasoned derivation**: Multiple primary sources support the conclusion, but no source prescribes this gate for this Data Agent verbatim.
- **No consensus found**: This research round found no cross-organization standard threshold or shared promotion vocabulary.

All URLs were accessed on **2026-08-11**.

## Conclusions from Primary Sources

### 1. An Investigation Should Be a Falsifiable Hypothesis Loop, Not Recent-Change Matching

**Strong support.** Google SRE defines troubleshooting as a hypothetico-deductive process: derive possible causes from observations and a system model, then repeatedly test each hypothesis through confirming or disconfirming evidence, or by making a controlled change to the system and observing the result. Google also explicitly warns that correlation is not causation; recent changes are a productive starting point; and some tests provide only suggestive, not definitive, evidence.

- [Google SRE, Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) (accessed: 2026-08-11)

Implications for this task:

- `change happened before drop`, `deploy and drop are close`, and `file owns affected path` only admit a candidate into the investigation.
- Promotion must record what observations the candidate predicted, what results would falsify it, and which disconfirming checks were actually performed.
- "No disconfirming evidence was found" is meaningful only when the scope of the search for disconfirming evidence is recorded.

### 2. SEV Mitigation and Root-Cause Confirmation Are Different States

**Strong support.** Google SRE advises restoring as much system functionality as possible during a major outage and preserving evidence, without making rapid root-cause identification the first priority. A proximate cause can be fixed first while the full root-cause analysis and postmortem continue.

- [Google SRE, Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) (accessed: 2026-08-11)

Cloudflare's `pipefail` incident is a concrete primary-source example: rewriting the config restored service, but the team explicitly said it still did not understand the event at that time. The later analysis explained the combined chain involving manual rollback, a thundering herd, the Addressing API, an empty config, a `dosd` crash, and a cache flush, and the team hardened each part of that chain.

- [Cloudflare, PIPEFAIL: How a missing shell option slowed Cloudflare down](https://blog.cloudflare.com/pipefail-how-a-missing-shell-option-slowed-cloudflare-down/) (accessed: 2026-08-11)

Implications for this task:

- `mitigated`, `recovered`, and `cause_confirmed` must be separate fields.
- Recovery after a rollback can raise confidence, but it does not automatically close the RCA.
- An incident action can proceed before the cause is confirmed; execution requires risk and permission gates, not a pretense that causality has already been confirmed.

### 3. A Complex Incident Should Not Be Reduced to One "Unique Root Cause"

**Strong support.** Google's postmortem definition uses root cause(s) and requires understanding all contributing root causes. Its troubleshooting chapter also cites the limitations of a single-root-cause perspective and recommends examining causative factors in both the system and its environment. Google's formal postmortem review checks whether the root cause is deep enough, the impact is complete, and the action plan is appropriate.

- [Google SRE, Postmortem Culture: Learning from Failure](https://sre.google/sre-book/postmortem-culture/) (accessed: 2026-08-11)
- [Google SRE Workbook, Postmortem Culture](https://sre.google/workbook/postmortem-culture/) (accessed: 2026-08-11)

Cloudflare's case likewise shows that multiple conditions had to coincide to produce the incident outcome; fixing one line of code does not explain why the system allowed the failure to expand.

- [Cloudflare, PIPEFAIL](https://blog.cloudflare.com/pipefail-how-a-missing-shell-option-slowed-cloudflare-down/) (accessed: 2026-08-11)

Implications for this task:

- `trigger`, `proximate mechanism`, `contributing factor`, and `systemic condition` should be modeled separately.
- "Confirming that a change triggered the drop" does not mean "the investigation is complete." Amplification, detection, containment, and recovery gaps must still be examined.
- Multiple necessary conditions can form a `candidate_group`; the absence of one sufficient cause does not justify forcing the system to select one file.

### 4. A High-Quality Postmortem Needs Complete, Traceable, and Reviewable Data

**Strong support.** The Google SRE Workbook's requirements for a good postmortem include quantified impact, links to raw data, a timeline, the root cause/trigger, recovery, clear owners, and action items with verifiable end states. Conclusions must be based on facts and data; long logs may be summarized, but links to the raw content must be retained. The document also emphasizes cross-team review to avoid missing contributing factors.

- [Google SRE Workbook, Postmortem Culture](https://sre.google/workbook/postmortem-culture/) (accessed: 2026-08-11)

Implications for this task:

- Every claim needs a stable evidence ID, source, query/receipt, time, scope, runtime identity, and freshness.
- `confirmed` is not a paragraph of natural language; it should be a state on the claim and evidence graph that has completed the promotion gate.
- Coverage gaps, source failures, and missing permissions must be first-class fields in the final packet.

### 5. An Experiment's Causal Power Comes from a Valid Control, Not a Before/After Metric

**Strong support.** Netflix explains that random assignment keeps treatment and control otherwise equivalent on average, allowing an A/B test to support a causal statement; before/after comparisons around a full rollout confound concurrent changes in content, partnerships, seasonality, and other factors. Netflix also requires a causal chain from the product change to the primary metric and uses secondary metrics and guardrails along that chain to check the expected mechanism and unintended effects.

- [Netflix, What is an A/B Test?](https://netflixtechblog.com/what-is-an-a-b-test-b08cc1b57962) (accessed: 2026-08-11)

Netflix also states explicitly that statistical decisions cannot eliminate uncertainty; false positives and false negatives must be quantified and controlled instead of treating one statistically significant result as absolute truth.

- [Netflix, Interpreting A/B test results: false positives and statistical significance](https://netflixtechblog.com/interpreting-a-b-test-results-false-positives-and-statistical-significance-c1522d0db27a) (accessed: 2026-08-11)
- [Netflix, Interpreting A/B test results: false negatives and power](https://netflixtechblog.com/interpreting-a-b-test-results-false-negatives-and-power-6943995cf3a8) (accessed: 2026-08-11)

Implications for this task:

- Scenario A must first establish that the experiment result is interpretable, then connect the miss to the code mechanism.
- `metric moved` alone cannot confirm the hypothesized code path; intermediate behavior along the causal chain should also move in the predicted direction.
- The primary metric, secondary/mechanism metrics, guardrails, and effect uncertainty must all enter the claim evidence.

### 6. SRM and Critical Data-Quality Failures Block Interpretation of an Experiment Effect

**Strong support.** Microsoft ExP explicitly requires every A/B test to pass an SRM check before its effect is analyzed. Its conclusion is that results should not be trusted when SRM occurs until the root cause is diagnosed. SRM is not a single cause; it may originate in assignment, execution, logging/joins, or analysis. Microsoft also requires checks for completeness, validity, join rates, uniqueness, data delay, the randomization unit, treatment assignment, and timestamps.

- [Microsoft Research, Diagnosing Sample Ratio Mismatch in A/B Testing](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/) (accessed: 2026-08-11)
- [Microsoft ExP, Data Quality: Fundamental Building Blocks for Trustworthy A/B Testing Analysis](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis/) (accessed: 2026-08-11)

Microsoft's pre-experiment guidance also emphasizes defining hypotheses and metrics clearly; providing counterfactual logging for treatment and control; preventing treatment leakage through shared infrastructure; retaining a standard control alongside a custom control; and managing risk and certainty through gradual population increases and ramps.

- [Microsoft ExP, Patterns of Trustworthy Experimentation: Pre-Experiment Stage](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/) (accessed: 2026-08-11)

Implications for this task:

- SRM, assignment contamination, critical join loss, and critical data-freshness failures can invalidate the experiment effect.
- When a failure occurs, the agent can confirm a validity or data-quality defect and preserve blocked hypotheses; it cannot use the invalid effect to propose a production change.
- "Overall clean" is insufficient; affected segments must be checked because a problem may exist only in a particular build, market, browser, or triggered population.

### 7. Scope, Runtime Identity, and a Typed Change Are Necessary Conditions, but This Research Found No Shared Industry Gate

**Reasoned derivation.** Google requires understanding current component state, logs, traces, and config, and aligning deployment/config events with behavior graphs. Cloudflare's case depends on a specific rollout batch, cron timing, config key, process, and cache state. Microsoft requires correct assignment, timestamps, population, and treatment/control identities.

- [Google SRE, Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) (accessed: 2026-08-11)
- [Cloudflare, PIPEFAIL](https://blog.cloudflare.com/pipefail-how-a-missing-shell-option-slowed-cloudflare-down/) (accessed: 2026-08-11)
- [Microsoft ExP, Data Quality](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis/) (accessed: 2026-08-11)

However, this research found no shared schema prescribed by Google, Microsoft, Netflix, or NIST, such as "a deployed SHA and line range are required for confirmation." That stricter product contract should be added to this system based on the task's goals, but it must not be presented as verbatim industry guidance.

### 8. Human Review Matters, but Human Confirmation Cannot Replace Causal Evidence

**Reasoned derivation, not a verbatim source rule.** Google requires senior engineers to review postmortems for completeness, impact, root-cause depth, and actions. At the same time, Google's troubleshooting method grounds causal identification in hypothesis tests and evidence. Together, these sources support the conclusion that people review the evidence gate, but a statement such as "I agree" is not new runtime, metric, or counterfactual evidence.

- [Google SRE, Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) (accessed: 2026-08-11)
- [Google SRE, Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) (accessed: 2026-08-11)

Recommended separation of human actions:

- `approve_action`: Approves a patch, rollback, or mitigation; does not change causal truth.
- `rule_on_semantics`: Rules on a metric definition, business tradeoff, or scope; becomes an input with provenance.
- `review_promotion`: Reviews whether the evidence satisfies the gate; cannot waive missing hard evidence.
- `accept_residual_uncertainty`: Allows the operational incident to close before the cause is confirmed; the RCA state remains unknown.

### 9. NIST Supports a Systems Approach but Does Not Provide the Confirmation Threshold This Product Needs

**Strong support for the definition; no consensus found for a product threshold.** NIST defines RCA as a principle-based, systems approach for identifying the underlying causes associated with particular risks. This definition supports examining the system and its environment instead of locating only one guilty line.

- [NIST CSRC Glossary, Root Cause Analysis](https://csrc.nist.gov/glossary/term/root_cause_analysis) (accessed: 2026-08-11; the page identifies NIST SP 800-30 Rev. 1 / SP 800-39 as the sources of the definition)

However, this NIST definition does not prescribe a `suspected/action-ready/confirmed` promotion matrix for software incidents, nor does it prescribe how many rollback or reproduction attempts are required. The gates below therefore cannot be described as NIST-certified.

## Practical Meaning of Each Evidence Type

| Evidence | What It Can Establish | What It Cannot Establish by Itself | Recommended Strength |
|---|---|---|---|
| Temporal order | The candidate took effect before the effect | The candidate caused the effect | Necessary, not sufficient |
| Runtime/deployed identity | The analysis concerns the version that actually ran | A particular change in that version is the cause | Necessary, not sufficient |
| Scope overlap | The candidate reached the affected cohort/path | The mechanism is correct | Necessary, not sufficient |
| Code/config mechanism | An explainable path of influence exists | The path was actually triggered in this incident | Necessary, not sufficient |
| Correlation / changepoint alignment | The candidate merits priority in the investigation | Causality | Suggestive |
| Reproduction | The effect can recur under the specified conditions | Production necessarily followed the same conditions at the time | Strong; identity/scope still required |
| Recovery after rollback / disable | Removing the candidate is consistent with recovery | No common cause, concurrent change, or natural recovery exists | Strong; not automatically definitive |
| Treatment/control or holdout | The effect differs under a stronger counterfactual | The experiment is free of validity defects | Strong; validity must pass first |
| Mechanism metric moves in the predicted direction | The hypothesized path receives support | All alternative paths have been excluded | Corroborating |
| A disconfirming test does not falsify the claim | A set of alternative explanations becomes weaker | All alternative explanations have been excluded | Depends on coverage |
| Code-owner / IC agreement | Someone accepts responsibility for review or action | The causal claim is true | Governance only |

## Strict Confirmation Gates for This Data Agent (Research Recommendation, Not an Owner Decision)

> [!NOTE]
> This section records the research path that informed the later policy. Its gate names, promotion vocabulary, and proposed ceilings are not executable requirements. Implementations must use the closed canonical policy ticket's G0–G7 definitions, independent Cause Verdict and Recommendation Readiness axes, GateReceipt fields, fail-closed behavior, and dependency-scoped recomputation rules.

### Gate 0 — The Claim Must Be Testable

Every cause claim must specify:

- actor/change: the exact typed change or candidate group;
- effect: the metric, segment, scope, and time window being explained;
- mechanism: the path from the change to the observed effect;
- predictions: what else should be observed if the claim is true;
- falsifiers: what results would falsify or materially weaken the claim;
- alternatives: the categories of alternative explanation that remain realistically possible, without padding the list to meet an arbitrary count.

A narrative without a falsifier cannot enter `action-ready` or `confirmed`.

### Gate 1 — Observation and Validity

Common requirements:

- metric definition/version, query receipt, freshness, completeness, and time basis;
- changepoint / effect interval and uncertainty;
- affected and unaffected comparison scopes;
- checks for data-quality and instrumentation incidents.

Additional requirements for A: results for assignment, SRM, exposure, treatment/control, sample/power, triggering, joins, interference/leakage, and primary/guardrail metrics. When a critical check fails, mark the effect claim `invalid` or `blocked`.

### Gate 2 — Production Identity and Reachability

- exact environment, service, and region/tenant/surface;
- deployed artifact identity: SHA, config/flag revision, and model/data version;
- effective interval and rollout percentage;
- repo/file/symbol/line must bind to the deployed revision, not the current main branch;
- the change must actually be reachable from the affected path/cohort;
- an unknown mapping, many-to-many mapping, or conflicting identity must explicitly block promotion.

### Gate 3 — Mechanism Coherence

- the code/config/data path can explain the direction and shape of the effect;
- at least one intermediate/mechanism metric or log matches the prediction;
- affected slices should fit the claim better than unrelated slices;
- when multiple conditions must hold together, use a `candidate_group` instead of presenting one member as a sufficient cause.

With only a plausible narrative and no runtime observation, the highest permitted state is `suspected`.

### Gate 4 — Independent Causal Challenge

Obtain at least one stronger form of independent validation:

- controlled reproduction / targeted replay;
- paired observation from rollback / re-enable / flag disable;
- valid treatment/control, holdout, or canary;
- unaffected cohort / negative control;
- a test on the real system state that distinguishes competing hypotheses.

The prediction, window, scope, and success/failure criterion must be recorded in advance. Selecting a favorable graph after the fact does not count as independent validation.

### Gate 5 — Alternative Hypotheses and Disconfirming-Evidence Coverage

At minimum, examine these evidence surfaces:

- concurrent code/config/flag/model/data changes;
- dependencies / upstream / downstream / external services;
- traffic mix, seasonality, load, and cache/state;
- the metric pipeline, logging, joins, and freshness;
- rollback, auto-healing, natural recovery, or another mitigation.

The requirement is not to "prove that no other cause exists anywhere in the universe." It is to record the search scope and show that no **strong alternative explanation that remains realistic and would change the action** has been left unresolved.

### Gate 6 — Recovery, Regression, and Recurrence

- After mitigation, the primary metric, guardrails, errors, latency, availability, and dependency health are observed continuously;
- the recovery window is long enough to cover the expected delayed effect;
- no evidence indicates that the fix merely hides the symptom;
- the targeted regression / replay passes;
- preventive actions address the trigger, mechanism, and contributing factors, not only the proximate line.

This gate may remain in progress after operational recovery. `recovered` does not equal `confirmed`.

### Gate 7 — Promotion and Review

Recommended promotion rules:

The list below is a **pre-contract research proposal**. In particular, it mixes evidence state, Cause Verdict, Recommendation Readiness, and output behavior on one axis. That model has been superseded and must not guide implementation.

- `observed`: A direct, recomputable fact; makes no causal claim.
- `suspected`: Gates 0–2 pass; the mechanism has some support, but strong independent validation is still absent or alternatives have not been adequately addressed.
- `action-ready`: Gates 0–3 pass; enough evidence exists to propose an exact patch/rollback with risks and a verification plan; a human must still approve the action. This state does not mean the cause is confirmed.
- `confirmed`: Gates 0–5 all pass; Gate 6 is complete or has an explicit continuing-monitoring state; no unresolved critical conflict remains; and an independent reviewer verifies the evidence links and promotion rules.
- `abstain / needs-human-ruling`: Critical identity, validity, or coverage is missing; conflicting evidence would change the verdict or action; or distinguishing evidence cannot be obtained safely.

No state authorizes agent mutation.

## Conditions That Require Abstention or Prohibit Promotion

If any of the following conditions holds, the claim must not be promoted to `confirmed`:

1. The experiment's SRM or a critical validity/data-quality gate remains unresolved.
2. The deployed runtime identity is uncertain, or the analysis concerns a commit that was not deployed.
3. The change occurred after the effect, or the rollout scope does not cover the affected scope.
4. The only evidence is temporal correlation / recent-change proximity.
5. The mechanism cannot explain the effect's direction, segment, or timing.
6. The rollback coincided with another change, traffic shift, or automatic recovery, and their effects cannot be distinguished.
7. A strong alternative remains that explains the evidence equally well or better.
8. Critical evidence sources are inaccessible, timed out, stale, or have unknown coverage.
9. Conflicting evidence would change candidate ranking, action, or risk.
10. Only a human assertion is available, with no new verifiable evidence.
11. A high-risk or large-blast-radius action can be justified only by treating uncertainty as certainty.
12. A multifactor chain has been incorrectly reduced to a single file/line cause.

## Strong Support, Reasoned Derivation, and No Consensus Found

### Strong Support

- A hypothesis should be tested repeatedly with confirming and disconfirming evidence.
- Correlation and a recent change do not establish causation.
- Mitigation / recovery can precede a complete RCA.
- A postmortem should cover the trigger, root cause(s), impact, timeline, recovery, data, and actions.
- A causal reading of an experiment depends on valid randomization/control; SRM makes the result untrustworthy.
- Causal chains, secondary metrics, guardrails, and data-quality checks all matter.

### Reasoned Derivation

- This system should make exact deployed identity, scope reachability, and a typed production change hard gates.
- Recovery after a rollback should be treated by default as strong but rebuttable evidence, not automatic confirmation.
- Human review provides governance; it does not replace causal evidence.
- `confirmed` should require independent validation, a challenge to material alternatives, and a coverage statement.

### No Cross-Industry Consensus Found

- There is no shared `observed / suspected / action-ready / confirmed` vocabulary.
- There is no shared rule for which form of independent validation is required or how many repetitions are needed.
- There is no shared numerical confidence threshold that applies to both experiment misses and SEVs.
- There is no shared rule that an exact code line is required for confirmation; a line may not even apply to a config, model, data, or dependency cause.
- No source supports the proposition that human confirmation alone can promote a cause to `confirmed`.

The final threshold should therefore be determined by this product's risk policy, real fixtures, the cost of false confirmation, and the human workflow, then validated with evaluation data. It should not be presented as a standard inherited from any company.

## Questions Recommended for a Subsequent Design Decision

1. Must `confirmed` require both independent validation and a material-alternative challenge, or may a SEV use `confirmed-with-residual-uncertainty` when validation cannot be performed safely?
2. Under which concurrent conditions can rollback recovery support only `action-ready`?
3. If Gate 6 is incomplete, may the cause be `confirmed` while the case is `monitoring`, or must the cause also wait?
4. Which validity failures are hard blockers for A, and which only lower confidence in a particular metric or segment?
5. Who can serve as an independent reviewer, and must the reviewer and action approver be separate people?
6. Which false-confirmation, false-abstention, coverage, and latency metrics must production fixtures test before thresholds can be frozen?

## Sources

- Google SRE, [Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) (accessed: 2026-08-11)
- Google SRE, [Postmortem Culture: Learning from Failure](https://sre.google/sre-book/postmortem-culture/) (accessed: 2026-08-11)
- Google SRE Workbook, [Postmortem Culture](https://sre.google/workbook/postmortem-culture/) (accessed: 2026-08-11)
- Microsoft Research, [Diagnosing Sample Ratio Mismatch in A/B Testing](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/) (accessed: 2026-08-11)
- Microsoft ExP, [Data Quality: Fundamental Building Blocks for Trustworthy A/B Testing Analysis](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis/) (accessed: 2026-08-11)
- Microsoft ExP, [Patterns of Trustworthy Experimentation: Pre-Experiment Stage](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/) (accessed: 2026-08-11)
- Netflix, [What is an A/B Test?](https://netflixtechblog.com/what-is-an-a-b-test-b08cc1b57962) (accessed: 2026-08-11)
- Netflix, [Interpreting A/B test results: false positives and statistical significance](https://netflixtechblog.com/interpreting-a-b-test-results-false-positives-and-statistical-significance-c1522d0db27a) (accessed: 2026-08-11)
- Netflix, [Interpreting A/B test results: false negatives and power](https://netflixtechblog.com/interpreting-a-b-test-results-false-negatives-and-power-6943995cf3a8) (accessed: 2026-08-11)
- Cloudflare, [PIPEFAIL: How a missing shell option slowed Cloudflare down](https://blog.cloudflare.com/pipefail-how-a-missing-shell-option-slowed-cloudflare-down/) (accessed: 2026-08-11)
- NIST CSRC, [Root Cause Analysis](https://csrc.nist.gov/glossary/term/root_cause_analysis) (accessed: 2026-08-11)
