# Handoff prompt for the Codex session

Copy everything below the line into the Codex session.

---

An independent Claude Opus 5 review of the greenfield KDD Data Agent package has completed.
Its verdict is **REVISE BEFORE IMPLEMENTATION PLANNING** (not production GO, not a rejection).
Your job this session is to **triage and respond to it** — not to implement it.

## Where it lives

```
docs/research/kdd-data-agent-workshop/reviews/2026-08-15-opus5-enterprise-plan-review/
  README.md                  <- start here; verdict, status/authority, reading order
  00-final-review.md         <- the review: 14 BLOCKER, 24 MAJOR, 13 MINOR + 10 required sections
  01-evidence-receipts.md    <- every load-bearing claim as a re-runnable read-only command
  agent-reports/*.md         <- 8 review-agent reports plus 1 image-extraction report, verbatim (~140KB)
```

Mirrored at the same relative path in the `cd68` worktree. Both copies are untracked working-tree
files; nothing was committed and no pre-existing file was modified.

## Read in this order

1. `README.md`
2. `00-final-review.md` sections 0 (the reviewer's corrections to itself), 1, and 3
3. `01-evidence-receipts.md`
4. Only then the individual `agent-reports/` for the areas you dispute

## Verify, do not trust

`01-evidence-receipts.md` exists so you can re-run every claim rather than believing prose.
Re-run the greps before accepting any finding. The review states its own limits explicitly:

- post-review correction: the main orchestration task independently verified all eight screenshot SHA-256 values against the enterprise profile; raw image rehash paths/command are no longer available. The final DeepSeek source was verified with `shasum -a 256` as `81feaa5e1c2514732707fa542a283162faafa435611f768e6887c8421bb64f52`;
- award repos, papers, videos, and workshop audio were **not** re-read from source;
- section 0 lists four claims an earlier draft got wrong or overstated. Assume more exist.

Every finding is labeled **[self-declared]** (a gap the package documented itself) or
**[discovered]**. If you think that label is wrong on any finding, say so — mislabeling a
self-declared TODO as a discovery is a real defect in the review, not a quibble.

## What to produce

Write a disposition file at:

```
docs/research/kdd-data-agent-workshop/reviews/2026-08-15-opus5-enterprise-plan-review/03-codex-disposition.md
```

One row per **BLOCKER and MAJOR** (38 findings: B1-B14, M1-M24), each with exactly one of:

- **ACCEPT** — the finding stands; state the smallest correction that closes it and which
  document/unit it lands in;
- **DISPUTE** — with a `file:line` or command receipt showing the review is wrong. Do not
  dispute on intent or on "we meant to"; dispute on evidence;
- **DEFER** — with the named gate (P2 / P3 / P4) or milestone it correctly belongs to, and what
  would make it actionable.

Do not silently accept. A blanket "agreed, will fix" row is not a disposition.

## Priority order

Work these first — they change **what gets built**, not just how:

1. **B3 — the reuse contract.** The owner's own flowchart marks `Ranking-diagnostics RCA` and
   `Verdict framework` as REUSED from `search-relevance-experiment-analysis`, and says the
   basis-table routing is already verified "in the sma playbook — reuse that routing".
   `implementation-sequencing.md:151` currently *forbids* touching `.agents/skills/sma/`.
   You cannot resolve this yourself — it needs an owner ruling. Write the options, not a decision.
2. **B2 — milestone re-cut and sizing.** The owner requested `Build + staffing` for **M0 only**;
   M1/M2 are `Direction only`; M3+ is `NOT REQUESTED`. The package has zero sizing content
   anywhere. Propose the M0-first re-slice and attach headcount/duration.
3. **B13 — reviewability.** The two newest documents have zero inbound references, and the
   trajectory increment (sections 16.1-16.5) exists **only** in the `cd68` worktree. This is the
   cheapest BLOCKER to close: move it into the main tree and index both documents.
4. **B1 — symbol/line attribution.** `code` candidates require file/symbol/line and no port,
   entity, receipt, or validator derives it. Either specify the attribution port or make G2
   return `inconclusive` at file-level identity.
5. **B11 — no fixtures exist on disk**, and no difficulty floor, trivial-baseline arm, or
   fixture-author independence rule.
6. **B4 / B5 — Trace ontology and packet immutability.** Trace is defined as a projection in the
   spec and as an independently collected store in the increment, with no precedence rule; and
   the digested packet manifest binds an explicitly unfrozen, deletable store.
7. **B6 / B7 / B8 / B9 — security.** These gate P2: redaction has no failure behavior, read-only
   has no enforcement point, the read identity model is undecided, and append-only immutability
   versus erasure obligations is never acknowledged.

## Owner decisions — do not decide these yourself

Section 6 of the review lists eleven. Route them to the owner with options and a recommendation;
do not encode a choice into a contract. In particular: whether M0 is slice 1; whether Scenario A
covers all four outcome classes or misses only; whether M2 is in the MVP; whether to lift the
`.agents/skills/sma/` prohibition; whether a central Trace store over every engineer's IDE is
acceptable; and the retention/erasure posture for packets containing document text.

## Where pushback is most likely to be justified

Stated so you argue with the review rather than around it:

- **Verdict.** The review's own fresh-context verifier recorded a counterargument: the profile's
  section 14 *already is* the revision, so ACCEPT-with-conditions is defensible. The review holds
  REVISE because the reconciliation is unmerged and partly invisible to the reviewed tree. If you
  think that's wrong, argue it in the disposition.
- **The `[discovered]` labels**, per above.
- **Domain findings** (B10, M9-M13, M24) come from one specialist lens each. Same-model agreement
  was explicitly **not** counted as corroboration; only four findings have genuine cross-lens
  confirmation (named in section 10). Single-lens findings are the ones most likely to be wrong.

## Boundaries for this session

- **No implementation.** This is triage and response only. `ce-work` remains unauthorized.
- **No commit, push, PR, deploy, rollback, or publication** without explicit owner approval.
- **No production access, credentials, replay, or shadow reads.**
- **Preserve the dirty worktree.** Do not `git checkout`/`reset` across untracked work.
- **Do not edit** `.agents/skills/sma/` or `.agents/skills/sma_rewrite/evals/`.
- **Do not edit the review bundle.** It is a dated finding record. Respond in `03-codex-disposition.md`.
- The review is a **finding, not authority**. Owner decisions and the closed policy contract
  outrank it. Where it disagrees with a canonical document, that is a question for the owner.

## Definition of done for this session

1. `03-codex-disposition.md` exists with a row for all 38 BLOCKER/MAJOR findings (B1-B14, M1-M24).
2. Every DISPUTE carries a `file:line` or command receipt.
3. Owner decisions are separated from engineering fixes, with options and a recommendation each.
4. A proposed M0-first re-slice with entry criteria, exit evidence, named tests, and sizing.
5. A one-line summary of which findings, if any, change the canonical documents — and which of
   those need an owner gate before the change is made.
