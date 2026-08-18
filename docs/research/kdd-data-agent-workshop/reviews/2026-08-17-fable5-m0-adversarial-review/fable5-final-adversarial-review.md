# Fable 5 Final Adversarial Review — M0 Freeze Candidate, Phase A, and Owner-Decision Delta

| Field | Value |
| --- | --- |
| Reviewer | Claude Code Fable 5 (lead adversarial reviewer), model `claude-fable-5`, effort `high` |
| Handoffs | `handoff.md` (this directory) and delta handoff `steelman-owner-decisions-review-handoff.md` (`kdd-m0-fable-adversarial-steelman-delta-20260818`) |
| Written | 2026-08-18 00:35 to 00:55 America/Los_Angeles |
| Repository / branch / HEAD | `/Users/surahli/Documents/projects/SMA_v2` · `codex/kdd-data-agent-practices-research` · `28cbbda6e4d4d7f08134952d38433e52d3ee8768` (unchanged start to finish; `git status --short` fingerprint unchanged) |
| Phase I artifact | `fable5-phase1-independent-findings.md`, sealed **sha256 `e4a634686f9a01796a73102228742495793e1c16d1c9207969bdf751f4492654`** (62013 bytes) at 2026-08-18T07:21:42Z, before any Opus freeze output or new packet bytes were read. It is immutable; this document does not rewrite it. |
| Phase A package | `.agents/skills/kdd_data_agent/` aggregate **sha256 `2f1001b93b19b2318c4c6419205ed2f7778ac23c02533e78a0c0899f15bf7d1e`** (42 files; unchanged throughout) |
| Roster | 5 subagents (1 Sonnet, 4 Opus), 0 workflow lanes; details in §1 |

---

## Executive verdict: **BLOCKED**

The review object changed while the review was running. The freeze candidate that this task, the independent Opus 5 freeze review, and every lane were handed — `m0-m2-build-alignment-packet.md` at **sha256 `40c7234f3c0d85f18ebfba656e7aec2ab5ab71b86451a077ecad340eac779396`** — was replaced on disk at 2026-08-17 19:44:57 by **sha256 `67c844d10dcafcf2637388bf579dfcd9866d7d69ea6f4d3b456fd6b6b15dfcfa`**, together with the Owner record, planning decision packet, spec, sequencing, evaluation plan and CE plan (§0 of the Phase I report). Per the handoff rule, no verdict may be transferred across that change, and no review here treats mixed bytes as one object.

Three separate conclusions, kept apart:

1. **On `40c7234f…` (Phase I, sealed):** not freezable as written — four BLOCKERs, all closable by specific edits plus two Owner sentences and a new start authorization; the design would then be `ACCEPT_WITH_CHANGES`. The independent Opus 5 review reached `ACCEPT_WITH_CHANGES` with three BLOCKERs on the same bytes; every Opus BLOCKER is inside the Fable set (§3).
2. **On `67c844d1…` (structural re-check only, §4):** the orchestrator applied the Opus BLOCKER fixes and the eight edits from the second (Phase-A-author) review. But the new bytes were superseded within hours by the Owner's decisions D1-D6 and S1-S8 (`architecture-decision-ledger.md` §D): §5.3 encodes "two coordinated stored fields" where D3 selects one stored state plus a derived projection; no controlling document contains any of S1-S8's vocabulary; five documents still call the fixture slice the "M0 MVP", which S1 now forbids. `67c844d1…` is therefore **not a freezable candidate either**; a new revision is required.
3. **On Phase A:** `PASS_WITH_GAPS` is confirmed independently by Fable and by Opus; the static-scanner claim must be narrowed (Fable FB-05, not found by Opus) and three guards are unwired (Opus MAJOR-5 = Fable FB-26). Phase A is a foundation, not an M0, not a local M0 MVP, not production authorization, and not Committee acceptance.

Nothing here freezes the packet, authorizes `M0-F1`-`M0-F5`, or grants production access.

---

## 1. Roster, method, and disclosures

| Lane | Model | Scope | Outcome |
| --- | --- | --- | --- |
| lane1-mechanical | Sonnet 5 | VAL registry, vocabulary, links, English-only, package inventory | Delivered |
| lane2-contract | Opus 5 | Owner-contract / architecture consistency, drift, two-implementer test, freeze mechanics | Delivered (28 findings; 5 rated BLOCKER by the lane) |
| lane3-phasea | Opus 5 | Phase A mutation and scanner-escape testing on an isolated copy | No report (idle, then session limit). Its scripts were re-run by Fable; results are Fable-executed evidence |
| lane4-stats-eval | Opus 5 | Statistics, fixtures, evaluation design, O6 deference | Delivered after two nudges (22 findings); Fable had already produced an independent substitute of the same scope, which agrees |
| lane5-workflow-transfer | Opus 5 | Workflow, production authority/ACL, continuity, KDD/DeepSeek transfer, toolchain | No report (idle, connection loss, session limit). Fable performed the scope personally |

Fable personally: read every controlling document section cited; read all 19 runtime modules, the scanner and capability tests, and the fixtures; reran the suite from three directories (225 passed each); reproduced deterministic replay across four hash seeds (digests equal to the receipt); reproduced the package aggregate and discovered its (unstated) method; probed the static scanner and proved four escape families executable; re-ran 38 mutations plus 3 consolidated-review claims on the isolated copy; verified every BLOCKER anchor cited by a lane or by the Opus review against the source text.

