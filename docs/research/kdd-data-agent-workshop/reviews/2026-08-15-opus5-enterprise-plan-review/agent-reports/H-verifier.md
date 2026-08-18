## C1 — CONFIRMED (verified myself)

Read the session-local attachment `IMG_3689.jpg`. Roadmap table, row "Approval requested": M0 = "Build + staffing", M1 = "Direction only", M2 = "Direction only", M3+ = "No build approval". Row "Status": M0 = `CURRENT TARGET`, M1 = `BLOCKED ON M0`, M2 = `BLOCKED ON M1`, M3+ = `NOT REQUESTED`. M0's question is "Can we trust the setup and primary read?", output "Flight Readiness Report". Claim is accurate; one nit — the status cells for M1/M2 read "BLOCKED ON M0/M1", the "Direction only" text is the approval row.

## C2 — CONFIRMED

`implementation-sequencing.md:171-406`: units D0, U1–U13 build the full engine before any Scenario A decision — U3 evidence registry, U6 ranking, U7 Claim registry, U8 fixture workflow + immutable packet, U11 one production-evidence path, U13 blind adjudication. `final-architecture-spec.md:374-458` (§10) fixes eight stages ending in `recommendation_and_risk` + `not_applied` diff. The mermaid terminus is `M1["Scenario A MVP decision"]` (`implementation-sequencing.md:105`) — one MVP decision, not a milestone ladder. There is no unit whose exit is a Flight Readiness Report alone. M0 as a standalone fundable slice does not exist in the delivery path.

## C3 — CONFIRMED (ran it)

`grep -c -E 'M0|M1|M2|FlightReadinessPacket|MetricMovementPacket|WinLossEvidencePacket|ExperimentReadContract'` → final-architecture-spec.md **0**, eval-acceptance-plan.md **0**, the greenfield plan **0**, implementation-sequencing.md **2**. Both hits are lines 105–106, the mermaid node `M1["Scenario A MVP decision"]` and `M1 --> B0`. Unrelated to milestone M1. Minor correction to the claim's wording: the 2 hits span lines 105 *and* 106, same node. See V4 — this is a self-declared reconciliation item, not a discovered defect.

## C4 — CONFIRMED, and stronger than stated

`grep -c -i` in final-architecture-spec.md: `win/loss` 0, `side-by-side` 0, `SBS` 0, `not_comparable` 0. I also tried the obvious synonyms — `query-level|query evidence|winners|losers|regression example` → **0**. §10.2 contemplates "head/tail query mix" and "query/trace" as *source planes* (`final-architecture-spec.md:398,403`), but no artifact, packet field, or gate produces per-query win/loss comparison. Requirement (e) genuinely has no architectural home.

## C5 — CONFIRMED, all three parts

- `grep -rn "search-relevance-experiment-analysis" docs/` → zero hits.
- IMG_3694: "REUSED" labels on **Ranking-diagnostics RCA** and **Verdict framework**; footer "Ranking RCA and the verdict framework are reused from the existing skill."
- IMG_3695 names it: "the ranking RCA and verdict framework are reused from `search-relevance-experiment-analysis`" and "verified against live Databricks + Statsig in the sma playbook — reuse that routing."
- Assets exist: `.agents/skills/sma/references/metric_registry/` (ai_metrics.md, click_quality.md, search_success_rate.md), `.agents/skills/sma/references/schema_catalog/` (connector_schema.md, search_success_rate_schema.md, templates).
- The plan doesn't just ignore the reuse — it **forbids** it: `implementation-sequencing.md:151` "The future implementation must not edit `.agents/skills/sma/`… These paths are protected references, not migration targets." Both stages are greenfield in U6 (`analysis/ranking.<source>`) and U7.

## C6 — CONFIRMED

`grep -rln "enterprise-experiment-post-analysis-profile" docs/` → exit 1, zero files. `grep -rln "deepseek-harness-practices" docs/` → one file only, the orphan profile itself. Both newest documents are unreferenced by the canonical package. See V4 — the profile declares this itself.

## C7 — CONFIRMED

Codex worktree copy 80,869 bytes; main-tree copy 53,020 bytes. Main tree `:269` = `## 16. Bottom line`. Worktree `:286` = `## 16. Agent-agnostic Trace across Codex, Claude Code, and Cursor`, with 16.1–16.5 at 288/316/341/359/370. The trajectory increment exists only outside the reviewed tree.

