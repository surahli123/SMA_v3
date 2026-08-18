# Opus 5 Independent Reconciliation and M0 Alignment Review

| Field | Value |
| --- | --- |
| Date | 2026-08-16 |
| Handoff | `opus5-m0-alignment-20260816` |
| Reviewer | Claude Code Opus 5, single independent judgment, no subagents |
| Review object | Working-tree state of the KDD Data Agent package on `codex/kdd-data-agent-practices-research` |
| Evidence class | **Worktree evidence only.** `docs/research/` and `docs/plans/` are untracked relative to HEAD `28cbbda` (`01-evidence-receipts.md:17-35`). Nothing here is committed, published, or production-validated. |
| Authority | Review finding, not product authority. This document closes no gate and authorizes no work. |

---

## 0. Method and honesty boundary

I read the original finding text in `00-final-review.md` first, then verified each claimed correction
against the current canonical document text. I did **not** accept `03-codex-disposition.md` as evidence
that a correction landed. Every row below cites the current worktree file and line I actually opened.

Four states are kept separate throughout and are never collapsed:

- **spec-addressed** — the canonical text now says the right thing;
- **implemented** — code exists (only the throwaway prototype qualifies anywhere in this package);
- **production-validated** — nothing in this package qualifies;
- **owner-accepted** — only the 2026-08-16 M0 funding boundary qualifies.

Coverage gaps in this review, stated plainly:

- I did not re-open the eight source screenshots; I relied on the transcriptions in
  `agent-reports/image-extractor.md` and the profile's receipt table.
- I did not execute any command, test, or prototype. The M17 repair is assessed from source
  inspection of `app.js` plus the repair receipt, not from a browser session I ran.
- I did not read the four competition/practice audits or the DeepSeek research doc in full; I read
  the sections the findings depend on.

---

## 1. Executive verdict

**Section A (30 accepted findings): the reconciliation is real and unusually faithful.**
No finding is MISSING. No finding is OVERREACH — which matters, because the common failure mode
in a 38-item reconciliation is quiet scope growth, and it did not happen here. 22 are EXACT, 5 are
SEMANTICALLY_EQUIVALENT with a small residual, and 3 are PARTIAL (M7, M16, M23) for reasons that are
either deliberately owner-gated or now de-risked by the M0 re-scope.

**Section B (8 disputed findings): I support the current position on seven and split on one.**
B3 is HYBRID: the plan no longer *forbids* reuse — which was the strongest single finding in the
original review and is now genuinely fixed — but the three-column reuse inventory still does not
exist, and M0's independent recomputation is exactly the place where that gap bites. Everything
else (B2, B11, M1, M3, M18, M19, M20) is SUPPORT_CURRENT with named residual corrections.

**Section C (M0 Build Alignment Packet): `ACCEPT_WITH_CHANGES`.**
The packet is correctly scoped and correctly forbids M1/M2 output. It fails the "two competent
implementers build the same thing" test for three concrete reasons, all cheap to fix:

1. its seven acceptance IDs (`M0-CON-001` … `M0-UI-001`) **collide with identically named IDs in the
   CE plan that describe different scenarios** — the packet tests the happy path, the CE plan tests
   the failure path, under the same names (`m0-build-alignment-packet-draft.md:133-141` vs
   `docs/plans/2026-08-12-001-...:85-91`);
2. the packet offers **only two outcomes, ready or blocked**, while the owner's own profile makes
   `directional_only` an M0 ceiling for a pre-runtime read
   (`enterprise-experiment-post-analysis-profile.md:121` vs `m0-build-alignment-packet-draft.md:35-38`);
3. the packet's 14-check list **drops four checks the owner's profile names for M0** — CUPED-mode
   identity and non-interchangeability, scorecard/UI reconciliation as a third source, unit and
   relative-percent versus percentage-point arithmetic, and source-change revalidation
   (`enterprise-experiment-post-analysis-profile.md:105-117` vs `m0-build-alignment-packet-draft.md:62-83`).

**Final decision: `GO_FOR_OWNER_ALIGNMENT`, conditioned on edits C1–C9 being applied to the draft
before the Owner review session.** This is a GO to hold the alignment conversation. It is explicitly
**not** a freeze approval and not an implementation authorization.

### The one thing that has not moved since 2026-08-15

The owner's roadmap screenshot requests **"Build + staffing"** for M0 (IMG_3689, transcribed at
`agent-reports/image-extractor.md:66`). Grepping the canonical package for
`person-week|headcount|staffing|FTE|sprint|effort estimate` returns **zero** sizing content; the only
hits are inside review artifacts and one M2 entry-gate mention (`profile:71`). The scope half of B2
is resolved. The pricing half is untouched, and the alignment packet does not add it either. The
Owner cannot approve staffing from this packet as written.

---

## 2. Accepted-finding audit — 30 rows

Verdict key: `EXACT` = the correction landed as written · `SEMANTICALLY_EQUIVALENT` = a different
wording achieves the requested semantics · `PARTIAL` = part landed · `MISSING` · `OVERREACH`.

Abbreviations: `spec` = `final-architecture-spec.md`, `seq` = `implementation-sequencing.md`,
`eval` = `eval-acceptance-plan.md`, `freeze` = `wayfinder/freeze-canonical-domain-policy-contracts.md`,
`intake` = `wayfinder/production-evidence-authority-intake.md`,
`gold` = `wayfinder/evaluation-gold-calibration-contract.md`,
`profile` = `enterprise-experiment-post-analysis-profile.md`, `CE` = `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md`.

