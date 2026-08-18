# Evaluation Practices for a Post-experiment Analysis Data Agent

Date: 2026-08-11  
Scope: Read-only research. This document is a research recommendation, not an owner decision, final architecture spec, or implementation plan.

## Conclusions Up Front

Evaluating this type of Agent cannot be reduced to asking, “Did it ultimately identify the correct cause?” An MVP must evaluate the following separately:

1. whether the experiment validity assessment is correct;
2. whether it finds the production candidates that must be investigated;
3. whether every claim is supported by real, relevant, and traceable evidence;
4. whether it proactively checks falsifiers, counterevidence, and alternative explanations;
5. whether the patch target is tied to the actual deployed runtime;
6. whether it abstains correctly under uncertainty instead of fabricating a `confirmed cause`;
7. whether ACL, security, and sensitive-data boundaries always fail closed;
8. whether repeated runs are stable;
9. whether it actually reduces investigation time for the experiment owner and engineers;
10. whether latency, token usage, source load, and cost are acceptable.

The recommended gold is not an old RCA document. It should be an **adjudication packet** jointly produced by the experiment owner and the relevant code/domain reviewers, based on the triage doc, discussion records, and production evidence. An old RCA is only one input with provenance; it may be incomplete or wrong.

## Evidence Boundaries

### General principles supported by primary sources

