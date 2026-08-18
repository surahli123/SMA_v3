# Freeze Evaluation Gold, Adjudication, and Calibration

Type: `wayfinder:grilling`
Status: open
Claim: 019ff4cc-9d54-7ea0-ba61-aa23d57dc901
Blocked by: none

## Question

For the current fixture-backed M0 slice, how should Flight Readiness use threshold-free fixtures and human review to detect false readiness, invalid or materially unknown reads, disagreement, and security/ACL failure? For the separately gated M1/M2 continuation, how should post-experiment analysis use blind evaluation and later pilots without treating the old RCA as sole truth or weakening hard NO-GO rules?

Scope update: the 2026-08-16 Owner decisions place M0, M1, and M2 in one validation program, with M0 first and primary. The current start receipt authorizes only local fixture-backed M0. Full causal ranking, patch-target, Win/Loss, replay, and shadow-read evaluation require their named gates and separate starts.

## Inputs

- [Experiment-analysis evaluation practices](../experiment-analysis-agent-evaluation-practices.md)
- [Planning decision packet](../planning-decision-packet.md)
- One real historical experiment miss and multiple de-identified fixtures.

## Resolution must define

- M0 fixtures for trusted, invalid, materially unknown, conflicting, stale, partial, and unauthorized reads, with deterministic `ExperimentReadContract` and `FlightReadinessPacket` expectations.
- M0 false-readiness and security/ACL hard vetoes, packet-digest review, and explicit no-M1-output assertions.
- Immutable adjudication packet: `required / acceptable / forbidden / unknown`, multiple causes, evidence, counterevidence, validity, and action constraints.
- Blind labels → reviewer agreement → experiment-owner adjudication → dispute process.
- Cases for invalid experiments, implementation/config bugs, ACL/index/pipeline failures, measurement bias, product-hypothesis failure, and correct abstention.
- Metrics for candidate/validity/claim-evidence/falsifier/patch-target/abstention/security/stability/human utility/latency/token/source-load/cost.
- Different authority and exit gates for offline fixtures, historical blind cases, production-like replay, and narrow shadow-read.
- Preregistered applicable always-abstain and most-recent-deploy baselines, pre-scoring suite distinguishability, adversarial decoys, and fixture-author/evaluator independence or conflicts.
- Exact-string/n-gram/symbol/prompt/index/cache leakage controls, prompt-freeze receipt, widely published-case exclusion, and hard-veto detector classes.
- Statistical/search-domain contracts for assignment/analysis units, variance, compositional SRM, arm parity, zero-result shifts, segments/multiplicity, click bias/interleaving, and offline-online judgment divergence.

## Invariants and failure behavior

- False `confirmed`, an incorrect patch target, or a security/ACL violation is a hard NO-GO.
- Gold is not the old RCA. The experiment owner's real judgment requires code/domain/production evidence.
- Numeric thresholds remain open until real pilots; do not invent them.
- Shadow output goes only to named reviewers and cannot enter formal decision, Slack, document, commit, PR, or action workflows.

## Acceptance scenarios

- A trusted M0 fixture becomes reviewable, while a material SRM, unit, estimator, join, source-consistency, authorization, or freshness failure remains blocked or incomplete with the exact receipt.
- No M0 packet contains a Cause Claim, production candidate, ranking, Recommendation, diff, or Win/Loss label.
- If the old RCA omits an acceptable alternative, set-valued gold does not wrongly penalize the Agent.
- Correct abstention on an invalid case is not failed for lacking a patch.
- Stability metrics catch repeated-run verdict flips despite a successful single run.

## Human gate

The experiment owner decides the real business judgment; code/domain reviewers verify production grounding; Eng and security/privacy jointly confirm pilot and shadow-read exit.

## Prepared asset

- [Evaluation Gold and Calibration Contract](evaluation-gold-calibration-contract.md) — prepared threshold-free contract for immutable set-valued gold, blind review and dispute handling, dual-axis and `G0–G7` evaluation, case and metric coverage, rung-specific gates, hard vetoes, and evidence-driven pilot calibration.

