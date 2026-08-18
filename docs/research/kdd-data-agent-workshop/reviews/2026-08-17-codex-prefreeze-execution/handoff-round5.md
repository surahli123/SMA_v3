---
handoff_id: kdd-m0-canonical-candidate-v5-20260818
created_at: 2026-08-18T00:45:19-07:00
source_thread: 019ff3f9-ee51-7e32-937a-85fd9be2226a
target_thread: 01a012d4-2868-7d63-906d-3e8749447eba
status_path: /Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/status-round5.json
expires_at: after one run
---

# Cross-Thread Handoff: Produce the M0 Canonical Candidate v5 Patch

## Current Blocker

The independently accepted v4 unapplied patch predates the Owner-confirmed steelman decisions S9-S11 and does not close the latest Fable delta findings or the policy implications surfaced by the independent Phase A review. Canonical documents must not be edited until a new exact patch is independently reviewed.

## Read First

- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/candidate-canonical-writeback-v4.patch`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-exact-digest-review/v4-patch-independent-review.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-m0-adversarial-review/fable5-final-adversarial-review.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-m0-adversarial-review/fable5-review-status.json`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-phase-a-independent-verification/phase-a-independent-review.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/architecture-design-draft.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/architecture-decision-ledger.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/steelman-owner-alignment-final.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/steelman-owner-alignment-codex-continuation.md`
- The current live bytes of every proposed patch target.

## Task

Perform one bounded documentation-only run. Produce a new **unapplied** v5 patch over the current live canonical bytes. Start with every accepted v4 change and incorporate all confirmed Owner decisions D1-D8 and S1-S11 plus evidence-backed contract corrections from the completed Fable and Phase A reviews.

The v5 candidate must, at minimum:

1. Encode S9: post-unblinding evidence can trigger urgent investigation but cannot alone carry `recommend_change` or `recommend_block`; require an independent confirmation receipt and preserve selection timing/tested-analysis inventory.
2. Encode S10: separate `m0_capability_state` from per-Flight `analysis_use`; a correctly blocked real Flight may establish capability while remaining non-decision-grade and retaining `positive_production_path_unverified`.
3. Encode S11: add a separate `candidate_diff_eligibility` gate driven by evidence and change type; require M2 for user-visible search semantics and allow versioned N/A only for deterministic technical corrections.
4. Add a typed append-only `FlightAdvisoryRevision`, separate from Cause Verdict, Recommendation Readiness, Action Approval, and Incident State. Include official metric result, evidence IDs, lineage classes, counterevidence, falsifier and execution state, `query_evidence_state`, selection timing, independent confirmation receipt, DS challenge record, and supersession.
5. Make challenge-evidence lineage operational. Evidence derived from the decision metric inputs is not independent. Human-judgment evidence requires a preregistered/blind rubric or remains exploratory/P4-gated.
6. Encode the S1-S8 items Fable found missing: `evidence_class`, versioned and sealed `core_check_set`, typed `PRODUCTION_BINDING_REQUIRED`, laptop export manifest/redaction receipt, Query Success union and component labels, and no hidden component guardrails.
7. Preserve D1-D8 exactly, including one stored `analysis_use` plus a derived projection, check-14 independence class/shared-snapshot Coverage Gap, the D7 fixed core floor, and D8 laptop-scoped receipt boundary.
8. Resolve the independent Phase A policy implications without pretending code is fixed: authorization and redaction are orthogonal axes; any Coverage Gap taxonomy extension must be an explicit versioned registry decision rather than an accidental code enum. Remove or narrow claims that the current Phase A package already proves the false/untested controls identified by the review.
9. Keep fixture-backed local completion distinct from production-backed capability, production authorization, a Flight's decision-grade status, and Committee Acceptance.
10. Preserve valid unapplied diffs, human-only delivery, capability isolation, no automation consumer, no mutation authority, and HIGH-risk fail-closed behavior.
11. Carry every still-open P2/P3/P4/production binding as an explicit gate. Do not invent tables, schemas, owners, thresholds, tolerances, retention values, credentials, or Committee decisions.
12. Reconcile terminology and acceptance IDs across all touched controlling documents. One identifier must have one meaning.

Permitted patch targets are limited to the minimum necessary controlling documents among:

- `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md`
- `docs/research/kdd-data-agent-workshop/final-architecture-spec.md`
- `docs/research/kdd-data-agent-workshop/implementation-sequencing.md`
- `docs/research/kdd-data-agent-workshop/eval-acceptance-plan.md`
- `docs/research/kdd-data-agent-workshop/planning-decision-packet.md`
- `docs/research/kdd-data-agent-workshop/enterprise-experiment-post-analysis-profile.md`
- `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md`

Do not modify those live files. Build and test the patch only in a fresh disposable copy.

## Output Required

- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/candidate-canonical-writeback-v5.patch`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/round5-disposition.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/status-round5.json`

The disposition must map every requirement above and every residual Fable BLOCKER/MAJOR or Phase A policy implication to one of: `implemented_in_patch`, `implementation_only`, `open_named_gate`, or `rejected_with_evidence`.

## Done When

- The v5 patch applies cleanly to a fresh disposable copy of the exact current live target bytes.
- Every target input digest and every post-apply digest is recorded.
- D1-D8 and S1-S11 have an exact traceability table.
- Stale live-authorization wording and the old fixture-equals-M0 language are absent.
- Acceptance-ID uniqueness and ownership checks pass.
- Markdown link checks and `git diff --check` on the patch result pass.
- No live canonical, Phase A, Fable artifact, prior patch/review, or Git-state byte changed.
- Status JSON is written and the task stops.

## Red Lines

- Do not edit live canonical documents or Fable-authored artifacts.
- Do not edit `.agents/skills/kdd_data_agent/`, its tests, or fixtures.
- Do not start M0-F1 through M0-F5.
- Do not create a freeze record or implementation authorization.
- Do not use Fable or Claude.
- Do not spawn subagents or reviewer lanes.
- Do not commit, push, install dependencies, access production, or modify Git state.
- Preserve all unrelated dirty-worktree changes as user-owned.

## Status Writeback

Write JSON to the `status_path` with:

```json
{
  "handoff_id": "kdd-m0-canonical-candidate-v5-20260818",
  "status": "done|blocked",
  "summary": "",
  "verdict": "CANDIDATE_READY_FOR_INDEPENDENT_REVIEW|BLOCKED",
  "patch_path": "",
  "patch_sha256": "",
  "input_digests": {},
  "post_apply_digests": {},
  "evidence": [],
  "next_step": "",
  "updated_at": ""
}
```