| ID | Original requested correction | Current location | Verdict | Residual risk / smallest exact fix |
| --- | --- | --- | --- | --- |
| **B1** | Add a `SymbolAttribution` port admissible only from build provenance or runtime observation, never a model-read diff; file-only identity makes G2 `inconclusive`, not `pass`. | `spec:187` (component), `spec:211` (port), `spec:258` (`AttributionRevision`), `spec:397` (G2 ceiling), `spec:849` (acceptance scenario), `seq:317`, `seq:329` (`ANA-007`). | **EXACT** | None on the text. Note the class boundary: this is spec-addressed and **direction-only** — `SymbolAttribution` sits in U6/G2, outside the funded M0 slice (`seq:202`). It is not implemented or validated anywhere. |
| **B4** | Amend the "projection" language; make canonical Evidence controlling and Trace divergence a diagnostic anomaly; add a §18 row. | `spec:195` (Trace Store holds no canonical truth), `spec:579` ("When Trace and canonical Evidence diverge, Evidence controls"), `spec:630`, `spec:942`. | **SEMANTICALLY_EQUIVALENT** | The §18 failure table has a row for *pin/capture failure* (`spec:741`) but no row for *Trace-versus-Evidence divergence*. The rule is normative at `:579`, so behavior is defined; add one §18 row for symmetry so an implementer reading only §18 reaches it. |
| **B5** | Exclude Trace cross-links from the digested manifest (or freeze `event_id` + retention); add a `TraceStore` component and a distinct append port. | `spec:260` and `spec:708` (separately versioned, **non-digested** Trace annex; "the packet digest never depends on an unfrozen or deletable Trace schema"), `spec:195` (component), `spec:218` (`TraceStore.append`). | **EXACT** | The stronger of the two offered options was chosen. No residual. |
| **B6** | Redaction failure fails closed with a typed no-body envelope and blocked publish; the pre-envelope intake gets owner/ACL/retention/approver or is removed; collector no-disk-write assertion plus a test. | `spec:661` ("Collectors persist no raw pre-redaction object"; typed `redaction_failure`; intake must have owner, ACL, retention, approver, deletion behavior "or it must not exist"), `spec:740`, `seq:309` (`ADP-006`), `intake:76`, `intake:238` (D18). | **EXACT** | None. |
| **B7** | Credential scope as the primary control: per-source write-incapable credentials, a broker outside model execution, egress allowlist, and a **real-credential** write-denial receipt from P2. | `spec:655`, `intake:74`, `intake:236` (D16), `seq:440` (`PROD-008` includes "a real-credential write attempt is denied with a receipt"). | **EXACT** | The mechanism is specified and P2-gated, which is correct. It remains unenforced because no adapter exists. |
| **B8** | Decide the identity model explicitly; synthetic principals for allow/deny; aggregate-only cross-user comparison; render-time per-document ACL against the recipient's live entitlements; time-boxed elevated authority. | `spec:659`, `intake:75` ("Identity and render authorization"), `intake:237` (D17). | **SEMANTICALLY_EQUIVALENT** | `spec:659` requires reauthorizing "every render, object open, and acknowledgement" against live recipient entitlements. It does not say **per-document**. For a packet containing many document bodies, per-object is the load-bearing granularity. Fix: change `:659` to "every render and **every contained document object**". |
| **B9** | Pointers plus keyed digests for erasure-eligible classes; separately keyed store; crypto-shredding with a tombstoned revision; name the retention owner and per-tier maximum before any real read. | `spec:663` (ACL-scoped opaque pointers in separately keyed storage; permitted deletion destroys the scoped key and appends a tombstoned revision), `intake:229` (D09), `intake:238` (D18), `intake:77`. | **EXACT** | Values correctly remain P2/privacy decisions. The legal conflict is now acknowledged rather than invisible, which was the finding. |
| **B10** | Add a `SegmentationContract` to G1 (preregistered set, min size, per-segment MDE, explicit FDR/Bonferroni, tenant-equal vs traffic-weighted); add `segment` to `ClaimRevision`; unpreregistered segment claim is G0-incomplete. | `spec:255` (`SegmentationContract` entity), `spec:249` (`ClaimRevision` now carries `segment`), `spec:396` (G1 requires "preregistered segmentation/multiplicity control"), `spec:432` (tenant-equal and traffic-weighted views). | **SEMANTICALLY_EQUIVALENT** | Two residuals. (a) "multiplicity-control method" is a required *field* but no method is named; the disposition gates the choice to owner/pilot, which is defensible — `Bonferroni|FDR` still return zero hits package-wide. (b) The requested rule **"an unpreregistered segment claim is G0-incomplete"** is not stated anywhere. Fix: add that sentence to `spec:395` (G0 row). Direction-only, not an M0 blocker. |
| **B12** | Replace `seq:343`'s "through the P3-approved interaction contract" with the CE plan's pre-P3 wording. | `seq:388` — `UI-001` is now "a technology-neutral **synthetic** projection reaches exact target proof and its validator receipt **without claiming P3 interaction acceptance**". | **EXACT** | None. The circular dependency is gone. |
| **B13** | Move the trajectory increment into the main tree; index the profile and the DeepSeek doc in `deliverable-index.md` and the authority order. | `deepseek-harness-practices.md:286` (§16 "Agent-agnostic Trace…" now present in the main tree, §17 Bottom line at `:394`); `deliverable-index.md:14,15,16,86,87,88,89`; `spec:955-957` adds all three to Canonical References. | **EXACT** | The orphan condition is closed and the worktree-only risk is eliminated. Fairness note preserved: the profile had self-declared this. |
| **B14** | Add `PROD-007` (per-case/per-window read ceilings; exceedance aborts and emits a Coverage Gap) and `PROD-008` (named halt role with a tested disable path); state that the ceilings bind replay and shadow-read. | `seq:439` (`PROD-007`), `seq:440` (`PROD-008`), `seq:470` (`CAL-003` — replay and shadow-read "stop at their P2/P4 load ceiling or named halt authority and preserve a partial receipt"), `intake:78`, `intake:239` (D19). | **EXACT** | None. |
| **M2** | Enumerate legal `(source_type, edge_type, target_type)` triples with `trace_event` legal only for `cross_links_to`; type `HumanRuling.evidence_citations`; add both to the conformance checklist. | `spec:278` ("The listed triples are closed. `trace_event` is legal only as the source of `cross_links_to`"), `spec:254` (citations restricted to `EvidenceRevision \| DerivedFactRevision \| GateReceipt`), `seq:233` (`POL-010`). | **SEMANTICALLY_EQUIVALENT** | The §22 Final Conformance Checklist (`spec:927-946`) does not carry either item, though both are normative elsewhere and test-covered. Fix: add one checklist bullet — "Typed-edge triples are closed and HumanRuling cites only admitted Evidence, DerivedFact, or GateReceipt IDs." |
| **M4** | Add a G4 predicate that the challenge's `SourceRead` set is disjoint from G3's supporting set, or that it is a predeclared counterfactual. | `spec:399` — G4 pass requires "Its SourceRead set is disjoint from G3 support, or it is a predeclared counterfactual such as a control, holdout, or negative control"; reused G3 support explicitly yields `inconclusive`. | **EXACT** | None. |
| **M5** | Replay/regression unavailable for authority, coverage, or budget reasons yields G6 `inconclusive`, never `not_applicable`. | `spec:401`, `seq:234` (`POL-011`), mirrored at `freeze:274`. | **EXACT** | None. |
| **M6** | Define "material" deterministically — any G1 check on the decision metric's assignment, exposure, join, or definition is material by construction; default unclassified to material. | `spec:396` ("Assignment, exposure, join, metric-definition, and unit/variance mismatches are material by construction; unclassified validity gaps default to material"), `spec:455`. | **EXACT** | The correction was strengthened correctly by adding unit/variance, which links M6 to M24. |
| **M7** | Add `outcome_class = positive \| negative \| neutral \| mixed` with per-class required hypothesis families, and a G1 rule that an underpowered-but-valid read yields `directional_only`. | `spec:238` (`outcome_class` present but "optional … pending the owner scope decision"), `spec:451` (`directional_only` allowed "only when the ExperimentReadContract permits it"). Per-class hypothesis families: absent. | **PARTIAL** | Deliberate: the disposition holds this behind Owner decision "four outcome classes vs miss-only", still open at `profile:453-454`. But note the consequence for M0 — `directional_only` is an M0 ceiling in the owner's own profile (`profile:121`) and the alignment packet has no such state. See C2. |
| **M8** | Either promote `WinLossEvidenceRevision` into the spec with the missing fields, or state in the scope section that the MVP does not satisfy win/loss and name M2. Do not leave both claims standing. | `spec:101` (§3.3 Deferred: "M2 Win/Loss Evidence and its query-level comparison packet. M2 is direction-only and requires a later owner funding decision"), `spec:38`, `spec:257` (excluded from `FlightReadinessPacket`). | **EXACT** | Option 2 taken cleanly. The two-standing-claims problem is gone. |
| **M9** | G1 must check arm parity on index generation, serving alias, ACL snapshot, and effective pipeline; divergence caps Cause at `suspected` and blocks win/loss comparability. | `spec:396` ("arm parity for index generation/serving alias/ACL snapshot/effective pipeline"; "Arm-parity divergence caps Cause at `suspected` and blocks query comparability"), `spec:434`, `seq:330` (`ANA-008`). | **EXACT** | None. |
| **M10** | Add compositional SRM and zero-result-rate delta to G1's required checks. | `spec:396`, `spec:432`, `spec:433`, `seq:330` (`ANA-008`), `eval:150`. | **EXACT** | None. |
| **M11** | Require a position-bias-corrected estimator with a named propensity source, or an interleaving arm, before any click-derived metric supports a G3 mechanism claim; add interleaving to G4's enumeration. | `spec:398` (G3: "Click-derived support is admissible only with a named position-bias/propensity correction source or an authorized interleaving design"), `spec:399` (G4 inputs now list interleaving), `seq:331` (`ANA-009`). | **EXACT** | None. |
| **M12** | Add `E15 Judgment / offline-eval` to the intake, plus an offline-online divergence hypothesis family in the plane list. | `intake:104` (E15 row), `intake:240` (D20), `spec:259` (`JudgmentEvidenceRevision`), `spec:435` (retrieval plane), `spec:438` (concurrent-change plane includes offline-online divergence). | **EXACT** | Correctly marked "unavailable until P2/P4 authority acknowledges the exact source and use". |
| **M13** | Adopt `index \| connector \| permission \| presentation \| telemetry` subtypes with their own exact-identity rows. | `spec:247` (entity), `spec:466`, `spec:477-481` (five exact-identity rows), `spec:438`. | **SEMANTICALLY_EQUIVALENT** | Adopted as **proposed** subtypes behind an Engineering/domain-owner schema gate, not as frozen types. That matches the disposition and is the right call pre-P2; the important half — "must not be collapsed into misleading generic `data` when exact identity differs" (`spec:466`) — is normative now. |
| **M14** | Define `uncalibrated_fixture` as an explicit lexicographic ordering over gate-derived booleans, recomputable by a reviewer before any weights exist. | `spec:569` (exact identity → G2 status → validated mechanism support → fewer material contradictions → stable candidate ID; "Gate ceilings are applied before this comparator, never as compensating weights"), `seq:332` (`ANA-010`). | **EXACT** | The comparator matches the requested order element for element. |
| **M15** | Annotate each veto with `detector: deterministic \| human \| not-yet-implemented`; state that exact-target acceptance is out of MVP scope until P2 or the archival receipt closes. | `eval:181`, `eval:277`, `seq:418` (`EVAL-012`), `gold:169`, `spec:832`; exact-target scoping at `eval:70` and `spec:769`. | **EXACT** | None. |
| **M16** | Specify the leakage detector concretely with preregistered thresholds; require a prompt-freeze receipt dated **before case selection**; exclude widely published incidents. | `eval:57` and `gold:76` (exact-string, n-gram, symbol, filename, prompt, retrieval-index, cache checks; published incidents excluded), `seq:417` (`EVAL-011`). | **PARTIAL** | Two gaps survive. (a) The prompt/config digest is sealed "before **case exposure**" (`eval:57`), not before case **selection** — which is the window in which curator knowledge of the resolution biases which case is chosen. (b) **Case-selection bias still has no control**: `gold:76` says "A case curator freezes the investigation-time snapshot" with no independence requirement, while fixture authors *do* have one (`eval:45`). Fix: extend the fixture-author/evaluator independence receipt at `eval:45` to cover the blind-case curator, and move the prompt-freeze to precede case selection. Direction-only; not an M0 blocker. |
| **M17** | Fix `app.js:124` before any live review; mark the inert controls non-functional in the README so a reviewer does not score them. | Repaired: `app.js:81`/`:297-301` use a distinct `data-claim` path; `app.js:173` returns an explicit "No synthetic Claim record exists for this identifier" instead of falling back. Disclosed: `prototypes/.../README.md:74` and `m17-interaction-repair.md:11-28`, `:38-48`. | **EXACT** | The correction was over-delivered relative to the ledger. **The ledger row is now stale**: `03-codex-disposition.md:47` still says "Prototype implementation changes … are not in this patch", but they were made and receipted. Fix: update that row. Separately, the P3 ticket (`prototype-observability-first-review-surface.md`) never records the two defects as blockers, as the disposition promised — moot now that they are fixed, but the ticket should cite the repair receipt. |
| **M21** | The manifest enumerates `(revision_id, content_digest)` pairs; each revision records `prev_digest` for its logical ID. | `spec:229` ("predecessor digest for the same logical ID"), `spec:260` ("manifest of `(revision_id, content_digest)` pairs"), `seq:271` (`EVD-006`), `seq:290` (`REV-006`), `eval:152`. | **EXACT** | None. |
| **M22** | Replace the unbounded universal negative with a positive capability allowlist, per-method denied-write receipts, and an import-graph assertion. | `seq:252` — `SKEL-004` now reads "the package exposes only the positive capability allowlist; every adapter method rejects writes with a typed denial receipt, and an import-graph check finds no reachable legacy runtime, arbitrary execution, publication, or mutation capability." Mirrored for the funded slice at `seq:53` (`M0-F0`) and `CE:31`. | **EXACT** | All three requested elements present. This is the single most important test in the funded slice and it is now falsifiable. |
| **M23** | Scope pre-P2 U6 to interfaces and unknown-authority failure paths; defer the matcher's feature set to a post-P2 `U6b`, stated explicitly. | `seq:317` still builds the `scope × interval × rollout` matcher, mapping precedence, normalization, and ranking before P2; `seq:334` only requires that "production mapping is explicitly blocked, never guessed". No `U6b` exists. | **PARTIAL** | The literal correction was not applied. **But the risk it targeted is now largely gone by a different route**: U6 is direction-only and unfunded (`seq:202`, `seq:483`), so no pre-P2 matcher work is authorized at all. Fix if M1 is ever funded: split U6 into `U6a` (ports, unknown/conflict failure paths) and `U6b` (matcher feature set, post-P2). Not an M0 issue. |
| **M24** | Require the variance estimator and its unit-of-analysis to be named in `ExperimentReadContract`; make a mismatch a G1 validity failure. | `spec:256` (`ExperimentReadContract` requires "Assignment and analysis units, estimator, ratio-metric variance method"), `spec:396` (unit/variance mismatch material by construction), `spec:433`, `seq:330` (`ANA-008`), `eval:150`, `CE:32`. | **EXACT** | This one propagated correctly into the **funded** slice, which most of the others did not. `M0-F1`/`M0-F3` both carry it (`seq:54`, `seq:56`). |

**Section A tally:** 22 EXACT · 5 SEMANTICALLY_EQUIVALENT · 3 PARTIAL · 0 MISSING · 0 OVERREACH.

**Class boundary, stated once and applied to all 30:** every row above is **spec-addressed only**.
Exactly one is implemented (M17, in a throwaway prototype). None is production-validated. The
2026-08-16 owner ruling covers scope, not any of these corrections.

---

## 3. Disputed-finding adjudication — 8 rows