## Completed preparation

- Defined the immutable `required / acceptable / forbidden / unknown` packet, multiple causal roles, Evidence, counterevidence, validity, action constraints, provenance, and append-only revisions.
- Defined blind labels → independent reviewer agreement → experiment-owner adjudication → typed dispute handling.
- Defined required case classes, metric vector, canonical `Cause Verdict × Recommendation Readiness` expectations, and `G0–G7` receipt mapping.
- Defined separate contracts, authorities, exits, and failure behavior for offline fixtures, blind historical cases, production-like replay, and narrow shadow-read.
- Preserved hard NO-GO rules and a threshold-free pilot-calibration protocol without inventing numeric values.
- Defined a sealed, non-production `pilot_ranking_policy` for ranking-bearing blind/pilot runs while P4 remains open; it is preregistered by rung and snapshot and cannot authorize production priority or GO.
- Defined the blind-case authority path: close P2 or use a case-specific archival-snapshot authority receipt. Without exact deployed identity, the case may test abstention/workflow behavior but cannot count for exact-target acceptance.

## Exact unresolved human and pilot gates

- The experiment owner must adjudicate one real blind historical experiment miss using the frozen investigation-time snapshot, independent labels, code/domain review, and production Evidence. The old RCA cannot be sole gold. Production grounding requires P2 closure or the exact archival-snapshot receipt defined in the prepared contract.
- The evaluation owner must seal the adjudication packet, agreement/dispute receipts, Agent-output digest, and clean-holdout provenance.
- The owner and experiment owner must decide the final case inventory, case count, product-utility trade-offs, risk weights, candidate depth or `k`, and excessive-abstention tolerance from pilot distributions.
- Eng must confirm exact deployed targets, production-like replay fidelity, permitted deterministic checks, repeated-run design and stability limits, human-utility evidence, latency, tokens, source load, cost, SLA, and operational-capacity gates.
- Security/privacy must confirm source authority, ACL and tenant scope, redaction, retention, sensitive Evidence handling, non-compensable vetoes, shadow isolation, and stop/exit conditions.
- Owner, experiment owner, Eng, and security/privacy must jointly approve any rung advancement. Missing Evidence, disagreement, or absent approval remains NO-GO.

## Closure checklist

- [x] Threshold-free evaluation/adjudication contract prepared and linked.
- [x] Hard NO-GO and threshold-free stop rules frozen without invented numbers.
- [ ] Real blind historical case selected, frozen, leakage-audited, and run.
- [ ] Independent experiment/domain and production/code labels completed before Agent-output review.
- [ ] Experiment-owner adjudication completed with code/domain and production Evidence.
- [ ] Agreement, disputes, unknowns, and immutable packet revision sealed.
- [ ] De-identified fixture suite run across all required case classes, applicable trivial baselines, adversarial decoys, leakage checks, detector classes, and hard failures; fixture-author/evaluator independence or conflicts are sealed.
- [ ] Production-like replay authorized and completed with fidelity, load, and provenance receipts.
- [ ] Pilot distributions and human baseline collected for case count, `k`, stability, utility, latency, tokens, source load, cost, SLA, and risk calibration.
- [ ] Owner, experiment owner, Eng, and security/privacy approve the applicable exit gates.
- [ ] Only after every applicable item above is evidenced: set `Status: closed`, retain Claim, write the final resolution in this ticket, and add exactly one Decisions-so-far pointer to `map.md`.

## Current outcome

**NOT RESOLVED.** The M0 acceptance contract is specified in the canonical evaluation plan, but M0 fixtures have not been implemented or reviewed. Direction-only experiment-owner adjudication and pilot evidence are also missing. This ticket remains open and claimed by `019ff4cc-9d54-7ea0-ba61-aa23d57dc901`.