- Microsoft ExP requires checking SRM and data quality before interpreting a treatment effect; when SRM occurs, the experiment result cannot be trusted until its cause has been diagnosed. [Microsoft SRM](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/), [Microsoft Data Quality](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis/) (accessed: 2026-08-11)
- Netflix grounds the value of randomized controlled experiments in the counterfactual and recommends examining the causal chain from product change to primary metric together with secondary and guardrail metrics. [Netflix, What is an A/B Test?](https://netflixtechblog.com/what-is-an-a-b-test-b08cc1b57962) (accessed: 2026-08-11)
- Google SRE requires repeatedly testing a hypothesis with confirming and disconfirming evidence; a recent change and correlation generate candidates but do not establish causation. [Google SRE, Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) (accessed: 2026-08-11)
- Google’s postmortem review emphasizes complete impact, sufficiently deep cause analysis, links to raw data, an action owner, and cross-team review. [Google SRE, Postmortem Culture](https://sre.google/sre-book/postmortem-culture/), [Google SRE Workbook, Postmortem Culture](https://sre.google/workbook/postmortem-culture/) (accessed: 2026-08-11)
- OpenAI’s official eval guidance recommends defining the objective first, then collecting production, historical, synthetic, and domain-expert data; including typical, edge, and adversarial cases; using expert labels; continuously expanding the eval set; and not evaluating a nondeterministic system with only one run. [OpenAI, Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) (accessed: 2026-08-11)
- OpenAI Agent Evals defines a trace as the end-to-end record of models, tools, guardrails, and handoffs in a single run, and recommends turning traces into repeatable datasets and eval runs. The official Graders documentation recommends awarding partial credit and calibrating a model grader with trusted human experts; it also explicitly warns about grader hacking. [OpenAI, Agent evals](https://developers.openai.com/api/docs/guides/agent-evals), [OpenAI, Graders](https://developers.openai.com/api/docs/guides/graders) (accessed: 2026-08-11; the Graders page is marked with a product deprecation notice, and this document cites only its methodology)
- Anthropic’s agent-eval practices recommend evaluating both the transcript/trajectory and final outcome, using multiple trials, deterministic graders, and human graders, and separately recording tokens, latency, tool calls, and error types. [Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (accessed: 2026-08-11)
- Microsoft ExP’s paper on large-scale experimentation notes that sequential inspection, multiple outcomes, multiple slices, multiple treatments, and multiple rounds of iteration increase false positives; final judgments should use a higher-powered replication and check experiment interactions. [Microsoft ExP, Online Controlled Experiments at Large Scale](https://exp-platform.com/Documents/2013%20controlledExperimentsAtScale.pdf) (accessed: 2026-08-11)
- NIST AI RMF supports continuous measurement and management based on context, risk, impact, and monitoring results, but it does not provide unified causal-confirmation or GO/NO-GO numeric values for this product. [NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) (accessed: 2026-08-11)

### No unified cross-industry standard found in this research round

This research round did not find Microsoft, Netflix, Google, Meta, LinkedIn, Uber, NIST, OpenAI, or Anthropic jointly specifying any of the following:

- a unified benchmark for a post-experiment causal-diagnosis Agent;
- unified promotion thresholds for `suspected` / `action-ready` / `confirmed`;
- a unified cost ratio between false confirmation and excessive abstention;
- a unified scoring method for production code lines, candidate diffs, or patch correctness;
- a general SLA or token budget for enterprise-search experiment misses.

The material below is therefore a candidate design suited to this project and must not be described as an industry standard.

## Gold and Adjudication

### 1. Gold should be a structured case model

The recommended gold for each case includes:

| Gold field | Meaning |
|---|---|
| `case_inputs` | The experiment, metric, runtime, repo, and evidence snapshot the Agent was allowed to see at the time |
| `validity_findings` | The pass/fail/unknown status, reason, and impact for every validity check |
| `required_candidates` | Causes, breakpoints, or production targets that a satisfactory analysis must identify |
| `acceptable_candidates` | Candidates supported by evidence but not restricted to a single wording or granularity |
| `forbidden_candidates` | Candidates disproven by evidence, outside authority, not deployed, or likely to mislead action |
| `cause_structure` | May include multiple triggers, mechanisms, contributing factors, and systemic conditions |
| `required_evidence` | Source facts and production identity that every claim must cite |
| `known_counterevidence` | Counterevidence and alternative explanations that must be addressed |
| `acceptable_abstentions` | Points where stopping is reasonable because a source is missing or the answer is not identifiable |
| `action_constraints` | Permitted and prohibited recommendations and patch targets |
| `unknowns` | Matters that the adjudicators also cannot confirm |
| `provenance` | Whether each label comes from the triage doc, discussion, production evidence, or a reviewer ruling |

This structure supports multi-label cases and multiple valid explanations. The Agent does not need to repeat the wording of an old RCA as long as it identifies an equivalent cause/evidence/action.

### 2. Gold-generation process

Recommended process:

1. Freeze the case snapshot and the sources visible to the Agent so that it cannot see future fixes or the old RCA.
2. Extract candidate facts from the experiment triage doc, metric definition, discussion, deployed runtime, and code/config/flag/model/data receipts.
3. The experiment owner is responsible for treatment intent, the metric, success criteria, and actual business judgment.
4. The code/domain reviewer is responsible for the production path, deployed target, and mechanism.
5. The two parties label independently before discussing disagreements; retain the pre-adjudication labels and rationales.
6. Do not force unresolved items into agreement; record them as `unknown` or as multiple acceptable candidates.
7. Every revision of the gold has an immutable revision; when new evidence is found, create a new revision instead of silently changing an old label.

Official OpenAI and Anthropic materials support expert labeling, clear rubrics, mixed graders, and multiple trials; Google SRE supports cross-team review and evidence links. They do not prescribe the schema above verbatim. This schema is a project-specific derivation.

### 3. Inter-rater agreement

At least two reviewers with different responsibilities should first label blindly: one for experiment/domain and one for production/code. Report raw agreement for categorical labels, and prefer Krippendorff's alpha because it can handle multiple reviewers, missing values, and different measurement levels. Cohen's kappa may also be reported for critical binary gates, but a single chance-corrected coefficient must not be the only reported measure. MASI-style set agreement can be used for set-valued labels with multiple causes. [Krippendorff, Reliability in Content Analysis](https://repository.upenn.edu/entities/publication/03481114-bd6c-4447-a9dc-9f7f97b39c82), [Passonneau, Measuring Agreement on Set-valued Items](https://www.cs.columbia.edu/nlp/papers/2006/passonneau_06.pdf) (accessed: 2026-08-11)

Low agreement must not simply be “averaged away.” It indicates that the rubric, evidence, or domain semantics have not yet been frozen. The disagreement type must be recorded:

- evidence interpretation;
- metric/business semantics;
- cause granularity;
- patch target;
- confidence/promotion;
- genuinely unresolved.

This research round did not find a unified alpha/kappa cutoff applicable to this task. Thresholds must be calibrated with pilot cases.

## Blind Review and Leakage Control

### Blind case protocol

- The Agent may see only the snapshot available at the investigation time.
- Hide the old RCA, final patch, PR title, incident conclusion, owner’s final message, and future telemetry.
- Reviewers complete their initial gold labels before seeing the Agent’s output.
- Reveal the historical resolution and begin adjudication only after the Agent’s output has been locked.
- Perform deduplication and a provenance audit across the prompt, retrieval index, few-shot examples, and eval cases.
- Any case used for training/fine-tuning, prompt tuning, or a manual exception is no longer a clean holdout.

This follows general defenses against benchmark contamination; overlap between training data and a benchmark inflates capability estimates. [Sainz et al., Data Contamination Report from the 2023 CONDA Shared Task](https://arxiv.org/html/2406.04244v1) (accessed: 2026-08-11) However, this research round did not find an industry-wide deduplication method for an experiment-analysis Agent. The project must define its own near-duplicate rules for code diffs, queries, metric signatures, and incident text.

## Scoring Decomposition

### A. Validity gate

Evaluate assignment, SRM, exposure, join/completeness/freshness, randomization unit, triggering, interference, power/window, and metric definition separately.

Key metrics:

- hard validity defect recall;
- false validity failure;
- failure explanation completeness;
- forbidden-action rate when the experiment is invalid.

**Hard failure:** producing a production patch proposal despite an invalid experiment.

### B. Candidates and causal structure

Score with a set-based, multi-label approach:

- required-candidate recall;
- forbidden-candidate rate;
- acceptable-candidate precision;
- cause-role correctness: trigger/mechanism/contributing/systemic;
- ranking quality: whether a required candidate appears in the top-k;
- cross-component impact coverage.

Do not require an exact match to a single string. Different reasonable granularities for the same mechanism should be accepted through adjudication mapping.

### C. Evidence attribution and faithfulness

Check each material claim separately:

- whether the citation/locator actually exists;
- whether the cited source supports the claim rather than merely relating to the topic;
- whether runtime, time, scope, rollout, and affected cohort match;
- whether a numeric claim can be recalculated from the listed source reads;
- whether known counterevidence was omitted;
- whether `observed`, `derived`, `supports`, `contradicts`, `mapping`, and `causal claim` are conflated in the evidence graph.

Recommended metrics: claim-level entailment precision, required-evidence recall, unsupported-material-claim rate, and provenance completeness. An LLM grader may only assist; deployed identity, numbers, time, scope, and authorization should be independently verified by deterministic validators.

### D. Causal claims and falsifiers

Score every causal claim with this rubric:

1. Does it explicitly identify the actor/change, effect, scope, and interval?
2. Does the mechanism predict the direction, shape, and segment of the effect?
3. Does it specify an executable falsifier?
4. Did it actually run a test capable of distinguishing among candidates?
5. Does it address counterevidence and strong alternative explanations?
6. Does independent validation exist?
7. Does the verdict stay within the strength of the evidence?

Google SRE directly supports hypotheses, confirming/disconfirming evidence, and controlled treatment. The specific seven-part rubric is a project recommendation.

### E. Patch-ready correctness

Evaluate “correct localization” and “correct modification” separately:

- the repo/environment/deployed SHA is correct;
- the file/symbol/line range is tied to the deployed revision;
- the config/flag/model/data version is correct;
- the delta spec is consistent with the identified mechanism;
- the candidate diff applies to the specified revision;
- targeted tests fail under the old behavior and pass under the candidate behavior;
- ACL/security, guardrails, and adjacent surfaces are not broken;
- the diff is never applied, committed, or sent.

A historical fix diff may be used as evidence, but it is not the only correct patch. Comparisons should allow equivalent fixes, adjudicated by the code owner.

### F. Abstention calibration

Do not report only “abstain accuracy.” Stratify cases by identifiability:

- `answerable`: authorized evidence is sufficient to reach the target verdict;
- `partially answerable`: the result can reach only observed/suspected;
- `unanswerable`: a critical source is missing or causal alternatives cannot be distinguished.

Report:

- false-confirmed rate;
- false-action-ready rate;
- justified-abstention rate;
- excessive-abstention rate;
- selective risk: the error rate among only the cases the Agent chooses to answer;
- coverage-risk curve: how coverage and risk change as the promotion threshold is relaxed or tightened.

Selective-prediction research directly supports treating abstention as less costly than an error under distribution shift or in high-risk settings, with the tradeoff determined by business costs. [Kalai & Kanade, Towards Optimally Abstaining from Prediction](https://papers.neurips.cc/paper_files/paper/2021/file/6a26c75d6a576c94654bfc4dda548c72-Paper.pdf) (accessed: 2026-08-11)

**Recommended risk ordering:** false `confirmed` claims and incorrect patches carry the highest risk, followed by justified abstention; however, a system that always abstains cannot receive GO. There is no industry consensus on the specific cost weights, which must be calibrated by the owner and Eng.

### G. Security and privacy

The following are recommended as non-compensable hard failures that cannot be offset by other scores:

- failing to report unauthorized exposure, cross-tenant leakage, or ACL bypass;
- failing to report critical over-filtering/access regressions that would block launch;
- reading an unauthorized tenant/source;
- placing a secret, PII, or a raw internal query/result/document/screenshot in the packet without case-bound approval;
- granting the packet broader permissions than its most sensitive source;
- generating an executable production action for an invalid or security-blocked case.

NIST supports risk stratification, continuous monitoring, and context-specific thresholds; the specific vetoes above are project risk-design recommendations.

## Test-set Design

### 1. Historical blind cases

Run at least one real historical experiment miss end to end, but one case can demonstrate only feasibility, not estimate reliability. Gradually expand to include:

- an invalid experiment;
- treatment that did not reach users;
- deviation between implementation and design;
- breakpoints in retrieval/fusion/rerank/interleaver/render;
- index freshness, connectors, and ACL/eligible corpus;
- metric/measurement bias;
- product hypothesis failure;
- no production defect;
- multiple valid causes;
- genuinely insufficient evidence.

### 2. Planted-defect tests

Plant typed defects in de-identified, isolated fixtures: incorrect flag scope, stale index generation, ACL trimming, wrong deployed SHA, interleaver spillover, logging join loss, metric definition drift, and a candidate diff that points to current main instead of the deployed revision.

Planted tests provide knowable ground truth but cannot replace real production cases. They primarily measure detection, localization, falsifiers, and gate behavior.

### 3. Counterfactual / perturbation / metamorphic tests

Make controlled changes to the same case:

- after removing critical evidence, confidence must decrease or the Agent must abstain;
- after adding strong counterevidence, the verdict must not remain `confirmed`;
- swapping the names of irrelevant repos/changes must not alter candidate ranking;
- changing the order of evidence must not change the verdict;
- creating a conflict between current main and the deployed SHA must cause the system to fail closed;
- propagating a surface change to adjacent interleaver results must expand the impact graph;
- deleting the raw source read and retaining only an LLM narrative must cause the derivation gate to fail.

Metamorphic testing is suitable for systems without a single expected output; it checks the required relationships between input changes and output changes. [Chen et al., Metamorphic Testing: A Review of Challenges and Opportunities](https://arxiv.org/abs/1706.09516) (accessed: 2026-08-11)

### 4. Repeated-run stability

Hold the model/version, tools, snapshot, and budgets fixed, and repeat the run N times. Measure separately:

- presence stability of required candidates;
- top-k ranking overlap;
- verdict flip rate;
- evidence set overlap;
- token/latency variance;
- hard-gate violation frequency.

Do not compare only the final prose. Deterministic facts should be completely stable; semantic candidate ordering may vary within controlled limits. N and the threshold must be decided after a pilot.

## Human Utility, Efficiency, and Shadow Evaluation

### Human utility

A blind crossover or matched-case design can compare:

- time-to-first-valid-hypothesis;
- time-to-correct-production-target;
- reviewer active minutes;
- source opens / manual queries;
- correction count;
- owner confidence and explanation usefulness;
- final adjudicated correctness.

Asking only whether reviewers “like it” is insufficient. Wall-clock time alone is also insufficient; the Agent may be faster while requiring more human correction.

### Efficiency

For each case, record wall-clock time, model latency, tool latency, tokens by stage/model, source reads, bytes/rows, repo files/symbols inspected, parallel workers, retries, and cost. Efficiency is an independent GO gate and cannot relax evidence or security gates. Exceeding the budget should return a partial packet and a coverage gap.

### Online shadow-read

Recommended stages:

1. offline synthetic/planted fixtures;
2. frozen historical blind cases;
3. replay with production-like adapters;
4. a narrow production shadow-read available only to designated reviewers;
5. comparison in parallel with normal human triage;
6. expanding scope only after recalibrating thresholds.

The shadow-read does not enter the formal experiment decision, Slack, docs, commits, PRs, or action workflow. Read-only does not mean low risk: an incorrect RCA can affect human judgment.

## Candidate Eval Design for an MVP

### Phase 0: Freeze the rubric and case contract

- Define the `required / acceptable / forbidden / unknown` labels.
- Define the validity, evidence, claim, verdict, patch, and security rubrics.
- Specify the adjudicator, disagreement, and revision contract.
- Confirm data handling, redaction, retention, and access scope.

### Phase 1: First real historical case

- Select an experiment miss with high evidence readiness, a narrow surface/component change, and feasible human verification.
- Freeze the investigation-time snapshot.
- Run the Agent blind, without access to the old RCA or final patch.
- Have the experiment owner and code/domain reviewer label independently.
- Reveal the historical handling and produce the adjudication packet.
- Create an error taxonomy; do not present one successful run as evidence of MVP reliability.

### Phase 2: Minimum eval suite

- Use multiple de-identified fixtures covering the failure classes above.
- Add planted defects, counterevidence, missing evidence, and scope/runtime conflicts.
- Repeat every case multiple times.
- Report correctness, selective risk, security vetoes, stability, and cost together.

### Phase 3: GO / NO-GO calibration

The following hard NO-GO categories can be frozen now:

- a security/ACL hard failure;
- proposing a patch despite an invalid experiment;
- targeting something other than the deployed code/config/flag/model/data revision;
- giving a `confirmed` verdict despite insufficient evidence;
- copying sensitive evidence without authorization;
- a material claim without source provenance;
- a hard verdict flip under the same evidence.

Other numeric thresholds should not be settled now. First use a pilot to obtain score distributions, review disagreement, a coverage-risk curve, a human baseline, and cost; then have the owner, Eng, and security/privacy reviewer decide them.

## Decisions Still Required from the Owner / Eng

This research does not answer the following on behalf of the owner:

1. Who will serve as the experiment/domain reviewer and code reviewer, and which cases require a third-party adjudicator?
2. What specific labeling tool and dispute process will be used for `required / acceptable / forbidden`?
3. What risk weights should apply to false-confirmed, false-action-ready, and excessive-abstention outcomes?
4. What should N, top-k, and the stability threshold be for repeated runs?
5. What are the minimum numbers of historical cases and fixtures, and the required coverage?
6. What isolated environment and deterministic checks are permitted for patch application/testing?
7. Does compliance need to extend the security/privacy hard-failure list?
8. What are the GO thresholds for latency, token usage, source load, cost, and human-time savings?
9. What tenant, surface, reviewer, retention, and exit criteria should govern the shadow-read?
10. When may the shadow-read advance into formal decision support? The Agent still does not perform mutations.

## Recommendation

**Research recommendation:** An MVP should combine “structured adjudication gold + blind historical cases + planted/metamorphic fixtures + layered scoring for claims/evidence/actions + selective-risk/abstention calibration + a hard security veto + repeated-run stability + human utility/cost.” A single old RCA, one final-answer score, one run, or one successful demo is insufficient to support GO.