## C8 — PARTIALLY CORRECT

First half CONFIRMED: `grep -c -i -E 'cuped|sample.ratio|srm|preregistered|underpowered|co-primary|directional_only' eval-acceptance-plan.md` → **0**.

Second half OVERSTATED. Profile §12's 25 cases and the spec/eval required case classes overlap materially: #18 "commit never deployed" ↔ `final-architecture-spec.md:751` "Current-main versus deployed-SHA conflict"; #21 "exact target unknown, abstention" ↔ "Correct abstention under missing evidence or authority"; #22 timeout/permission ↔ same; #23 adversarial ship request ↔ "unauthorized-access attempts"; #24 deterministic replay ↔ "Invalidation, partial recomputation, packet supersession". What genuinely has no home is the **M0/M2-specific** subset: CUPED mismatch (#10), preregistered runtime (#9), underpowered neutral (#4), co-primary, offsetting effects (#5), denominator drift (#13), `not_comparable` queries (#17). Say "the M0 validity and M2 comparability cases have no home," not "no overlap."

## C9 — CONFIRMED on the arithmetic, PARTIALLY CORRECT on the controls

`eval-acceptance-plan.md:12` "one blind historical experiment miss"; `:207` the same singular; `:15` and `:203` and `:207` all say explicitly it "does not prove general reliability." n=1 → no false-`confirmed` rate is estimable, and the hard veto (`:408` profile / `final-architecture-spec.md:772`) has no denominator. That part stands.

But planted negatives and a baseline **do** exist: `:29` "planted defects", `:33` "planted truth" in the de-identified fixture contract, `:163` "comparison with a human-only baseline", `:213` "human baselines". The claim as written ("is there any trivial-baseline control or planted-negative case?") reads as if none exist; the fixture rung has them. The missing piece is a *trivial baseline* (e.g. "always abstain" or "rank by repo proximity") — I found none.

## C10 — PARTIALLY CORRECT

Second half CONFIRMED: `prototypes/observability-review-surface/build-test.json` shows `project_build`, `project_lint`, `project_tests` all `"skipped"`. But calling the rest "rendering/mechanical" undersells it — it records real browser interactions (`review_to_exact_proof`, `trace_to_evidence`, `claims_node_inspection`, physical keyboard F1–F4), overflow, reduced-motion, and console checks. The file self-labels `"artifact": "PROTOTYPE / THROWAWAY"` and `"remaining_gate": "Owner live acceptance is pending."`

First half REFUTED as stated. P3 has an exit, it just isn't numeric: `implementation-sequencing.md:55` "Accepted review hierarchy and interactions"; `:398` U12 exit "the owner/reviewer can efficiently identify the conclusion, coverage, conflicts, exact target, validator receipt, and next safe check; interaction tests and authorization tests pass"; `:475` "Human decision: owner/reviewers accept or reject the interaction contract. A polished appearance is not acceptance evidence." Accurate version: P3's exit is a named human judgment with no operationalized measure (no time-to-target, no task-success rate), and the spec deliberately forbids claiming review time improved until it closes (`final-architecture-spec.md:669`).

---

## V1 — REVISE is correct

The decisive fact is C1+C2+C5 together, and none of them is a documentation gap. The owner asked to fund **M0 flight readiness** — trust the setup and the primary read — and offered "Build + staffing" for that and nothing else. The canonical package's smallest fundable increment is D0→U8, a contract-first evidence/claim/gate substrate whose first output is a Scenario A packet. The owner's M0 needs WHN reads, `use_cuped` handling, registered-metric checks, and basis-table recomputation; **none of those words appear in the eval plan** (C8) and the packets that would carry them appear nowhere in the canonical three (C3). Meanwhile the owner marked two of five stages "REUSED" from a named existing component, and the sequencing document forbids touching it (C5). A funding decision made on this package would buy a different first deliverable than the one requested, on a different build-vs-reuse premise. That is a revise, not a next step.

Not REJECT: nothing is broken. The domain contract, the gate ladder, and the open-gate discipline are sound and reusable as-is; the fix is a re-slicing plus a reconciliation pass the authors already specified (profile §14).

**Strongest argument against my choice:** the profile itself already *is* the revision — §14 lists all nine reconciliation edits, §13 lists 15 owner decisions that must precede them. One could argue the honest verdict is ACCEPT-with-conditions, since "revise" asks the authors to do exactly what their own newest document says to do next. I hold REVISE because the reconciliation is unmerged, unreferenced, and lives partly in a worktree the reviewed tree can't see (C6, C7) — an approval today would attach to the unreconciled package.

