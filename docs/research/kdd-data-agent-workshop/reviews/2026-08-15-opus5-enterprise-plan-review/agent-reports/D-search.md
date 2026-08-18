The file write was blocked by the harness — subagents in this setup cannot write report files, so the session-local `report-D-search.md` does **not** exist. Here is the complete report as text.

---

# Enterprise Search Domain Coverage Review

Anchors: `spec` = `docs/research/kdd-data-agent-workshop/final-architecture-spec.md` · `prof` = `.../enterprise-experiment-post-analysis-profile.md` (self-labelled "research synthesis draft… does not supersede the canonical specification", spec:482) · `prac` = `.../enterprise-search-experiment-failure-practices.md` (research-only) · `intake` = `.../wayfinder/production-evidence-authority-intake.md` (every answer row `UNKNOWN`) · `seq` = `.../implementation-sequencing.md`.

Grading rule applied as instructed: a concept present only in `prac` but absent from the canonical spec or sequencing is **NAMED-ONLY**, never COVERED.

## 1. COVERAGE MATRIX

| # | Chain hop / plane | (a) Named? | (b) Evidence source/adapter? | (c) Check/diagnostic? | (d) Verdict |
|---|---|---|---|---|---|
| H1 | Intended treatment | spec:10.2 plane 1 "control integrity" | intake E02/E07 | G1 SRM/exposure/trigger/ramp (spec:9) | **COVERED** |
| H2 | Eligible corpus | spec:10.2 plane 4 | intake E09/E10 | none — plane listed, no diagnostic | **NAMED-ONLY** |
| H3 | Permission-trimmed corpus | spec:10.2 "permission trimming, identity/ACL sync" | intake E11 (proof: allow/deny assertions, group-expansion revision) | pre/post-trim count comparison only in prac:2 | **NAMED-ONLY** |
| H4 | Retrieved candidates | spec:10.2 plane 5 "candidate recall" | intake E12 "per-stage counts" | per-lane isolation only in prac:5 | **NAMED-ONLY** |
| H5 | Fusion / rerank / rendered | spec:10.2 planes 5–6 | intake E12 "render digest" | none in spec; prac:5–6 falsifiers only | **NAMED-ONLY** |
| H6 | User & session interaction | spec:10.2 plane 6 "session/task success" | intake E12 event joins | none | **NAMED-ONLY** |
| H7 | Metric | spec:2, spec:9 G1 | intake E01 | G1 numeric/lineage validators; prof:5.2 M0 checklist | **COVERED** |
| P1 | Tenant/role/locale/surface heterogeneity | spec:10.2 plane 2; spec:417 "aggregate lift MUST NOT hide tenant, tail, locale…" | intake E01 "allowed dimensions" | **no segment contract anywhere** | **NAMED-ONLY** |
| P2 | ACL / identity sync | spec:10.2 plane 4 | intake E11 | prac:2 only | **NAMED-ONLY** |
| P3 | Connector / index freshness | spec:10.2 plane 4; spec:10.4 `data` = "index/connector generation, alias/checkpoint, shard/coverage" | intake E09/E10 | spec:10.4 exact-identity requirement (identity, not health) | **NAMED-ONLY** |
| P4 | Query-mix shift | spec:10.2 "head/tail query mix, cohort shifts" | intake E12 | **not a G1 validity check** | **NAMED-ONLY** |
| P5 | Zero-result / low-recall | spec:10.2 plane 5 "zero results" | intake E12 | none | **NAMED-ONLY** |
| P6 | Latency / timeout / fallback / cache | spec:10.2 plane 7 | intake E12 (timeout/cache/fallback status) | none | **NAMED-ONLY** |
| P7 | Click / position bias | spec:10.2 plane 3 "position and intent bias"; spec:417 "CTR alone MUST NOT be treated as relevance" | intake E12 rank/viewport | **no estimator, no propensity, no correction** | **NAMED-ONLY** |
| P8 | Interleaving | **absent from all five docs** | — | — | **ABSENT** |
| P9 | Offline–online gap | prac:7 bullet only | **no evidence class for judgments/query sets in E01–E14** | — | **ABSENT** from spec/seq |
| P10 | Per-query win/loss | prof:7 (M2) | prof:7.2 field list | human `win\|loss\|unclear\|not_comparable` | **ABSENT** from spec + seq |

Sequencing check: `seq` names ~60 test IDs (POL / SKEL / EVD / REV / ADP / ANA / ORC / A-001…008 / UI / EVAL / PROD). **None is a search-domain test.** No implementation unit owns the eight evidence planes spec:10.2 declares mandatory.

## 2. THE HARDEST HOPS

**ACL / permission-trimmed corpus.** Needs per-arm candidate counts before and after security trim, on the same index generation, for a pseudonymous identity class; plus group-expansion revision and its effective time vs. the exposure window. `intake E11` specifies exactly the right proof shape ("authorized-test receipt … allow/deny assertions, effective time") — the strongest row in the package — but it is an unanswered intake, and the analysis-side check lives only in prac:2. Without it an analyst cannot separate "the ranker demoted the document" from "the user could no longer see the document." Opposite fixes, and one of them is a security incident.

