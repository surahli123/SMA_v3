# Enterprise Plan Review — KDD-informed Data Agent, Scenario A

**Verdict: REVISE BEFORE IMPLEMENTATION PLANNING**

| Field | Value |
| --- | --- |
| Date | 2026-08-15 |
| Reviewer | Claude Opus 5 lead orchestrator + 8 review agents plus 1 image-extraction agent (see section 10) |
| Repo / branch | `SMA_v2` @ `codex/kdd-data-agent-practices-research`, HEAD `28cbbda` |
| Review object | The greenfield Data Agent package as it exists in the working tree on this branch |
| Status of this artifact | **Review finding, not product authority.** It does not amend the canonical package, close any gate, or authorize implementation. |
| Authority | Owner decisions and the canonical policy contract outrank this review. Where this review disagrees with a canonical doc, the disagreement is a finding for the owner to rule on, not a change. |

**This is not a production GO decision, and it is not a rejection of the work.** The
canonical specification package is strong engineering: internally coherent, unusually honest
about its own gaps, and in several places safer than what the source screenshots ask for. The
revision required is reconciliation and re-scoping, not redesign.

## Evidence classes used throughout

Following the package's own convention:

- **screenshot observed** — visible in one of the eight inspected images
- **repo observed** — anchored to a file and line in this working tree
- **command receipt** — output of a read-only command, recorded in `01-evidence-receipts.md`
- **owner decision** — recorded in the planning packet or the profile's open-decision list
- **reviewer inference** — a judgment; carries a falsifier
- **self-declared** — a gap the package authors documented themselves
- **discovered** — a gap this review found

The `self-declared` / `discovered` split matters. This package documents its own TODOs
extensively; reporting those as discoveries would misrepresent it. Findings are labeled.

---

## 0. Corrections the lead reviewer made to an earlier draft of this review

Recorded because the reasoning trail matters more than looking clean.

1. **Prototype critique scores.** An earlier draft repeated "3.6/5, 4.1/5, 4.5/5" from
   `deliverable-index.md:49`. Checked against the source files: baseline is **1.8-2.0**
   (`critique-before.json:4,7,11,15,19,23`), cycle 1 **3.7-4.1**, cycle 2 **4.0-4.5** — and
   all are superseded by an owner-run panel scoring **2.1** with
   `"convergence": {"passed": false, "threshold": 4.0}`
   (`critique-owner-ai-slop-2026-08-12.json:12`; `"supersedes": "All prior 4.x agent
   self-scores"` at `:13`). A number was propagated from an index without re-derivation. The
   index line is itself stale — see finding m13.
2. **"P3 has no measurable exit"** — overstated. P3 has an exit; it is a named human judgment
   (`implementation-sequencing.md:475`, `:398`), and two of its three acceptance scenarios are
   measurable (`wayfinder/prototype-observability-first-review-surface.md:37-39`). Accurate
   finding: the exit is not *operationalized*.
3. **"`build-test.json` proves only rendering/mechanical checks"** — undersells it. It records
   real browser interactions, keyboard navigation, overflow, and console checks. Accurate
   finding: it proves nothing about content correctness or reviewer outcome, and
   `"git_diff_check": "pass"` (`:34`) is unexplained.
