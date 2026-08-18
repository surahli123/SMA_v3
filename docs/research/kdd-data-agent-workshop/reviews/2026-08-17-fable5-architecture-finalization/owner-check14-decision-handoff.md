---
handoff_id: kdd-m0-owner-check14-decision-20260817
created_at: 2026-08-17T21:18:00-07:00
source_thread: 019ff3f9-ee51-7e32-937a-85fd9be2226a
target_thread: e8c60598-be86-4971-b887-09c20db86c2b
status_path: /Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/owner-check14-decision-status.json
expires_at: after one run
---

# Cross-Thread Handoff: Record the Owner's Check-14 Decision

## Current Blocker

The Fable architecture-finalization session paused on one Owner question: how independent the M0 Check-14 recomputation path must be. The Owner has now answered.

## Read First

- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/architecture-decision-ledger.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/architecture-finalization-status.json`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/candidate-canonical-writeback-v4.patch`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-exact-digest-review/v4-patch-independent-review.md`

## Owner Decision

The Owner explicitly selected the recommended option:

**M0 Check 14 uses the same authoritative source snapshot plus an independently versioned transform.**

Binding intent:

- The reported primary read and the candidate recomputation bind to the same immutable authoritative source snapshot, interval, scope, and source receipt.
- Metric meaning comes from the current production metric-definition registry/catalog and named production authority, never from old SMA by default.
- The recomputation transform is Data-Agent-owned, deterministic, independently versioned from the reporting/scorecard transform, and produces its own input manifest, transform digest, output digest, and receipt.
- A shared source snapshot is an explicit M0 boundary: Check 14 can challenge transform/parameter/definition application, but it cannot independently detect corruption already present in that source snapshot. That limitation must remain visible as coverage, not be hidden as independence.
- A second independently lineaged source is not required for M0. It may be added later behind P2 as an optional stronger cross-check.
- The decision does not grant production access, P2, implementation authority, a tolerance value, a passing verdict, or permission to start `M0-F1`-`M0-F5`.

## Task

Resume the existing Chinese one-question-at-a-time architecture finalization. Record this as the next Owner decision in the English architecture decision ledger and update the status artifact. Reconcile it with the accepted-for-writeback-review v4 candidate without editing canonical documents or the v4 patch.

Define the minimum technology-neutral Check-14 contract needed for the final architecture/design documents, including source-snapshot identity, transform independence, receipts, deterministic comparison, fail-closed missing/conflict behavior, and the shared-source Coverage Gap. Do not invent a numeric tolerance; leave tolerance selection versioned and metric-policy-owned unless existing Owner evidence already settles it.

Then continue only with any remaining Owner architecture question that truly changes M0 semantics. If no such question remains, produce the session's planned final architecture/design deliverables and status under the existing handoff boundary.

## Output Required

- Update `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/architecture-decision-ledger.md`.
- Update `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/architecture-finalization-status.json`.
- Produce any final architecture/design-flow artifacts already required by the original Fable handoff.
- Write `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/owner-check14-decision-status.json`.

## Done When

- The Owner decision is recorded as Owner authority, not reviewer inference.
- The ledger distinguishes source-snapshot sharing from transform independence.
- No numeric tolerance, P2 authority, implementation authority, or pass verdict is invented.
- Candidate v4 remains unapplied and not frozen.
- Remaining questions or completion state are explicit.

## Red Lines

- Do not modify canonical architecture, plan, sequencing, evaluation, Phase A, or product-code files.
- Do not apply or edit v4.
- Do not start `M0-F1`-`M0-F5`.
- Do not access production.
- Do not commit, push, open a PR, deploy, install, or publish externally.
- Do not call the Codex advisory v4 verdict an Opus/Fable verdict or Owner writeback approval.

## Status Writeback

Write JSON to `status_path` with the decision recorded, files changed, remaining questions, and next lawful step.
