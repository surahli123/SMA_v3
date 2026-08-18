# SMA v3 Private Repository Publication Manifest

Target repository: `surahli123/SMA_v3`

Target visibility: private

Target branch: `main`

## Include Set

- `README.md`, `PROVENANCE.md`, `COMPLETION_LEDGER.md`, and this manifest.
- `.agents/skills/kdd_data_agent/` without cache, bytecode, or runtime state.
- `docs/research/kdd-data-agent-workshop/` without `.omc` runtime state.
- `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md`.
- `docs/adr/0004-*.md` through `docs/adr/0008-*.md`.
- `sources/papers/` with the two provenance-bound PDFs.

## Exclude Set

- All legacy SMA application and protected SMA skill/evaluation paths.
- Private raw audio, video, screenshots, ASR, HEIC enterprise screenshots, production/company data, credentials, tokens, and cookies.
- Runtime state, caches, bytecode, `.workflow`, `.omc`, `.gstack`, root scratch, and unrelated dirty content.
- External winner repositories and any third-party source code not covered by a separate vendoring decision.

## Required Checks Before Push

1. Reproduce accepted package aggregate `9eea3014…b19a`.
2. Verify the Round 5 verdict and frozen/supporting hashes.
3. Parse JSON, check Markdown links/fences, and validate JavaScript syntax.
4. Run secret, private-media, cache/runtime, oversized-file, and protected-path scans.
5. Run the M0 suite from the exported repository and confirm deterministic replay.
6. Verify authenticated GitHub owner and exact private target before commit and push.
7. Inspect the complete initial commit and verify remote `main` after push.

This publication transfers research and local fixture-backed implementation evidence. It grants no production access, deployment authority, M1/M2 implementation authority, public-release authority, or Committee Acceptance.
