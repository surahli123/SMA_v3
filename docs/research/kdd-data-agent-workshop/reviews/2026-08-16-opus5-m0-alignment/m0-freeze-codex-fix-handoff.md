---
handoff_id: m0-freeze-codex-fix-20260818
from: Claude Code Opus 5, session b9d777ba-71e9-4a04-b474-f49c188419cc
to: Codex continuation session
created_at: 2026-08-18T02:30:14Z
reviewed_packet_sha256: 40c7234f3c0d85f18ebfba656e7aec2ab5ab71b86451a077ecad340eac779396
verdict: ACCEPT_WITH_CHANGES
blocks: the freeze record
---

# Handoff: Apply the Opus 5 Freeze-Review Findings, Then Freeze

Full review: `m0-freeze-opus5-adversarial-review.md`
Status JSON: `m0-freeze-opus5-review-status.json`

The packet is close. Zero blockers. Nine C-edits landed, all eight adjudications are
implemented, and the Q10 budget-drift fix is real and verified. Eight edits stand between
this revision and a defensible freeze, and none of them needs an Owner decision.

**Do not freeze against `40c7234f…79396`.** Apply the edits, produce a new digest, and
write the freeze record against that.

## Scope note you need before you read the findings

This review answers Q1–Q10 and Q13 only. **Q11 and Q12 were declined for conflict of
interest**: my session authored the original Phase A package and the self-authored receipt
that Q12 explicitly says not to trust. Phase A verification must be routed to a third
session that wrote neither the implementation nor this review. Please do not treat the
freeze as fully reviewed until that happens — the review's §6 lists what that reviewer
should start from so they do not rediscover it.

## Edits required in `m0-m2-build-alignment-packet.md`

### 1. §5.3 — stop calling the readiness fields orthogonal (MAJOR-1)

`analysis_use` fully determines `post_analysis_eligibility`. Three legal rows out of six,
and eligibility carries zero independent information. Two separately stored fields that
must always agree, with no stated precedence when they do not.

Pick one:

- **(a) preferred** — declare `post_analysis_eligibility` a derived projection of
  `analysis_use`, computed at render, never independently settable; or
- **(b)** keep both stored and add: *a packet whose pair is not one of the three legal
  rows is invalid and must be rejected, not interpreted.*

Also drop or reword "two orthogonal fields" — the pair is a single three-state contract
with a convenience projection, which is fine, but calling it orthogonal invites an
implementer to vary the axes independently.

### 2. §5.2 closing paragraph — split the two enums (MAJOR-3)

The paragraph carries the check-outcome enum and the materiality enum together, and ends
with "`NOT_APPLICABLE` requires a versioned applicability rule and rationale; otherwise it
is `UNKNOWN`." "It" reads as either the check outcome or the materiality; the two readings
write different fields.

Split into two labelled rules, and state explicitly whether an unclassified result
**stores** `materiality = unknown` while the **applied ceiling** is material, or is
rewritten to `material`. P1's style keeps the record and applies the ceiling; rewriting
loses the fact that nobody classified it, which is the reviewable signal.

### 3. §5.4 — bind runtime completion to recomputation (MAJOR-4)

A `blocked + directional_only` packet is correct only until the preregistered runtime
completes, then it is stale but still syntactically valid and citable as the Flight's read.

Add: a pre-runtime packet's reopen condition names the preregistered runtime end as its
trigger, and its `expiry` does not exceed that time.

### 4. §11 `VAL-REM-002` — restore `validity` (MINOR-2)

The row says "instrumentation/data-quality"; your own §5.4, O3, and CE plan:133 all say
"validity, instrumentation, or data-quality". The row silently narrows what O3 permits.

### 5. §13 — name what else the freeze binds (MINOR-4)

M18, M19, and M20 are implemented in `final-architecture-spec.md` (:690, :691, :648) and
the CE plan, not in the packet. The freeze record binds the packet digest, so those rules
are not transitively bound and can drift without tripping packet change control. Name the
controlling spec revision and digest that the freeze also binds.

### 6. §5.3 or §11.2 — one sentence on triage (MINOR-3)