**Index / connector freshness.** Needs connector run and checkpoint receipt, delete-propagation lag, index generation and serving alias per arm, and proof that **treatment and control were served by the same generation**. spec:10.4 requires generation identity for a *candidate change*; it never requires arm-parity of the serving corpus. prac:262 lists arm-generation divergence as a hard stop; the canonical spec does not carry it forward. Otherwise every ranked-list comparison is confounded by corpus drift and no win/loss example is comparable.

**Click bias.** Needs logged rank and viewport per impression plus an estimator separating position effect from relevance effect (IPS/propensity, or an interleaved arm). The docs name the bias twice and specify no estimator and no propensity source. An analyst cannot say whether CTR moved because results got better or because they moved up the page.

## 3. HETEROGENEITY

Required and unmechanised. prof:388 acceptance case 6 is "segment-specific effect hidden by aggregate movement"; spec:417 forbids aggregate lift hiding tenant/tail/locale/component/ACL regression; spec:10.2 plane 2 names "heterogeneous regressions".

Missing everywhere: segment enumeration, minimum segment size or per-segment MDE, and any multiple-comparison discipline — "Bonferroni", "FDR", "false discovery", "multiple comparison" appear in none of the five files. `ClaimRevision` (spec:7.2) carries `scope/window` and **no `segment` field**; prof:6.2 asks for one, the canonical entity lacks it.

Reviewer inference: failure runs both directions. No contract → false "no effect". Segmentation without error-rate control → manufactured segment claims wrapped in deterministic-derivation receipts (invariant 11) and ranked, attacking the false-`confirmed` veto (invariant 9) from inside the machinery meant to protect it.

## 4. QUERY MIX

Not a validity threat in the canonical spec. G1's Scenario A list (spec:9) is `assignment, SRM, exposure, trigger/ramp/power, joins, interference, guardrails` — unit-level SRM only. Compositional SRM (query distribution balance across arms by intent / head-tail / tenant / locale) is absent; prac:46 asks it, the spec does not adopt it. Zero-result rate is a plane keyword at spec:10.2 plane 5, never a required guardrail. "head/tail" appears once as a keyword; no torso bucket, and no stage in spec:10.1 requires the decomposition.

## 5. OFFLINE–ONLINE GAP

Not modelled as a hypothesis family. Neither spec:10.2's eight planes nor prof:6.1's ten contain "relevance improved but exposure, latency, rendering, or user behavior absorbed it." `intake E01–E14` has **no evidence class for relevance judgments, golden query sets, or offline eval runs** (the fourteen are Metric, Experiment, Runtime, Deploy, Repo/symbol, Config, Flag, Model, Data/index, Connector, ACL/identity, Query/result/session, Incident, Mapping). The most common enterprise-search story has neither a claim template nor a named source. prof:6.1 plane 10 ("product-hypothesis failure with no implementation defect") is coarser and different: a wrong hypothesis, not a real gain absorbed downstream.

## 6. WIN/LOSS EVIDENCE — MAJOR

Credible per-query artifact needs: query + intent class (navigational / known-item / informational / people / acronym); tenant, role, locale, surface; **both arms' full ranked lists with per-document position delta**; judged relevance per result with judge identity class and rubric version; the stage at which the document entered or disappeared (recall / fusion / rerank / filter / render); session outcome (click, dwell, reformulation, abandonment); corpus and index generation parity; human verdict and rationale.

prof:7.2 covers about two-thirds — stable query/trace identity, candidate origin, tenant/role/locale/surface/ACL-safe scope, both arms' runtime identity, replay config + data/index/corpus snapshot, exact query/params/result digest, side-by-side artifact or explicit counterfactual gap, comparability checks, linked M1 claim, named reviewer, and the four-valued judgment. It **omits ranked lists with position deltas, judged relevance labels, query-intent class, and session outcome**.

None of it reaches the canonical artifacts: no `WinLossEvidencePacket` in `spec`, no M2 stage in spec:10.1, no test in seq U8; prof:17 still lists M2's MVP inclusion as an open owner decision. **MAJOR**, stated as such.

## 7. SEARCH-SPECIFIC BLIND SPOTS THE DOCS MISS ENTIRELY

Reviewer domain inference; each checked against all five files.

