---
handoff_id: sma-v3-task-migration-20260818
created_at: 2026-08-18T14:33:32-07:00
source_thread: 019ff3f9-ee51-7e32-937a-85fd9be2226a
target_thread: SMA v3 main orchestrator and all future implementation/review tasks
status_path: /Users/surahli/Documents/projects/SMA_v3/docs/handoffs/2026-08-18-sma-v3-task-migration-status.json
expires_at: superseded by a later repository migration record
---

# Cross-Thread Handoff: Move the Data Agent Initiative to SMA v3

## Decision

`/Users/surahli/Documents/projects/SMA_v3` and `surahli123/SMA_v3` are the only writable repository targets for new Data Agent initiative work after this handoff.

`/Users/surahli/Documents/projects/SMA_v2` and its Codex tasks remain read-only historical evidence. Do not continue implementation, planning, review writeback, commits, or pushes there.

## Verified Baseline

- Repository: `https://github.com/surahli123/SMA_v3`
- Visibility: private
- Default branch: `main`
- Baseline commit: `a6c1a528d910e3560b1e8ef1b917c26d498b0414`
- Local checkout: `/Users/surahli/Documents/projects/SMA_v3`
- Baseline worktree state: clean
- Accepted local M0 package aggregate: `sha256:9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a`
- Independent verdict: `ACCEPT_LOCAL_M0_EVIDENCE`

The authorized SMA v2 export roots were compared with SMA v3 on 2026-08-18. No newer implementation or research artifact was missing. The only content differences were the intentional SMA v3 export/provenance annotations in `deliverable-index.md` and `source-manifest.md`; runtime `.omc`, caches, private media, protected legacy paths, and unrelated dirty content remain excluded.

## Historical Task Index

These tasks are evidence sources, not writable continuations:

| Role | Historical task ID |
| --- | --- |
| Original main orchestrator | `019ff3f9-ee51-7e32-937a-85fd9be2226a` |
| Planning and Owner grill | `019ff40c-ce33-7b71-83c6-61b6b24e5b8c` |
| Champion reverse audit | `019ff479-d88f-7552-8c2c-e69b02a36750` |
| Fourth-place reverse audit | `019ff489-5bd3-7143-acc3-d1998f1062ea` |
| DeepSeek Harness research | `01a003d5-3e80-7e70-9606-d9536dcbf71b` |
| CE plan | `019ff4bd-dad1-7af1-ba0f-5e4e3a007852` |
| Prototype review surface | `019ff4cf-be73-7381-a086-6425c2a0bdf2` |
| M0 implementation continuation | `01a00e6c-b16d-7d82-85a5-74009513137e` |
| Exact-digest and correction reviews | `01a012d4-2e66-7893-9fd0-2cf0455317d1`, `01a01427-a5a6-75a1-a314-bb7391eccd41`, `01a01441-064c-75b2-8259-d51e6762818e`, `01a014a8-83b7-7140-a9bd-365cd2b8606f` |

Full durable context is already present under `docs/research/kdd-data-agent-workshop/`, including the original grill records, Fable 5 and Opus 5 review bundles, architecture drafts, freeze records, execution receipts, and independent M0 verdicts.

## Task Routing Rules

1. Create every new Codex task under the registered `SMA_v3` project, preferably in its own worktree.
2. New Claude Code sessions must use `/Users/surahli/Documents/projects/SMA_v3` or an explicit SMA v3 feature worktree.
3. Every implementation task receives a bounded English handoff with exact input digests, owned paths, stop conditions, status writeback, and one-run authority.
4. A reviewer must not share authorship of the bytes it accepts. Review tasks use a clean SMA v3 checkout or isolated worktree and bind the exact reviewed digest.
5. Never transfer a historical verdict to changed bytes. Preserve separate proof for fixture evidence, local MVP completion, production authorization, P2/P3/P4 closure, M1/M2, and Committee Acceptance.
6. Never re-import the excluded legacy SMA application, private workshop media, company data, credentials, caches, or runtime state.

## Red Lines

- Do not write to SMA v2.
- Do not infer production authority from the export or local tests.
- Do not modify accepted M0 package bytes without creating a new aggregate and independent review lane.
- Do not commit, push, open a pull request, deploy, or publish unless the relevant handoff explicitly grants that action.

## Status Writeback

The new SMA v3 main orchestrator writes:

```json
{
  "handoff_id": "sma-v3-task-migration-20260818",
  "status": "done|blocked",
  "summary": "",
  "new_main_thread_id": "",
  "active_feature_worktrees": [],
  "evidence": [],
  "next_step": "",
  "updated_at": ""
}
```
