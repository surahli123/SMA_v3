# SMA v3 Export Provenance

Exported: 2026-08-18 (America/Los_Angeles)

Target: private repository `surahli123/SMA_v3`

Source checkout: `/Users/surahli/Documents/projects/SMA_v2`

Source branch observed at export: `codex/kdd-data-agent-practices-research`

This export creates a new initiative-only repository. It does not preserve or extend the SMA v2 Git history and does not claim that the legacy SMA implementation is part of the target architecture.

## Included

- Full `docs/research/kdd-data-agent-workshop/` tree, excluding runtime `.omc` state.
- `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md`.
- ADRs 0004–0008 covering the owner-aligned M0–M2 decisions.
- `.agents/skills/kdd_data_agent/`, excluding caches, bytecode, and runtime state.
- PiTrace / Team 1286 report and Cordiverse paper, with hashes and source records.

## Excluded

- Legacy SMA application code, `.agents/skills/sma/`, and `.agents/skills/sma_rewrite/evals/`.
- `.omc/`, `.workflow/`, `.gstack/`, caches, bytecode, and transient session state.
- Credentials, tokens, `.env` files, cookies, production data, and company data.
- Private workshop audio/video, raw ASR, workshop screenshots, and the enterprise HEIC screenshot folder.
- Root `critique.json`, unrelated `designs/`, and unrelated dirty worktree content.
- Personal root-level handover/session-log artifacts; the comprehensive, speaker-labelled grill records under the research tree are retained instead.
- External winner repositories; the research cites audited fixed commits instead of vendoring source without a specific redistribution decision.

## Accepted Evidence Binding

| Evidence | Binding |
| --- | --- |
| Local M0 package | 59-file aggregate `sha256:9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a` |
| Independent verdict | `ACCEPT_LOCAL_M0_EVIDENCE` |
| Frozen M0 packet | `sha256:82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` |
| Frozen architecture | `sha256:9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` |
| CE plan | `sha256:2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` |
| Sequencing plan | `sha256:8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` |

The accepted local M0 verdict does not authenticate production sources, authorize production reads, readjudicate Phase A, close P2/P3/P4, complete M1/M2, authorize deployment/publication, or establish Committee Acceptance.

## Fable 5 Architecture Custody

The architecture finalization draft is retained with verdict `ALIGNED_WITH_GAPS`. The alignment review identifies stale draft state, a Coverage Gap registry mismatch, a `VAL-*` ownership conflict, terminology drift, and proposed-but-unfrozen extensions. The draft must be read together with `deliverable-alignment-review.md`; the freeze record and Round 5 independent review govern current state.
