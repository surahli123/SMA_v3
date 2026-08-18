---
handoff_id: kdd-m0-prefreeze-execution-20260817
created_at: 2026-08-17T20:05:00-07:00
source_thread: main-orchestrator
target_thread: Codex Sol Medium execution-readiness task
status_path: /Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/status.json
expires_at: after one run
---

# Cross-Thread Handoff: M0 Pre-Freeze Execution Readiness

## Current Blocker

M0-F1 through M0-F5 cannot begin until an exact packet/spec binding receives the
required reviews, the Owner acknowledges the binding, and a fresh bounded start
authorization exists. Claude Opus review is rate-limited until 00:10 PT. Product code
must remain unchanged meanwhile.

## Read First

- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-freeze-codex-disposition.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/architecture-decision-ledger.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/coordination-update-2026-08-17.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/final-architecture-spec.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/implementation-sequencing.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md`
- `/Users/surahli/Documents/projects/SMA_v2/.agents/skills/kdd_data_agent/alignment/seams.py`

## Task

Prepare the largest safe execution-ready package that does not require Claude or a
freeze. Work against the live bytes and preserve the dirty worktree.

1. Recompute the packet, spec, CE plan, sequencing, and Phase A package digests.
2. Translate durable Owner decisions D1-D3 and the known residual drift into an
   unapplied candidate patch. D3 now supersedes the earlier two-stored-field candidate:
   `analysis_use` is stored; `post_analysis_eligibility` is a render-time projection.
3. The patch must reconcile at least:
   - `final-architecture-spec.md:469` with D1's declared sufficiency rule;
   - packet `VAL-M0-002` with runtime and preregistered sample sufficiency;
   - D1's no-post-hoc-power rule kinds `runtime_only | runtime_and_sample`;
   - D2 arm parity and versioned applicability behavior;
   - D3 single stored readiness state and derived eligibility projection;
   - any directly affected CE-plan/sequencing/evaluation wording.
4. Create a bounded M0-F1-F5 start-handoff draft with placeholders for final path,
   revision, digest, independent verdicts, Owner acknowledgement, and one-run budget.
5. Create a completion ledger mapping M0-F1-F5 to observable acceptance evidence,
   while keeping Phase A verification, local MVP completion, production authorization,
   and Committee Acceptance separate.

Do not apply the candidate patch. Do not modify canonical documents or product code.

## Output Required

Write only inside this directory:

- `candidate-canonical-writeback.patch`
- `m0-f1-f5-start-handoff-draft.md`
- `m0-f1-f5-completion-ledger.md`
- `status.json`

Use concise Chinese commentary. Durable artifacts must be English.

## Done When

- Every patch hunk has a source decision or finding anchor.
- The patch applies cleanly in a disposable copy or passes an equivalent dry-run.
- No canonical, implementation, test, fixture, Git, production, or external state was
  changed.
- `status.json` records observed digests, outputs, verification, and blockers.

## Red Lines

- Do not start or implement M0-F1 through M0-F5.
- Do not edit `.agents/skills/kdd_data_agent/` or any canonical planning/spec file.
- Do not freeze, commit, push, create a PR, deploy, access production, install packages,
  or send external messages.
- Do not decide unresolved Owner questions.
- Do not claim that a dry-run patch, passing tests, or a prepared handoff is an accepted
  freeze or implementation authorization.

## Status Writeback

Write JSON to the declared `status_path` with `handoff_id`, `status`, `summary`,
`evidence`, `next_step`, and `updated_at`.
