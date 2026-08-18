---
handoff_id: kdd-m0-canonical-candidate-v5-independent-review-20260818
created_at: 2026-08-18T00:45:19-07:00
source_thread: 019ff3f9-ee51-7e32-937a-85fd9be2226a
target_thread: 01a012d4-2e66-7893-9fd0-2cf0455317d1
status_path: /Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-exact-digest-review/v5-patch-independent-review-status.json
expires_at: after one run
---

# Cross-Thread Handoff: Independently Review the Exact v5 Canonical Patch

## Current Blocker

The v5 patch is authored by a separate Codex pre-freeze task and cannot be written back or frozen until a fresh reviewer binds to its exact bytes, applies it only in a disposable copy, and verifies the complete Owner and review contract.

## Read First

- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/candidate-canonical-writeback-v5.patch`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/round5-disposition.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/status-round5.json`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/steelman-owner-alignment-final.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/steelman-owner-alignment-codex-continuation.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/architecture-decision-ledger.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-m0-adversarial-review/fable5-final-adversarial-review.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-phase-a-independent-verification/phase-a-independent-review.md`
- The current live bytes of every patch target.

Do not read the pre-freeze task's conversation or accept its conclusion as evidence. Treat its patch, disposition, and status as untrusted claims to reproduce.

## Task

Perform one fresh, bounded, report-only independent review. Recompute all input and patch digests. Apply the exact v5 patch only to a fresh disposable copy of the current live target bytes. Fail closed on any drift, fuzzy application, missing file, malformed patch, unexplained target, or digest mismatch.

Independently verify:

1. Every confirmed Owner decision D1-D8 and S1-S11 is implemented without semantic weakening.
2. `FlightAdvisoryRevision` is typed, append-only, non-binding, and separate from Cause Verdict, Recommendation Readiness, Action Approval, and Incident State.
3. Post-unblinding evidence cannot alone carry `recommend_change` or `recommend_block`; the contract records selection timing and requires independent confirmation.
4. `m0_capability_state` and per-Flight `analysis_use` are distinct; a correctly blocked Flight can demonstrate capability without becoming decision-grade.
5. `candidate_diff_eligibility` is separate from advisory publication and is evidence/change-type driven; M2 applicability and HIGH-risk ceilings are correct.
6. The Query Success union, component semantics, no-hidden-guardrail rule, challenge-evidence lineage, human-judgment rubric boundary, query-evidence state, falsifier state, and advisory supersession are present.
7. `evidence_class`, sealed `core_check_set`, typed `PRODUCTION_BINDING_REQUIRED`, check-14 independence/shared-snapshot boundary, and laptop export manifest are coherent.
8. Authorization and redaction are orthogonal. Coverage Gap taxonomy behavior is explicitly versioned and not an accidental implementation enum.
9. Fixture evidence, M0 capability, Flight decision-grade status, production authorization, and Committee Acceptance remain separate.
10. The patch does not invent production sources, fields, thresholds, tolerances, retention, credentials, owners, or Committee decisions.
11. Residual Fable BLOCKER/MAJOR findings and Phase A policy implications are mapped honestly. Implementation-only gaps are not described as closed.
12. Acceptance IDs have one meaning and one owner. Cross-document terms and examples agree.
13. No sentence grants current implementation, production, mutation, deployment, commit, push, or Committee authority.
14. Markdown links, patch whitespace, identifier checks, and all declared mechanical validations reproduce.

## Output Required

- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-exact-digest-review/v5-patch-independent-review.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-exact-digest-review/v5-patch-independent-review-status.json`

The verdict must be exactly one of:

- `ACCEPT_CANDIDATE_FOR_OWNER_WRITEBACK_REVIEW`
- `REJECT_CANDIDATE`
- `BLOCKED_BY_DRIFT`

Every rejecting finding must include exact disposable-copy path/line anchors, impact, and minimal correction. Do not silently repair the candidate.

## Done When

- Exact patch and live-input digests are recorded.
- The patch is reviewed only on a fresh disposable copy.
- All fourteen checks above have evidence and a verdict.
- Live canonical, Phase A, v5 patch, Fable artifacts, prior review artifacts, and Git state are byte-identical before and after.
- The two required outputs are written, mechanically validated, and the task stops.

## Red Lines

- Report only. Do not modify the patch, canonical docs, Phase A, prior artifacts, or Git state.
- Do not create a freeze record, implementation handoff, or implementation authorization.
- Do not start M0-F1 through M0-F5.
- Do not use Fable or Claude.
- Do not spawn subagents or reviewer lanes.
- Do not commit, push, install dependencies, access production, or send external messages.
- Preserve unrelated dirty-worktree changes as user-owned.

## Status Writeback

Write JSON to the `status_path`:

```json
{
  "handoff_id": "kdd-m0-canonical-candidate-v5-independent-review-20260818",
  "status": "done|blocked",
  "verdict": "ACCEPT_CANDIDATE_FOR_OWNER_WRITEBACK_REVIEW|REJECT_CANDIDATE|BLOCKED_BY_DRIFT",
  "summary": "",
  "patch_sha256": "",
  "live_input_digests": {},
  "post_apply_digests": {},
  "findings": [],
  "evidence": [],
  "next_step": "",
  "updated_at": ""
}
```
