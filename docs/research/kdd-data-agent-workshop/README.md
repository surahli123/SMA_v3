# KDD Data Agent Greenfield Redesign

This directory is the English research, planning, architecture, evaluation, and continuation package for a new search-metric Data Agent. It starts from the owner's real post-experiment and SEV workflows. Old SMA, KDD workshop systems, and award-winning solutions are evidence and design references only; none is a required architecture or compatibility target.

## Product Destination

The owner-confirmed first gate and main deliverable is **M0 Flight Readiness**: freeze an `ExperimentReadContract`, determine whether the Experiment setup and decision-metric read are trustworthy, and produce an immutable `FlightReadinessPacket` with blockers, disagreements, Coverage Gaps, coordinated readiness fields, and a typed next safe action.

M0, M1 Metric Movement and Production Grounding, and M2 Win/Loss Evidence belong to one Owner-aligned validation program for one Flight. The current executable scope is the local fixture-backed M0 MVP. M1/M2 require their named gates and separate implementation-start receipts; Scenario B requires a later separately approved plan.

The Agent is read-only. No output, verdict, readiness state, evaluation result, human review, or handoff grants authority to mutate production, apply a diff, deploy, roll back, commit, push, send a message, or publish a document.

## Start Here

1. [Deliverable index](deliverable-index.md) — complete inventory and reading order.
2. [Planning decision packet](planning-decision-packet.md) — owner-confirmed product contract.
3. [Owner alignment record](reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md) — O1-O6 product authority for the M0-M2 validation program.
4. [Frozen M0-M2 alignment packet](reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md) and [canonical freeze record](reviews/2026-08-18-m0-canonical-freeze/m0-canonical-freeze-record.md) — exact revision and SHA-256 authority for the bounded local M0 build.
5. [Round 5 independent review](reviews/2026-08-18-m0-f1-f5-correction-round5/independent-review.md) — accepts the exact local fixture-backed M0 package aggregate and preserves every external gate.
6. [Final architecture specification](final-architecture-spec.md) — canonical target design.
7. [Implementation sequencing](implementation-sequencing.md) — dependency-ordered delivery route.
8. [Evaluation and acceptance plan](eval-acceptance-plan.md) — threshold-free evaluation, hard vetoes, and pilot gates.
9. [CE implementation plan](../../plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md) — concrete engineering units and tests.
10. [Enterprise experiment post-analysis profile](enterprise-experiment-post-analysis-profile.md) — supporting profile; Owner-aligned decisions are authoritative where its older addendum drifted.
11. [DeepSeek harness practices](deepseek-harness-practices.md) — supporting fixed-artifact research on safe reuse and diagnostic Trace boundaries.
12. [Opus 5 review bundle](reviews/2026-08-15-opus5-enterprise-plan-review/README.md), [Codex disposition](reviews/2026-08-15-opus5-enterprise-plan-review/03-codex-disposition.md), and [M0 alignment review](reviews/2026-08-16-opus5-m0-alignment/opus5-review.md) — adversarial findings, receipts, and reconciliation evidence; reviewer text is not product authority.
13. [Cloud/internal-agent handoff](cloud-agent-handoff.md) — continuation boundaries and exact safe next steps.

Use the [research synthesis](research-synthesis.md) for Adopt/Adapt/Reject navigation and the [source manifest](source-manifest.md) for provenance. Material claims must still route to the underlying audit or fixed source revision.

## Current Gate State

