---
handoff_id: m0-flight-readiness-exact-byte-review-20260820
created_at: 2026-08-20T00:34:53-07:00
authorized_by: Owner through main orchestrator thread 019ff3f9-ee51-7e32-937a-85fd9be2226a
mode: independent review only
model: Claude Code Opus 5 high effort
worktree: /private/tmp/SMA_v3-opus-m0
branch: codex/m0-flight-readiness-review
base_commit: 5a04097565cce140dcccd3427234582ef00208da
expected_output_aggregate: sha256:7a860b034edc15774ad59f2a678d2ca081003482da614f6bd313bba4edd4324d
expected_output_file_count: 36
accepted_m0_aggregate: sha256:9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a
status_path: docs/reviews/2026-08-20-m0-flight-readiness-exact-byte-review/status.json
verdict_path: docs/reviews/2026-08-20-m0-flight-readiness-exact-byte-review/review.md
---

# Independent Exact-Byte Gate for the M0 Review Surface

## Outcome and time discipline

Perform one bounded, independent acceptance review of the current uncommitted
M0 Flight Readiness review-surface bytes. This is the release gate for the
Owner's first transferable GitHub version. Be adversarial where the evidence is
material, but do not redesign, refactor, expand scope, or repeat already-passed
work without a concrete falsifier. Finish with either `ACCEPT_EXACT_BYTES` or a
specific fail-closed verdict and the smallest evidence-backed correction list.

Do not spawn subagents or workflows. Do not wait for another session. Do not
commit, push, merge, open a PR, deploy, publish, or access production.

## Independence and write boundary

You did not author the implementation or its continuation. Treat every prior
claim as untrusted until reproduced. You MUST NOT modify anything under:

- `prototypes/m0-flight-readiness-review/**`
- `docs/reviews/2026-08-18-m0-flight-readiness-review-surface/**`
- `.agents/skills/kdd_data_agent/**`
- the frozen architecture, packet, plan, sequencing, migration, or handoff files

You may write only these two new English files:

- `docs/reviews/2026-08-20-m0-flight-readiness-exact-byte-review/review.md`
- `docs/reviews/2026-08-20-m0-flight-readiness-exact-byte-review/status.json`

The present `handoff.md` is orchestrator-owned and MUST remain unchanged.

## Fail-closed byte gate

Before interpreting behavior, independently recompute the output aggregate
using the documented recipe and independently inspect the manifest. It MUST be
exactly:

- 36 files
- `sha256:7a860b034edc15774ad59f2a678d2ca081003482da614f6bd313bba4edd4324d`

Also recompute the accepted 59-file M0 package aggregate. It MUST be exactly:

- 59 files
- `sha256:9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a`

If either binding differs, stop immediately with `BLOCKED_BYTE_DRIFT`; do not
transfer any verdict from older bytes.

Read completely:

- `docs/reviews/2026-08-18-m0-flight-readiness-review-surface/evidence-receipt.md`
- `docs/reviews/2026-08-18-m0-flight-readiness-review-surface/status.json`
- `docs/reviews/2026-08-18-m0-flight-readiness-review-surface/completion-ledger.md`
- `docs/reviews/2026-08-18-m0-flight-readiness-review-surface/build-test.json`
- `docs/reviews/2026-08-18-m0-flight-readiness-review-surface/opus5-continuation-handoff.md`
- `docs/handoffs/2026-08-18-opus5-m0-review-surface-execution.md`

## Minimum independent checks

Run and independently assess, rather than merely quote, enough evidence to
accept or reject the exact bytes:

1. Reproduce the 36-file output aggregate and 59-file accepted-M0 aggregate.
2. Verify every frozen input binding recorded in the receipt.
3. Run the full build-test battery or its recorded underlying commands; no
   unexplained skipped checks are allowed.
4. Confirm deterministic fixture/render input across at least three distinct
   `PYTHONHASHSEED` values and from repository-root plus unrelated cwd.
5. Inspect all twelve PNG captures directly for real rendered content and the
   required desktop/narrow states; do not accept file-existence alone.
6. Verify keyboard access to the exact source-read and D4/D6 receipts within at
   most two read-only interactions.
7. Verify read-only behavior, fail-closed invalid/absent input handling,
   capability and authority boundaries, and absence of network/storage/write or
   automation-consumable apply surfaces.
8. Check that the durable claims do not overstate the evidence. The strongest
   permitted result is a local fixture-only, read-only, pre-P3 prototype. It is
   not production authorization, real-Flight proof, P3 acceptance, M1/M2,
   deployment, publication, or Committee Acceptance.
9. Confirm no reviewed-root byte changed during the review by recomputing both
   aggregates after all checks and immediately before writing the verdict.

Do not reject solely for already-disclosed external gaps such as unavailable
screen-reader/cross-browser/live-reviewer evidence unless the artifact falsely
claims those checks passed or the gap invalidates the local fixture-only result.

## Required outputs

`review.md` MUST contain:

- reviewer independence statement;
- exact reviewed branch, HEAD, output digest/file count, accepted-M0 digest/file
  count, and reviewed time;
- commands/checks executed with outcomes;
- findings separated into blocking, non-blocking, and accepted disclosed gaps;
- proof boundary;
- one final verdict token: `ACCEPT_EXACT_BYTES`, `REJECT_EXACT_BYTES`, or
  `BLOCKED_BYTE_DRIFT`.

`status.json` MUST be valid JSON and include at least:

- `status`: `done` or `blocked`;
- `verdict`: the exact token above;
- `reviewed_output_digest` and `reviewed_output_file_count`;
- `reviewed_m0_digest` and `reviewed_m0_file_count`;
- `branch`, `head`, `dirty_paths_before`, `dirty_paths_after`;
- `tests_run`, `tests_passed`, `tests_failed`, `tests_skipped`;
- `blocking_findings`, `non_blocking_findings`, `accepted_disclosed_gaps`;
- `reviewed_roots_modified_by_reviewer`: false;
- `production_authorized`: false;
- `p3_accepted`: false;
- `committee_accepted`: false.

If accepted, state explicitly that Commit B may contain the exact reviewed
implementation/evidence bytes and Commit C may contain this independent review
record. Do not create either commit yourself.