## V2 — What the package gets right, and a critical review must credit

**The refusal to fake closure.** `final-architecture-spec.md:663-673` (§17) names three OPEN GATES with an explicit four-column "work allowed now / prohibited until closure" table, and states "This specification MUST NOT be used to mark any of them resolved." §13.2 refuses to invent ranking weights: fixture ranking runs under a versioned `uncalibrated_fixture` policy that "MUST NOT be presented as production priority"; a pilot needs a sealed, preregistered `pilot_ranking_policy` bound to one rung, and its results "may calibrate but never retroactively change that run's ordering." §19 fixes the ladder's *shape* while leaving every numeric threshold unset until human receipts exist. `implementation-sequencing.md:422`: "No open prerequisite may be closed by repository inference, a model opinion, a prototype screenshot, or a mechanically green test."

Second: §8's orthogonal state design. Cause Verdict and Recommendation Readiness are separate axes with a legality matrix (`:298-303`), so "confirmed cause, unsafe action" and "unconfirmed cause, safe mitigation" are both expressible. That is the exact confusion that sinks real post-analysis tooling, and it is designed out at the contract layer, not patched at the UI.

## V3 — Material defect nobody flagged

**Two.**

**(a) `confirmed` has no legal exit transition.** `final-architecture-spec.md:274-278` lists every legal Cause Verdict edge: `unassessed → suspected|ruled_out|inconclusive`, `suspected → confirmed|ruled_out|inconclusive`, `inconclusive → suspected|ruled_out` (with an explicit "new Evidence or reopened generation required" annotation). There is **no edge out of `confirmed`**. Line 279: "New Evidence creates a new verdict revision; it never overwrites `confirmed` or `ruled_out`." §12's invalidation algorithm (step 5) does create new `VerdictEvent` revisions — but the transition table never says what state a post-`confirmed` revision may take. The system's single hard veto is a **false `confirmed`** (`:772`), and the retraction path for exactly that failure is unspecified. The only implied escape is a new generation (`:333`), which is a heavier and different operation than correcting a verdict. This needs an explicit `confirmed → inconclusive | ruled_out [contradicting validated Evidence]` edge or a stated rule that retraction requires a new generation.

**(b) Zero effort, duration, or staffing content anywhere.** I grepped `engineer-week|person-week|headcount|FTE|N weeks|staffing` across the spec, the sequencing doc, and the greenfield plan — every hit was an unrelated prose word ("weeks" never appears as an estimate). The owner's M0 ask is literally **"Build + staffing"**. The package cannot answer the question the approval is for: how many people, how long, at what cost, to reach the first reviewable output. For a reviewability verdict this is the gap between a sound design document and a fundable milestone.

## V4 — Technically true but unfair

**C3 and C6 are the clearest cases.** `enterprise-experiment-post-analysis-profile.md:468-482` (§14 "Required Canonical Reconciliation") states, unprompted: "This addendum should be reconciled into the canonical package only after review," then lists the exact edits — item 1, add `ExperimentReadContract`, `FlightReadinessPacket`, `MetricMovementPacket`, `WinLossEvidencePacket` to the domain model; item 2, add M0/M1/M2 milestones; item 7, "extend evaluation fixtures and implementation sequencing with the cases and components in this profile." It closes: "Until reconciliation is complete, this document is a research synthesis draft and does not supersede the canonical specification." §15 goes further and retracts a prior completeness claim: "Any earlier claim that the specification is complete must be narrowed…" So C3's zero-count, C6's orphan status, and C8's missing case classes are all **authored TODOs the writers declared and dated**, not defects a reviewer uncovered. Reporting them as discoveries would misrepresent the package's honesty. The legitimate finding is narrower: *the reconciliation is unmerged, so the approval object is the unreconciled package.*

**C10 is the second case.** The build-test file self-labels `"PROTOTYPE / THROWAWAY"` and names its own remaining owner gate; §17 independently prohibits any claim that review quality improved until P3 closes. "Proves only mechanical checks" describes a limitation the authors wrote down first.

**C1 is not unfair** — the scope mismatch is real and undeclared. **C5 is not unfair** — nothing in the package acknowledges that the owner's flowchart marks two stages REUSED from a component the sequencing doc places off-limits; that contradiction is genuinely unnoticed.