4. **"The profile's 25 acceptance cases have no overlap with the eval case classes"** —
   overstated. Cases #18, #21, #22, #23, #24 map to existing classes. What genuinely has no
   home is the **M0-validity and M2-comparability subset**: CUPED mismatch (#10),
   preregistered runtime (#9), underpowered neutral (#4), co-primary, offsetting effects (#5),
   denominator drift (#13), `not_comparable` queries (#17).

One finding got **stronger** on verification: the plan does not merely omit the reuse the
owner specified — `implementation-sequencing.md:151` **forbids** it.

---

## 1. Executive decision and the five most material reasons

1. **Scope inversion.** The owner asked to fund **M0 Flight Readiness only** — `CURRENT
   TARGET`, approval requested "Build + staffing"; M1 and M2 "Direction only"; M3+ "No build
   approval" (*screenshot observed*, IMG_3689). The package's smallest fundable increment is
   D0 -> U8, whose first output is a full Scenario A packet. M0 vocabulary count in the
   canonical three documents: **0, 0, 0** (*command receipt* R3).
2. **The package cannot answer the question the approval is for.** The ask is literally
   *"Build + staffing."* Grepping `estimat|effort|week|day|sprint|size|person-` across the
   architecture spec, sequencing, and CE plan returns **zero** sizing content. No unit carries
   a duration, headcount, or cost.
3. **The exact-target chain has an unbridgeable hop.** `code` candidates require "file, symbol,
   and line" (`final-architecture-spec.md:438`), but **no port, entity, receipt, or validator
   derives symbol/line from a deployed artifact**. In practice that field gets filled by a
   model reading a diff — which is precisely the "keyword proximity" tie the docs forbid
   (`planning-decision-packet.md:35`), re-entering through an unguarded field. "Wrong exact
   target" is a named hard NO-GO.
4. **The evaluation gate has no power layer.** `find … -iname "*fixture*"` returns **zero
   files** — the fixture suite does not exist. No difficulty target, no trivial-baseline arm,
   no rule that fixture authors differ from architecture authors, no proof the method detects
   a planted positive. A team can produce a sealed adjudication packet with a clean receipt
   and learn nothing.
5. **The reuse premise is inverted.** Two of five pipeline stages are marked **REUSED** in the
   owner's own flowchart, from `search-relevance-experiment-analysis`, with basis-table
   routing "verified … in the sma playbook — reuse that routing" (IMG_3694, IMG_3695). That
   component name appears **nowhere** in `docs/`, and sequencing forbids touching the assets.
   A funding decision on this package buys a different first deliverable, on a different
   build-vs-reuse premise, than the one requested.

---

## 2. Evidence coverage

**All eight screenshots inspected directly by the lead reviewer** (converted with `sips`;
originals untouched; raw images not copied into this repo). Per-image observations are in
`agent-reports/image-extractor.md`; the lead reviewer independently opened all eight and
confirmed the transcription.

**Repo artifacts** read in full or in the deciding sections: the enterprise profile (all 505
lines), the architecture spec (sections 8-19 plus full outline), implementation sequencing
(all units and gate tables), the eval acceptance plan, both wayfinder freeze documents, the P2
intake, the CE plan's R1-R37, the prototype sources and receipts, and the **worktree** copy of
`deepseek-harness-practices.md` sections 16.1-16.5 in full.

**Coverage gaps, stated plainly:**

- **Post-review receipt correction:** the main orchestration task independently verified that all eight screenshot SHA-256 values match `enterprise-experiment-post-analysis-profile.md:27-34`; raw image paths and the rehash command are no longer available in this workspace. The final DeepSeek source was later verified with `shasum -a 256` as `81feaa5e1c2514732707fa542a283162faafa435611f768e6887c8421bb64f52`. The original review-time denial remains documented in `01-evidence-receipts.md`.
- Award repos, papers, videos, and workshop audio were **not** re-read from source. This
  review assessed only how the package represents them.
- No production, credential, or network access was used at any point.

---

## 3. Findings by severity

### BLOCKER

**B1 — No symbol/line attribution mechanism exists at any layer. [discovered]**
`final-architecture-spec.md:438` requires it; `:444` forbids inventing it;
`ProductionChangeRevision` (`:220`) lists "exact locator" as a *field* with no population
rule; `MappingResolver.resolve` (`:185`) is defined only by return type. Searched sections
6.2, 7.2, 10.4, 13, 17 and the G0-G7 contract.
*Consequence:* every code-type candidate either abstains permanently, or an unspecified step
fills the field — a model reading a diff, i.e. the forbidden proximity tie.
*Correction:* add an attribution port, e.g.
`SymbolAttribution.resolve(deployed_artifact, affected_component) -> AttributionRevision | CoverageGap`,
admissible only from build provenance (source map, debug info, package manifest) or a runtime
stack/profile observation — never from a model reading a diff. Make G2 return `inconclusive`,
not `pass`, when only file-level identity exists.

**B2 — Delivery plan targets the wrong milestone, and cannot price it. [discovered]**
IMG_3689 versus `implementation-sequencing.md:169-406`. Compounded by the total absence of
sizing content.
*Correction:* re-cut slice 1 as M0; attach headcount and duration to it.

**B3 — Reuse contract missing, and actively prohibited. [discovered]**
IMG_3694 / IMG_3695 versus `grep -rn "search-relevance-experiment-analysis" docs/` -> nothing
(*command receipt* R5). `implementation-sequencing.md:151` and `:167` forbid touching
`.agents/skills/sma/`, where `references/metric_registry/` and `references/schema_catalog/`
live.
*Correction:* a three-column reuse inventory separating *architecture* (reject old SMA) from
*verified domain assets* (adopt metric registry, schema catalog, basis-table routing) from
*reused components* (adopt `search-relevance-experiment-analysis` with an interface contract).

**B4 — Trace is defined two incompatible ways; no precedence rule exists. [discovered]**
`final-architecture-spec.md:539` and `:840` call Trace a **projection over the same canonical
workspace**. The trajectory increment terminates in an "**append-only diagnostic Trace
store**" (`deepseek-harness-practices.md:297`) fed from host hooks, explicitly "outside the
canonical Case Workspace" (`:17`). A projection cannot contain a fact the workspace lacks; an
independently collected store structurally can.
*Consequence:* Trace shows a completed retrieval with timings; Evidence shows "zero reads,
authority missing". **No rule says which governs** (searched sections 12, 14, 18).
*Correction:* amend `:539` / `:840` to call Trace an independently collected diagnostic store;
add a section-18 row making canonical Evidence controlling and Trace divergence a diagnostic
anomaly, never evidence or counterevidence.

**B5 — The immutable packet binds an unfrozen, deletable store. [discovered]**
`:653` puts Trace cross-links inside the digested manifest; `:655` digests that manifest;
`:214` has `RunAttempt` carrying Trace references; `deepseek-harness-practices.md:332` puts
five canonical IDs *inside* `TraceEnvelope`, which `:386` says "remains unfrozen"; and `:377`
permits deleting or rebuilding the Trace projection.
*Consequence:* a schema bump or pseudonymization key rotation re-keys every cross-link, so
sealed packets reference IDs that no longer resolve. **No packet may currently be described as
immutable.** Trace also has no owning component and no port (sections 6.1, 6.2).
*Correction:* either exclude Trace cross-links from the digested manifest (carry them in a
separately versioned, non-digested annex), or freeze `event_id` and require Trace retention
>= packet retention. Add a `TraceStore` component and an `append` port distinct from
`Workspace.append`.

**B6 — Redaction failure has no defined behavior, and the collector holds raw transcripts. [discovered]**
`deepseek-harness-practices.md:302` requires bodies dropped before envelope construction;
`:230` mandates redaction with no failure path. Searched sections 12, 13, 16.1-16.5: **what
happens when redaction fails is absent.** The raw path is concrete: host hook -> collector ->
`transcript_path` -> collector reads the file (the reused `sessions.py` slice, `:349`) -> raw
prompts and tool bodies in collector memory. Controls at `:372` bound environment, shell, and
output — **not filesystem retention**. `:337` adds a "secured pre-envelope intake" plus an
authorized raw re-open route: a third store and a back-door, both with no owner, ACL,
retention, or approver. Contradicts `final-architecture-spec.md:612`.
*Correction:* redaction failure fails closed (typed `redaction_failure` envelope, no body,
`coverage_status=blocked`, dependent publish gate blocks); give the pre-envelope intake an
owner, ACL, retention, and approver, or remove it; add a collector no-disk-write assertion and
a matching test.

**B7 — "Read-only" is asserted, not enforced. [partly self-declared]**
The only chokepoint is a logical component inside the Agent's own trust domain
(`final-architecture-spec.md:159`); the actual mechanism is deferred (`:613`). Nothing requires
read-only credential scope, a separate broker process, or egress control. `:608` ("source text
cannot change capabilities") is a requirement, not a mechanism.
*Consequence:* an LLM plus an in-process allowlist is not a read-only system.
*Correction:* make credential scope the primary control — per-source credentials physically
incapable of write, issued to a broker process the Agent cannot execute arbitrary code in,
behind an egress allowlist. P2 must produce a **per-source write-denial receipt obtained with
the real production credential.**

**B8 — Whose identity the Agent reads with is undecided, and ACL diagnosis is the hardest case. [discovered]**
Scenario A's own evidence plane requires ACL diagnosis (`:400`). Diagnosing over-filtering
means comparing what different users could retrieve — a service identity broad enough to do
that sees documents no single reviewer is cleared for. `:609` and `:205` apply permission
intersection *of the source records*, not of the **reviewing human's entitlements against each
document's ACL**. There is no per-document, per-recipient ACL evaluation at render time
anywhere in scope.
*Correction:* decide the identity model explicitly — recommend synthetic test principals for
allow/deny probes, aggregate-only for cross-user comparison, no broad service identity over
document bodies. Require render-time per-document ACL evaluation against the recipient's live
entitlements. Time-box any elevated authority with a named approver and expiry.

**B9 — Append-only immutability versus deletion/erasure obligations is never acknowledged. [discovered]**
`:121`, `:162`, and `freeze-canonical-domain-policy-contracts.md:289` make immutability
absolute; retention is entirely UNKNOWN in the intake. A sealed packet containing queries,
document text, and session data cannot be deleted by design. This is a legal conflict, not a
design nit.
*Correction:* pointers plus keyed digests for erasure-eligible classes, content in a
separately keyed store, crypto-shredding (destroy the per-subject key, leave a tombstoned
revision) as the deletion path. Name the retention owner and maximum per artifact tier before
any real read.

**B10 — No segmentation or multiple-comparison contract. [discovered; independently corroborated]**
`:417` forbids aggregate lift hiding tenant/tail/locale regression; profile acceptance case #6
requires detecting it; **`ClaimRevision` has no `segment` field**, and "Bonferroni", "FDR", and
"multiple comparison" appear in none of the documents.
*Consequence:* failure runs both directions. No contract -> false "no effect" on a genuinely
heterogeneous experiment. Segmentation without error-rate control -> manufactured segment
claims wrapped in deterministic-derivation receipts and ranked, attacking the false-`confirmed`
veto from inside the machinery meant to protect it.
*Correction:* add a `SegmentationContract` to G1 — preregistered segment set, minimum segment
size and per-segment MDE, an explicit FDR or Bonferroni rule, and the tenant-equal versus
traffic-weighted duality. Add `segment` to `ClaimRevision`. Make an unpreregistered segment
claim G0-incomplete.

**B11 — The evaluation suite has no power layer and does not exist on disk. [discovered]**
Zero fixture files found. No difficulty target, no expected baseline failure rate, no
trivial-baseline arm, no adversarial-distractor requirement, and no rule that a weak agent
must fail. No constraint that fixture authors are not the architecture authors — if the spec's
authors plant the defects, the fixtures test whether the design does what its authors
intended, not whether the Agent finds causes.
*Correction:* mandatory trivial-baseline arms (most-recent-deploy heuristic plus an
always-abstain arm) on every rung, with the pre-registered rule that a suite the trivial
baseline passes is **rejected before the Agent is scored**; at least two adversarial fixtures
where the most recent deploy is a decoy and the true cause is a config or data change;
fixture-author independence recorded as a packet receipt.

**B12 — U9's `UI-001` is unsatisfiable at U9. [discovered]**
`implementation-sequencing.md:343` requires the test to run "through the P3-approved
interaction contract", while `:335` says P3 may still be open and `:350` says acceptance
remains open. The CE plan already fixed this (`docs/plans/2026-08-12-001-…md:559`).
*Correction:* replace `:343` with the plan's wording. Sequencing is stale relative to its own
downstream plan.

**B13 — The package is not reviewable as a package: the two newest requirement documents are unreachable, and one exists only in a transient worktree. [discovered]**
This finding answers the review's literal question — *is the plan reviewable?* — and is the
cheapest of all the BLOCKERs to fix.

- `grep -rln "enterprise-experiment-post-analysis-profile" docs/` returns **zero** inbound
  references. The newest requirement document is absent from `deliverable-index.md`,
  `README.md`, `wayfinder/map.md`, `cloud-agent-handoff.md`, and `source-manifest.md`.
- `deepseek-harness-practices.md` is referenced **only** by that orphan.
- The trajectory increment (sections 16.1-16.5, the strongest privacy analysis in the package)
  exists only in the `cd68` Codex worktree copy (80,869 bytes) and is **absent** from the
  main-tree copy (53,020 bytes), whose section 16 is still the old "Bottom line". Verified by
  `ls` and a full `diff`; see `01-evidence-receipts.md` sections 5 and 6.

*Consequence:* anyone following the package's own documented reading order never reaches the
documents that define the current requirements, and the trajectory work disappears if that
Codex worktree is cleaned up. An approval granted today attaches to the unreconciled package.
*Correction:* move the trajectory increment into the main tree; add both documents to
`deliverable-index.md` and to the authority order in `cloud-agent-handoff.md`; then re-review.
*Fairness note:* the profile declares its own unreconciled status (its sections 14 and 15), so
the **[discovered]** part is the orphan/worktree condition, not the fact that reconciliation is
pending. See section 0 and the section 10 verifier note.

**B14 — U11 has no operational stop. [discovered]**
`PROD-001` through `PROD-006` cover correctness. Absent: rate/QPS/byte/row limits,
blast-radius caps (max rows, tenants, time range per case), runtime abort triggers, and a
**named halt authority**. "Source load" appears only as a measurement in U13.
*Correction:* add `PROD-007` (per-case and per-window read ceilings; exceeding one aborts the
run and emits a Coverage Gap, never partial-as-complete Evidence) and `PROD-008` (named
on-call halt role with a tested disable path that leaves preserved Evidence intact — note
`PROD-006` tests revocation from the *source* side, not halt from ours). State that U11's
ceilings also bind production-like replay and shadow-read.

### MAJOR

**M1 — `confirmed` has no legal exit transition. [discovered]**
`:274-278` enumerates every legal Cause Verdict edge; there is **no edge out of `confirmed`**,
and `:279` says new Evidence "never overwrites" it. The system's single hard veto is a *false
`confirmed`* — and the retraction path for exactly that failure is unspecified. The only
implied escape is a new generation (`:333`), a heavier and different operation.
*Correction:* add `confirmed -> inconclusive | ruled_out` on contradicting validated Evidence,
or state explicitly that retraction requires a new generation.

**M2 — Human rulings can cite Trace, and that path reaches `confirmed`. [discovered]**
Exactly one enforced Trace boundary exists —
`EvidenceAdmission.evaluate(SourceRead, AdmissionPolicy) -> EvidenceRevision | CoverageGap`
(`:183`), a genuine type boundary. But `HumanRuling` "evidence citations" (`:227`) is
unconstrained; Trace sits in the packet (`:653`) and on the first screen (`:547`); and G7
requires the reviewer to "cite Evidence" (`:370`) without requiring the citation to resolve to
an `EvidenceRevision` ID. `:243` never enumerates legal edge source types, so nothing
schema-level forbids `trace_event --supports--> claim`.
*Correction:* enumerate legal `(source_type, edge_type, target_type)` triples with
`trace_event` legal only for `cross_links_to`; type `HumanRuling.evidence_citations` as
`EvidenceRevision[] | DerivedFactRevision[] | GateReceipt[]`, validated at submission; add both
to the conformance checklist.

**M3 — `not_applied` is a label, not a mechanism. [discovered]**
`:450-458` enforces the label in metadata and rendering. But a unified diff bound to an exact
deployed SHA is directly `git apply`-able; the packet is a machine-readable, digest-bound
artifact; and `action_ready` is a machine-readable state whose only stated guard is prose.
Nothing forbids a downstream system polling for it.
*Correction:* make the diff non-applicable by construction (context-annotated fragment, or a
mandatory sentinel that breaks `git apply`), and add a publish-barrier predicate that the
recipient channel is a human review surface, not an automation endpoint.

**M4 — Nothing forbids reusing the G3 observation as the G4 challenge. [discovered]**
G3 passes on "at least one runtime observation matches a prediction" (`:366`); G4 needs "at
least one challenge complete with `challenge_result=supports`" (`:367`); `:695` covers repeated
*workers*, not evidence reuse.
*Correction:* add a G4 predicate that the challenge's `SourceRead` set is disjoint from the G3
supporting set, or that the challenge is a predeclared counterfactual (control, holdout,
negative control).

**M5 — G6's `not_applicable` escape can empty the gate. [discovered]**
`:369` says pre-action replay "may" satisfy G6; `not_applicable` needs only "a deterministic
applicability receipt" (`:357`); replay is P2-blocked. No rule states that *missing replay
authority* must yield `inconclusive`. Note the freeze doc is stronger here
(`freeze-canonical-domain-policy-contracts.md:277`).
*Correction:* replay/regression unavailable for authority, coverage, or budget reasons -> G6
`inconclusive`, never `not_applicable`. Reserve `not_applicable` for provably unreplayable
change classes with a named human rationale.

**M6 — "Material" inconclusive is undefined, and it is the sole hinge of the invalid-experiment block. [discovered]**
The block itself is real and well built (`:364`, `:116`, `:420-428`, `:628-638`), and UNKNOWN
validity does fail closed (`:116`, `:347`). But the trigger is "a critical `fail` or
**material** `inconclusive` result" (`:421`), and materiality is a field (`:218`) with no
classifier and no named owner.
*Correction:* define materiality deterministically — any G1 check on the decision metric's
assignment, exposure, join, or definition is material by construction — and default
unclassified to material.

**M7 — Neutral and mixed are not first-class. [self-declared as an open owner decision]**
Zero hits for `neutral|mixed|offsetting|underpowered|dilut` in the spec outside
"technology-neutral" and "mixed rollout". Power appears only as a G1 validity input token
(`:364`), so an underpowered neutral is either pushed into the invalid branch — blocking all
system hypotheses on a possibly real effect — or falls through to a miss-shaped candidate
hunt. Neither is correct.
*Correction:* add `outcome_class = positive | negative | neutral | mixed` to `MetricQuestion`
(`:211`) with per-class required hypothesis families (neutral: true null / underpower /
dilution / ceiling / counteracting segments; mixed: related-metric coherence plus trade-off
reality), and a G1 rule that an underpowered-but-valid read yields `directional_only`, not
invalidity.

**M8 — Win/loss has no canonical home. [discovered]**
`win/loss`, `side-by-side`, `SBS`, `not_comparable` -> **0 hits** in the architecture spec, and
synonyms (`query-level|winners|losers|regression example`) also return 0. No
`WinLossEvidencePacket`, no M2 stage in the stage contract, no test in U8. The profile's field
list (`:203-215`) covers roughly two-thirds of what a search reviewer needs — it **omits ranked
lists with per-document position deltas, judged relevance labels, query-intent class, and
session outcome**.
*Correction:* either promote `WinLossEvidenceRevision` plus a `query_evidence` stage into the
spec with the missing fields, or state in the spec's scope section that the Scenario A MVP does
not satisfy the win/loss requirement and name M2 as the follow-on. Do not leave both claims
standing.

**M9 — Per-arm corpus and index parity is never checked. [discovered]**
`:10.4` requires generation identity for a *candidate change*; nothing requires that treatment
and control were **served by the same index generation, serving alias, and ACL snapshot**. The
research doc lists arm-generation divergence as a hard stop; the canonical spec does not carry
it forward.
*Consequence:* every ranked-list comparison is confounded by corpus drift, and no win/loss
example is comparable.
*Correction:* G1 must check arm parity on index generation, serving alias, ACL snapshot, and
effective pipeline; divergence caps Cause at `suspected` and blocks win/loss comparability.

**M10 — Query-mix shift is not a validity check. [discovered]**
G1's Scenario A list is unit-level SRM only. **Compositional SRM** — query distribution
balance across arms by intent, head/torso/tail, tenant, and locale — is absent. Zero-result
rate is a plane keyword, never a required guardrail.
*Correction:* add compositional SRM and zero-result-rate delta to G1's required checks.

**M11 — Click and position bias are named twice and estimated never. [discovered]**
No propensity source, no IPS estimator, no interleaving. `:417`'s own "CTR alone MUST NOT be
treated as relevance" has no enforcing mechanism. Interleaving — the highest-power
ranking-specific discriminating challenge — is absent from G4's enumeration and from all five
documents.
*Correction:* require a position-bias-corrected estimator with a named propensity source, or
an interleaving arm, before any click-derived metric supports a G3 mechanism claim. Add
interleaving to G4's enumeration.

**M12 — No evidence class for relevance judgments or offline eval. [discovered]**
The intake's E01-E14 has no judgment or golden-query-set class, so offline-online
reconciliation and judged win/loss remain unbuildable **even after P2 closes**. The
offline-online divergence story — relevance improved but exposure, latency, rendering, or user
behavior absorbed it — is the most common enterprise-search outcome and has neither a claim
template nor a named source.
*Correction:* add `E15 Judgment / offline-eval` (query-set version, rubric, judge identity
class, judgment date, coverage by tenant and query class), plus an offline-online divergence
hypothesis family in the M1 plane list.

**M13 — Permission, presentation, and telemetry have no typed change class. [discovered]**
The spec kept `code | config | flag | model | data` against its own research doc's
recommendation to add `index | connector | permission | presentation | telemetry`. `data`
absorbs index and connector, but the three planes most likely to kill a search experiment
silently cannot be normalized, ranked, or exact-targeted.
*Correction:* adopt the recommended subtypes with their own exact-identity rows.

**M14 — Ranking is byte-stable but not reviewer-reproducible. [discovered]**
`uncalibrated_fixture` (`:529`) has no defined comparator anywhere. Byte-stability (`:525`) is
a replay property; a reviewer holding the packet cannot recompute the order, only re-run the
same engine and observe agreement.
*Correction:* define `uncalibrated_fixture` as an explicit lexicographic ordering over
gate-derived booleans (exact-identity -> G2 status -> mechanism support -> contradiction count
-> candidate ID), recomputable by a reviewer before any weights exist.

**M15 — Two of three hard vetoes have no detector on the case that matters. [discovered]**
On the blind case, false-`confirmed` gold is a human adjudication; wrong-exact-target is inert
until P2 closes (the eval plan concedes this); ACL violation is mechanical only if an enforcing
broker logs denials, and that broker is design-only and unfrozen. Partial mechanical cover
exists for *unearned* `confirmed` (missing receipts) but not *wrong* `confirmed`.
*Correction:* annotate each veto with `detector: deterministic | human | not-yet-implemented`,
and state that exact-target acceptance is out of MVP scope until P2 or the case-specific
archival receipt closes.

**M16 — Blinding's leakage detector is undefined; model pretraining contamination is unaddressed. [partly self-declared]**
The freeze procedure is real and specific, and the archival-snapshot receipt closes corpus
contamination *by construction* for a genuinely time-bounded snapshot. Not closed: the
near-duplicate method is explicitly left to "the project" and does not exist; nothing addresses
the vendor model having seen the incident in pretraining; and case-selection bias has no
control (the curator selects knowing the resolution).
*Correction:* specify the detector concretely (exact-string plus n-gram plus symbol-name
overlap against the snapshot, thresholds pre-registered); require a prompt-freeze receipt dated
before case selection; state that a widely published incident is ineligible as the MVP blind
case.

**M17 — The prototype opens the wrong evidence record for competing claims. [discovered]**
`prototypes/observability-review-surface/app.js:124` falls back to `EV-DEP-17` for any
non-`EV-` node, so clicking competing claim C-09 or C-22 shows the Evidence Inspector for
validated support belonging to C-17. Additionally "Show answer path" / "Show evidence path"
carry `data-action="path"` (`app.js:134`) while `bind()` binds only `risk`, `relayout`, and
`collapse` (`:207-209`) — both inert; the Verify tabs (`:166`) and all Trace filters (`:192`)
are also inert.
*Consequence:* this actively misinforms a reviewer and would corrupt any P3 session.
*Correction:* fix `app.js:124` before any live review; mark the inert controls
non-functional in the README so a reviewer does not score them.

**M18 — Digests function as membership and confirmation oracles. [discovered]**
`:439` requires a "redacted value digest" for config candidates. A plain SHA-256 of a
low-entropy value (flag state, threshold, hostname, short config string) is brute-forceable,
and a document digest lets anyone holding a candidate document confirm its presence in another
tenant's case. The same applies to the eight screenshot hashes at
`enterprise-experiment-post-analysis-profile.md:27-34` and to the "authorized integrity digest"
in the trajectory increment.
*Correction:* keyed HMAC with per-tenant keys for all content and value digests, or bucketed
change-indicators for config. Never a bare hash of source content.

**M19 — The collector fleet is an employee-monitoring pipeline with no DPIA. [discovered]**
Passive collectors run on every engineer's Codex / Claude Code / Cursor host and feed a central
store. Cursor's user email is dropped by policy, but session-attributable engineer activity is
still collected centrally. No document names an employee-monitoring, DPIA, or works-council
review, or who may query the Trace store.
*Correction:* add that review as a prerequisite for the collector, and name the Trace store's
query-authority model.

**M20 — Transcript backfill is fail-open. [discovered]**
Upgrade detection reduces to a self-reported version string (`host_artifact_digest` is
"observed only from a trusted install manifest, otherwise null"). The inherited parser skips
malformed lines with warnings and silently defers unfinished tails. The increment claims a
missing capture receipt "fails closed", but the publish barrier
(`final-architecture-spec.md:628-638`) lists **no** capture receipt among its nine conditions.
Composite behavior today: mismatched pin -> warnings -> packet publishes.
*Correction:* add "required capture receipts present and adapter pin matches observed host
version" to the publish barrier; pin mismatch -> adapter emits no envelopes,
`coverage_status=unsupported`, dependent gate blocks.

**M21 — "Append-only" is API-enforced, not cryptographically enforced. [discovered]**
`:162` (no mutable update/delete API), `:202` (per-revision content digest), `:486-493` and
`freeze:289-295` (a complete supersession / invalidation / dependency-closure algorithm) are
all sound. Missing: a **digest chain**. Revisions link by ID (`:236`), not by predecessor
digest, and the manifest carries identifiers rather than `(revision_id, content_digest)` pairs.
An operator with store access can alter a historical revision's bytes undetected except by that
record's own self-digest.
*Correction:* the manifest enumerates `(revision_id, content_digest)` pairs; each revision
records `prev_digest` for its logical ID.

**M22 — `SKEL-004` is an unbounded universal negative. [discovered]**
"No code path exposes source writes, arbitrary file writes, external publication, or
production mutation" (`implementation-sequencing.md:216`) cannot pass or fail deterministically
— and it is the single test guarding the entire read-only claim.
*Correction:* restate as a positive capability allowlist — the capability registry enumerates
exactly N read methods; a denied-write attempt per method emits a policy receipt; plus an
import-graph assertion that no write, network, or subprocess symbol is reachable from the
package root.

**M23 — U6/U8 build the production-grounding machinery against fixtures that may not survive P2. [self-declared, under-weighted]**
Roughly 60% of the pre-gate build — deployed-SHA binding, exact-target blocking,
`scope x interval x rollout` matching, the `production_identity_and_scope` stage — is
byte-stable against invented inputs the plan itself forbids validating ("No test or
documentation claims production fidelity"). P2 closure can invalidate their input shape
wholesale. The plan acknowledges this only in a failure-recovery row.
*Correction:* scope pre-P2 U6 to interfaces and unknown-authority failure paths; defer the
matcher's feature set to a post-P2 U6b, stated explicitly in the sequencing.

**M24 — Randomization-unit versus analysis-unit mismatch. [discovered — domain]**
User-randomized experiments with query-level ratio metrics require clustered or delta-method
variance. **No document mentions variance estimation for ratio metrics.** This is the leading
cause of false positives in search experimentation; careful `use_cuped` handling without it is
precision theater.
*Correction:* require the variance estimator and its unit-of-analysis to be named in
`ExperimentReadContract`, and make a mismatch a G1 validity failure.

### MINOR

- **m1** Shared-state interference (click-feature stores, learned counters, per-user result caches) makes SUTVA violation the default in search, not an edge case; "interference" appears once in G1's input list with no mechanism, no detection, and no evidence source.
- **m2** Novelty/primacy and enterprise weekday seasonality: no requirement to check effect stability across the window or exclude ramp days. A fixed-horizon read over a non-integer number of weeks is systematically biased.
- **m3** Known-item and navigational regression is catastrophic in enterprise search and invisible in averaged NDCG; it appears only inside one research-doc falsifier sentence, never as a required query class.
- **m4** Product-side ACL over-permissiveness — the search product leaking documents — has no guardrail metric and no NO-GO. Section 15 governs only the *Agent's own* access. Worth separating explicitly.
- **m5** `MetricQuestion` omits `locale` and `device`, which `:417` makes named failure modes.
- **m6** No search-domain test exists among the roughly 60 test IDs in sequencing; the eight evidence planes are declared mandatory and owned by no unit.
- **m7** U12 and U13 carry no test IDs, breaking the `XXX-00N` convention every other unit follows; D0, U9, and U12 have document-not-test exits ("ready for review" is not evidence).
- **m8** `M1` identifier collision: `implementation-sequencing.md:105` uses bare `M1` for "Scenario A MVP decision"; the profile uses `M1` for "Metric Movement".
- **m9** Pseudonymization key material sits inside a hook-launched process on a developer machine; custody, rotation, and re-identification risk are unspecified, and the P2 intake does not name a collector-held key.
- **m10** "Safe" reuse is never defined as a testable predicate; the DeepSeek-derived sub-portion of the forked UI is unanchored to any file, line, or SHA; no SBOM or dependency license scan for the reused slices; no contributor-provenance check on a single-author third-party repo.
- **m11** Repeated-run count N is unset, so N=2 satisfies the stability contract's letter. Floor it at 5 for the MVP as a stated engineering default.
- **m12** Two internal-architecture disclosures in a package whose sharing scope cannot be verified from here: the experimentation-platform vendor name alongside an internal metric-source contract, and internal product-surface interleaving relationships.
- **m13** `deliverable-index.md:49` reports superseded prototype critique scores; the current owner-run panel scored 2.1 with `convergence.passed: false`. Self-generated critique scores should not sit in the deliverable index at all.

### What the package gets right, and must not be lost in revision

A fair review has to credit this, because a re-slicing risks discarding it.

- **The refusal to fake closure.** Section 17 names three OPEN GATES with an explicit
  "work allowed now / prohibited until closure" table and states the specification must not be
  used to mark any of them resolved. `implementation-sequencing.md:422`: "No open prerequisite
  may be closed by repository inference, a model opinion, a prototype screenshot, or a
  mechanically green test."
- **Orthogonal state design.** Cause Verdict and Recommendation Readiness as separate axes with
  a legality matrix (`:298-303`), so "confirmed cause, unsafe action" and "unconfirmed cause,
  safe mitigation" are both expressible. That is the exact confusion that sinks real
  post-analysis tooling, and it is designed out at the contract layer rather than patched at
  the UI.
- **G0-G7**, especially the G4 two-field split (`challenge_execution_status` versus
  `challenge_result`) that prevents operational failure from reading as causal falsification,
  and the single path to `confirmed` that explicitly excludes vote, consensus, narration, and
  confidence scores.
- **The invalid-experiment branch hard-blocks** (`:419-428`): system hypotheses become
  non-ranked, non-publishable blocked leads; production recommendations go `not_applicable`;
  any production proposal from this branch is an evaluation NO-GO.
- **Exact-target discipline** (`:430-444`): per-type identity requirements, "Do not invent false
  file-line precision", and the explicit rejection of keyword proximity as a tie.
- **Ranking as filters and ceilings, never offsettable weights** (`:521`), with the sealed
  `pilot_ranking_policy` / `uncalibrated_fixture` separation (`:529-530`).
- **Abstention is genuinely first-class** — canonical output behavior, an invariant, a required
  case class, set-valued gold allowing abstention to be `required`, budget exhaustion yielding
  a partial packet, forced terminal submit rejected, human timeout never approving. **No
  specified pressure can force `confirmed`.**
- **P4's veto and stability layers are real:** hard NO-GOs are non-compensable, and *any*
  hard-gate flip under frozen inputs stops the rung — a rule that bites without a number.
- **`EvidenceAdmission`'s type boundary** (`:183`) and `SKEL-003` ("Trace input cannot satisfy
  an Evidence dependency") are real enforcement, not assertions.
- **The trajectory increment's per-host limits** are more honest than most vendor-integration
  designs. Its defect is uniform and narrow: it consistently specifies what should be true and
  what to test, and consistently omits what happens when the check fires.

---

## 4. Requirement -> architecture -> implementation -> evaluation traceability

| Owner requirement (source) | Architecture | Implementation unit | Evaluation case |
| --- | --- | --- | --- |
| Validate flight and primary read (M0) | partial — G1 only | **none** | **none** |
| WHN primary read / arm join / `use_cuped` / registered-metric caveat / basis-table fallback | **none** | **none** | **none** |
| Four outcome classes (positive / negative / neutral / mixed) | **none** — CE plan R33 scopes to "miss" | **none** | **none** |
| Explain movement, ranked falsifiable claims | yes (`:386-387`, section 13) | yes (U6, U7) | yes |
| Tie to exact deployed SHA plus file/symbol/line | partial — required, **not derivable** (B1) | yes (U6, U11) | gated on P2 |
| Win/loss query evidence (M2) | **none** | **none** | **none** |
| Immutable human-reviewable packet | yes (`:642-661`) — but see B5 | yes (U8) | yes |
| Read-only, no launch decision | yes in contract; **not enforced** (B7) | SKEL-004 (unfalsifiable, M22) | yes (hard vetoes) |
| Reuse ranking RCA plus verdict framework | **none — prohibited** (B3) | **none** | **none** |
| `Log + learn` growing check set | **none** | **none** | **none** |

Four requirement lines are absent end-to-end, plus two the owner's design assumes. All belong
to the milestones the owner actually prioritized. Separately, the spec declares the eight
evidence planes mandatory and **no implementation unit owns them**.

---

## 5. KDD / DeepSeek `Adopt | Adapt | Reject` corrections

The dispositions are, in the main, correctly drawn, and the CE plan states as source fact that
"No audited work proves the complete production causal chain." Corrections:

| Source | Docs' verdict | Reviewer correction |
| --- | --- | --- |
| Champion / Fourth-place repos | Adapt plus explicit Rejects, fixed SHAs | **Concur** — strongest evidence class in the set |
| Team 1286 (PiTrace) | Adapt | **Concur**, but the author-claim label must travel into U3, which inherits shared-replayable-state design and cites no provenance |
| Team 1401 (Data Agent Studio) | **Adopt** UI affordances | **Downgrade to Adapt-with-P3-gate.** A single 8:32 video of a system whose backend the manifest itself says is unproven cannot carry an Adopt into U9's ten-scenario surface |
| DeepSeek Harness section 16 `TraceEnvelope` | Adapt | **Reject for the Scenario A MVP; defer to a post-P3 proposal.** A cross-host collection subsystem with no unit ID, no requirement in R1-R37, no gate, and six self-declared unknowns is scope arriving through a research door. Adopt only its section-13 *tests* (Trace != Evidence, crash-tail unknown, no blind retry) into U7/U9 |
| Codex Trajectory reuse | Direct licensed reuse | **Adapt, not Adopt-now** — a fixture-backed adapter is scheduled against an envelope the same document calls unfrozen. Freeze the envelope first, or build only the view component against synthetic envelopes |
| Old SMA | Reference only, non-binding, protected path | **Split it.** Reject the architecture; **Adopt** the verified metric registry, schema catalog, and basis-table routing per IMG_3695 |
| Local KDD code | Reject verdicts | **Concur on verdicts; downgrade the evidence class** to reviewer-observed, non-reproducible — "local source, not included" means no reviewer can re-derive those line anchors |

**Cargo-cult risks:** the Evidence Graph and the eight-plane sweep are both inherited from
competition-UI observation and RCA literature rather than from an M0 requirement. M0 needs a
checklist with `PASS | FAIL | MISSING | UNKNOWN | NOT_APPLICABLE`, which the profile correctly
specifies and the graph-centric prototype does not serve. Build the checklist; defer the graph.

---

## 6. Owner decisions still required

**Product decisions (owner only):**

1. Is M0 the first build slice? *(Reviewer recommendation: yes — it is what the screenshots requested.)*
2. Does Scenario A cover only metric misses, or all four outcome classes? *(Screenshots say all four, and that neutral/mixed is where the value is.)*
3. Is M2 in the first MVP? *(Recommendation: no — the roadmap marks it Direction only and blocked on M1.)*
4. Canonical meaning of `flight` versus experiment, rollout, exposure window, analysis window.
5. One decision metric versus an approved co-primary policy.
6. May an invalid experiment carry a bounded unapplied instrumentation or data-quality fix?
7. Which raw query, result, SBS, and Trace fields may enter the packet versus remain digest-linked.
8. Whether the first review screen is milestone/packet centered.
9. Named approver per milestone, and whether roles may overlap.
10. **New:** is a central Trace store collecting session-attributable activity from every engineer's IDE acceptable? (M19)
11. **New:** what is the retention and erasure posture for packets containing document text? (B9)

**Engineering proposals (need a named owner, not owner sign-off):** schema encoding, storage,
language, framework, `TraceEnvelope` serialization, adapter API, UI stack, and whether the
three milestone packets are separate schemas or one shared envelope.

---

## 7. Review-pass checklist with observable evidence

| Gate | Observable evidence that closes it |
| --- | --- |
| **P2a — source inventory** | Signed table per source: owner, semantic-version authority, freshness SLA. Seed from the tech spec rather than starting blank |
| **P2b — access boundary** | Per-source **write-denial receipt obtained with the real production credential**; a written egress/network policy artifact; the B8 identity decision plus a render-time document-ACL design; the redaction spec with planted-positive recall *and* a sampled false-negative estimate; the B9 erasure design; a data-flow inventory naming every store (workspace, Trace, cache, fixtures, packets, logs) with tenant partition key and retention; a dated, named approval with <=90-day expiry and defined re-approval triggers |
| **P3 — reviewer acceptance** | At least 2 real reviewers (one experiment owner, one code/domain reviewer), at least 2 cases including one where the Agent's conclusion is **wrong**, and a pre-declared pass rule: both reach exact proof in <=2 interactions, both name the strongest contradiction unprompted, both correctly identify the stale-evidence recompute impact. Fix `app.js:124` first (M17) |
| **P4 — evaluation** | Fixtures existing on disk; trivial-baseline arms (most-recent-deploy and always-abstain); a fixture-author independence receipt; >=2 adversarial decoy cases; every veto annotated with its detector; N>=5 repeated runs |
| **U1-U13** | Each unit's named `XXX-00N` tests green in a hermetic run — including the missing U12/U13 IDs and the `SKEL-004` replacement |
| **One real historical Scenario A** | Experiment id -> reviewed report; DS plus experiment owner review every prerequisite; disagreements surfaced as explicit failed/missing checks; unsupported state stays `UNKNOWN` |
| **Exact deployed mapping** | `PROD-004` green (deployed identity wins over repository working state, conflicts stay visible) **plus** a specified symbol/line attribution port (B1) |
| **Human review** | Named approver accepts one reviewed report; timeout, expiry, and non-acknowledgement never mean approval |
| **Hard-veto-free calibration** | A full pilot run with zero false `confirmed`, zero wrong exact target, zero ACL violation — with a denominator large enough for that to mean something |

---

## 8. Recommended first authorized implementation slice

**M0 Flight Readiness, fixture-backed, zero production access — and smaller than the plan's U1.**

`U1` as written is the risk, not `U2`. `POL-001` demands a deterministic result *and rationale*
for all 25 Cause Verdict x Recommendation Readiness pairs, crossed with gate ceilings and
reopen rules, before a line of the skeleton exists. That is a contract-authoring project in
front of the walking skeleton, inverting the plan's own stated "not a large horizontal build"
principle.

**Slice 1 = D0 + a vertical U1' + U2 retargeted to M0.**

- `U1'` encodes only: the closed enums as total functions that fail closed on any un-enumerated
  pair; the exact matrix cells the skeleton path traverses; and the two fail-closed obligations
  (`POL-004`, `POL-005`). Remaining matrix cells land in `U1''` alongside U7/U8, when there is
  a consumer to prove them against.
- `U2` emits a `FlightReadinessPacket` against de-identified fixtures derived from one real
  past flight, plus an `ExperimentReadContract` schema and the M0 deterministic check list.
- **Reuse** the metric registry and schema catalog from `.agents/skills/sma/references/` rather
  than re-deriving them (which requires lifting the `implementation-sequencing.md:151`
  prohibition — an owner decision).
- Deliverable: one hermetic command producing a byte-stable packet digest, plus the `SKEL-004`
  replacement from M22.

**Stop conditions — halt and return to the owner if any fires:**

1. The fail-closed default is bypassed by an enum alias or a default branch.
2. Any file appears under `adapters/production/`.
3. Any test requires a network socket, a secret, or a path outside the package.
4. The packet digest is not byte-stable across two clean runs.
5. The fixture set cannot produce a *failing* case for each of SRM, CUPED-mode mismatch,
   unregistered decision metric, and pre-runtime invocation. (If the baseline passes
   everything, the fixtures are too lenient — redesign before proceeding.)
6. The slice exceeds its budget without a green hermetic command — re-scope, do not start U3.

**Explicitly not in this slice:** Evidence Graph, Trace UI, candidate ranking, production
adapters, the trajectory collector, and Scenario B.

---

## 9. Scenario B / SEV deferral and prerequisites

**Deferral confirmed, on stronger grounds than the package itself claims.** The package defers
Scenario B architecturally (`:459-470`). The screenshots add a decisive point: **SEV and
incident response appear nowhere in the owner's roadmap** — all four milestones concern
experiment post-analysis. Scenario B is not merely deferred; it is currently outside the
requested product.

Prerequisites before it re-enters scope:

- M0-M2 packets accepted on more than one real flight;
- a separate owner scope gate and a new owner-approved plan;
- human IC / on-call ownership of `recovered | stable | closed`;
- a rollback-packet contract bound to deployed SHA or exact non-code state;
- Scenario B-specific schemas, stage policy, safe-action latency, load budgets, and fixtures;
- no silent broadening of Scenario A source authority or evaluation scope.

"Recovery after rollback is strong but rebuttable evidence and does not automatically set
Cause=`confirmed`" is correct and should survive unchanged.

---

## 10. Coverage and independence statement

**8 review agents plus 1 image-extraction agent, within the review's stated cap of nine.**

| Agent | Model | Scope | Delivered |
| --- | --- | --- | --- |
| `image-extractor` | Sonnet 5 | HEIC conversion and transcription | yes |
| `A-consistency` | Sonnet 5 | Mechanical identifier/enum/traceability/link audit | yes |
| `B-architecture` | Opus 5 | Truth-store separation, Trace/Evidence, trajectory increment | yes |
| `C-causal` | Opus 5 | Exact-deployed-tie chain, verdict ceiling, invalid-experiment block | yes |
| `D-search` | Opus 5 | Enterprise-search domain coverage | yes |
| `E-eval` | Opus 5 | P4 evaluation design and P3 reviewer workflow | yes |
| `F-security` | Opus 5 | Security, privacy, P2 production authority | yes |
| `G-sequencing` | Opus 5 | Sequencing executability and source-transfer audit | yes |
| `H-verifier` | Opus 5 | Fresh-context verification of the draft verdict | yes |

The verifier saw the goal, the acceptance criteria, the evidence, and the draft verdict — but
not the lead reviewer's reasoning. No Fable, Haiku, Codex, or unspecified model was used.

**Delivery incident, recorded honestly.** Six reviewers plus the verifier completed their
analysis but their reply messages did not reach the lead context; an earlier version of this
review wrongly characterized that as "failed to deliver" and drew conclusions around the gap.
All eight reports were subsequently recovered from the session's `subagents/agent-*.jsonl`
transcripts and are reproduced verbatim in `agent-reports/`. That recovery is why this review
contains roughly 30 findings the first version lacked, including four of its BLOCKERs. Two
agents noted the harness had blocked their own attempts to write report files.

**Genuine independent corroboration** (different prompts, different lenses, same conclusion):

- the segmentation / multiple-comparison gap — found separately by `C-causal` (M4 in its report) and `D-search` (its lead BLOCKER);
- win/loss absence — found by the lead reviewer, `C-causal`, `D-search`, and `H-verifier`;
- M0 absence downstream — lead reviewer, `A-consistency`, `H-verifier`;
- the packet-immutability problem — reached from two unrelated angles by `B-architecture` (unfrozen Trace schema) and `F-security` (erasure obligations).

**What does not count as independence:** agreement between the lead reviewer and any same-model
agent reading the same files. Per the package's own principle, which this review endorses,
same-model or shared-context agents are not independent support. Independence comes from source
reads, deterministic checks, frozen gold, and named reviewers.

**The verifier's own challenge to the verdict, recorded rather than buried.** The profile's
section 14 *already is* the revision — nine reconciliation edits, fifteen owner decisions — so
one could argue the honest verdict is ACCEPT-with-conditions, since REVISE asks the authors to
do exactly what their own newest document says to do next. The verifier held REVISE, and the
lead reviewer agrees, on this ground: the reconciliation is unmerged, unreferenced, and partly
lives in a worktree the reviewed tree cannot see, so an approval today attaches to the
unreconciled package.

**Post-review receipt correction:** the main orchestration task independently verified the eight screenshot SHA-256 values against the enterprise profile. The final DeepSeek source was independently hashed as `81feaa5e1c2514732707fa542a283162faafa435611f768e6887c8421bb64f52`. Raw screenshot rehash paths and command output are no longer available here.
