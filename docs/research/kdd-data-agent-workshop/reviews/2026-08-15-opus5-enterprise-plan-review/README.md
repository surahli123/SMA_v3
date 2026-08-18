# Opus 5 Enterprise Plan Review — 2026-08-15

**Verdict: `REVISE BEFORE IMPLEMENTATION PLANNING`** — not a production GO decision, and not a
rejection of the work.

Independent review of the greenfield KDD-informed Data Agent package against the **actual
enterprise Scenario A** defined by eight owner screenshots of the "Search Experiment Deep-Dive
Analyzer" roadmap and tech spec.

## Status and authority

| | |
| --- | --- |
| Status | **Review finding.** Supporting artifact; not canonical product authority. |
| Authority | Does **not** amend the canonical package, close P2/P3/P4, or authorize implementation. Owner decisions and the closed policy contract outrank it. |
| Scope | Read-only review. No repo file outside this directory was created, modified, or deleted. No production, credential, or network access was used. |
| Review object | The working-tree package on `codex/kdd-data-agent-practices-research` @ `28cbbda`, plus the newer `deepseek-harness-practices.md` in the `cd68` Codex worktree. |

Where this review disagrees with a canonical document, the disagreement is **a finding for the
owner to rule on**, not a change.

## Reading order

1. **[`00-final-review.md`](00-final-review.md)** — the review. Verdict, five material reasons,
   ~50 findings by severity with anchors and corrections, traceability table,
   Adopt/Adapt/Reject corrections, owner decisions, review-pass checklist, recommended first
   slice, Scenario B deferral, independence statement. **Start here.**
2. **[`01-evidence-receipts.md`](01-evidence-receipts.md)** — every load-bearing claim as a
   re-runnable read-only command with its recorded output. Use this to reproduce or refute any
   finding rather than trusting the prose.
3. **[`agent-reports/`](agent-reports/)** — reports from 8 review agents plus 1 image-extraction agent, verbatim.
4. **[`02-codex-handoff-prompt.md`](02-codex-handoff-prompt.md)** — the triage brief handed to
   the Codex session: reading order, priority ordering, what to produce, owner-decision
   boundaries, and where pushback on this review is most likely to be justified. Codex's
   response is recorded in [`03-codex-disposition.md`](03-codex-disposition.md).

Finding counts: **14 BLOCKER, 24 MAJOR, 13 MINOR.**

## The five headline findings

1. **Scope inversion.** The owner requested `Build + staffing` for **M0 Flight Readiness only**
   (`CURRENT TARGET`); M1/M2 are `Direction only`, M3+ is `NOT REQUESTED`. The package's
   smallest fundable increment is D0 -> U8, whose first output is a full Scenario A packet.
   M0 vocabulary count in the canonical three documents: **0, 0, 0**.
2. **The package cannot price the ask.** Zero sizing, duration, or headcount content anywhere,
   against an approval request that is literally "Build + staffing".
3. **The exact-target chain has an unbridgeable hop.** `code` candidates require file, symbol,
   and line; **no port, entity, receipt, or validator derives symbol/line from a deployed
   artifact.** In practice a model reading a diff fills it — the proximity tie the docs forbid.
4. **The evaluation gate has no power layer.** No fixtures exist on disk; no difficulty target,
   no trivial-baseline arm, no fixture-author independence rule.
5. **The reuse premise is inverted.** Two of five pipeline stages are marked **REUSED** in the
   owner's flowchart from `search-relevance-experiment-analysis`; that name appears nowhere in
   `docs/`, and sequencing *forbids* touching the referenced assets.

## What the package gets right

Recorded so a re-slicing does not discard it: the refusal to fake closure; orthogonal Cause
Verdict / Recommendation Readiness axes with a legality matrix; the G0-G7 ladder and its G4
execution-versus-result split; the hard invalid-experiment branch; ranking as filters and
ceilings rather than offsettable weights; first-class abstention with no specified pressure
that can force `confirmed`; P4's non-compensable vetoes and stability stop-rule; and the
`EvidenceAdmission` type boundary. Details in section 3 of the review.

## Evidence-class convention

`screenshot observed` · `repo observed` · `command receipt` · `owner decision` ·
`reviewer inference` — plus every finding labeled **[self-declared]** (a gap the package
authors documented themselves) or **[discovered]** (found by this review). That split is load
bearing: this package documents its own TODOs unusually well, and reporting those as
discoveries would misrepresent it.

## Known limits of this review

- **Post-review receipt correction:** the main orchestration task independently verified all eight screenshot SHA-256 values against the enterprise profile; raw image paths and the rehash command are no longer available here. The final DeepSeek source was verified with `shasum -a 256` as `81feaa5e1c2514732707fa542a283162faafa435611f768e6887c8421bb64f52`.
- Award repos, papers, videos, and workshop audio were **not** re-read from source; only the
  package's representation of them was assessed.
- Domain findings outside the mechanical-consistency lane come from one lead reviewer plus one
  specialist agent each. Same-model agreement is **not** counted as independent corroboration;
  the four genuine cross-lens corroborations are named in section 10 of the review.
- A first draft of this review contained four overstated or incorrect claims, corrected in
  section 0 of `00-final-review.md`. The corrections are kept in the record deliberately.

## Suggested follow-up for the owner

The canonical reconciliation is applied locally and links this bundle from `deliverable-index.md` and the package `README.md`. On 2026-08-16 the owner closed B2 by selecting M0 Flight Readiness as the first build/funding slice and main deliverable; M1/M2 remain direction-only. The review remains supporting evidence, not product authority, and this ruling does not authorize implementation or close P2/P3/P4.
