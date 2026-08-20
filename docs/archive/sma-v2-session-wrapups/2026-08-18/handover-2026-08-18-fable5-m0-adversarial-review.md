# Handover — Fable 5 independent adversarial review of the KDD M0 freeze candidate (2026-08-17/18)

**Project:** SMA_v2 — `/Users/surahli/Documents/projects/SMA_v2`
**Branch:** `codex/kdd-data-agent-practices-research` (HEAD at wrapup `13e62af`; the review ran at `28cbbda`; the orchestrator committed the review artifacts in `13e62af`)
**Job:** background review task `4bda4e93` (Fable 5 lead, 5 subagents: 1 Sonnet + 4 Opus; no workflow lanes)

## Last session summary

Ran the Owner-authorized independent adversarial review of the M0 freeze candidate (`m0-m2-build-alignment-packet.md`, sha256 `40c7234f…`) and the Phase A package (`.agents/skills/kdd_data_agent/`, aggregate `2f1001b9…`), in two phases: a blind Phase I (sealed sha256 `e4a63468…`, 41 findings, 4 BLOCKER) and a Phase II comparison with the independent Opus 5 freeze review, plus an Owner-decision delta (five steelman attacks on the eight new Owner decisions S1–S8). Final verdict **BLOCKED**: the packet and six controlling documents changed at 19:44:57 during the review (`40c7234f…` → `67c844d1…`); no verdict was transferred; the new bytes were superseded within hours by Owner decisions D1–D6/S1–S8. Phase A `PASS_WITH_GAPS` confirmed independently.

## Current state

- All four artifacts are committed at HEAD `13e62af` with digests equal to the review's own record:
  `fable5-phase1-independent-findings.md` `e4a63468…`; `fable5-final-adversarial-review.md` `70ce33c6…`; `fable5-review-status.json` `3157f1b9…`; `steelman-owner-decisions-review-status.json` `b82efe23…` (all under `docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-m0-adversarial-review/`).
- The world moved on after this review: a canonical freeze (`reviews/2026-08-18-m0-canonical-freeze/`) and M0-F1–F5 correction Round 5 (`reviews/2026-08-18-m0-f1-f5-correction-round5/`, 370 tests, aggregate `9eea3014…`) exist per CHANGELOG. This review's freeze question is superseded; its Phase A and contract findings remain traceable and should be checked against Round 5.
- CHANGELOG/BACKLOG updated at wrapup (uncommitted, in the shared checkout; the review handoff forbade Git changes, so no commit was made by this session).

## Next steps (ordered)

1. Verify against the Round 5 package which Fable findings are closed: FB-05 scanner escapes (attribute-chain / from-import smuggling / `Path.walk` / test-file aliases; receipt wording), unwired guards (duplicate receipt id, `_case_path` containment, planted-count lock, non-empty registry-resolving `rule_source`), FB-27 default gap-kind inference, FB-28 timestamp normalization.
2. Verify the freeze packet encodes the delta contract items (final review §5/§8): `evidence_class`, `m0_capability_state`, "M0 MVP" renaming, `CHK-*` + sealed `core_check_set`, `AdvisoryRevision` with evidence-lineage class and rubric rule, `query_evidence_state`/`falsifier_execution_status`, typed `PRODUCTION_BINDING_REQUIRED`, export manifest schema, D3 §5.3 shape, D1/D4/D6 semantics in checks 2/14/19.
3. Owner decisions still open at wrapup time (per final review §7): first-Flight core-check set content/ownership; revalidation owner; admissible human-judgment challenge streams + rubric owner; Committee-facing "decision_grade = validity only" sentence; commit authorization for the Continuity Checkpoint (before 2026-08-24); confirmation of facilitator rulings F1–F22.
4. Process: set `OMC_STATE_DIR` (or never `cd` into the package/review dirs) in any session that touches `.agents/skills/kdd_data_agent/` — hooks write `.omc/state` relative to cwd (three occurrences this session, two by other sessions).

## Key context / gotchas

- Two "Opus freeze reviews" existed for `40c7234f…`: the independent one (session `session_01YAsh…`, 3 BLOCKERs, at the canonical paths) and the Phase-A-author's (`b9d777ba`, "zero blockers", overwritten; its `m0-freeze-codex-fix-handoff.md` survived). The orchestrator applied both edit sets → `67c844d1…`.
- Fable-only findings the Opus review lacked: scanner escapes with executable proof (FB-05), `human_state` undefined (FB-07), no check-ID/materiality registry (FB-08), no typed fixture-vs-production class (FB-10), evaluation-design weakness and pooled fixtures (FB-13/14), continuity impossible while untracked (FB-16), budget-cap contradiction (FB-18).
- Conflict resolved by the Owner: arm parity is M0 (D2) — Opus position.
- Independence leaks (disclosed): one line of the Opus status reached Fable via a lane-1 grep; ~10 grep lines of the codex-fix handoff reached lane 2.
- Lanes 3 and 5 died on session limit without reports; lane 3's mutation/escape scripts were re-run by Fable (results in the final review §2); lane 5's scope was done by Fable personally.
- Write/Edit into the shared checkout are blocked for background jobs without a worktree; artifacts were written to job scratch and `cp`'d (disclosed in the report), the same workaround the 2026-08-16 Opus session used.

## Relevant files (read first)

1. `docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-m0-adversarial-review/fable5-final-adversarial-review.md` — verdict, Opus comparison, delta attacks, corrections (§8), gates (§9), next-session sequence (§10).
2. `.../fable5-phase1-independent-findings.md` — full finding list with evidence (§3), verification evidence (§2).
3. `.../fable5-review-status.json`, `.../steelman-owner-decisions-review-status.json`.
4. `docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/architecture-decision-ledger.md` — D1–D6, S1–S8, F1–F22.
5. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-freeze-opus5-adversarial-review.md` — the Opus review compared against.
6. Job scratch (may be deleted with the job): `~/.claude/jobs/4bda4e93/tmp/lane-{1,2,4}/report.md`, `lane-3/*.py`, `artifacts/`.
