---
handoff_id: m0-prealignment-foundation-20260816
created_at: 2026-08-17T05:16:45Z
source_thread: side-conversation-01a00e1f-a213-7c30-988f-50e79a415ffb
target_thread: claude-code-opus5-m0-foundation-builder
status_path: /Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-prealignment-foundation-status.json
expires_at: after M0 alignment digest is delivered and one build run completes
---

# Cross-Thread Handoff: Start the M0 Foundation Before Final Alignment

## Current Blocker

The Owner's goal is to finish a fixture-backed M0 MVP today. Codex and a separate Opus 5 reviewer
are still aligning the exact final deliverable. Waiting would waste implementation time, but
inventing unsettled product semantics would recreate the prior spike/spec mismatch.

Start immediately on the low-rework engineering foundation. Stop at the explicit alignment gate
for any behavior whose meaning depends on the final M0 Build Alignment Packet. After the main
session supplies the frozen packet digest, continue in this same session and bind Phase B to that
exact digest.

The Owner authorizes local, fixture-only M0 implementation within this handoff. This does not
authorize production access, M1/M2 work, deployment, commit, push, PR, or mutation of legacy paths.

## Read First

- `/Users/surahli/Documents/projects/SMA_v2/AGENTS.md`, if present
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/implementation-sequencing.md`, especially lines 41-72, 142-200, 479-523, and 576
- `/Users/surahli/Documents/projects/SMA_v2/docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md`, especially lines 12-91 and 761-767
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/wayfinder/freeze-canonical-domain-policy-contracts.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-build-alignment-packet-draft.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/opus5-review.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/status.json`

Treat the draft and review as provisional. The frozen packet digest, when provided, will outrank
them for Phase B implementation semantics.

## Task

### Phase A — implement now

Own only a new isolated greenfield M0 package, its tests, and a build receipt. Inspect the dirty
worktree first and select a non-conflicting package root consistent with M0-F0. Do not extend or
import `.agents/skills/sma/` or `.agents/skills/sma_rewrite/`.

Implement the foundation that is invariant across the remaining alignment decisions:

1. Select and record the minimum local toolchain, package boundary, test command, schema boundary,
   and replacement seam. Prefer the repository's existing supported toolchain when it satisfies
   the hermetic requirements.
2. Add canonical JSON serialization and deterministic content digests for immutable revisions.
3. Add generic append-only revision and receipt primitives with explicit source identity,
   authorization state, timestamp/interval, derivation inputs, and Coverage Gap support.
4. Add a fixture-only read-adapter interface and local fixture implementation. It must have no
   production credential, network, subprocess, publication, source-worktree write, or arbitrary
   execution capability.
5. Support typed fixture read outcomes needed by M0: trusted, blocked, partial, stale, conflicting,
   unauthorized, unavailable, and redaction failure. Preserve `UNKNOWN`; never guess.
6. Add a hermetic local runner and deterministic replay test. Identical frozen fixture inputs must
   produce byte-stable serialized receipts and digests.
7. Add a positive capability allowlist plus tests/import-graph evidence showing that legacy
   runtime, production network, external publication, and mutation paths are unreachable.
8. Add test-fixture infrastructure and representative raw fixture inputs. Expected final readiness
   outcomes may be marked `alignment_pending` where they depend on the frozen packet.

Do not freeze or independently reinterpret the following during Phase A:

- the final `ready | directional_only | blocked` decision rules;
- the final required-check inventory or materiality policy;
- the exact final `ExperimentReadContract` and `FlightReadinessPacket` field set;
- acceptance scenario identifiers currently under C1 reconciliation;
- first-screen information hierarchy or final reviewer interaction;
- Owner decisions about flight definition, primary/co-primary metrics, invalid-experiment fixes,
  role overlap, staffing, or protected-domain-asset use.

### Alignment gate

When Phase A passes, write the status as `blocked` with `next_step` requesting the exact frozen
packet path and digest. List every code seam awaiting alignment. Do not fill those seams with your
own product decision.

### Phase B — continue only after the main session supplies the frozen digest

Bind the implementation to the exact digest, then complete M0-F1 through M0-F5:

- final contract validation;
- final readiness checks and outcome computation;
- immutable `FlightReadinessPacket`;
- packet-centered read-only projection;
- the complete aligned fixture and adversarial acceptance suite;
- one end-to-end hermetic vertical slice and build receipt.

Any conflict between the frozen packet and an older planning document must stop as a typed
alignment blocker; do not silently choose one.

## Output Required

- New isolated M0 package and tests in the selected greenfield root.
- A short English build receipt beside this handoff named
  `m0-prealignment-foundation-receipt.md`, containing:
  - owned files;
  - toolchain decision and replacement boundary;
  - commands run and exact outcomes;
  - capability/import evidence;
  - deterministic replay evidence;
  - completed Phase A work;
  - exact Phase B seams awaiting alignment;
  - dirty-worktree preservation statement.
- Status writeback to the absolute `status_path`.

## Done When

Phase A is complete when:

- one documented hermetic command runs the foundation suite;
- fixture reads and typed failures require no network, credential, production source, or legacy
  runtime;
- identical frozen inputs produce byte-stable receipt/digest output;
- prohibited capability reachability is mechanically checked;
- no unsettled M0 product meaning was invented;
- all changed files are within the newly owned package, its tests, the build receipt, and status;
- the session is ready to continue Phase B against a supplied frozen digest.

The full handoff is complete only when Phase B later passes the frozen M0 acceptance ledger. A
green Phase A is progress, not proof that M0 is finished.

## Red Lines

- Do not modify canonical research, planning, architecture, Wayfinder, alignment, or review files.
- Do not modify `.agents/skills/sma/` or `.agents/skills/sma_rewrite/evals/`.
- Do not import or depend on legacy SMA/KDD runtime code.
- Do not access production, external services, credentials, company data, or live reviewers.
- Do not implement M1 Metric Movement, M2 Win/Loss, causal claims, ranked production candidates,
  candidate diffs, SEV analysis, Trace-as-Evidence, deployment, rollback, or mutation.
- Do not overwrite or revert user-owned dirty-worktree changes.
- Do not commit, push, open a PR, install software, or modify global settings.
- Do not declare M0 complete from Phase A.
- Stay inside the task and write back status.

## Status Writeback

Write JSON to `status_path`:

```json
{
  "handoff_id": "m0-prealignment-foundation-20260816",
  "status": "done|blocked|skipped",
  "summary": "",
  "evidence": [],
  "next_step": "",
  "updated_at": ""
}
```
