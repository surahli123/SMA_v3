---
handoff_id: kdd-m0-prefreeze-execution-round2-20260817
created_at: 2026-08-17T20:23:00-07:00
source_thread: main-orchestrator
target_thread: existing Codex Sol Medium execution-readiness task
status_path: /Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/status-round2.json
expires_at: after one follow-up run
---

# Round 2 Handoff: Close the Codex Advisory Defects in the Unapplied Patch

## Read First

- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-exact-digest-review/exact-digest-review.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-exact-digest-review/status.json`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/candidate-canonical-writeback.patch`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/status.json`
- The same live canonical inputs used in Round 1.

## Task

Create a superseding unapplied patch against the unchanged live canonical bytes. Preserve
all correct D1-D3 changes from Round 1 and close the two additional advisory classes:

1. Replace every stale claim that the exhausted Phase A/continuation authorization is
   still live. At minimum inspect the advisory anchors in the CE plan, sequencing,
   evaluation plan, architecture spec, and packet. The result must require a new exact-
   digest Owner start authorization and bounded receipt before M0-F1-F5.
2. Add one authoritative, complete mapping for every active packet `VAL-*` ID. Each ID
   must have exactly one owning M0-F unit, later U unit, or explicit external gate, plus
   its proving test/receipt or open-gate evidence. Do not force M1/M2 or P2/P3/P4 IDs into
   an M0 implementation unit. Reference the authoritative mapping from the packet rather
   than duplicating conflicting meanings.

Preserve B3, M18, M19, and M20 as open actions. Do not convert them into cleared states.
Do not introduce an answer to the still-open independent-recomputation architecture
question; label any affected check-14 wording as pending the Owner/Fable decision.

The historical Phase A aggregate `2f1001...` is not a current verified binding. Do not
copy it into the new status as observed truth. Record the digest-contract mismatch and
leave the future start-handoff value unresolved pending Opus Q11/Q12.

## Output Required

Write only:

- `candidate-canonical-writeback-v2.patch`
- `round2-disposition.md`
- `status-round2.json`

Do not modify the Round 1 patch, canonical docs, code, tests, fixtures, or Git state.
Use direct work only; do not spawn subagents.

## Verification

- `git apply --check --whitespace=error-all` against live bytes;
- actual application in a disposable copy;
- post-apply digest manifest;
- mechanical proof that all active `VAL-*` IDs occur exactly once in the ownership
  mapping and no stale live-authorization phrase survives in the patched copy;
- explicit statement that check 14 remains pending the Owner/Fable ruling.

Stop after one follow-up run. The result is still an unapplied candidate, not a freeze or
implementation authorization.