Disclosures (details in the Phase I report §1): artifacts were authored under the job scratch directory and copied into this directory with `cp` because the background-session guard blocks direct writes without a worktree (a worktree would change Git state and lack the untracked review directory); OMC hooks created `.omc/state` files inside the package during Bash `cd` (this session at 19:29, and session `61ce23e2` at 19:53 — the Phase I report calls the latter "a lane"; the architecture ledger E11 identifies `61ce23e2` as the parallel independent Phase A verification job, so that attribution is corrected here) — removed by Fable at 19:55, aggregate unchanged; at 00:33 a further concurrent session `66cd206d` recreated one such file inside the package; it is not this task's and was left in place. Recommendation: every future session touching the package should set `OMC_STATE_DIR` or avoid `cd`-ing into it; one line of the Opus status JSON reached Fable via a lane-1 grep before sealing; ~10 grep lines of `m0-freeze-codex-fix-handoff.md` reached lane 2. Three of Fable's post-19:44:57 reads (`seq:11-19`, `spec:859-862`, CE `:361`) hit new bytes and were used only to confirm lane-2 claims made on old bytes.

One correction to the Opus review's disclosure: the two `.omc/state/sessions/4bda4e93-…` files it attributes to "a shell call in this review" carry **this Fable session's** id and were created by this session's `cd` at 19:29:22-24; Opus observed them and could not delete them; Fable removed them at 19:55. The Opus "action for the Owner: delete that `.omc` directory before the Continuity Checkpoint" is therefore already done, and re-verified (`.omc` absent; aggregate `2f1001b9…` over 42 files).

---

## 2. Reproduced evidence