| ID | Current position | Verdict | Strongest evidence for the current position | Strongest counterargument | Falsifier | Required action |
| --- | --- | --- | --- | --- | --- | --- |
| **B2** | Preserve the broader architecture; fund and build M0 Flight Readiness only. Owner-confirmed 2026-08-16. | **SUPPORT_CURRENT** on scope; **OWNER_DECISION_REQUIRED** on the unpriced half | The re-cut is complete and internally consistent: `planning-decision-packet.md:9,93`; `spec:34-38`; `seq:7,49-58`; `eval:8-10`; `CE:20,31-36`; `deliverable-index.md:113`. `M0-F0`–`M0-F5` is a real, dependency-ordered, testable backlog with exit evidence per unit — materially smaller and better bounded than the original review's own proposed `D0 + U1' + U2` slice. | The original B2 had two halves. Only one was answered. The owner's screenshot requests **"Build + staffing"** (IMG_3689, `agent-reports/image-extractor.md:66`), and the package still carries **zero** duration, headcount, or cost content. The alignment packet adds none either. An Owner asked to approve staffing has nothing to approve against. | Produce a per-unit estimate for `M0-F0`–`M0-F5` (headcount × duration, with the stated uncertainty) and B2 is fully closed. If the Owner says staffing is decided outside this package, B2 closes by scope instead. | Attach a sizing line to each of the six `M0-F*` rows in `seq:51-58`, or record explicitly that sizing lives outside this package. Do not hold the alignment session without one of the two. |
| **B3** | Protected legacy paths are read-only references; independently validated domain assets may be reused after interface, provenance, tests, security, and license review. | **HYBRID** | This is the biggest genuine repair in the reconciliation. `seq:151`'s outright prohibition is gone. `seq:45`, `spec:901`, and `CE:101` now permit reading and independently validating domain assets and clean-room reimplementation behind new contracts, with a named review gate for direct reuse. The clean-room boundary is the right default for a greenfield package. | The **three-column inventory the finding actually asked for still does not exist**, and neither does the named component: `search-relevance-experiment-analysis` returns zero hits outside review artifacts. `.agents/skills/sma/references/metric_registry/` and `schema_catalog/` are never named as candidate assets in any canonical document. This is not abstract — M0's `metric registration` check and `independent recomputation` (`m0-build-alignment-packet-draft.md:71,79`; `seq:56`) are precisely the work the owner said is already verified via basis-table routing (IMG_3695). Building M0 without the inventory means re-deriving assets that exist, or silently reusing them without the review the policy now requires. The only current acknowledgement is one clause in the P2 ticket (`establish-production-evidence-authority.md:12`, "the independent recomputation/basis-table path"). | Write the inventory. If every row lands in "read-only reference, clean-room reimplement", the current position is fully vindicated and nothing changes. If any row lands in "direct reuse", the review gate must fire before `M0-F1`. | Add a one-page reuse inventory before `M0-F1` with one row per asset (metric registry files, schema catalog files, basis-table routing) and one of three dispositions: `read-only reference` / `clean-room reimplement` / `direct reuse pending interface+provenance+test+security+license review`. Owner decides whether M0 fixtures may be **derived from** those files. |
| **B11** | Missing fixture files were not a planning blocker before implementation authorization; baseline, decoy, difficulty, and author/evaluator conflict controls were accepted. | **SUPPORT_CURRENT** on timing; **HYBRID** on binding | Correct on timing: demanding fixture files before implementation is authorized inverts the order. And the substantive controls did land — `eval:43-45` (always-abstain and most-recent-deploy baselines, adversarial decoys, sealed author/evaluator independence), `eval:221` (reject an indistinguishable suite **before** Agent scoring), `seq:415-416` (`EVAL-009`, `EVAL-010`), `gold:88`, `spec:798`, `spec:830`. | **Those controls do not bind the funded slice.** They sit in `eval:§3.1`/`§8.A` and the calibration contract, which are P4-scoped and written around the direction-only blind causal case. The M0 rungs — `M0-F5` (`seq:58`), `eval:§8.M0` (`eval:205-217`), and the alignment packet's `§9` — contain **no baseline arm, no decoy, and no author-independence requirement at all**. The two baselines named in the eval plan are also the wrong ones for M0: the M0-relevant trivial baselines are *always-ready* and *always-blocked*. A fixture set that an always-blocked stub passes teaches nothing, and nothing currently forbids shipping one. (Glob confirms zero fixture files still exist on disk — expected and fine at this stage.) | Add always-ready and always-blocked arms to the M0 fixture suite. If the M0 suite cannot separate the real evaluator from both, the suite is rejected before scoring — exactly the rule `eval:221` already states for the causal suite. | Extend `seq:58` (`M0-F5`) and `eval:205-217` with the two M0 trivial baselines plus a fixture-author independence receipt, and mirror them into the alignment packet `§9`. See C6. |
| **M1** | Never mutate a confirmed `VerdictEvent`; append a superseding revision inside an active generation; require a new linked generation for a closed generation or sealed packet. | **SUPPORT_CURRENT** | This is a better answer than the original correction. Adding a raw `confirmed -> inconclusive` edge would have made the system's single hard veto silently reversible; the generation split preserves immutable history while giving false-`confirmed` a real retraction path. Fully specified at `spec:404`, `spec:142` (invariant 7), `seq:235` (`POL-012`), `seq:374` (`A-010`). | **The closed policy contract, which outranks the spec, still contradicts it.** `freeze:171-173` enumerates the legal transitions with **no edge out of `confirmed`**, and `freeze:174` adds prose about a new verdict revision without the active-versus-closed-generation split. Authority order at `spec:11-17` puts the closed freeze resolution **above** the spec, so an implementer following authority correctly reads `freeze:171-173` and implements no exit. | Show a `POL-012`-conformant implementation derived only from the freeze document. It cannot be done. | Add to `freeze:174`: "Within an active generation, contradicting validated Evidence appends superseding Claim and VerdictEvent revisions. For a closed generation or sealed closed packet, retraction requires a new linked generation." One sentence, in the higher-authority document. Direction-only — M0 emits no verdicts. |
| **M3** | Keep a syntactically valid `not_applied` diff; control risk through capability isolation, human-only delivery, and prohibition of automation consumers rather than corrupting the artifact. | **SUPPORT_CURRENT** | Deliberately corrupting the diff is the weaker control: it degrades human reviewability — the entire purpose of the artifact — and invites a five-line de-sentinel script, which converts a hard boundary into a speed bump. Capability isolation is enforceable and testable: `spec:497` prohibits apply, commit, PR, deploy, rollback, webhook, queue, polling, "and no automation-consumable action feed"; `seq:373` (`A-009`) tests exactly that; `spec:496` forbids writing into a worktree. | The original M3 also asked for a **publish-barrier predicate that the recipient channel is a human review surface**. `spec:690` only requires that "recipient and projection authorization can be evaluated" — an automation service account can hold a valid authorization. Channel *type* is not checked at the barrier. | Register an automation service principal as a packet recipient. If the publish barrier admits it, the control is incomplete. | Add one publish-barrier condition at `spec:689-690`: "the recipient channel is a registered human review surface, not an automation endpoint." Direction-only — M0 produces no diff (`spec:257`). |
| **M18** | Prohibit bare digests for secret, confidential, or low-entropy values; do not generalize to every public full-file or image digest. | **SUPPORT_CURRENT** | The narrowing is correct. A blanket HMAC requirement would break legitimate public-artifact byte-identity verification and add key-management burden with no threat reduction. The line is drawn precisely at `spec:672`: ordinary hashes for public software and approved releasable artifacts; opaque ACL-scoped receipts for confidential content; versioned tenant/case/field-scoped keyed commitments for equality testing; "A digest proves byte identity only, not authority, membership, truth, or causality." | **The rule as written is already violated inside the package.** `profile:27-34` publishes eight bare SHA-256 digests of the owner's internal roadmap and tech-spec screenshots. Those are not public software and not approved releasable artifacts — they are confidential internal material, and the digests are a confirmation oracle for anyone holding a copy. The reconciliation adopted the rule and never applied it to the one concrete instance the original finding named. | Classify the eight screenshots. If Security/Privacy rules them releasable, the row is closed as written. If not, the digests must move behind an ACL-scoped receipt. | Route `profile:27-34` to the Security/Privacy Owner for classification before this package is shared outside the team. Note this also touches the share-safe publication manifest. |
| **M19** | Limit Trace collection to authorized Data Agent-owned enterprise-managed runtime; prohibit unrelated engineer IDE/session monitoring. | **SUPPORT_CURRENT** | This is a stronger control than the original correction, which only asked for a DPIA and a query-authority model. `spec:673` **prohibits the collection pattern outright**: no personal IDE or endpoint installation, no unrelated-session collection, no employee performance or behavior monitoring; Trace queries require case-scoped purpose, named roles, per-render authorization, audit, retention, and deletion; any future endpoint collection needs separate authority plus jurisdiction-dependent privacy or labor review. Removing the fleet removes the DPIA trigger, which is the right order of operations. | The design that motivated the finding still sits in the package as readable research: `deepseek-harness-practices.md:286-392` describes host hooks across Codex, Claude Code, and Cursor, with a "direct source reuse plan" at §16.3. It is labeled supporting research and cannot override `spec:673`, but an implementer who opens it first sees a build plan for the prohibited pattern. | If a future implementer produces a collector spec citing §16.3 without `spec:673`, the labeling was insufficient. | Add one pointer line at the head of `deepseek-harness-practices.md:286`: "Collection boundary is controlled by `final-architecture-spec.md:673`; the host topology below is research, not an authorized deployment pattern." Out of M0 scope entirely — M0 has no Trace. |
| **M20** | Require minimal Data Agent RunAttempt receipts; cross-host Trace is optional, and its absence blocks only assertions that depend on it while remaining a visible Coverage Gap elsewhere. | **SUPPORT_CURRENT** | The narrowing is right and the original was overbroad. Adding a global capture receipt to the publish barrier would let a Trace-collector outage block an otherwise Evidence-complete packet — importing a diagnostic dependency into the canonical path, which is exactly the Trace/Evidence confusion B4 exists to prevent. The current split is clean: `spec:674` (mandatory minimal RunAttempt receipt), `spec:630`, `spec:691-695`, `spec:741`. | The word **"predeclared"** is load-bearing and unowned. `spec:692` omits or marks unsupported "a Trace-dependent operational assertion or **required diagnostic view**", but nothing says **who** declares that set or **when**. If the dependent-assertion set can be narrowed after a capture failure is observed, the fail-open the original finding identified returns through the back door — you simply declare the failed assertion non-dependent. | Attempt to publish after a capture failure by editing the dependent-assertion list post hoc. If the barrier accepts it, the control is circular. | Add to `spec:692`: "The Trace-dependent assertion and view set is declared in the frozen generation inputs (or the sealed rung authorization) and cannot be narrowed after a capture failure." Direction-only for now. |

**Section B tally:** 6 SUPPORT_CURRENT · 2 HYBRID (B3, B11) · 0 SUPPORT_ORIGINAL · B2 additionally carries one OWNER_DECISION_REQUIRED item (sizing).

Per the handoff instruction, I did not reopen B2's scope ruling. The B2 row above challenges only
the implementation ambiguity that survives the Owner's decision.

---

## 4. M0 Build Alignment Packet — verdict and exact corrections

**Verdict: `ACCEPT_WITH_CHANGES`.**

### 4.1 Against the six criteria

| # | Criterion | Assessment |
| --- | --- | --- |
| 1 | Narrow enough to keep M1/M2 out of the first build | **Yes.** `§2:29` and `§6:99` are unambiguous, and `§9`'s `M0-PKT-001` makes contamination a schema/policy rejection rather than a review note. This matches `spec:257`, `spec:408`, and `seq:521`. The best line in the packet is `§6:99`'s explicit forbidden list including "Trace-only fact". |
| 2 | Concrete enough that two competent implementers build materially equivalent behavior | **No.** Three defects, all mechanical: the acceptance-ID collision with the CE plan (C1), the missing third outcome state (C2), and four dropped owner-named checks (C3). Also `§4` and `§5` never say which check consumes which contract field, so the mapping is left to the implementer. |
| 3 | Represents the real post-experiment workflow without pretending M0 does causal analysis | **Mostly.** `§3:33` is a genuinely good statement of the user's job. But `§6:99` forbids "Recommendation" outright, while `spec:137` (invariant 2) and `profile:124` permit `validity_fix \| instrumentation_fix \| data_quality_fix` for an invalid experiment. The packet's "next safe action" (`§6:94`) is left untyped, so it is unclear whether it is one of those Recommendation kinds or free text. See C4. |
| 4 | First screen, packet content, forbidden outputs, vertical spike, and acceptance scenarios testable | **Partly.** `§6` and `§7` are testable. `§8`'s spike is testable. `§9` is not, because of C1 and because `M0-UI-001` requires a "named reviewer" — a P3 event that `seq:481` forbids before P3 closes and that has no M0 prototype to run against (`prototype-observability-first-review-surface.md:58`). See C5. |
| 5 | Leaves the right decisions with Owner, Engineering, P2, P3, P4 | **Partly.** `§11` and `§12` handle Owner and Engineering well. P2/P3/P4 are **never named in the packet**, so the reader cannot tell which of the 14 checks are P2-blocked, that live review is P3, or that fixture/baseline design is P4-adjacent. See C7. |
| 6 | Creates a real stop-and-review gate before implementation expands | **Partly.** `§8:129` states the stop and correctly rejects a green unit test as acceptance. But there are no deterministic halt triggers and no budget cap — the original review's six stop conditions (`00-final-review.md:675-684`) are not carried over. A gate with no trip wire is a request, not a gate. See C8. |

### 4.2 Can the vertical spike be the acceptance artifact?

**Partly — and the packet must say so explicitly.**

The `§8` spike (`ExperimentReadContract → authorized fixture read → independent recomputation →
deterministic checks → immutable FlightReadinessPacket → packet-centered review screen`) is a
sufficient acceptance artifact for six of the seven `§9` scenarios: `M0-CON-001`, `M0-READ-001`,
`M0-VAL-001`, `M0-DET-001`, `M0-PKT-001`, and `M0-SEC-001`. All six are deterministic and hermetic.

It is **not** sufficient for `M0-UI-001`, which requires a named human reviewer. That is a P3 event
(`seq:481`: "M0 live review acceptance — No. P3 must accept the packet-centered M0 review interaction
with real reviewers"), and the M0 packet-centered prototype does not exist — the current Evidence
Room is explicitly direction-only M1 research
(`prototype-observability-first-review-surface.md:12,58`; `deliverable-index.md:51`).

Split it, as the CE plan already does: `M0-UI-001` becomes the pre-P3 synthetic proof
(`CE:91` — reaches the exact source and recomputation receipt without implying a cause), and a new
`M0-UI-101` becomes the post-P3 named-reviewer receipt.

### 4.3 Exact edits required before Owner review

**C1 — Resolve the acceptance-ID collision.** The packet's `§9` IDs and the CE plan's `CE:85-91`
IDs are identical strings describing **different scenarios**: the packet tests happy paths
(`M0-CON-001` = "complete, internally consistent frozen contract"), the CE plan tests failure paths
(`M0-CON-001` = "missing identity … fails contract validation"). Same for `M0-READ-001` and
`M0-SEC-001`. This is the m8-class identifier collision the original review already flagged once.
Fix: renumber the packet's positive cases to `M0-*-002` and state that `§9` **extends** `CE:85-91`
rather than restating it, or delete `§9` and cite the CE plan as the single test registry. One
registry, one meaning per ID.

**C2 — Add the third outcome state.** `§3:35-38` offers only `Ready for post-analysis` and
`Blocked`. The owner's own M0 ceiling requires a third: "Before the preregistered runtime completes,
the result is `directional_only` and cannot pass the decision metric" (`profile:121`), and the spec
carries `directional_only` at `spec:451`. Fix: add `directional_only` to `§3` with its exact meaning
(valid read, insufficient basis for a decision-metric conclusion), and add the corresponding
`ExperimentReadContract` permission field to `§4`.

**C3 — Restore four owner-named M0 checks.** `§5:62-83` has 14 checks; `profile:105-117` names four
that are missing or under-specified:
  - **CUPED-mode identity and non-interchangeability** (`profile:108,122`) — packet check 10 says
    "estimator and variance-method consistency", which does not carry the hard rule that adjusted and
    unadjusted reads must never be silently substituted. Add it as its own check.
  - **Primary-source versus scorecard/UI reconciliation** (`profile:111`) — packet check 12 compares
    reported versus independently recomputed. The owner names a **third** comparison against the
    scorecard/UI surface. Add it or state explicitly that it is out of M0.
  - **Numerator/denominator/unit/ratio/relative-percent/percentage-point checks** (`profile:113`) —
    packet check 8 covers "join-key and denominator integrity" only. Relative-percent versus
    percentage-point confusion is a top source of real DS error and is cheap to check. Add it.
  - **Source-change revalidation for meaning, coverage, and attribution** (`profile:116`) — packet
    check 11 covers "source and lineage identity", which is not the same as revalidating semantics
    after a source change. Add it.

**C4 — Type the "next safe action".** `§6:94` lists "next safe action and reopen condition" while
`§6:99` forbids "Recommendation". Reconcile with `spec:137` and `profile:124-125`. Fix: state that
the next safe action is a typed field of kind
`evidence_collection \| contract_correction \| validity_fix \| instrumentation_fix \| data_quality_fix`,
that it carries no exact production target and no diff, and that whether a bounded unapplied
instrumentation or data-quality proposal is permitted remains the open Owner decision recorded at
`profile:125`.

**C5 — Split `M0-UI-001`.** As in 4.2: pre-P3 synthetic proof keeps `M0-UI-001` and matches `CE:91`;
the named-reviewer scenario becomes `M0-UI-101` and is explicitly marked P3-gated per `seq:481`.

**C6 — Bind the B11 controls to M0.** Add to `§9`: preregistered **always-ready** and
**always-blocked** trivial baselines; a suite that cannot materially distinguish the evaluator from
both is rejected before scoring (mirroring `eval:221`); and a fixture-author independence receipt
(mirroring `eval:45`). Without this, the accepted B11 disposition does not reach the funded slice.

**C7 — Name the gates.** Add a short subsection mapping each `§5` check and each `§9` scenario to
`fixture-only now` versus `P2-gated` / `P3-gated` / `P4-gated`, citing `seq:479-488`. In particular,
`§5` check 13 ("authorization, tenant/ACL, recipient, and redaction status") needs to say what
"authorized" means against a fixture, since no real credential or ACL exists in the M0 slice.

**C8 — Add deterministic stop conditions and a budget cap to `§8`.** Import the six from
`00-final-review.md:675-684`, adapted: (1) the fail-closed default is bypassed by an enum alias or a
default branch; (2) any file appears under `adapters/production/`; (3) any test requires a network
socket, a secret, or a path outside the package; (4) the packet digest is not byte-stable across two
clean runs; (5) the M0 fixture set cannot produce a *failing* case for each of SRM, CUPED-mode
mismatch, unregistered decision metric, and pre-runtime invocation; (6) the slice exceeds its budget
without a green hermetic command. Any one firing halts the spike and returns to the Owner.

**C9 — Add the two missing Owner decisions to `§11`.** The canonical meaning of `flight` and its
boundary from experiment, rollout, exposure window, and analysis window (`profile:453`); and whether
exactly one decision metric is required or an approved co-primary policy is allowed
(`profile:454`, `profile:89`). Both are still open, both are M0-critical, and the packet currently
uses "flight" and "primary metric" (singular) as if they were settled. See §5 below.

### 4.4 Missing acceptance examples and adversarial cases

Add to `§9`:

- **`M0-PRE-001` — pre-runtime read.** A contract whose observed runtime is shorter than the
  preregistered runtime yields `directional_only`, never `Ready` (`profile:121`).
- **`M0-CUP-001` — CUPED-mode mismatch.** The reported read is CUPED-adjusted and the recomputation
  is unadjusted (or the reverse). The packet must block and preserve both values; silent
  substitution is a hard failure (`profile:122`).
- **`M0-UNIT-001` — unit mismatch.** A user-randomized experiment with a query-level ratio metric and
  no named clustered or delta-method variance estimator fails check 10 (`spec:396`, `M24`).
- **`M0-BASE-001` — trivial-baseline rejection.** An always-blocked stub is run against the fixture
  suite before the real evaluator is scored; if it passes, the suite is rejected (C6).
- **`M0-SUP-001` — supersession.** A corrected source read after sealing produces a **superseding**
  packet with a new digest and invalidates the prior acknowledgement, rather than editing the sealed
  packet (`spec:194`, `seq:289`). The packet currently has no supersession scenario at all, despite
  `§6:97` requiring a supersession link.
- **`M0-CONF-001` — reviewer conflict.** Two named reviewers disagree on materiality. The packet must
  preserve both positions and stay blocked; it must not resolve by seniority or timeout
  (`freeze:306`).
- **Adversarial:** a contract that is internally consistent and complete but names a metric whose
  registered definition version differs from the one the source computed — everything looks green
  except check 3. This is the M0 analogue of the decoy case B11 requires, and it is the failure mode
  most likely to produce a false `Ready`.

### 4.5 Ten Owner questions, ranked

1. Should M0 have a third outcome, `directional_only`, for a valid but pre-runtime or underpowered
   read — or must every such case be `Blocked`? (C2; `profile:121`)
2. What exactly is a **flight**, and where is its boundary against experiment, rollout, exposure
   window, and analysis window? Every M0 check depends on this. (`profile:453`)
3. Exactly one decision metric, or an approved co-primary policy? If co-primary, what is the
   combination rule? (`profile:454`, `profile:89`)
4. May M0 fixtures be **derived from** the existing `metric_registry/` and `schema_catalog/`
   references, or must they be authored independently? (B3)
5. Is the "next safe action" allowed to name a bounded instrumentation or data-quality fix, or is it
   restricted to evidence collection and contract correction? (`profile:125`, C4)
6. Which named roles review and approve an M0 packet in the real organization, and may the reviewer
   and approver be the same person for M0? (packet `§11.2`)
7. Which real, de-identified past experiment becomes the first fixture, and who signs its
   de-identification receipt?
8. Is the `§7` first-screen order (decision → blocking checks → primary-read comparison →
   Coverage Gaps → next safe action → receipts) the order in which you actually decide?
9. What is the M0 budget — headcount and duration — so "the slice exceeds its budget" is a real stop
   condition and the "Build + staffing" ask has an answer? (B2, C8)
10. Should the eight internal screenshot SHA-256 digests at `profile:27-34` stay in a package that may
    be shared, given the digest policy you just accepted at `spec:672`? (M18)

### 4.6 Proposed freeze / signoff record

Create `reviews/2026-08-16-opus5-m0-alignment/m0-alignment-freeze-record.md` at acceptance, containing:

| Field | Rule |
| --- | --- |
| `frozen_artifact` | Exact path **and SHA-256** of the accepted `m0-build-alignment-packet-draft.md` revision. The digest, not the filename, is the contract. |
| `revision` | `m0-alignment-vN`, monotonic. |
| `party_records` | One row per party (Owner, Opus 5, Codex): verdict `accept \| accept_with_changes \| reject`, sections reviewed, requested changes, unresolved decisions, conflicts of interpretation, reviewed digest, timestamp. A verdict recorded against a digest other than `frozen_artifact` does not count. |
| `open_decisions` | The `§11` list plus C9's two additions, each carrying `open \| resolved` and the resolving Owner statement. Freeze is permitted with items still `open` **only** if each names the M0 behavior that is blocked until it resolves. |
| `gate_map` | Per `§5` check and `§9` scenario: `fixture-only \| P2 \| P3 \| P4`. (C7) |
| `test_registry_binding` | Explicit statement that `CE:85-91` is the single acceptance-ID registry and that the packet extends rather than restates it. (C1) |
| `stop_conditions` | The six from C8, verbatim, with the named halt authority. |
| `change_control` | Any change to the M0 question, required inputs, check meaning, packet content, forbidden outputs, first-screen hierarchy, or acceptance scenarios creates `m0-alignment-v(N+1)` and requires a new Owner signature. Implementation convenience, framework defaults, legacy architecture, and reviewer preference are never sufficient cause. (`§12`, made enforceable) |
| `drift_check` | Before each `M0-F*` unit starts, the implementer records the frozen digest in that unit's exit evidence. A mismatch halts the unit. This is the mechanism that actually prevents silent drift — a prose commitment does not. |

---

## 5. Unresolved Owner decisions

Carried forward from `00-final-review.md:613-631`, with current status verified in the worktree.

| # | Decision | Status | M0-critical? | Evidence |
| --- | --- | --- | --- | --- |
| 1 | Is M0 the first build slice? | **Resolved 2026-08-16** | — | `planning-decision-packet.md:93`; `spec:34-38` |
| 2 | Does Scenario A cover only metric misses or all four outcome classes? | Open | Indirectly — drives `directional_only` | `spec:238` ("pending the owner scope decision"); `profile:452` |
| 3 | Is M2 in the first MVP? | **Resolved — no** | — | `spec:101`; `planning-decision-packet.md:10` |
| 4 | Canonical meaning of `flight` vs experiment, rollout, exposure window, analysis window | **Open** | **Yes** | `profile:453`. Not in the alignment packet's `§11`. C9. |
| 5 | One decision metric vs an approved co-primary policy | **Open** | **Yes** | `profile:454`, `profile:89`. Not in `§11`. C9. |
| 6 | May an invalid experiment carry a bounded unapplied instrumentation or data-quality fix? | Open | **Yes** | `profile:125`; conflicts with packet `§6:99`. C4. |
| 7 | Which raw query, result, SBS, and Trace fields may enter the packet vs remain digest-linked | Open, P2-routed | Partly — fixture de-identification | `spec:661`; `intake:228` (D08). `§11.5` covers screen placement, not field policy. |
| 8 | Is the first review screen milestone/packet centered? | **Resolved — packet-centered** | — | `planning-decision-packet.md:22`; `spec:581-587`; packet `§7` |
| 9 | Named approver per milestone; may roles overlap? | Open | **Yes** | packet `§11.2`; `spec:132` requires Causal Reviewer ≠ Action Approver but is silent on M0 reviewer/approver overlap |
| 10 | Is a central Trace store collecting session-attributable engineer IDE activity acceptable? | **Resolved by prohibition** | No — M0 has no Trace | `spec:673` |
| 11 | Retention and erasure posture for packets containing document text | Open, P2-routed | Low for M0 (fixtures only) | `spec:663`; `intake:229,238` |
| **12 (new)** | M0 sizing — headcount and duration, against the "Build + staffing" ask | **Open** | **Yes** | Zero sizing content package-wide; IMG_3689 via `agent-reports/image-extractor.md:66` |
| **13 (new)** | May M0 fixtures and the recomputation path be derived from the existing protected domain assets? | **Open** | **Yes** | B3; `seq:45`, `spec:901`, `establish-production-evidence-authority.md:12` |
| **14 (new)** | Classification of the eight internal screenshot digests under the newly accepted digest policy | **Open** | No | M18; `profile:27-34` vs `spec:672` |

Decisions 4, 5, 6, 9, 12, and 13 all block M0 implementation start. Four of the six are absent from
the alignment packet's `§11`.

**Engineering proposals needing a named owner, not Owner sign-off** (unchanged): schema encoding,
storage, language, framework, `TraceEnvelope` serialization, adapter API, UI stack, and whether the
three milestone packets share one envelope. Correctly held as proposals at `seq:19` and
`CE:20`.

---

## 6. Final decision

### `GO_FOR_OWNER_ALIGNMENT`

**Conditioned on C1–C9 being applied to `m0-build-alignment-packet-draft.md` before the Owner review
session, and on the six blocking Owner decisions (4, 5, 6, 9, 12, 13) being placed on that session's
agenda.**

Reasoning. The reconciliation quality is high enough to justify the Owner's time: 30 of 30 accepted
findings landed with no MISSING and no OVERREACH, the two structurally worst findings from
2026-08-15 — the reuse prohibition and the unreachable requirement documents — are genuinely fixed,
and the M0 re-cut produced a smaller, better-bounded first slice than the original review itself
proposed. The alignment packet's defects are specification defects with named one-line fixes, not
design errors.

What this GO is **not**:

- It is not a freeze approval. The packet fails criterion 2 today; two competent implementers would
  build different M0 behavior because of C1, C2, and C3.
- It is not implementation authorization. `seq:576` and `spec:965` both require a separate explicit
  Owner start decision, and I concur.
- It does not close P2, P3, or P4, and it does not convert any spec-addressed finding into an
  implemented or validated one.

If the Owner prefers to hold the alignment session on the packet as it stands, the session should
open by resolving C2 and C9, because every other question in `§11` reads differently once `flight`,
the decision-metric policy, and the third outcome state are settled.

---

## 7. Statement on implementation and validation

**No implementation occurred and no production validation occurred.**

During this review I read files and ran content searches. I did not write, modify, or delete any
canonical product or specification document. I did not run, build, or test any code. I did not start
the prototype. I did not access any production source, credential, network service, or company data.
I created no commit, branch, push, or PR. I installed nothing and changed no global settings. I
spawned no subagents; this is one independent Opus 5 judgment.

The only files written by this review are `opus5-review.md` and `status.json` inside
`reviews/2026-08-16-opus5-m0-alignment/`.

Every judgment above is **specification review against untracked worktree text**. Nothing here
demonstrates that the Data Agent works, that any check is correct in practice, or that any control
holds under a real production credential. The single piece of executed evidence anywhere in this
package is the M17 prototype repair, and that is a throwaway synthetic artifact whose own receipt
states that owner live acceptance remains pending.

---

# Prior Review Session Reconstruction

*Added 2026-08-16 under the Phase 2 Addendum in `handoff.md:38-94`. This section reconstructs how
the 2026-08-15 Opus 5 review (session `20f39af5-ad53-4f82-9b12-830c583dc175`) was actually
performed, from its own local raw records, and tests the Phase 1 audit above against that record.
Session archaeology only: nothing was resumed, mutated, or committed.*

## P0. Continuity gap in this review's own record — stated first, because it is the honest frame

**Phase 1 of this review has no raw transcript.** The Phase 1 Opus 5 session wrote
`opus5-review.md` and `status.json` (mtimes 2026-08-17T04:55Z and 04:56Z) but its CLI session ID
was never persisted, and no transcript for it exists on disk. Searched:
`~/.claude/projects/-Users-surahli-Documents-projects-SMA-v2/*.jsonl` — the newest two files are
`20f39af5-….jsonl` (mtime 2026-08-17T04:09Z) and `b8d1c1c5-….jsonl` (2026-08-15T06:40Z). Neither
covers the 04:45–04:58Z Phase 1 window. There is no `subagents/` directory, no job `timeline.jsonl`,
and no `usage-data/session-meta` entry for it.

So the two Phase 1 artifacts are its **complete** output evidence. I am **not** the continuation of
that session's context — I am a fresh context reading its two written files plus the same worktree.
Where this section says Phase 1 "reasoned" or "relied on," that is inferred from the Phase 1 text
itself, not from a transcript. The irony is exact and worth recording: this review's whole Phase 2
mandate is that raw records outrank later summaries, and Phase 1 left only a summary. The 2026-08-15
session it reconstructs is, on this axis, better preserved than the review reconstructing it.

**Consequence for reading this document:** §§1–7 above are auditable against the worktree they cite,
but not against the process that produced them. This section is auditable against both.

## P1. Chronology

All times UTC, from `jobs/20f39af5/timeline.jsonl`, `usage-data/session-meta/20f39af5….json`,
`teams/session-20f39af5/config.json` (epoch-ms `joinedAt`), and file mtimes.

| Time | Event | Raw anchor |
| --- | --- | --- |
| 08-15 06:20Z | Eight HEIC screenshots staged read-only outside the repo | `/private/tmp/kdd-enterprise-review.XFOmYI/` (8 files, mtime 06:20Z) |
| 08-15 06:22Z | Review prompt authored | `/private/tmp/kdd-enterprise-opus5-review-prompt.md` |
| 08-15 06:23:17Z | Job created; team `session-20f39af5` created 06:23:18.200Z | `state.json:115`; `config.json:3` |
| 08-15 06:23:18Z | Session starts. `--model opus`, `--effort high`, `--permission-mode auto`, CLI 2.1.233, add-dirs = `cd68` worktree + screenshot dir + `/private/tmp` | `state.json:84-99,107` |
| 08-15 06:23:53Z | Entry prompt: "Start by reading … follow it exactly" | `timeline.jsonl:1` |
| 08-15 06:23:55–06:25:26Z | Lead reads the prompt, compares worktree copies, inspects `cd68` git state, reads `wayfinder/map.md` | `timeline.jsonl:2-6` |
| 08-15 06:25:25Z | `image-extractor` (Sonnet) joins | `config.json:21` |
| 08-15 06:26:22Z | `A-consistency` (Sonnet) joins | `config.json:35` |
| 08-15 06:26:49 → 06:29:06Z | `B-architecture`, `C-causal`, `D-search`, `E-eval`, `F-security`, `G-sequencing` (all Opus) join, ~27 s apart | `config.json:49,63,77,91,105,119` |
| 08-15 06:32:59Z | Lead posts five findings it verified **itself** by grep/diff/ls, and records a permissions coverage gap: `shasum`, `sips`, `python3`, `openssl`, `git -C` denied | `timeline.jsonl:18` |
| 08-15 06:33:25Z | Lead independently opens `build-test.json`; confirms `project_build/lint/tests` skipped | `timeline.jsonl:20` |
| 08-15 06:35–06:36Z | Image conversion succeeds (`sips`); lead **independently opens all eight** converted JPGs rather than trusting the extractor | `timeline.jsonl:24-27` |
| 08-15 06:36:11Z | First idle notifications from C/B/D/E — **no report content** | `timeline.jsonl:28` |
| 08-15 06:37:10Z | `A-consistency` delivers content through the channel; other six re-requested | `timeline.jsonl:32` |
| 08-15 06:39:27Z | `H-verifier` (Opus) dispatched with C1–C10, V1–V4, and the draft verdict — but not the lead's reasoning | `config.json:133`; `timeline.jsonl:33-34` |
| 08-15 06:39:32Z | Lead declares the six a delivery failure and stops retrying | `timeline.jsonl:34-35` |
| 08-15 06:47:10Z | **Review v1 delivered** on the lead's own pass + `A-consistency` only, with an independence-shortfall statement | `timeline.jsonl:39` |
| 08-15 06:47:10Z | Owner pushes back: "I can read the output when I click them" | `timeline.jsonl:40` |
| 08-15 06:48:25Z | Lead concedes the error, asks all seven to `Write` reports to the job scratch dir | `timeline.jsonl:44` |
| 08-15 06:50:02Z | No files appear. Lead enumerates six blocked retrieval routes and asks the Owner to choose among four options | `timeline.jsonl:49` |
| 08-15 06:50:43Z | **All nine `report-*.md` written in one batch** — identical mtime `06:50:43Z` — by extracting each transcript's longest assistant text message | `jobs/20f39af5/tmp/report-*.md`; method stated at `01-evidence-receipts.md:299-303` |
| 08-15 06:54:45Z | **Review v2 delivered**: ~30 findings the first version lacked, 4 of them BLOCKERs, plus 4 self-corrections | `timeline.jsonl:50` |
| 08-15 06:54:47Z | Session limit hit; Owner asks for persistence into the repo | `timeline.jsonl:52-53` |
| 08-16 04:48:42Z | Session resumed ("continue") | `timeline.jsonl:57` |
| 08-16 04:58:01Z | Bundle written to the repo and mirrored to `cd68`. The `Write` tool was blocked by the background-isolation guard, so the lead staged outside the repo and `cp`'d in — disclosed, not routed around silently | `timeline.jsonl:58` |
| 08-16 06:08–06:11Z | Writing the Codex handoff, the lead re-reads its own artifact and finds the orphan/worktree BLOCKER **lost its standalone entry during restructuring**; restores it as **B13**, moves U11's operational stop to **B14** | `timeline.jsonl:63-70` |
| 08-16 06:12:33Z | Second self-caught count error: BLOCKER 13→14 makes "37 findings" wrong; corrected to **38** (B1–B14, M1–M24) | `timeline.jsonl:74` |
| 08-16 06:18–06:23Z | Wrap-up; session ends **blocked**, awaiting Owner approval for memory writes and a commit. `git_commits: 0` | `state.json:2-3,78`; `session-meta:24` |
| 08-16 16:19–16:37Z | **A later actor** creates `03-codex-disposition.md` and amends the persisted bundle (see P5) | repo mtimes; `03-codex-disposition.md:3` |
| 08-16 (date only) | **Owner rules M0 Flight Readiness is the only funded slice** | `03-codex-disposition.md:18` |
| 08-17 04:43–04:58Z | Phase 2 handoff authored; `m0-build-alignment-packet-draft.md`, then Phase 1 `opus5-review.md` + `status.json` | `handoff.md:3`; repo mtimes |

Session totals: 1355 minutes, 12 user messages, 265 assistant messages, 9 `Agent` calls, 23
`SendMessage`, 5 `Write`, 15 tool errors, 0 commits, 0 pushes (`session-meta:6-46`).

## P2. Model and role per prior agent — from metadata only

`config.json` carries an explicit `model` field for every child; each is corroborated by the
matching `subagents/agent-*.meta.json`. No model is guessed.

| Agent | `agentType` | Model | Role (from its own dispatch prompt) | Config anchor |
| --- | --- | --- | --- | --- |
| `team-lead` | `team-lead` | **Not in `config.json`** — `members[0]` has no `model` key. Session ran `--model opus` per `state.json:96-97`, and `00-final-review.md:8` names Opus 5 | Orchestrator, synthesis, independent verification | `config.json:7-16` |
| `image-extractor` | `general-purpose` | `sonnet` | Extraction only, explicitly "not an interpreter" | `config.json:25` |
| `A-consistency` | `general-purpose` | `sonnet` | Mechanical identifier / enum / traceability / link audit; "No architecture opinions" | `config.json:39` |
| `B-architecture` | `general-purpose` | `opus` | Truth-store separation, Trace↔Evidence, trajectory increment | `config.json:53` |
| `C-causal` | `general-purpose` | `opus` | Exact-deployed-tie chain, verdict ceiling, invalid-experiment block | `config.json:67` |
| `D-search` | `general-purpose` | `opus` | Enterprise-search domain coverage | `config.json:81` |
| `E-eval` | `general-purpose` | `opus` | P4 evaluation design, P3 reviewer workflow | `config.json:95` |
| `F-security` | `general-purpose` | `opus` | Security, privacy, P2 production authority | `config.json:109` |
| `G-sequencing` | `general-purpose` | `opus` | Sequencing executability + source-transfer audit | `config.json:123` |
| `H-verifier` | `general-purpose` | `opus` | Fresh-context verifier; given the draft verdict, denied the lead's reasoning | `config.json:137` |

The prompt's routing rule — Sonnet for bounded mechanical work, Opus for judgment, no Fable, Haiku,
Codex, or unspecified model (`kdd-enterprise-opus5-review-prompt.md:5`) — was followed exactly. The
nine-child cap was hit precisely, which is what later blocked re-spawning the six silent agents
(`timeline.jsonl:49`).

**COULD NOT VERIFY — per-agent reasoning effort.** `--effort high` is a session-level respawn flag
(`state.json:84-85`); no `effort` key exists on any `config.json` member. Not asserted.

## P3. Four evidence layers, kept separate

**Layer 1 — raw session events.** `timeline.jsonl` (82 records), `state.json`, `session-meta`,
`config.json`, `teams/session-20f39af5/inboxes/*.json`, and the nine
`subagents/agent-*.jsonl` transcripts (0.78–8.9 MB each). These record what happened, including
what went wrong. Load-bearing detail: **all nine inbox files contain exactly `[]`** (2 bytes each)
— hard confirmation that the teammate message channel delivered nothing durable, which is the
mechanical root of the incident at 06:39–06:50Z.

**Layer 2 — specialist reports.** `jobs/20f39af5/tmp/report-{A…H}.md`, all nine written at
06:50:43Z. These are **lead-extracted transcriptions**, not agent-written files: `report-D-search.md:1`
and `report-E-eval.md:1` both open with the agent stating its own `Write` was blocked by the harness.
`report-image-extractor.md` is a 511-byte stub; the real 13 KB transcription reached the lead through
the message channel and was re-authored by the lead a day later into
`agent-reports/image-extractor.md`, which discloses this at its `:6-9`.

**Layer 3 — team-lead synthesis.** `00-final-review.md` (740 lines), `01-evidence-receipts.md`,
`02-codex-handoff-prompt.md`, `README.md`. This layer re-severities, merges, and renames the
specialist findings into B1–B14 / M1–M24. P6 records what that compression cost.

**Layer 4 — later Codex and Owner decisions.** `03-codex-disposition.md` (2026-08-16T16:19Z), the
Owner's M0 scope ruling of 2026-08-16 (`03-codex-disposition.md:18`), and the post-hoc amendments in
P5. This layer is **not** review evidence; Phase 1 was right to refuse it as such
(`opus5-review.md:16-18` above).

## P4. Provenance of all 38 findings

`report-*` paths are under `~/.claude/jobs/20f39af5/tmp/`. "Lead" means the team-lead's own
command or image read, receipted in `01-evidence-receipts.md`.

| ID | Origin | Raw anchor | Class |
| --- | --- | --- | --- |
| B1 | `C-causal` (its own B1) | `report-C-causal.md:5-9`, chain table `:57` | Single specialist |
| B2 | Lead + `G-sequencing` + `H-verifier` | `timeline.jsonl:27`; `report-G-sequencing.md:56`; `report-H-verifier.md:73` (V3b) | **Triple-sourced** |
| B3 | Lead + `H-verifier` | `timeline.jsonl:27`; `report-H-verifier.md:17-23` (C5), `:81` | Lead + verifier |
| B4 | `B-architecture` (3a/3b) | `report-B-architecture.md:32-46` | Single specialist |
| B5 | `B-architecture` (3c) | `report-B-architecture.md:48-63` | Single specialist |
| B6 | `B-architecture`, partly seconded by `F-security` M1 | `report-B-architecture.md:69-77`; `report-F-security.md:20-23` | Two lenses |
| B7 | `F-security` (its B1) | `report-F-security.md:3-6` | Single specialist |
| B8 | `F-security` (its B2) | `report-F-security.md:8-11` | Single specialist |
| B9 | `F-security` (its B3) | `report-F-security.md:13-16` | Single specialist |
| B10 | `D-search` **and** `C-causal`, independently | `report-D-search.md:82`; `report-C-causal.md:34` | **Corroborated** |
| B11 | `E-eval` B1 **+** B2, merged | `report-E-eval.md:9-12`, `:14-17` | Two specialist findings merged into one |
| B12 | `G-sequencing` | `report-G-sequencing.md:34` | Single specialist |
| B13 | Lead + `H-verifier` C6/C7 | `timeline.jsonl:18`; `report-H-verifier.md:25-31` | Lead + verifier; **dropped then restored** 08-16 06:08–06:11Z |
| B14 | `G-sequencing` | `report-G-sequencing.md:48-52` | Single specialist |
| M1 | **`H-verifier` V3(a) only** | `report-H-verifier.md:71` | **Fresh verifier challenge** — no specialist raised it |
| M2 | `B-architecture` item 2 | `report-B-architecture.md:7-26` | Single specialist |
| M3 | `C-causal` (its B4, rated **BLOCKER**) | `report-C-causal.md:21-24` | Single specialist, **downgraded** |
| M4 | `C-causal` M5 | `report-C-causal.md:36` | Single specialist |
| M5 | `C-causal` M2 | `report-C-causal.md:30` | Single specialist |
| M6 | `C-causal` M3 | `report-C-causal.md:32` | Single specialist |
| M7 | `C-causal` (its B3, rated **BLOCKER**) | `report-C-causal.md:16-19` | Single specialist, **downgraded** |
| M8 | `C-causal` B2 (**BLOCKER**) + `D-search` + Lead + `H-verifier` C4 | `report-C-causal.md:11-14`; `report-D-search.md:59-65,90`; `report-H-verifier.md:13-15` | **Quadruple-sourced**, **downgraded** |
| M9 | `D-search` | `report-D-search.md:39,84` | Single specialist |
| M10 | `D-search` | `report-D-search.md:51-53,86` | Single specialist |
| M11 | `D-search` | `report-D-search.md:41,88` | Single specialist |
| M12 | `D-search` | `report-D-search.md:55-57,92` | Single specialist |
| M13 | `D-search` blind spot 8 | `report-D-search.md:78,94` | Single specialist, self-labelled domain inference |
| M14 | `C-causal` M1 | `report-C-causal.md:28` | Single specialist |
| M15 | `E-eval` B4 | `report-E-eval.md:25-31` | Single specialist |
| M16 | `E-eval` B3 | `report-E-eval.md:19-23` | Single specialist |
| M17 | `E-eval` M5 | `report-E-eval.md:51-54` | Single specialist |
| M18 | `F-security` M2 **+** N2 (screenshot digests) | `report-F-security.md:25-28`, `:51` | Two findings merged |
| M19 | `F-security` M4(d) | `report-F-security.md:39` | Single specialist |
| M20 | `B-architecture` | `report-B-architecture.md:79-87` | Single specialist |
| M21 | `B-architecture` | `report-B-architecture.md:89-95` | Single specialist |
| M22 | `G-sequencing` §1 | `report-G-sequencing.md:9` | Single specialist |
| M23 | `G-sequencing` §3 | `report-G-sequencing.md:42` | Single specialist |
| M24 | `D-search` blind spot 1 | `report-D-search.md:71` | Single specialist, self-labelled domain inference |

**Tally.** 30 of 38 findings rest on **exactly one** specialist report. 5 are multi-sourced
(B2, B6, B10, B13, plus M8's four). 2 are lead-originated and specialist-confirmed (B3, B13).
**1 (M1) exists only because a fresh-context verifier was mandated** — the strongest single
argument in the raw record for keeping that role.

### What was independently verified versus inherited

**Verified by the lead's own commands or reads** — receipted in `01-evidence-receipts.md`, and
these are the only findings with first-hand lead evidence: the M0-vocabulary zero counts, the
win/loss zero hits, the orphan-document greps, the worktree-versus-main-tree `diff`, the
`search-relevance-experiment-analysis` zero-hit grep, the `build-test.json` inspection, the
zero-sizing grep, and **all eight screenshots, opened directly by the lead rather than taken from
the extractor** (`timeline.jsonl:27`). That covers B2, B3, B13, M8, and the image-derived premises.

**Inherited, not re-verified.** The other ~33 findings are specialist text, recovered at 06:50:43Z
and shipped in review v2 at 06:54:45Z — a **four-minute window** across ~140 KB of specialist prose,
immediately before a session limit. There was no time for independent re-derivation, and the lead
does not claim any: `00-final-review.md:732-738` says only that the reports were recovered and
"reproduced verbatim." That is honest, and it means the finding *text* for those 33 is
specialist-authored and lead-transcribed.

**Based on an author/reviewer claim rather than a check.** `G-sequencing`'s Part 2 transfer audit
turns on source-manifest hashes it did not recompute; `E-eval`'s deferred-numbers table takes each
document's own statement of what is deferred; the image transcriptions are `image-extractor`'s
reading, though the lead re-read all eight originals. The reviewers labelled these correctly.

**Phase 1 framing gap (not a verdict change).** §2 above treats every row's "original requested
correction" as a single reviewer's intent. The raw record shows two different provenance classes
behind that text — lead-verified for four findings, specialist-inherited for the rest — and Phase 1
had no way to see the split from `00-final-review.md` alone.

## P5. The persisted bundle was amended after the session ended

Verified by diffing the session's staged bundle (`jobs/20f39af5/tmp/bundle/`, frozen
2026-08-16T06:09–06:22Z) against the repo copies (mtimes 2026-08-16T16:19–16:37Z, alongside the
creation of `03-codex-disposition.md`):

1. **Share-safe path scrub, benign.** Absolute machine paths were replaced with placeholders in
   `01-evidence-receipts.md:41-44`, `agent-reports/D-search.md:1`, and `agent-reports/H-verifier.md:3`.
   No substantive text changed; trailing newlines were normalised.
2. **A documented coverage gap was converted into an asserted verification.** The staged bundle
   said the eight screenshot SHA-256 values and the DeepSeek digest "could **not** be independently
   verified, because `shasum`, `openssl`, and `python3` were denied by session policy." The persisted
   copies replace this at `00-final-review.md:113`, `:760` and `01-evidence-receipts.md:11-12`, `:293`
   with a "Post-review receipt correction" claiming the main orchestration task verified all eight,
   while stating the raw images "are no longer available in this workspace."
3. **That stated reason is factually wrong here.** All eight originals are present at
   `/private/tmp/kdd-enterprise-review.XFOmYI/` (8 `.HEIC` files, mtime 2026-08-15T06:20Z). The
   images are available; the amendment says they are not.
4. **The 38 finding texts are untouched.** The `00-final-review.md` diff has exactly four hunks —
   the reviewer line, the coverage-gap paragraph, the §10 header, and the §10 closing paragraph.
   B1–B14 and M1–M24 are byte-identical to the staged bundle. **Phase 1's baseline was intact for
   every finding it audited**, so no §2 or §3 verdict is affected.

**COULD NOT VERIFY — the amendment's own claim.** It cites no command, no output, and no session. I
attempted to re-derive it: `shasum -a 256` was denied by this session's Bash policy, and the
`python_repl` MCP tool was not permission-granted. I stopped after two mechanisms rather than a
third. So the eight digests remain unverified here — the same class of gap the original review
recorded honestly, now papered over in the artifact. **Recommendation: either produce the rehash
receipt or restore the original coverage-gap wording.** An amendment that upgrades an evidence claim
while asserting the evidence is gone is exactly the pattern this package's own digest and receipt
rules exist to prevent.

## P6. Prior methodology — strengths, weaknesses, blind spots, and compression loss

**Strengths, from the raw record rather than the summary.**
- The nine dispatch prompts (`config.json:26,40,54,68,82,96,110,124,138`) each demand `file:line`
  anchors, force a `docs observed` versus `reviewer inference` split, and require
  "ABSENT — searched `<sections>`" instead of silence. Every returned report honours this.
- The lead re-verified the extractor's two decisive images itself before relying on them
  (`timeline.jsonl:27`).
- `H-verifier` was given the draft verdict and told to refute it, and it did partially refute —
  C8, C9, C10 all came back `PARTIALLY CORRECT`/`REFUTED as stated`
  (`report-H-verifier.md:33,39,45`). Those corrections are carried into `00-final-review.md:36-60`
  instead of being buried. The self-correction section of the prior review is genuine.
- `H-verifier` V4 (`report-H-verifier.md:77-81`) forced the `[discovered]` versus `[self-declared]`
  labelling that keeps the review from claiming the authors' own TODOs as findings.

**Weaknesses.**
- **Single-lens dominance.** 30 of 38 findings have one source. The prior review's own §10 claims
  independent corroboration for four items only, and inspection confirms that count is right.
- **A four-minute integration window.** Review v2's ~30 added findings were merged under a session
  limit. Nothing was checked; the reports were trusted as written.
- **The delivery incident nearly lost the review.** Version 1 shipped at 06:47:10Z built on one
  Sonnet report, with an independence-shortfall statement constructed around evidence that was on
  disk the whole time. Only Owner pushback recovered it. The lead's own wrap-up names this as the
  session's serious error (`timeline.jsonl:79`).
- **A finding vanished in a restructure** and survived only because the lead re-read its own artifact
  before the handoff (`timeline.jsonl:70`). B13 exists by luck.

**Evidence lost when the specialists were compressed into `00-final-review.md`.**
- **Three `C-causal` BLOCKERs were silently downgraded to MAJOR.** Its B2 (win/loss), B3
  (neutral/mixed), and B4 (`not_applied` is a label) became M8, M7, and M3. The synthesis nowhere
  discloses the re-grading. The prompt did instruct "reconcile contradictions rather than voting"
  (`kdd-enterprise-opus5-review-prompt.md:78`) — and `D-search` did rate win/loss MAJOR — so the
  reconciliation is defensible. Its invisibility is not.
- **`E-eval` B2's blind-case-curator clause was dropped.** It required that *both* the fixture author
  and "the blind-case curator" be independent of the architecture authors
  (`report-E-eval.md:15`). Merging B2 into B11 kept fixture-author independence and lost the curator
  half, which then survived only as a sentence inside M16.
- **`A-consistency`'s `ExperimentReadContract` finding never became a numbered finding.** Its report
  records that the entity is absent from the spec's required-entity table
  (`report-A-consistency.md:47`). It appears only inside §4's traceability table. Under the Owner's
  M0 ruling, `ExperimentReadContract` is now the central M0 input — the most consequential omission
  of the compression.
- **`F-security` M5's seven pre-production-read prerequisites** (`report-F-security.md:45`) and
  **`E-eval`'s eleven-row deferred-numbers table** (`report-E-eval.md:72-84`, five rows with no
  producing pilot) survive only as §7 checklist prose, not as tracked findings.
- **`M8` was not labelled "independently corroborated"** despite four sources, while B10 was with
  two. The label was applied inconsistently.

**Blind spots the whole panel shared.** No agent was assigned cost, staffing, or delivery sizing —
that gap surfaced only as a by-product of `G-sequencing` §5 and `H-verifier` V3(b), which is why B2's
pricing half is thin. No agent owned the reuse question directly; B3 exists because the lead read the
screenshots. And all eight children were same-family models reading the same files — a limit the
prior review states plainly and correctly refuses to count as independence
(`00-final-review.md:747-750`).

## P7. Does the raw record change the Phase 1 30/8 audit?

Tested each Phase 1 verdict against the specialist text that actually generated the finding.
**Thirty-seven of thirty-eight stand as written.** One reason is corrected; three verdicts keep their
letter but gain weight; three are confirmed harder than Phase 1 could show.

**Corrected — M1, reason only. Verdict remains `SUPPORT_CURRENT`.**
*Before:* §3 above argued the current generation-split position is "a better answer than the original
correction," on the reading that the original asked for a raw `confirmed → inconclusive` edge.
*After:* the original correction offered **two** options — "add `confirmed -> inconclusive | ruled_out`
… **or state explicitly that retraction requires a new generation**" (`00-final-review.md:294-295`,
sourced from `report-H-verifier.md:71`). The current position is a refinement of option two, i.e.
*inside* the original reviewer's intent, not an improvement on it.
*Why it matters:* the residual gets sharper, not softer. The original's option two required the rule
to be **stated explicitly**, and the higher-authority freeze document
(`freeze-canonical-domain-policy-contracts.md:171-174`) states neither option. So M1's residual is not
a refinement gap — it is the accepted correction failing to reach the controlling document. The
one-sentence fix in §3 is unchanged and should be treated as closing an accepted finding.

**Weight raised, verdicts unchanged — M7, M3, M8.** All three were rated **BLOCKER** by `C-causal`
and downgraded to MAJOR in synthesis (P6).
- **M7 (`PARTIAL`, owner-gated).** Its specialist origin was a blocker, and the missing
  `directional_only` state is an M0 ceiling in the Owner's own profile. Edit **C2** in §4.3 should be
  read as restoring a specialist BLOCKER correction to the funded slice, not as a nicety.
- **M3 (`SUPPORT_CURRENT`).** `C-causal`'s B4 had two halves: make the diff non-applicable by
  construction, and add a publish-barrier human-channel predicate. The first was rejected on good
  grounds; the second was simply never implemented. §3's required edit is the unimplemented half of a
  specialist BLOCKER. Still direction-only for M0 (`spec:257`), but it should not be filed as
  housekeeping.
- **M8 (`EXACT`).** The verdict holds — option 2 was taken cleanly — but this was the most heavily
  corroborated finding in the review (four sources) and one of them called it a blocker. The Owner's
  M0 ruling is what makes deferring win/loss to M2 correct; nothing in the package did.

**Confirmed harder than Phase 1 could show — M16, B11, B3.**
- **M16.** §2 flagged that fixture authors have an independence receipt (`eval:45`) but the blind-case
  curator does not. The raw record shows `E-eval` B2 asked for **both**
  (`report-E-eval.md:15,17`) and the curator half was lost in the merge into B11. Phase 1
  independently rediscovered a requirement the prior review dropped in compression. The `PARTIAL`
  verdict and its fix are correct and now have a documented origin.
- **B11.** §3's `HYBRID` on binding is exactly right: `E-eval` B1 required the trivial-baseline rule
  "run on **every rung**" (`report-E-eval.md:12`), and the funded M0 rung carries none. Edit **C6**
  restores the specialist's own scope.
- **B3.** `H-verifier` C5 confirmed all three parts of the reuse contradiction and V4 explicitly
  ruled it "not unfair" (`report-H-verifier.md:17-23`, `:81`). §3's `HYBRID` and its inventory
  requirement are the prior review's unfinished business, not a new demand.

**Nothing in the raw record contradicts any Phase 1 verdict.** No specialist report shows a
correction landing differently from how §2 recorded it, and no `SUPPORT_CURRENT` in §3 rests on a
misreading of the original text. **The 22 EXACT / 5 SEMANTICALLY_EQUIVALENT / 3 PARTIAL / 0 MISSING /
0 OVERREACH tally and the 6 / 2 / 0 disputed tally stand unchanged.**

**One structural note on the 30/8 split itself.** The partition came from the Phase 2 handoff, not
from `03-codex-disposition.md`. Measured against that ledger it is slightly mis-cut: **B11** is
`ACCEPT (scoped)` and **M3** is a plain `ACCEPT` (`03-codex-disposition.md:27,33`), yet both were
audited as disputed; meanwhile M7, M8, M13, M17, M23, and M24 are all qualified accepts
(`:37,38,43,47,53,54`) audited as accepted. No finding was double-counted or missed — all 38 appear
exactly once — and each was judged on its merits, so the audit is sound. But the labels "accepted"
and "disputed" in §§2–3 are the handoff's, not the ledger's.

## P8. Prior scope assumptions versus the Owner's later authority

The 2026-08-15 review ran **before any Owner scope ruling existed**. Keeping this boundary clean:

**Then-valid reviewer assumptions, now superseded.** `H-verifier`'s V1 rests on C1+C2+C5 — the
mismatch between an M0-only funding ask and a package whose smallest increment is D0→U8
(`report-H-verifier.md:55`). The prior review therefore listed "Is M0 the first build slice?" and
"Is M2 in the first MVP?" as **open Owner decisions with a reviewer recommendation**
(`00-final-review.md:617,619`) and proposed its own slice — "D0 + a vertical U1′ + U2 retargeted to
M0" (`timeline.jsonl:50`) — as a *proposal*. The Owner's 2026-08-16 ruling
(`03-codex-disposition.md:18`) settles all of it: M0 Flight Readiness only, M1/M2 direction-only,
broader architecture preserved. §5 above records decisions 1 and 3 as resolved. Correct.

**Not superseded by that ruling.**
- **The sizing half of B2.** The ruling addressed scope; the Owner's screenshot asks "Build +
  **staffing**" (`agent-reports/image-extractor.md:66`). Two independent prior sources found zero
  sizing content (`report-G-sequencing.md:56`; `report-H-verifier.md:73`), and §1 above confirms it
  is still zero. Open decision 12 is the correct carry-forward.
- **The reuse question (B3).** The prior review's §5 correction — "Reject the architecture; **Adopt**
  the verified metric registry, schema catalog, and basis-table routing per IMG_3695"
  (`00-final-review.md:603`) — is a *reviewer* correction the Owner has never ruled on. It is the
  direct ancestor of open decision 13.
- **Every finding whose subject is not milestone scope.** The ruling changes which findings are
  *funded*, not whether they are *right*. §2's class boundary — spec-addressed ≠ implemented ≠
  production-validated ≠ owner-accepted — is exactly the discipline that keeps these separate, and it
  survives contact with the raw record.

**One inheritance worth flagging.** Edit **C8** in §4.3 imports the prior review's six stop
conditions. Five come from `G-sequencing` (`report-G-sequencing.md:71`); the sixth — the fixture set
must produce a *failing* case for SRM, CUPED-mode mismatch, unregistered decision metric, and
pre-runtime invocation — was added by the lead, folding `E-eval` B1's difficulty rule into the slice
gate. C8 is therefore 5/6 specialist-derived and 1/6 lead-authored, and the lead-authored one is the
one that binds the M0 fixture suite. It should not be dropped as an editorial flourish.

## P9. Unresolved reconstruction gaps — `COULD NOT VERIFY`

1. **Phase 1's raw session record.** Absent. Searched
   `~/.claude/projects/-Users-surahli-Documents-projects-SMA-v2/*.jsonl` (newest: `20f39af5` at
   2026-08-17T04:09Z, `b8d1c1c5` at 2026-08-15T06:40Z); no `subagents/` dir, no job timeline, no
   session-meta entry for the 04:45–04:58Z window. See P0.
2. **The eight screenshot SHA-256 values, and the post-hoc claim that they were verified.** Tried
   `shasum -a 256` (denied by this session's Bash policy) and the `python_repl` MCP tool (permission
   not granted). Stopped at two mechanisms. The originals exist and are readable, so the check is
   possible with permission — it simply has never been receipted anywhere I can find.
3. **Who applied the 2026-08-16T16:19–16:37Z amendments.** Inferred from mtimes co-located with the
   creation of `03-codex-disposition.md`; no transcript for that actor exists in this project's
   transcript directory (searched as in item 1). The actor is **not asserted**.
4. **The exact extraction mechanism at 06:50:43Z.** `session-meta:12` records exactly one
   `python_repl` call, all nine reports share one mtime, and `01-evidence-receipts.md:299-303` states
   the method was "extracting each transcript's longest assistant text message." I did **not** open
   the 12.3 MB session JSONL to confirm the call itself. Searched: `timeline.jsonl`, `state.json`,
   `session-meta`, file mtimes.
5. **Whether the six Opus specialists actually ran the verification commands they report.** Their
   transcripts (0.78–3.7 MB each) were not opened; only the extracted final reports were read. Four
   transcripts (`B`, `C`, `F`, `G`) continued to receive appends until 06:53:12Z, after the 06:50:43Z
   extraction — consistent with post-extraction idle traffic, but not confirmed.
6. **Per-agent reasoning effort.** Session-level `--effort high` only; no per-member field. See P2.
7. **`team-lead`'s model as team metadata.** Absent from `config.json:7-16`; taken from
   `state.json:96-97` and `00-final-review.md:8`.

## P10. What this reconstruction changes for the Owner session

Nothing in §6's `GO_FOR_OWNER_ALIGNMENT` decision changes. Three additions to the agenda:

1. **C2 and C6 are restorations, not additions.** Both re-attach a specialist finding — one rated
   BLOCKER — to the funded slice after it was diluted in synthesis. Treat them as the highest-value
   edits in C1–C9.
2. **`ExperimentReadContract`'s absence from the spec's entity table was found in 2026-08-15 and
   never became a finding** (`report-A-consistency.md:47`). It is now the centre of M0. Worth one
   check before the alignment session.
3. **The receipt amendment in P5 should be resolved before this package is shared.** Either produce
   the rehash receipt or restore the honest coverage-gap wording. It also compounds open decision 14
   (M18): the same eight digests are both the subject of an unverified verification claim and of an
   unresolved classification question.

**Statement on this section.** Read-only reconstruction. I read local session records, specialist
reports, and the persisted bundle; I ran `ls` and `diff` for comparison. I attempted `shasum` and
`python_repl` for the digest check and was denied both; no third attempt was made. I spawned no
subagents, modified no canonical document, ran no code, resumed no session, and created no commit.
The only files this Phase 2 pass wrote are `opus5-review.md` and `status.json` in this directory.
