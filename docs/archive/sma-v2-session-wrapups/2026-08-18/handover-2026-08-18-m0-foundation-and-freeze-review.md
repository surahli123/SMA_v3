# Handover — M0 Foundation + Freeze Review (session `b9d777ba`)

**Project:** SMA_v2 — `/Users/surahli/Documents/projects/SMA_v2`
**Branch:** `codex/kdd-data-agent-practices-research`
**HEAD at handover:** `13e62af docs(kdd): preserve enterprise data-agent research`
**Suite:** `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider .agents/skills/kdd_data_agent/tests -q` → 370 passed

## Last session in three sentences

Built Phase A of the M0 pre-alignment foundation (`.agents/skills/kdd_data_agent/`) and
stopped at the alignment gate rather than inventing unfrozen product semantics. Ran two
dynamic workflows (97 agents) reviewing that package against the real champion and
fourth-place source cloned at their audited SHAs, not just the local audit prose. Then
performed the independent adversarial review of Codex's M0 freeze candidate on Q1-Q10 and
Q13, handing over eight findings that Codex applied 8/8.

## Current state

**Working.** The package is committed and green at 370 tests. Codex has substantially
extended Phase A beyond what this session wrote (immutability helper, expanded capability
constants, 46 planted-violation tests). The freeze candidate has been revised in response
to the review: `post_analysis_eligibility` is now a render-time projection, the materiality
rule is split into two labelled rules with `unknown` stored rather than rewritten, the
pre-runtime reopen trigger is bound to the preregistered runtime end, and the CE plan's
`VAL-M0-002` disjunction is discharged.

**Blocked.** The freeze itself. Codex's disposition records an evidence conflict that
prevents a freeze claim, and the packet digest has moved from `40c7234f…79396` (what this
session reviewed) to `82747da9…f07b19`, so the existing `ACCEPT_WITH_CHANGES` signoff row
is bound to a superseded digest.

## Next steps, in priority order

1. **Route Q11/Q12 to a third reviewer.** Phase A verification is unowned. This session
   wrote the implementation and its receipt; Codex wrote the continuation. Neither is
   independent. §6 of `m0-freeze-opus5-adversarial-review.md` lists what that reviewer
   should start from so they do not rediscover it.
2. **Fresh signoff against the current packet digest.** Recompute, then have each party
   record a row against that digest. A verdict recorded against another digest does not
   count, by the packet's own rule.
3. **Resolve the evidence conflict** named in `m0-freeze-codex-disposition.md` §"Evidence
   conflict that prevents a freeze claim".
4. **Complete the 30-finding reconciliation** against
   `reviews/2026-08-15-opus5-enterprise-plan-review/00-final-review.md`. Currently PARTIAL
   — verified only transitively through C1-C9 propagation.
5. **Re-check the four findings** that were live against the package at last check
   (materiality gate, `CoverageGapKind` breadth, sentinel decode asymmetry, float
   deviation) — Codex may have closed some since.

## Key context and gotchas

- **Authority order matters and has changed.** `owner-alignment-record.md` (O1-O6) is
  authority #1 and supersedes older planning statements — notably, M1/M2 are **no longer
  direction-only**, and M0 **may** carry an unapplied candidate diff limited to
  validity/instrumentation/data-quality. Anything asserting otherwise is stale.
- **The real upstream source is obtainable.** The three reverse audits cite GitHub fixed
  SHAs; a shallow fetch at those SHAs takes under a minute and the audits are wrong in
  places — one grades a trace subsystem "Strong; directly implemented" whose real
  emission path has zero callers. Prefer source over audit and report disagreements.
- **`KDD_Competition` at HEAD `7270e3b`** is an authorized read-only local source, dirty,
  never to be modified. The two `KDD_Competition*` trees are our own older work, not the
  reference teams'.
- **The multi-agent review's own numbers understate what is unchecked.** Its filter
  counted findings whose verifiers died on the session limit as "killed"; only 5 of 42
  were adversarially verified. The report discloses this — read the disclosure before
  citing its confirmed/killed split.
- **Parallel sessions are active on this branch.** Check `git status` before editing;
  the dirty files at handover belong to the Fable 5 architecture-finalization work.
- **Vault scripts resolve paths relative to cwd.** `scripts/inbox-append.py` invoked by
  absolute path from this checkout creates a stray `SMA_v2/inbox/` and leaves the vault
  untouched, while reporting success. Run it with the vault as cwd and verify by grepping
  the vault file.

## Read first

```
docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/
  owner-alignment-record.md               ← authority #1, read before anything else
  m0-m2-build-alignment-packet.md         ← the freeze candidate
  m0-freeze-codex-disposition.md          ← what Codex applied and what still blocks
  m0-freeze-opus5-adversarial-review.md   ← this session's review, §6 for Q11/Q12
  m0-multiagent-review-consolidated.md    ← 42 findings + its own method defect
docs/research/kdd-data-agent-workshop/wayfinder/
  freeze-canonical-domain-policy-contracts.md   ← P1, closed and binding
.agents/skills/kdd_data_agent/
  README.md, ENGINEERING_DECISIONS.md, TOOLCHAIN_RECEIPT.md, alignment/seams.py
```
