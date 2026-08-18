# Share-Safe GitHub Publication Manifest

- Status: approved scope; publication checks passed at `2026-08-18T04:59:13-07:00`; bounded commit and push pending at the recorded check snapshot.
- Target repository: `surahli123/SMA_v2` (private).
- Target branch: `codex/kdd-data-agent-practices-research`.
- Publication authority: Owner-authorized commit and push after exact-byte independent local M0 acceptance and all checks in this manifest.
- Verification receipt: `publication-verification-receipt.md`.

## Intended Include Set

Only these repository-relative paths are candidates for the research handoff commit:

- `docs/research/kdd-data-agent-workshop/`
- `.agents/skills/kdd_data_agent/`
- `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md`
- `docs/adr/0004-start-m0-with-one-decision-metric-without-limiting-the-target.md`
- `docs/adr/0005-make-invalid-experiment-diffs-a-gated-m0-capability.md`
- `docs/adr/0006-separate-production-experiment-ownership-consultation-and-approval.md`
- `docs/adr/0007-run-m0-through-m2-as-one-active-time-bounded-validation-slice.md`
- `docs/adr/0008-treat-old-sma-domain-assets-as-candidates-not-production-authority.md`
- `docs/handover-2026-08-15-kdd-enterprise-plan-review.md`
- `docs/session-logs/2026-08-15-kdd-enterprise-plan-review-wrapup.md`
- `BACKLOG.md`
- `CHANGELOG.md`
- `CONTEXT.md`

The research directory includes the original KDD workshop synthesis, source/provenance manifest, audio/screenshot alignment receipts, award-work and repository audits, external-practice research, owner decision packet, canonical architecture specification, implementation sequence, evaluation plan, Wayfinder artifacts, Evidence Room prototype, Fable/Opus/Codex review history, complete grill-session records, exact freeze and correction receipts, and cloud/internal-agent handoffs. The implementation directory contains the independently accepted fixture-only M0 package and tests.

## Explicit Exclude Set

Do not stage, commit, or push any of the following as part of this package:

- raw private `.m4a`, `.wav`, `.mp4`, or `.mov` source media;
- the 73 raw workshop screenshots or other private attachments;
- raw ASR output, credentials, secrets, cookies, tokens, production data, or company data;
- machine-local paths, temporary item-provider paths, local cache paths, or local-only manifests, except immutable historical review receipts explicitly classified as non-executable provenance;
- `.omc/`, `.gstack/`, `.workflow/`, root `critique.json`, root `designs/`, or `.agents/skills/sma_rewrite/workspace/`;
- `.agents/skills/sma/` or `.agents/skills/sma_rewrite/evals/`;
- unrelated user changes or generated runtime caches.

The generated PNG files inside the Evidence Room prototype are synthetic design references and browser-review artifacts, not raw workshop screenshots. They may be included with the prototype bundle.

Public paper PDFs or source files may be included when the source URL, version, and redistribution basis are recorded. No PDF is present in the current include set.

### Immutable historical-path exception

This is a private-repository handoff, not a public release. Some exact-byte historical review receipts contain inert local checkout or disposable-directory path literals. At least three are hash-bound by the canonical freeze record and cannot be redacted without falsifying that record. Preserve such receipts byte-for-byte, classify the literals as non-executable provenance, and exclude them from any later public export unless a separately labeled redacted copy is produced. This exception never permits credentials, tokens, production data, or private attachment paths.

## Pre-Publication Checks

Immediately before staging:

1. Verify `origin` resolves exactly to `surahli123/SMA_v2` and that the authenticated account may write to it.
2. Verify the current branch is `codex/kdd-data-agent-practices-research`, not `main`.
3. Re-read `git status --short` and preserve all paths outside the include set.
4. Verify the Round 5 independent verdict, exact aggregate, and four frozen/supporting hashes again; preserve rejected/interrupted Round 1-4 evidence as historical evidence.
5. Re-run local Markdown links, JSON parsing, JavaScript syntax, private-path classification (including the immutable historical-path allowlist), secret, raw/private-media, protected-path, and cache/runtime-state checks. Run the default Git whitespace check on current implementation, plan, ADR, and root-navigation paths; separately classify intentional Markdown hard breaks and exact-byte historical patch/receipt whitespace instead of rewriting hash-bound evidence.
6. Confirm every durable artifact is English except the explicitly requested Chinese six-question collaboration HTML; translate remaining option labels elsewhere.
7. Stage only the intended include paths above and inspect `git diff --cached --stat` plus the complete staged diff.
8. Commit only after the staged diff matches this manifest. Push only after commit succeeds and the target remote/branch is re-verified.

## Publication-Check Snapshot

At `2026-08-18T04:59:13-07:00`:

- `origin` is `https://github.com/surahli123/SMA_v2.git`.
- GitHub authentication is the `surahli123` account, and GitHub reports `surahli123/SMA_v2` as a private repository with default branch `main`.
- The local feature branch is `codex/kdd-data-agent-practices-research`.
- No remote branch with that feature-branch name was observed.
- The Round 5 aggregate and all four frozen/supporting digests reproduce exactly.
- All mechanical, content-safety, deterministic-replay, and three-directory test checks in `publication-verification-receipt.md` pass.
- No raw source media, private attachment, credential, production data, or company data appears in the intended include set.
- No publication action had occurred at this check snapshot.

This is a pre-Git-action receipt, not a claim about later branch state. Repository, authentication, branch, staged paths, and reviewed digests must be revalidated immediately before commit and push; subsequent publication state belongs to Git history.
