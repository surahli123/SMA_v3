# Cloud and Internal Coding Agent Handoff

Status: continuation handoff for the research/specification package
Repository: `surahli123/SMA_v2`
Feature branch: `codex/kdd-data-agent-practices-research`

## Whole Goal and Current Boundary

The whole goal is a greenfield, production-grounded Data Agent for two user problems:

1. Scenario A: explain why a post-experiment search metric missed its expected outcome and rank exact deployed `code | config | flag | model | data` candidates, with an optional candidate diff that is clearly `not_applied`.
2. Scenario B: investigate a SEV metric drop, rank matching production changes, and prepare a rollback-ready packet while continuing causal analysis and recovery verification.

The current branch contains research, product contracts, architecture, implementation sequencing, evaluation design, continuation guidance, and an independently accepted isolated fixture-backed M0 implementation. M0 Flight Readiness is the first gate and main deliverable. M1/M2 continue the same one-Flight validation program after separate gates/start receipts; Scenario B is deferred and must reuse, not fork, the Evidence/runtime/change/claim/gate/packet substrate. This handoff does not authorize production access or mutation.

## Read First

Read these in order before proposing or changing implementation:

1. [Package README](README.md)
2. [Planning decision packet](planning-decision-packet.md)
3. [Owner alignment record](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md)
4. [Frozen M0-M2 alignment packet](reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md), [canonical freeze record](reviews/2026-08-18-m0-canonical-freeze/m0-canonical-freeze-record.md), and [Round 5 independent review](reviews/2026-08-18-m0-f1-f5-correction-round5/independent-review.md)
5. [Closed canonical domain and policy contract](wayfinder/freeze-canonical-domain-policy-contracts.md)
6. [Final architecture specification](final-architecture-spec.md)
7. [Implementation sequencing](implementation-sequencing.md)
8. [Evaluation and acceptance plan](eval-acceptance-plan.md)
9. [CE implementation plan](../../plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md)
10. [Wayfinder map](wayfinder/map.md) and all three open tickets
11. [Enterprise experiment post-analysis profile](enterprise-experiment-post-analysis-profile.md) as supporting, non-authoritative requirements context
12. [DeepSeek harness practices](deepseek-harness-practices.md) as supporting fixed-artifact research
13. [Opus 5 review bundle](reviews/2026-08-15-opus5-enterprise-plan-review/README.md), [Codex disposition](reviews/2026-08-15-opus5-enterprise-plan-review/03-codex-disposition.md), and [M0 alignment review](reviews/2026-08-16-opus5-m0-alignment/opus5-review.md)
14. [Deliverable index](deliverable-index.md)
15. [Research synthesis](research-synthesis.md) and [source manifest](source-manifest.md) when a design claim needs evidence

Do not use [greenfield-requirements.md](greenfield-requirements.md) as architecture authority. It is a historical, non-canonical draft.

## Frozen Product Contracts

- Begin from Scenario A/B user needs; old SMA and KDD systems are rejectable references, not migration or compatibility constraints.
- Keep Case lifecycle, Stage, Evidence, Claim, Cause Verdict, Recommendation Readiness, Action Approval, and Incident State independent and append-only.
- Cause Verdict is `unassessed | suspected | confirmed | ruled_out | inconclusive`.
- Recommendation Readiness is `not_applicable | blocked | proposal_ready | action_ready | rejected`.
- `observed` is an Evidence or Observed Fact state, not a Cause Verdict.
- Apply the deterministic two-axis policy matrix and `G0-G7` fail-closed contract exactly.
- A model, worker, vote, consensus, confidence score, or human opinion without Evidence cannot produce `confirmed`.
- Invalid Experiments allow only typed validity, instrumentation, and data-quality guidance or a separately typed exact, correct, gated `not_applied` remediation diff. They block production-cause and product-logic Recommendations.
- HIGH-risk or large-blast-radius Recommendations cannot become `action_ready`.
- False `confirmed`, a wrong exact patch target, and any security/ACL violation are hard NO-GO.
- Evidence invalidation and human correction create new revisions, retain history, and recompute the dependency closure.
- Evidence Graph is a canonical packet projection. Trace is a separate, cross-linked diagnostic store and never Evidence. Use tables, timelines, diffs, or receipts when clearer.
- No state, receipt, review, evaluation result, or handoff authorizes mutation.