1. **Randomization-unit vs analysis-unit mismatch.** User-randomized experiments with query-level metrics need clustered or delta-method variance. No document mentions variance estimation for ratio metrics. Top cause of false-positive search results; careful attention to `use_cuped` (prof:5.1) without it is precision theater.
2. **Interleaving / team-draft as a discriminating challenge.** G4 (spec:9) enumerates `replay, holdout/control, negative control, discriminating test, externally authorized paired action`. The highest-power ranking-specific challenge is absent; "interleav" appears nowhere.
3. **Query-volume-as-outcome.** If treatment changes how much people search, per-query denominators are themselves treated. The denominator-composition trap is unnamed: raising the zero-result rate can raise CTR while task success falls.
4. **Shared-state interference.** Click-feature stores, learned counters, and per-user result caches are shared across arms — SUTVA violation is the default in search, not an edge case. "interference" appears once in G1's input list with no mechanism, no detection, no evidence source.
5. **Product-side ACL over-permissiveness as a hard veto.** prac:62 notes under-filtering raises CTR and is a security regression, not a win. spec:15 governs only the *Agent's own* access; the search product leaking documents has no guardrail metric and no NO-GO. A conflation worth fixing explicitly.
6. **Novelty/primacy and enterprise weekday seasonality.** No requirement to check effect stability across the window or exclude ramp days, despite extreme weekday/weekend asymmetry — a fixed-horizon read (prof:5.1) over a non-integer number of weeks is systematically biased.
7. **Known-item / navigational regression.** Catastrophic in enterprise search, invisible in averaged NDCG; appears only inside one prac falsifier sentence, never as a required query class.
8. **Typed-change vocabulary narrowed against explicit research advice.** prac:326 recommended first-class `index | connector | permission | presentation | telemetry | external_dependency`; spec:10.4 kept `code | config | flag | model | data`. `data` absorbs index/connector, but **permission, presentation, and telemetry changes have no typed home** — the three planes most likely to kill a search experiment silently cannot be normalized, ranked, or exact-targeted by spec:13's machinery.

## FINDINGS BY SEVERITY

**BLOCKER — no segmentation or multiple-comparison contract.** Anchors: spec:417, spec:7.2 `ClaimRevision`, prof:388. Consequence: false "no effect" on a genuinely heterogeneous experiment, or unadjusted segment scans promoted as deterministic facts, defeating the false-`confirmed` veto. Correction: add a `SegmentationContract` to G1 — preregistered segment set, minimum segment size and per-segment MDE, explicit FDR or Bonferroni rule, tenant-equal vs traffic-weighted duality (prac:46). Add `segment` to `ClaimRevision`. Make an unpreregistered segment claim G0-incomplete.

**MAJOR — no per-arm corpus/pipeline parity check.** Anchors: spec:10.2 plane 4, spec:10.4; hard stop only at prac:262. Consequence: arms compared across different serving corpora; every ranked-list difference uninterpretable. Correction: G1 must check that both arms share index generation, serving alias, ACL snapshot, and effective search pipeline; divergence caps Cause at `suspected` and blocks win/loss comparability.

**MAJOR — query-mix shift is not a validity check.** Anchor: spec:9 G1 input list. Consequence: triggered-population composition change read as a treatment effect. Correction: add compositional SRM (query class × tenant × locale × surface) and zero-result-rate delta to G1's required checks.

**MAJOR — click/position bias named but unestimated.** Anchors: spec:10.2 plane 3, spec:417. Consequence: a presentation or position change attributed to ranking quality; spec:417's own MUST NOT has no enforcing mechanism. Correction: require a position-bias-corrected estimator with a named propensity source, or an interleaving arm, before any click-derived metric supports a G3 mechanism claim; add interleaving to G4's enumeration.

**MAJOR — no win/loss artifact in the canonical spec.** Anchors: prof:7.2 (partial) vs spec (absent), seq U8 (absent). Consequence: aggregate explanations never become concrete; the M2 deliverable has no canonical schema or test. Correction: promote `WinLossEvidencePacket` into spec §7.2 and seq U8; add the four missing fields.

**MAJOR — no evidence class for relevance judgments / offline eval.** Anchor: intake E01–E14. Consequence: neither offline-online reconciliation nor judged win/loss has an authoritative source, so both stay unbuildable even after P2 closes. Correction: add `E15 Judgment / offline-eval` (query-set version, rubric, judge identity class, judgment date, coverage by tenant and query class), plus an offline-online divergence hypothesis family in the M1 plane list.

**MAJOR — permission / presentation / telemetry have no typed change class.** Anchors: spec:10.4 vs prac:326. Consequence: an ACL-config change, SERP layout change, or logging change cannot be typed, ranked, or exact-targeted. Correction: adopt the recommended subtypes with their own exact-identity rows.

**MINOR — eight-plane coverage has no owning implementation unit.** Anchor: seq U1–U13 test IDs. Consequence: spec:10.2 declares the planes mandatory; nothing in the delivery plan verifies them. Correction: add `SRCH-001…008` plane-coverage tests to U8 and matching fixture classes to U10, mirroring spec:19.1's "ACL, index, connector, or pipeline failure" case class.

**MINOR — `MetricQuestion` omits locale and device.** Anchor: spec:7.2. Consequence: spec:417 makes locale regression a named failure the canonical entity cannot express. Correction: add `locale` and `device` to its required fields.