- Validation program: **M0 is the first gate and main deliverable; M1/M2 continue the same one-Flight program after their named gates and separate start receipts**.
- Current implementation: **the exact 59-file local fixture-backed `M0-F0`-`M0-F5` package is independently accepted** at aggregate `sha256:9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a`; `370` tests passed from three working directories. This proves local fixture behavior only. Production capability and M1/M2 implementation remain unproven or unauthorized.
- Canonical domain and policy contract: **closed**.
- Production evidence authority and access: **open**; human source/ownership/security decisions are required.
- Observability-first review surface: **open**. The current Evidence Room prototype is an M1 research artifact. Its `Review | Claims | Verify | Trace` workflow passed static and browser checks, but the current M0 slice still needs a packet-centered Flight Readiness prototype and live owner/reviewer acceptance.
- Evaluation gold and calibration: **open**; the threshold-free contract is prepared, but blind adjudication and pilot evidence are incomplete.
- Opus 5 enterprise-plan review and exact-byte freeze path: **completed**. The 38 findings were reconciled, Owner decisions were recorded, and the accepted packet/architecture bindings are frozen by `m0-canonical-freeze-v1`.
- Fable 5 review: **later completed against historical candidate bytes and returned `BLOCKED` after detecting byte drift and unresolved Owner-decision deltas**. It is retained as adversarial evidence, not transferred to the later frozen revision. The earlier availability receipt remains historical context only.
- Local M0 independent review: **`ACCEPT_LOCAL_M0_EVIDENCE`** for Round 5 exact bytes. Phase A was not readjudicated; production authority/capability, P2/P3/P4, M1/M2, deployment/publication, and Committee Acceptance remain separate.
- Numeric reliability, stability, latency, token, cost, source-load, SLA, and shadow-read thresholds: **unset by design**.

The local fixture-backed M0 implementation is complete for the accepted exact package bytes. P2/P3/P4 remain open and must not be described as closed; they gate normalized production authority, live interaction acceptance, and blind/pilot exits respectively. The first real Flight still requires its separately scoped company-laptop authorization receipt and production source bindings.

## Source and Publication Boundary

This scaffold contains derived research, public-source provenance, and synthetic implementation evidence. It does not contain raw private audio, workshop screenshots, private video, credentials, company data, or private attachments. Public paper source files may be included when their provenance and redistribution basis are recorded; no PDF is currently present in this package. Machine-local research locations are not portable authority and must be redacted or explicitly classified as immutable historical provenance before publication.

The original Voice Memos item-provider temporary paths are no longer available. The recorded SHA-256 values, durations, and 100% alignment receipts remain the package authority for the completed historical audit, but this package does not claim a current live re-read of those media. A future source revalidation that requires the original recordings must record their unavailability as a Coverage Gap; it must not invalidate the recorded audit merely because the temporary files expired.

Unknown or unavailable sources create Coverage Gaps. They are not negative Evidence and must not be guessed from summaries.

## Canonical Safety Summary

- Cause Verdict: `unassessed | suspected | confirmed | ruled_out | inconclusive`.
- Recommendation Readiness: `not_applicable | blocked | proposal_ready | action_ready | rejected`.
- The axes are independent and governed by a deterministic policy matrix.
- `confirmed` requires all applicable `G0-G7` gates and independent human causal review.
- Invalid Experiments permit only validity, instrumentation, and data-quality guidance or a separately typed, exact, gated, correct `not_applied` remediation diff; they never permit a production-cause or product-logic proposal.
- False `confirmed`, wrong exact patch target, and security/ACL violations are hard NO-GO.
- Corrections are append-only; invalidation triggers dependency-scoped recomputation.
- Evidence Graph is a canonical packet projection. Trace is a separate, cross-linked diagnostic store and never Evidence.

## Continuation Rule

Continue only on the verified user-owned feature branch and preserve unrelated changes. The Owner has authorized a bounded commit and push of the verified research plus local M0 package after the publication checks pass. That authority does not include a PR, deployment, production access, M1/M2 implementation, or public release. See the [share-safe publication manifest](share-safe-publication-manifest.md) and [cloud/internal-agent handoff](cloud-agent-handoff.md) for the full rule set.

For M0 P3 review, first adapt or replace the current [Evidence Room prototype](prototypes/observability-review-surface/README.md) with a packet-centered Flight Readiness surface. The existing prototype remains useful evidence for later M1 conclusion, contradiction, claim-graph, exact-proof, and Trace separation behavior, but it is not the M0 review artifact and cannot close P3 by itself.