## Source Availability Boundary

The repository scaffold contains derived English research and provenance records, not raw meeting or award-team media.

Do not add or upload:

- raw workshop audio;
- the 73 screenshots;
- private award-team video or unreleasable source files;
- private attachment, download, Desktop, temporary-directory, or worktree paths;
- credentials, tokens, tenant identifiers, raw company queries/results/screenshots, or other sensitive production material.

The [source manifest](source-manifest.md) is the routing authority for coverage, fixed revisions, hashes, and availability boundaries. Public paper source files may be carried when their provenance and redistribution basis are recorded. Exact-byte historical review receipts may retain inert local path literals when the freeze record binds those bytes; classify them as non-executable provenance and never treat them as current paths. Do not introduce credentials, private attachments, or production data.

The original Voice Memos item-provider temporary paths are currently unavailable. The stored recording hashes, durations, and 100% audio/alignment receipts remain the authority for the completed historical audit; this handoff does not claim that the original media were re-read live at continuation time. If new source revalidation requires those recordings, record the unavailable source as a Coverage Gap and request a stable, authorized source copy. Do not treat expiration of a temporary path as retroactive invalidation of the recorded audit.

If any source is unavailable in a cloud environment, record a Coverage Gap. Do not infer that a failed retrieval disproves a claim, reconstruct missing media from summaries, or promote an author claim to a verified fact.

## Open Gates

### Program and current implementation scope

The Owner confirmed on 2026-08-16 that M0 Flight Readiness is the first gate and main deliverable. M1 Metric Movement and M2 Win/Loss belong to the same one-Flight, four-to-six-active-week validation program. The exact local fixture-backed `M0-F0`-`M0-F5` package is independently accepted at aggregate `9eea3014…b19a`; this is local evidence, not production capability. Production access and M1/M2 implementation remain separately gated. Scenario B requires a later plan.

### Production evidence authority

The [authority ticket](wayfinder/establish-production-evidence-authority.md) remains open. Its [intake](wayfinder/production-evidence-authority-intake.md) is prepared, not approved. Do not implement production adapters, map sensitive evidence, expand tenants, access live sources, or start shadow-read until production owner, Engineering, security/privacy, experiment owner, and relevant on-call/IC owners provide evidence-backed source, ownership, credential, ACL, retention, redaction, and deletion decisions.

### Review interaction acceptance

The [observability ticket](wayfinder/prototype-observability-first-review-surface.md) remains open. The current [Evidence Room prototype](prototypes/observability-review-surface/README.md) is an M1 research artifact. The current M0 slice still needs a packet-centered Flight Readiness surface for both readiness fields, blockers, primary/scorecard-or-UI/recomputed disagreement, Coverage Gaps, receipts, typed next safe action, and named human state, with no implied production cause.

Exactly four unified generated references cover the M1 Review, Claims, Verify, and Trace modes. The current owner review panel scored that prototype `2.1` with `convergence.passed=false`; earlier agent critiques are superseded history. Static and browser checks remain valid mechanical receipts for that artifact, not evidence of M0 suitability, reviewer efficiency, or P3 closure. Do not reuse its M1 claim graph as an M0 conclusion surface, freeze interaction behavior, choose a UI framework as product policy, or claim acceptance until live M0 owner/reviewer feedback closes the ticket.

### Evaluation gold and calibration

The [evaluation ticket](wayfinder/freeze-evaluation-gold-and-calibration.md) remains open. The [prepared contract](wayfinder/evaluation-gold-calibration-contract.md) supports threshold-free implementation, but it is not adjudicated. Do not invent case count, risk weights, top-k, repeated-run, stability, human-utility, latency, token, source-load, cost, SLA, replay, or shadow-exit thresholds. These require the blind historical case and production-complexity pilot receipts.

### Adversarial review history