`blocked + directional_only` needs *time*; `blocked + not_permitted` needs *work*. A
surface filtering on `post_analysis_eligibility == blocked` cannot separate them. State
that triage keys on `analysis_use` and `next_safe_action.kind`, never on eligibility alone.

## Edits required in `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md`

### 7. Line 129, `VAL-M0-002` — discharge the disjunction (MAJOR-2)

Current: "any material SRM, CUPED, unit, source, ACL, freshness, runtime, or comparable
validity failure **blocks or makes the Flight directional** and produces no M1/M2 output."

The "or" is never discharged — the CE plan does not say which input maps to which state,
while the packet does. This is C1's defect in a new form: one ID, two precisions. It also
trips your own §12 stop condition 9 (two competent implementers cannot map a requirement
to the same meaning).

Replace with the packet's exact mapping: runtime insufficiency with no other material
blocker is exactly `blocked + directional_only`; a material validity, source, ACL,
isolation, or evidence failure is `blocked + not_permitted`.

### 8. Line 132, `VAL-UNIT-001` — restore the outcome binding (MINOR-1)

The CE plan stops at "fails materially" and drops the packet's
"and the packet is `blocked + not_permitted`".

## What I verified, so you do not redo it

- The phrase "authorized 2026-08-16 build session" is gone corpus-wide; §9.1's replacement
  binds exactly to `m0-codex-continuation-20260817`, one non-recurring task, its enumerated
  surface, expiry after one run, and Owner + main-orchestrator halt authority, with the
  four-to-six week envelope kept separate. **Q10 passes as written.**
- All 22 shared `VAL-*` identifiers were extracted and diffed across both documents. 19 are
  consistent; the three exceptions are edits 4, 7, and 8 above. The packet's four
  `VAL-M1-*`/`VAL-M2-*` are packet-only, consistent with "this section extends that
  registry". **C1's namespace unification is real.**
- All eight adjudications verified present: B2 (O5 + §5/§10/§13), B3 (§8 + O6), B11
  (§11.1), M1 (spec:193, :422), M3 (§5.4 + `VAL-REM-002`), M18 (spec:690), M19 (spec:691),
  M20 (spec:648).
- C3's four owner-named checks map to checks 11, 13, 8, and 15.
- "M1 and M2 receive no implementation work" no longer appears in
  `implementation-sequencing.md` or the CE plan, and all three controlling documents
  reference the Owner record.

**A correction against myself, so you can trust the rest:** my first pass used
`grep -i "IDE"` and matched `wIDEn`/`provIDEs`, which led me to score M19 and M20 as
MISSING. A word-boundary re-check found both implemented verbatim. The finding was
withdrawn before it reached the report. Flagging it because it is the failure mode most
likely to produce a false finding against your work, and if you see me assert an absence
elsewhere, it is fair to ask how I searched.

## Not verified — do not report as cleared

The full 30-finding list in `00-final-review.md` was **not** re-read and re-derived. I
verified those findings transitively through C1–C9 propagation and spot checks only. The
review's 30/8 reconciliation is marked PARTIAL for exactly this reason.

## One item that touches Phase A and belongs to you

The Phase A receipt (`m0-prealignment-foundation-receipt.md`) justifies its
no-retained-body invariant by citing the alignment packet draft and the CE plan as *two
independent agreeing sources*, using `M0-SEC-001` and `M0-READ-001` — the exact identifiers
C1 flagged as colliding. The invariant fails closed and is almost certainly correct; the
**argument** is circular. Now that the registry is unified under `VAL-*`, restate it
against the current non-colliding text. I wrote that receipt, which is why I am handing
this to you rather than fixing it myself.

## Requested response

Apply or reject each of the eight edits with a reason, produce the new packet digest, and
record your verdict row against **that** digest, not against `40c7234f…79396`. If you
reject any finding, say which and why — I would rather be shown wrong than have a bad
finding applied silently.

Then write the freeze record. I did not freeze anything, did not touch
`.agents/skills/kdd_data_agent/` or any canonical document, and made no commit. The
worktree is unchanged apart from the three review outputs in this directory.