| Item | Result |
| --- | --- |
| Suite | `225 passed` from repository root, package root, and an external cwd (Phase I §2) |
| Deterministic replay | run `sha256:7837c3e6…`, log `sha256:7221d8a4…`, build receipt `sha256:63ba4074…`, 47274 bytes; identical across `PYTHONHASHSEED` 0/1/12345/987654321 and equal to the continuation receipt (Opus used a different `run_id`/`recorded_at` and therefore different digests; both prove seed-independence, only Fable reproduces the receipt's exact values) |
| Aggregate | `2f1001b9…` reproduced by sha256 over `"<sha256>  <repo-relative path>\n"` lines for the 42 non-cache files; the receipt does not state the method |
| Mutations | 38 run by Fable on the isolated copy: 32 caught; survivors `o` (planted count not locked), `s1` (`_case_path` containment), `s3` (redundant `verify_chain`), `s4` (duplicate receipt id), `s9` (equivalent), `s10` (not testable); plus consolidated-review claims re-tested: empty/free-text `rule_source` accepted; `_parse_authorization_state` fail-open mutation survives (225 passed); dropping `actor` from `Receipt` identity survives (225 passed); `_require_exact_keys` no-op is caught (claim refuted) |
| Scanner escapes | `enum.bltns.exec/eval/__import__`, `from pathlib import os as _host`, `pathlib.os.*`, `pathlib.io.FileIO(...,"w")` (wrote 57 bytes), `typing.sys.*`, `Path.walk` — zero findings; a scanner-clean planted module kept the suite green (225) while reading `HOME`, listing `/`, running `eval`, and creating a file (isolated copy, reverted) |
| Toolchain citations | 5/5 spot-checked lines say what `TOOLCHAIN_RECEIPT.md` says |

---

## 3. Phase II — comparison with the independent Opus 5 freeze review (both on `40c7234f…`)

Opus 5 review: `m0-freeze-opus5-adversarial-review.md` (session `session_01YAshweqBjaqSc7S2SfufFS`, `ACCEPT_WITH_CHANGES`, 3 BLOCKERs, 7 MAJORs, Phase A `PASS_WITH_GAPS`). A second review by the Phase-A-author session `b9d777ba` (`m0-freeze-codex-fix-handoff.md`, "zero blockers", 4 MAJOR + 4 MINOR edits, Q11/Q12 declined for conflict of interest) wrote to the same paths and was overwritten (`architecture-decision-ledger.md` E4); its edits were applied by the orchestrator together with the Opus BLOCKER fixes (`coordination-update-2026-08-17.md`).

### 3.1 Agreements (finding by finding)

| Opus | Fable | Note |
| --- | --- | --- |
| BLOCKER-1 spent authorization presented as live (packet:7,:19; OWN:75) | **FB-03 BLOCKER** | Same evidence, same fix. Both note it is a stale-authority error, not a budget-conversion error |
| BLOCKER-2 `directional_only` reachable only via runtime; `spec:469` permission field undefined; underpowered full-runtime read → `decision_grade` | **FB-04 BLOCKER** (+ FB-21/22 adjacent) | Fable adds: no check examines achieved exposure; Committee reading of "decision grade"; option (b) "state validity-only" |
| BLOCKER-3 `spec:271` fields (arm parity, legal readiness-combination policy) missing from §5.1; no arm-parity check | **FB-01 BLOCKER** (broader) + FB-36 NOTE | Fable's FB-01 lists six more missing field groups (CUPED identity/covariate window, scorecard/UI surface, recomputation contract/validator identity, numerator/denominator/grain and pp-vs-relative interpretation, attribution, monitoring labels) and shows checks 8/11/13/14/17 have no consuming input; Opus scoped it to the two `spec:271` items. Fable rated arm parity a NOTE (defensible M1 scoping) — **conflict resolved in Opus's favour by Owner D2** (arm parity is M0) |
| MAJOR-1 seams cite draft sections | **FB-06 MAJOR** | Same |
| MAJOR-2 first-screen dropped but referenced | **FB-19 MAJOR** | Same |
| MAJOR-3 code cites `M0-SEC-001`/`M0-READ-001` | Fable: comment-only, folded into FB-06 closure | Fable rates it MINOR (behavior correct and mutation-proven); Opus MAJOR. Difference is severity only |
| MAJOR-4 `CoverageGapKind` 9 vs `freeze:61` 5, digest-bound, unseamed/unreported | **FB-09 MAJOR** | Same; Fable adds the receipt's silent hypothesis disposition |
| MAJOR-5 unwired guards (duplicate receipt id; `seal()`→`verify_chain`; `scan_package` non-vacuity) | **FB-26 MINOR** (s4 duplicate receipt; `o` planted count; s1 containment) | Overlap on the duplicate-receipt guard; the other two survivors differ (Opus: seal→verify_chain and scan_package vacuity; Fable: `_case_path` containment and the planted-count lock). Union of both lists is the real fix set. Fable rated MINOR (latent, not live); Opus MAJOR |
| MAJOR-6 B3 reuse inventory absent; fixture derivation open | **FB-12 MAJOR / owner_decision_required** | Same; **now closed by Owner D5** (fixtures may not derive from protected assets) |
| MAJOR-7 20 of 22 VAL IDs bind to no sequencing unit | **FB-30 MINOR** (eval list has no VAL IDs) | Opus's framing (unit binding) is sharper; adopt it |
| C2 partial, C8 partial; others satisfied | FB-32 NOTE (C1-C9 landed; C2/C8 residuals = FB-04/FB-18) | Same |
| Adjudicated: B3 open, M18 open, M19 open, M20 open, M1 partial | Fable: B3 open (FB-12), M1 residual noted, M18/M19/M20 not re-examined | No conflict |
| Phase A `PASS_WITH_GAPS`; semantics-independence except `CoverageGapKind` | Same | Fable adds `DEFAULT_GAP_KIND_BY_OUTCOME` inference (FB-27) as a second small choice |

### 3.2 Findings only Fable raised (missing coverage in the Opus review)

- **FB-05 static-scanner escapes with an executable proof** (attribute chains, from-import smuggling, `enum.bltns.exec`, `pathlib.io.FileIO`, `Path.walk`; scanner-clean planted module keeps the suite green while writing a file). Opus ran a runtime audit hook over the executed hermetic path (a genuine complement) but did not test the scanner against evasive shapes; its `TOOLCHAIN_RECEIPT.md` "rejects builtin recovery through allowed modules" claim stands unchallenged there. This is the most important coverage gap between the two reviews.
- **FB-02** readiness contract not Owner-decided (now closed by Owner D3).
- **FB-07** `human_state` undefined; ruling actor unnamed.
- **FB-08** no check-ID / materiality-rule registry (Opus notes rule-source is enforced mechanically; Fable shows the *registry* is absent and that an empty or free-text `rule_source` is accepted).
- **FB-10** no typed `evidence_class` for fixture vs production packets (now central to Owner S1/S2).
- **FB-11** open-decision register deleted; freeze-record fields absent.
- **FB-13/FB-14** evaluation-design weakness and pooled per-arm-less fixtures (Lane 4).
- **FB-15/FB-20** recomputation independence undefined; estimator "validity" unregistered; co-primary multiplicity (now partly closed by Owner D4/D6).
- **FB-16** continuity checkpoint impossible while untracked.
- **FB-17/FB-18** freshness state undetermined; §9.1 vs §12(6) budget-cap contradiction (Opus rated C8 partial for the spent cap, not for this contradiction).
- FB-21..FB-31 minors (MISSING vs UNKNOWN, total mapping, comparison rule, `decision_grade` meaning, CUPED covariate window, timestamp normalization, Python 3.14-only interpreter trigger, aggregate method unstated).

### 3.3 Findings only Opus raised

- MAJOR-3 (dangling draft IDs in code comments) as a MAJOR — Fable agrees on the fact, disagrees on severity.
- MAJOR-7 unit binding by identifier — Fable adopts it.
- The `sys.addaudithook` runtime probe (0 write/network/subprocess events on the executed path) — Fable did not run one; it complements, not replaces, the scanner-escape finding.
- M3 "implemented at `spec:515`" and M1 "partial at `freeze:171-174`" — Fable did not re-examine these direction-only items.

### 3.4 Conflicts and how they resolve

| Topic | Opus | Fable | Resolution |
| --- | --- | --- | --- |
| Arm parity in M0 | BLOCKER (must be M0 or the spec must drop it) | NOTE (defensible M1) | **Owner D2 rules M0** — Opus was right to force the decision |
| Severity of dangling ID comments | MAJOR | MINOR | Fix in the binding change either way; no Owner decision |
| Severity of unwired guards | MAJOR | MINOR | Fix set = union of both survivor lists; test before `M0-F1` exit |
| Scope of §5.1 gap | Two `spec:271` items | Eight field groups + five inputless checks | Both true; Fable's is the superset — packet §5.1 (or an explicit "spec:271 is the field authority" sentence) must cover all |
| Overall verdict on `40c7234f…` | `ACCEPT_WITH_CHANGES` | "not freezable as written; ACCEPT_WITH_CHANGES conditional on FB-01..04 + two Owner sentences" | Same substance; Fable states the Owner-decision precondition explicitly (FB-02, now met by D3) |

Unsupported-by-evidence check: no Opus finding was found to rest on a false anchor; every BLOCKER anchor was re-read by Fable in the source text. Opus's `.omc` attribution is the only factual error found (§1).

---

## 4. Structural re-check of `67c844d1…` (labelled; not a full review; no verdict transfer)

Read after Phase I was sealed. Fable read the new packet in full once and grepped the other changed documents for specific tokens; this is a targeted re-check of named findings, not a fresh adversarial pass.

| Phase I / Opus finding | State in `67c844d1…` and the changed docs |
| --- | --- |
| FB-03 / BLOCKER-1 | Header `:7` and `:19` now state the authorization is exhausted; OWN `:75` likewise. **Residual:** §9.1 `:200` still reads "The current fixture-backed M0 execution is bounded by handoff `m0-codex-continuation-20260817` … expiry after that task's one run" — stale wording that contradicts the header |
| FB-04 / BLOCKER-2 | §5.1 adds "preregistered power/MDE sufficiency rule, inputs, and directional-use policy"; check 19 added; materiality rule maps power/MDE insufficiency to `blocked + directional_only`; CE `VAL-M0-002` updated. **Residuals:** §5.3 `:127` still says "or another frozen sufficiency rule"; packet `VAL-M0-002` `:240` still says only "Runtime insufficiency" while CE `:129` says "runtime or preregistered-power/MDE insufficiency" — one ID, two texts again; `spec:469` clause not amended (ledger E10). Owner D1 fixes the *meaning* (declared `runtime_only | runtime_and_sample`, no post-hoc power) — not yet in the packet |
| FB-01 / BLOCKER-3 | Arm-parity identities and legal readiness-combination policy added to §5.1; arm parity in check 5. **Still missing:** CUPED identity/covariate window/adjusted label, scorecard/UI surface identity, recomputation contract/validator identity (D4/D6 `independence_class`, `comparison_rule_id`), numerator/denominator/grain, attribution, monitoring labels — FB-01 remains open |
| FB-02 | Not in packet; **closed by Owner D3** — but D3's shape (single stored `analysis_use`, derived projection) **conflicts** with §5.3 `:117-132` "two coordinated fields … neither takes precedence" |
| FB-07 human state, FB-08 registries, FB-09 gap taxonomy, FB-10 evidence_class, FB-11 register, FB-19 first-screen, FB-18 cap contradiction, FB-21 "minimum" | Unchanged (grep: `CHK-` 0, `materiality_rule_id` 1, `evidence_class` 0, `human_state` 0, "minimum check set" present, §9.1/§12(6) unchanged) — remain open; facilitator rulings F1-F19 propose closures but are not in the candidate |
| FB-12 | **Closed by Owner D5** (fixtures may not derive from protected assets); reuse inventory still to be written as `read-only reference` rows |
| FB-15 | **Partly closed by Owner D4/D6** (`independence_class`, `shared_source_snapshot` gap, `comparison_rule_id`); revalidation owner (profile item 3) still open; candidate check 14 text unchanged |
| FB-17 | CE `VAL-M0-002` rewritten; freshness mapping still unstated in packet (F14 proposes `not_permitted`) |
| FB-30 | `VAL-REM-002` restores "validity"; §13 `:327` binds the spec digest independently (new) |
| Opus MAJOR-1/-2/-3/-5/-7; FB-06, FB-26 | Code and unit-binding items unchanged (Phase B / binding change) |

Consequently `67c844d1…` closes the three Opus BLOCKERs in structure, leaves FB-01/07/08/09/10/11/18/19 open, introduces one fresh registry inconsistency (`VAL-M0-002` packet vs CE), keeps one stale sentence (§9.1), and now conflicts with Owner D3 and omits D1/D4/D6 semantics and all of S1-S8. It is a post-review correction candidate, as its own header says, not a freeze candidate.

---

## 5. Owner-decision delta — five two-way steelman attacks (per `kdd-m0-fable-adversarial-steelman-delta-20260818`)

Object under attack: the current candidate `67c844d1…`, the current spec/sequencing/eval/CE bytes, and the facilitator's `architecture-decision-ledger.md` (D1-D6, S1-S8, F1-F22), against the eight Owner decisions relayed in `steelman-owner-alignment-handoff.md`. Phase I lanes never saw these decisions; nothing below is attributed to them.

**Baseline fact for all five attacks.** `grep` for `recommend_pass|recommend_change|recommend_block|advisory`, `evidence_class|production_authorized`, `Query Success|TraditionalResultSuccess|AIAnswerSuccess`, `core material|core check`, `company laptop|PRODUCTION_BINDING_REQUIRED` over the current packet, spec, sequencing, evaluation plan and planning packet returns **0 hits in every file**. The only new-decision mechanism present anywhere is `independence_class` in the facilitator's design draft (7 hits). So the current freeze candidate cannot implement S1-S8 by construction; each attack below states what the contract must add and whether the residual is a contract defect or a production-binding gate.

### Attack 1 — False M0 completion (S1, S2)

- *Strongest supporting case (cannot be faked):* fixtures record `expected_final_readiness: alignment_pending`; `VAL-APR-001` separates technical state from Committee acceptance; §11.2 says fixture authorization "is not evidence of a real production ACL"; Phase A receipts carry `ActorKind.FIXTURE`; S1/S2 are now durable Owner decisions and F12 proposes `evidence_class`.
- *Strongest opposing case (can be faked today):* no packet or receipt field types `fixture | production_authorized`; the projection (`M0-F4`) renders both identically; PDP `:11,:98`, packet `:33`, sequencing `:505,:617` all call the fixture slice the "M0 MVP", the exact term S1 reserves for a real Flight; §10 V1 exit "Trusted and blocked fixtures plus one authorized Flight produce a `FlightReadinessPacket`" merges the two evidence classes in one exit; a correctly `blocked + not_permitted` production packet whose core checks returned `MISSING` (source not yet reachable) is indistinguishable from one whose core checks executed and failed.
- *Decision-changing variables:* (1) a typed `evidence_class` on every packet and receipt, rendered first-screen, with the rule that a `fixture` packet can never satisfy S1; (2) a typed `m0_capability_state` (`fixture_ready | production_capability_proven | flight_eligible`) that is `production_capability_proven` only when the preregistered core checks *executed* (outcome ≠ `MISSING`/`UNKNOWN`) against real evidence — a blocked packet with un-executed core checks stays `fixture_ready`-equivalent.
- *Disposition:* **product-contract defect** (fix before any freeze): add `evidence_class`, `m0_capability_state`, rename "fixture-backed M0 MVP" to "fixture-backed M0 pre-production slice" in PDP/packet/sequencing/CE, split V1's exit into fixture exit and production exit. Production-binding gate: which sources make core checks executable on the laptop (P2).
- *Falsifier:* render a fixture packet and a production packet through the same projection to a reviewer who has not seen the inputs; if they cannot name the class from the first screen, the contract fails.

### Attack 2 — Core-check discretion (S1)

- *Supporting:* the always-material list (packet `:111`) is fixed and cannot be waived by a rule; `NOT_APPLICABLE` needs a versioned applicability rule; `non_material` needs a preregistered rule and "reviewer convenience is not a rule"; F20 proposes the core set be preregistered in the production start receipt.
- *Opposing:* the packet still says "the **minimum** check set" (`:87`); there are no check IDs (`CHK-` 0 hits) so a "core subset" cannot even be named stably; no `core_check_set` field, no rule that a core check with outcome `MISSING`/`UNKNOWN` leaves capability unproven; the applicability rule lives in the `DecisionMetricPolicy`, which the Experiment Owner authors, so the party running the Flight can declare a check `NOT_APPLICABLE` after seeing the data unless the policy is sealed before the read and owned by a different role.
- *Decision-changing variables:* (1) core set = a versioned list of `CHK-nn` sealed in the production start receipt (digest-bound) **before** the first read, owned/countersigned by the Independent DS Consultant or the Committee's rule registry, not the Experiment Owner alone; (2) fail-closed semantics: a core check `MISSING`/`UNKNOWN`/`NOT_APPLICABLE`-without-rule → `m0_capability_state` stays unproven and `next_safe_action = evidence_collection`, even when the packet is a correct `not_permitted`.
- *Disposition:* **product-contract defect** (fix before freeze): check IDs (FB-08), delete "minimum", add `core_check_set` + sealing rule + ownership; the *content* of the core set for the first Flight is an Owner/DS decision (ledger F20 "pending Owner Q6"), and which checks are executable is a P2 gate.
- *Falsifier:* after results are visible, submit a start receipt naming a different core set for the same Flight; the second receipt must be rejected by digest/precedence, and any packet built from it must fail `VAL-*` acceptance.

### Attack 3 — Unaccountable metric challenge (S5, S6, S7)

- *Supporting:* S7's evidence floor (≥1 valid, scope-matched outcome stream not mechanically derived from the union) and `insufficient_evidence` default; the freeze contract forbids the Agent from producing `confirmed`; the advisory is explicitly non-binding and separate from the official read; F21 requires evidence IDs, counterevidence, an explicit falsifier and the DS challenge record on every advisory.
- *Opposing:* (i) "not mechanically derived from the same union metric" is not operationalized: reformulation, abandonment and session outcome are computed from the same click/session logs as `TraditionalResultSuccess`, and "AI-answer dwell" is itself a component input — without a lineage class on the challenge stream a component can be re-labelled as independent evidence; (ii) "human usefulness judgment" and "reviewed query/result evidence" are listed as admissible streams — without a preregistered, blind rubric this is subjective preference wearing an evidence badge; (iii) no `Advisory` object exists in any controlling document; the freeze contract's Recommendation Readiness enum (`not_applicable | blocked | proposal_ready | action_ready | rejected`) and Cause Verdict have no slot for `recommend_change`, and a Recommendation needs an exact target that an advisory does not have; (iv) S5 forbids inventing a hidden component guardrail after observing results, but nothing in the packet detects a post-hoc rule (no `rule_registered_at` vs `first_read_at` ordering check).
- *Decision-changing variables:* (1) `challenge_evidence_lineage_class` on each challenge stream (`independent_instrumentation | shared_logs_independent_definition | derived_from_decision_metric_inputs`), with the last class inadmissible for S7; (2) human-judgment streams admissible only under a preregistered rubric with sealed digest and blind adjudication (P4-owned); (3) a typed `AdvisoryRevision` (kind, evidence IDs, lineage classes, counterevidence, falsifier and its execution status, DS challenge record, official metric result beside it) distinct from Recommendation and from Cause Verdict; (4) rule-registration timestamps ordered before first read for every rule the advisory cites.
- *Disposition:* **product-contract defect** (design/freeze): the objects and lineage classes are missing; not a production-binding gate, though which streams exist on the laptop is P2.
- *Falsifier:* construct an advisory whose only challenge stream is a component of the union re-labelled; the contract must classify it `derived_from_decision_metric_inputs` and force `insufficient_evidence`.

### Attack 4 — M1 without M2 (S8)

- *Supporting:* packet §6 requires M1 to carry falsifiers, alternatives, counterevidence and Coverage Gaps; the freeze contract's G4/G5 keep Cause Verdict ≤ `suspected` while an independent challenge is missing; S8 makes M2 optional only for the *advisory*, not for causal confirmation; `insufficient_evidence` covers the no-orthogonal-stream case.
- *Opposing:* (i) without M2 there is no typed way to say "query-level evidence absent" — a Coverage Gap kind such as `no_query_level_evidence` does not exist; (ii) an advisory's falsifier may be executable only through query-level replay (M2); publishing an advisory whose falsifier cannot run gives the Committee a claim that looks testable and is not; (iii) Committee usability: an advisory rendered without the official read, the lineage class of its evidence, and its falsifier state reads as a causal verdict; (iv) M2 "may falsify" the advisory later — supersession of an advisory needs the same append-only rule as packets (new revision, prior acknowledgement invalidated).
- *Decision-changing variables:* (1) `query_evidence_state = absent | partial | present` on the advisory and M1 packet with a typed Coverage Gap when absent; (2) `falsifier_execution_status` on the advisory (`runnable_now | requires_m2 | requires_p2`); (3) advisory revisions are append-only and superseded, never edited, when M2 arrives.
- *Disposition:* **design gap** in packet §6/§7 (fix before freeze); not a production-binding gate.
- *Falsifier:* publish an advisory with `falsifier_execution_status = requires_m2` and no `query_evidence_state`; the projection must refuse to render it as review-ready.

### Attack 5 — Company-laptop boundary (S2)

- *Supporting:* Phase A digests are content-addressed, so a laptop-side run can be attested by receipt; F22's export model (packet + receipts + redaction manifest with digests leave the laptop; raw evidence and snapshots stay); spec already has ACL-scoped opaque pointers and the keyed-commitment rule for low-entropy confidential values (M18); `PRODUCTION_BINDING_REQUIRED` keeps field bindings out of this repository.
- *Opposing:* (i) reproducibility: a laptop-only replay receipt is self-attested by the person who ran it; the repository can never re-run it; (ii) handoff/continuity: the only production-capable environment is one person's laptop during a three-week absence (O5) — the Continuity Checkpoint cannot include the production path; (iii) privacy: bare digests of query strings, user ids or low-entropy locators in an exported packet are confirmation oracles (the M18 rule exists but no export manifest schema enforces it); (iv) `PRODUCTION_BINDING_REQUIRED` is a placeholder word today, not a typed sentinel — a fixture could fill the field with a plausible value and nothing rejects it; (v) the export itself is a publication step the Agent must not perform (packet §4 "no publication") — the human export path and its recipient scope are undefined.
- *Decision-changing variables:* (1) `PRODUCTION_BINDING_REQUIRED` as a typed sentinel with the same no-truth-value discipline as `UNKNOWN`, rejected by fixture validators; (2) an export manifest schema (what leaves the laptop, redaction receipt, keyed digests for confidential values, recipient scope, human exporter identity) — the packet's "authorization/redaction manifest" field is the natural home; (3) dual attestation for laptop runs (second person or second run signs the replay receipt) before the Committee treats it as reproducible.
- *Disposition:* items (1)-(2) are **contract items** (add before freeze); reproducibility attestation, laptop custody, and continuity through the absence are **production-binding / operational gates** (P2 + Owner staffing), not contract defects.
- *Falsifier:* export a packet containing a bare sha256 of a raw query; the export validator must reject it (keyed commitment or opaque pointer required).

**Delta summary.** All five attacks land on the same fact: the current candidate has no typed home for the new decisions. Contract defects (must be added before any freeze): `evidence_class`, `m0_capability_state`, "MVP" renaming, check IDs + `core_check_set` sealing, `AdvisoryRevision` with lineage classes and rubric rule, `query_evidence_state` + `falsifier_execution_status`, typed `PRODUCTION_BINDING_REQUIRED`, export manifest schema, D3 shape in §5.3, D1/D4/D6 semantics in checks 2/14/19. Production-binding gates (not defects): which sources make core checks executable, achievable `independence_class`, which challenge streams exist, laptop custody and dual attestation, exact metric thresholds and timers.

---

## 6. Complete finding table

Phase I findings (FB-01..FB-41) are listed in full in the sealed Phase I report §3 with evidence, counterargument, falsifier and disposition; the table below adds the current state after Opus comparison, the new bytes and the Owner decisions.

| ID | Sev (Phase I) | Claim (short) | Opus | State now |
| --- | --- | --- | --- | --- |
| FB-01 | BLOCKER | §5.1 field set subset of `spec:271`/profile; five inputless checks | BLOCKER-3 (narrower) | Partly closed in `67c844d1…` (arm parity, readiness policy); six field groups still missing |
| FB-02 | BLOCKER | Readiness contract not Owner-decided | — | Closed by Owner D3; candidate §5.3 must be rewritten to D3's shape |
| FB-03 | BLOCKER | Spent authorization presented as live | BLOCKER-1 | Closed in header/§1/OWN:75; §9.1 `:200` sentence still stale |
| FB-04 | BLOCKER | Underpowered full-runtime read forced to `decision_grade` | BLOCKER-2 | Closed structurally (check 19, §5.1 field); Owner D1 fixes meaning; §5.3 phrase, packet `VAL-M0-002`, `spec:469` still to align |
| FB-05 | MAJOR | Static-scanner escapes; receipt overstates | — | Open (Phase B hardening + receipt correction) |
| FB-06 | MAJOR | Seams cite draft sections; binding proves file only | MAJOR-1 | Open (binding change) |
| FB-07 | MAJOR | `human_state` undefined; ruling actor unnamed | — | Open; F10 proposed |
| FB-08 | MAJOR | No check-ID / materiality-rule registry | — | Open; F11 proposed; now also load-bearing for S1 core set |
| FB-09 | MAJOR | No Coverage Gap kind taxonomy; Phase A superset unreported | MAJOR-4 | Open; F1 proposed |
| FB-10 | MAJOR | No typed fixture-vs-production class | — | Open; F12 proposed; now load-bearing for S1/S2 |
| FB-11 | MAJOR | Open-decision register / freeze-record fields absent | — | Open |
| FB-12 | MAJOR | B3 inventory absent; fixture derivation open | MAJOR-6 | Owner D5 closes the decision; inventory still to write |
| FB-13 | MAJOR | Evaluation design too weak (baseline bar, precision, decoys) | — | Open; F13 proposed |
| FB-14 | MAJOR | Fixtures pooled, no per-arm data; partial-fixture arithmetic | — | Open (M0-F5) |
| FB-15 | MAJOR | Recomputation independence / revalidation owner open | — | D4/D6 close independence; revalidation owner open |
| FB-16 | MAJOR | Continuity checkpoint impossible while untracked | — | Open; needs Owner commit authorization |
| FB-17 | MAJOR | `VAL-M0-002` dual meaning; freshness state | — | CE fixed; new packet-vs-CE text divergence; F14 proposed |
| FB-18 | MAJOR | §9.1 vs §12(6) budget-cap contradiction | (C8 partial) | Open; F15 proposed |
| FB-19 | MAJOR | First-screen dropped but change-controlled | MAJOR-2 | Open; F5 proposed |
| FB-20 | MAJOR | Estimator "validity" unregistered; multiplicity absent | — | Open; F16 proposed |
| FB-21..FB-31 | MINOR | see Phase I | MAJOR-5/-7 overlap | Open; F17-F19 proposed for some |
| FB-32..FB-41 | NOTE | see Phase I | — | — |
| **FD-01** | **BLOCKER (delta)** | Current candidate contains none of S1-S8 and conflicts with D3; "M0 MVP" wording contradicts S1 | — | New revision required before any freeze |
| **FD-02** | MAJOR (delta) | No `evidence_class` / `m0_capability_state`; V1 exit merges fixture and production evidence | — | Attack 1 |
| **FD-03** | MAJOR (delta) | No check IDs / `core_check_set` sealing / ownership; "minimum" wording | — | Attack 2 |
| **FD-04** | MAJOR (delta) | No `AdvisoryRevision`, lineage class, rubric rule, or rule-timestamp ordering | — | Attack 3 |
| **FD-05** | MAJOR (delta) | No `query_evidence_state` / `falsifier_execution_status` / advisory supersession | — | Attack 4 |
| **FD-06** | MAJOR (delta) | `PRODUCTION_BINDING_REQUIRED` untyped; no export manifest schema; laptop attestation | — | Attack 5 (contract items) + P2 |
| **FD-07** | MINOR (delta) | `67c844d1…` residuals: §9.1 `:200` stale sentence; `VAL-M0-002` packet vs CE; `spec:469` clause; "another frozen sufficiency rule" | — | Fix in the next revision |

Counts — Phase I: BLOCKER 4 · MAJOR 16 · MINOR 11 · NOTE 10. Delta: BLOCKER 1 · MAJOR 5 · MINOR 1.

---

## 7. Unresolved Owner decisions (not P2/P3/P4)

1. Content of the first-Flight core material-check set and its ownership/countersignature (ledger F20 "pending Owner Q6").
2. Revalidation owner when a metric source/table/join/estimator/event definition migrates (profile item 3).
3. Admissible human-judgment challenge streams and who owns their preregistered rubric (Attack 3).
4. Whether the `analysis_use`/`decision_grade` wording states validity only (D1 says no post-hoc power; the Committee-facing sentence is still needed).
5. Owner authorization to commit the package and research documents to a feature branch so a Continuity Checkpoint can exist before 2026-08-24 (FB-16).
6. Confirmation of facilitator rulings F1-F22 at freeze (they are engineering/domain-model proposals until confirmed).
7. A new implementation start authorization and start receipt for `M0-F1`-`M0-F5` (BLOCKER-1/FB-03; the packet itself now says so).

---

## 8. Exact corrections required before any freeze (new packet revision)

1. Rewrite §5.3 to D3: single stored `analysis_use`, `post_analysis_eligibility` derived at render; keep the three legal readings; delete "another frozen sufficiency rule".
2. Encode D1 in checks 2/19 and §5.1 (`sufficiency_rule ∈ {runtime_only, runtime_and_sample}`; no post-hoc power; `MISSING` inputs → `contract_correction`); align packet `VAL-M0-002` with CE `:129`; amend `spec:469`.
3. Encode D2 handling (`MISSING`/`NOT_APPLICABLE` semantics for arm parity) and D4/D6 (`independence_class ≥ independent_transform`, `shared_source_snapshot` gap, `comparison_rule_id`) in check 14 and §5.1.
4. Complete §5.1 (FB-01): CUPED identity/covariate window/adjusted label; scorecard/UI surface identity; recomputation contract and validator identity; numerator/denominator/grain and pp-vs-relative interpretation; attribution; monitoring/diagnostic labels; or state that `spec:271` is the field authority.
5. Add S1-S8: `evidence_class`, `m0_capability_state`, "M0 MVP" renaming in PDP/packet/sequencing/CE, split V1 exit; `core_check_set` sealing and ownership; `AdvisoryRevision` with lineage classes, rubric rule and rule-timestamp ordering; `query_evidence_state` and `falsifier_execution_status`; typed `PRODUCTION_BINDING_REQUIRED` sentinel; export manifest schema; Query Success union shape as the named decision metric with component labels and fixed-within-Flight thresholds as `PRODUCTION_BINDING_REQUIRED`.
6. Define `human_state` (FB-07/F10) and the materiality ruling actor; assign `CHK-01..CHK-19` and name the materiality/applicability rule registry (FB-08/F11); freeze the Coverage Gap kind set or declare it engineering-owned (FB-09/F1); restore the first-screen pointer (FB-19/F5); make the cap/expiry halt unconditional (FB-18/F15); state the freshness mapping (FB-17/F14); add the open-decision register and freeze-record rules (FB-11); state the authority rank of the frozen packet in the spec's authority order (FB-30); delete the stale §9.1 sentence (FD-07).
7. Owner sentences recorded in `owner-alignment-record.md` (or its successor) for D1-D6 and S1-S8, so the packet's authority line resolves to a durable record rather than to a handoff.
8. Phase B binding change (not packet bytes): rewrite `SEAM-M0-*` references against the frozen headings; repoint dangling `M0-SEC-001`/`M0-READ-001` comments; add the four unwired-guard tests (duplicate receipt id, `seal()`→`verify_chain`, `scan_package` non-vacuity, `_case_path` containment) and the planted-count lock; harden the scanner and correct the receipt sentence (FB-05); allow `kind = UNKNOWN` instead of the default gap-kind map (FB-27); require a non-empty, registry-resolving `rule_source`.

---

## 9. Gates that remain after a local M0 freeze

P2 (production evidence authority: sources, owners, credentials, ACL/tenant, retention, redaction, load ceilings, halt authority; plus, per D2/D4/S1/S2, per-arm index generation and ACL snapshot sources, achievable `independence_class`, and the laptop export/attestation path); P3 (live review surface with named reviewers; first-screen hierarchy); P4 (sealed fixtures, blind evaluation, adjudication, calibration, thresholds, human-judgment rubric); Experiment Review Committee acceptance for a real Flight; new Owner start receipt for `M0-F1`-`M0-F5`; the S1 production-backed M0 completion run on the company laptop; unapplied adjudications B3 (inventory rows), M18, M19, M20.

---

## 10. Recommendation for the next implementation session

Sequence (after the packet revision in §8 is accepted and digest-bound, and a new start receipt exists):

| Step | Work | Binds | Execute | Independently verify |
| --- | --- | --- | --- | --- |
| 0 | Packet revision + Owner record update + seam rewrite | §8 items 1-7 | Codex (document maintenance) under Owner sign-off | Opus 5 (contract review, exact-digest) + Fable 5 arbitration if conflicts |
| 1 | `M0-F1` contracts incl. `evidence_class`, `m0_capability_state`, `human_state`, `CHK-*`, D3 shape | `VAL-FLT-001`, `VAL-MET-001/002` | Codex or Opus 5 executor, fresh session, not the Phase A author | Opus 5 reviewer with mutation battery; Fable 5 personally inspects BLOCKER-level claims |
| 2 | `M0-F2` reads/receipts with `independence_class` receipt | exit evidence `seq:57` | same | same |
| 3 | `M0-F3` decoys first (`VAL-SRC-001`, `VAL-CUP-001`, `VAL-UNIT-001`), then `VAL-PRE-001`, `VAL-M0-002`, `VAL-M0-001`, `VAL-CONF-001`; checks 2/5/14/19 per D1/D2/D4/D6 | | same | statistician lens (Opus 5) for checks 4/6/11/13/14/19 |
| 4 | `M0-F4` seal, supersession, projection with `evidence_class` banner | `VAL-SUP-001`, `VAL-UI-001`, new `VAL-DET-001`, `VAL-REM-001` | same | Fable 5 first-screen review against S1/S2 |
| 5 | `M0-F5` per-arm fixtures, paired decoys, three baselines, `VAL-BASE-001`, `VAL-DECOY-001`, `VAL-SEC-001` | | same | independent Opus 5 fixture adversary (author ≠ evaluator receipt) |
| 6 | Continuity Checkpoint before 2026-08-24 (needs Owner commit authorization) | `VAL-CON-001`, `VAL-APR-001` | primary builder | fresh-context rehearsal by a session that has read nothing but the start-here index |
| 7 | Production-backed M0 run on the company laptop (S1) | core check set, export manifest | primary builder under P2 | second attester on the laptop; Committee sees `m0_capability_state` |

Model guidance: implementation by a fresh Opus 5 or Codex session that did not author Phase A; contract/security/statistics review by Opus 5 in a separate context with an isolated-copy mutation battery every slice; Fable 5 as lead arbiter who personally inspects every BLOCKER; Sonnet 5 only for bounded greps, digests and link checks. Never let the Phase A author self-verify (the second freeze review declined exactly this, correctly).

---

## 11. Boundary statement

No product, agent, test, fixture, controlling, policy, or candidate-patch file was modified. No commit, branch, stash, checkout, worktree, push, PR, install, network, production, credential, or external-message action. Writes: the three authorized artifacts in this directory (Phase I report, this report, `fable5-review-status.json`), the delta status `steelman-owner-decisions-review-status.json` authorized by the delta handoff, all via scratch + `cp` (disclosed), and the removal of hook-created `.omc` state files inside the package (disclosed; aggregate unchanged). All mutations, planted modules and probes ran on the isolated copy under the job scratch directory and were reverted. Nothing here freezes the packet, authorizes implementation, or claims production validation or Committee acceptance.