An early Fable attempt failed its live availability gate before session creation; that receipt remains historical. A later authorized Fable 5 review completed against older candidate bytes and returned `BLOCKED` because the review object changed and later Owner decisions superseded the candidate. Its findings were reconciled into later work, but its verdict does not transfer to the exact frozen packet or Round 5 implementation. The Round 5 independent Codex review accepts only local fixture-backed M0 evidence. Reviewers remain reviewers, not product or production authority.

## Exact Safe Continuation Steps

1. Verify the checked-out repository is exactly `surahli123/SMA_v2` and the branch is `codex/kdd-data-agent-practices-research`; inspect dirty state before editing.
2. Read the frozen contracts and compare any proposed schema or code vocabulary against the closed Wayfinder resolution. Reject single-axis or legacy terms.
3. Preserve the independently accepted local fixture-backed `M0-F0` through `M0-F5` bytes and their exact aggregate. Any implementation change requires a new manifest and fresh independent review. This handoff grants no broader authority.
4. Do not start U1-U13, M1, M2, production reads, or Scenario B from the M0 authorization. Each requires its named gates and a separate implementation-start receipt, although M1/M2 program membership is already Owner-aligned.
5. Before the production-authority gate closes, use only de-identified fixtures and fake read-only adapters. Do not assume production source names, schemas, identity, ACL, retention, redaction, or credentials.
6. Implement only threshold-free evaluation schemas, fixtures, hard-veto receipts, blind-isolation controls, and calibration hooks before pilot adjudication. The harness must refuse a numeric GO decision while thresholds are unset.
7. Keep the Agent's derived-record submission narrow, append-only, and policy-enforced. It must not provide arbitrary file, database, source-system, network, message, or publication writes.
8. Stop and return to the responsible gate when source authority, mapping, authorization, deployed identity, experiment validity, contradiction handling, reviewer independence, or calibration Evidence is missing.
9. Treat Evidence Room only as M1 research. Preserve its receipts, but do not use it as the M0 P3 artifact or convert its scores/checks into owner acceptance. Build and review an M0 packet-centered surface first.
10. Preserve exact acceptance evidence and update the completion/handoff artifacts after each accepted slice; never rewrite historical receipts in place.

## GitHub Continuation Rules

- Treat the feature branch as the continuation branch. Never push or merge `main` as an implicit next step.
- Before every commit or push, verify the GitHub account and exact `owner/repo` remote. A similarly named repository is not sufficient.
- Keep commits limited to the authorized slice. Preserve unrelated user changes and do not bulk-stage the worktree.
- Do not commit raw media, local paths, secrets, credentials, production data, generated caches, or unrelated workspace artifacts.
- The Owner has authorized one bounded commit and push of the verified include set after publication checks. Reverify both the local commit scope and exact remote immediately before each action; this authority does not authorize a PR or merge.
- Do not open a PR, deploy, roll back, send an external message, or publish formal documentation unless the owner explicitly requests that action.
- If the package is moved to another repository or cloud workspace, preserve source hashes, fixed repository revisions, evidence grades, unresolved conflicts, open gates, and relative links.

## Before Claiming an Implementation Milestone

- The relevant Wayfinder gate is closed, or the milestone explicitly remains pre-gate and fixture-only.
- Every requirement in the final spec maps to an implementation unit and acceptance scenario.
- Canonical state, GateReceipt, policy-matrix, invalidation, and immutable-packet tests pass.
- The invalid-experiment path cannot produce a production Recommendation.
- Exact targets are tied to deployed identity, not current main or keyword proximity.
- Hard NO-GO failures are visible and cannot be averaged away.
- Correct abstention returns Coverage Gaps and useful next safe checks.
- Evidence Graph, tables, timelines, diffs, and receipts read canonical packet objects. Trace remains a separate diagnostic store with opaque authorized cross-links.
- No component can mutate production or perform external publication/action.

## Evidence Navigation Rule

For every material implementation decision, cite the canonical product contract first and the primary audit or source manifest second. Research synthesis is navigation, not a replacement for source anchors. When evidence conflicts, preserve the conflict, state the current ceiling, name the cheapest discriminating check, and identify what result would falsify the proposal.
