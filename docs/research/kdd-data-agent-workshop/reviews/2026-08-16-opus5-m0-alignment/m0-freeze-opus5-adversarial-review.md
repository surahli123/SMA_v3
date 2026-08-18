# Independent Opus 5 Adversarial Review of the M0 Freeze Candidate and Phase A

Reviewer model: Claude Opus 5 (`claude-opus-5`), Claude Code background session
Session ID: `session_01YAshweqBjaqSc7S2SfufFS`
Review timestamp: 2026-08-18T02:27:48Z
Repository: `/Users/surahli/Documents/projects/SMA_v2`
Branch: `codex/kdd-data-agent-practices-research`
HEAD inspected and preserved: `28cbbda6e4d4d7f08134952d38433e52d3ee8768`
Mode: independent adversarial review, read-only except this file and the paired status JSON

## Reviewed artifact binding

Findings below are bound to these exact bytes, verified at the start and end of the review:

| Artifact | SHA-256 |
| --- | --- |
| `m0-m2-build-alignment-packet.md` (the freeze candidate) | `40c7234f3c0d85f18ebfba656e7aec2ab5ab71b86451a077ecad340eac779396` |
| `owner-alignment-record.md` | `0c717916c3a469a4aa56a522add09887c4735e244a3526b08d058b6963f8436a` |
| `opus5-review.md` | `2b851aaf788f260267946daa2aa63ca483ddfa0a7e8fc225a235644e9265b0c0` |
| `m0-freeze-opus5-review-handoff.md` | `3cd255c016e368405577b65ec57ba44aa0a555c19e523f0897b186b15db07ff0` |
| `.agents/skills/kdd_data_agent/` aggregate (py+json+md, caches excluded) | `2f1001b93b19b2318c4c6419205ed2f7778ac23c02533e78a0c0899f15bf7d1e` |

The package aggregate covers every `.py`, `.json`, and `.md` file under the package, excluding
`__pycache__`, `.pytest_cache`, and `.omc` harness state. It matches the value recorded in
`m0-codex-continuation-receipt.md` section 2, so this review inspected the same Phase A bytes the
continuation task receipted. It was re-measured after every probe and after writing this report, and
every package source file is byte-for-byte unchanged.

One honest exception, disclosed rather than smoothed over: two ephemeral OMC harness state files were
created at `.agents/skills/kdd_data_agent/.omc/state/sessions/4bda4e93-.../` at 02:29Z because a
shell call in this review ran with its working directory inside the package, and the harness writes
session state relative to the working directory. They are
`last-tool-error-state.json` (a record of one of this review's own failed `cd` commands) and
`pre-tool-advisory-throttle.json`. They contain no package content, are operational artifacts that
`CLAUDE.md` classifies as ignored state, and do not affect the source aggregate above. I attempted to
delete them to restore the directory exactly; the deletion was denied by the environment's permission
classifier, so they remain. **Action for the Owner: delete that `.omc` directory inside the package
before the Continuity Checkpoint snapshot is taken**, so the checkpoint's clean-checkout claim is
literally true.

The prior Claude attempt `ed33fb08` produced no verdict and was not used as evidence.

## Verdict

**`ACCEPT_WITH_CHANGES`**

The candidate is materially better than the draft it replaces, and most of it is freezable today.
It fails freeze requirement 2 in its own section 13 — "Opus 5 finds no unresolved ambiguity that
would produce materially different M0-M2 behavior" — because of three blockers, two of which cause
two competent implementers to build different M0 behavior, and one of which presents a spent
authorization as a live one.

Phase A receives an independent **`PASS_WITH_GAPS`**. Its claims reproduce, and 19 of 22 mutation
probes were caught. It has not silently chosen an unfrozen semantic meaning.

## What was actually inspected

Documents read in full: the freeze candidate; `owner-alignment-record.md`; `opus5-review.md`
(section 2 30-row audit, section 3 8-row adjudication, sections 4.1-4.6 including C1-C9, section 5
decision table); `m0-codex-continuation-handoff.md`; `m0-codex-continuation-status.json`;
`m0-codex-continuation-receipt.md`; `m0-build-alignment-packet-draft.md` (structure only, to prove
supersession drift).

Documents read in relevant part: `final-architecture-spec.md`; `implementation-sequencing.md`;
`eval-acceptance-plan.md`; `planning-decision-packet.md`;
`enterprise-experiment-post-analysis-profile.md`;
`wayfinder/freeze-canonical-domain-policy-contracts.md`;
`docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md`; `docs/adr/0004`-`0008`.

Code read in full: `alignment/seams.py`, `core/capabilities.py`, `core/canonical_json.py`,
`core/coverage_gap.py`, `core/immutability.py`, `core/unknown.py`, `core/revisions.py`,
`core/digest.py`, `adapters/fixture.py`, `adapters/outcomes.py`, `runner/hermetic.py`,
`tests/_import_graph.py`, `tests/test_capability_allowlist.py`, and the nine fixture files.

Commands actually run (all read-only against the repository; every mutation ran on an isolated
byte-identical copy under the job scratch directory):

```text
shasum -a 256 <packet, authority docs>
find .agents/skills/kdd_data_agent -type f ... | xargs shasum -a 256 | shasum -a 256
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider .agents/skills/kdd_data_agent/tests
  -> 225 passed in 0.21s   (repository root, independent reproduction)
tar -cf - kdd_data_agent | (cd $JOB/mut1 && tar -xf -)      # isolated copy, aggregate verified equal
python3 mutate.py            # 22 single-guard mutation probes, suite re-run per probe
PYTHONHASHSEED={0,1,99991} python3 runtime_probe.py          # audit-hook + determinism probes
python3 adversarial.py       # 38 object-level fault injections against the real package
grep/sed cross-document consistency sweeps (VAL registry, readiness contract, check inventory)
```

## C1-C9 propagation table

Scope of each verdict: does the correction reach the freeze candidate **and** the controlling
plan/spec/eval documents with one meaning?

| Edit | Verdict | Evidence | Residual |
| --- | --- | --- | --- |
| **C1** resolve acceptance-ID collision | **satisfied** | Candidate section 11:224 states the single-registry rule; the section 11 table and `CE:125-146` share 22 `VAL-*` IDs with no string collision; the candidate extends by exactly 4 (`VAL-M1-001/002`, `VAL-M2-001/002`). The colliding `M0-CON-001`/`M0-READ-001`/`M0-SEC-001` strings are gone from the CE plan. | `implementation-sequencing.md` binds only `VAL-UI-001`/`VAL-UI-101` (seq:59); the other 20 shared IDs map to no sequencing unit. `eval-acceptance-plan.md` section 8.M0 carries the same requirements as unlabelled prose with zero IDs. See MAJOR-7. |
| **C2** third outcome state | **partial** | The orthogonal two-field contract is a stronger answer than the requested third enum value and propagated verbatim to `spec:36`, `spec:199`, `spec:274`, `seq:56`, `CE:32`, `CE:198`, `planning-decision-packet.md:22`, `eval:212-213`, candidate section 5.3. | The `ExperimentReadContract` permission field that `spec:469` still requires is absent from candidate section 5.1, and no non-runtime sufficiency rule exists anywhere. See BLOCKER-2. |
| **C3** restore four owner-named checks | **satisfied** | Candidate section 5.2 carries 18 checks. CUPED non-interchangeability = check 11; primary-source vs scorecard/UI = check 13; numerator/denominator/unit/ratio/relative-percent/percentage-point = check 8; source-change revalidation = check 15; independent recomputation = check 14. `seq:58` lists the same 18 in the same order; `eval:` section 8.M0 and `spec:271` carry them. | None. This is the cleanest propagation in the packet. |
| **C4** type the next safe action | **satisfied** | Candidate section 5.4:132-136 fixes exactly five kinds, "no exact production target and no diff", and routes any diff to the separately typed `InvalidExperimentRemediation`. Mirrored at `spec:273`, `spec:275`, `seq:56`, `CE:198`, `eval:` section 8.M0. | None. |
| **C5** split `VAL-UI-001` / `VAL-UI-101` | **satisfied** | Candidate section 11 rows 250-251; gate map section 11.2:271-272; `seq:59`; `CE:35`, `CE:143-144`. | None. |
| **C6** bind the B11 controls to M0 | **satisfied** | Candidate section 11.1:257-261 (always-ready and always-blocked arms, planted truth, suite rejection before scoring, decoys, author/evaluator independence or disclosed conflict); `VAL-BASE-001`, `VAL-DECOY-001`; mirrored `eval:` section 8.M0, `spec:870`, `CE:145-146`. | None. The conflict-never-expires-by-seniority-or-timeout rule survived. |
| **C7** name the gates | **satisfied** | Candidate section 11.2:263-276 maps every check group and every `VAL-*` family to fixture-only / P2 / P3 / P4, and closes with the "fixture authorization is not evidence of a real production ACL" sentence. | None. |
| **C8** deterministic stop conditions and budget cap | **partial** | Candidate section 12 carries 13 deterministic triggers (a superset of the requested six) with named halt owners split 1-6 local / 7-13 contract authority; section 9.1 requires a slice-specific cap, run/read/tool cap, expiry, and halt owner on every start receipt. The drifting phrase "authorized 2026-08-16 build session" is **gone** — its only occurrence corpus-wide is inside the review handoff's own question text. | The named cap is already spent. See BLOCKER-1. |
| **C9** add the two missing Owner decisions | **satisfied** | O1 (Flight = one Experiment) and O2 (decision-metric set + policy, one by default, no permanent singular cardinality) in `owner-alignment-record.md:13-19`; ADR-0004; candidate section 3:37-44. `profile:446` records both as resolved. | None. |

## 30/8 reconciliation verdict

**The 30 accepted findings.** The prior audit's tally (22 `EXACT`, 5 `SEMANTICALLY_EQUIVALENT`,
3 `PARTIAL`, 0 `MISSING`, 0 `OVERREACH`) holds against the current worktree for the rows I
re-verified, with one correction. I confirmed M22 (positive capability allowlist plus import-graph
assertion) has moved from spec text to a mechanically enforced and independently falsifiable
control; M24 (named variance estimator and unit of analysis) reaches candidate section 5.1 and
check 4; M6 (materiality by construction, unclassified defaults material) reaches candidate
section 5.2:105 and `spec:272`; M21 (`(revision_id, content_digest)` manifest with `prev_digest`)
is implemented in `core/revisions.py:66-76`.

The correction is **M9**. Its `EXACT` rating is true of the spec and false of the slice about to be
frozen: `arm parity` appears twice in `final-architecture-spec.md` (`:271`, `:414`) and **zero
times** in the candidate, in `seq` rows `M0-F1`/`M0-F3`, or in the CE plan's `M0-F*` rows. See
BLOCKER-3. No finding was implemented as overreach.

**The eight adjudicated dispositions.** Three are fully implemented, one is partial, and four still
carry an unapplied required action:

| ID | State | Evidence |
| --- | --- | --- |
| **B2** | **implemented** | M0 first and main (candidate section 2:29, `seq:49-58`); M1/M2 inside the same separately gated validation slice (section 2:29-33, section 11.2:273). The sizing half that was `OWNER_DECISION_REQUIRED` is now answered: two builders, four to six active weeks, leave excluded (section 9.1, O5). |
| **B3** | **open — required action not performed** | Policy is stated (candidate section 8:179-181, O6). The per-asset reuse inventory the adjudication required "before `M0-F1`" does not exist; `metric_registry`, `schema_catalog`, and business-table routing are still named as candidate assets in **no** canonical document. See MAJOR-6. |
| **B11** | **implemented** | Candidate section 11.1 plus `VAL-BASE-001`/`VAL-DECOY-001`, mirrored into `eval:` section 8.M0 and `spec:870`. Baselines, decoys, and the independence/conflict receipt now bind the funded slice, which was the entire HYBRID objection. |
| **M1** | **partial** | `freeze:171-174` now carries an exit: "New Evidence never overwrites `confirmed` or `ruled_out`; it creates a new claim/verdict revision...". The no-exit contradiction is repaired. The **active-versus-closed-generation split** that `spec:404` depends on is still absent from the higher-authority freeze document. Direction-only: M0 emits no verdicts. |
| **M3** | **implemented** | `spec:515` now requires delivery "only through an authorized human review surface", names "recipient/**channel** enforcement", and keeps the diff correct rather than corrupted. The channel-type gap the adjudication identified is closed. `not_applied`, human-only, no automation consumer all hold. |
| **M18** | **open — required action not performed** | The rule is correctly narrow at `spec:672` and is **not** overgeneralized to public full-file or image digests. But the eight bare SHA-256 digests of internal roadmap and tech-spec screenshots are still published at `enterprise-experiment-post-analysis-profile.md:27-34`, unclassified. Out of M0 scope; blocks external sharing, not the freeze. |
| **M19** | **open — required action not performed** | `spec:673` prohibits the collection pattern outright, so the first-version Trace limit to Data Agent-owned runtime holds. The requested pointer line at the head of `deepseek-harness-practices.md:286` was not added; section 16.3's host-hook topology still reads as a build plan on first open. Direction-only: M0 has no Trace. |
| **M20** | **open — required action not performed** | Optional-Trace-absence-is-a-Coverage-Gap holds (`spec:648`, `spec:709`). The requested sentence preventing post-hoc narrowing of the Trace-dependent assertion set was not added; `grep` for "cannot be narrowed" and "frozen generation inputs" returns nothing. The circularity the adjudication named survives. Direction-only. |

## Blockers

### BLOCKER-1 — The packet presents a spent authorization as a live one

**Evidence.** Candidate `m0-m2-build-alignment-packet.md:7`: "`m0-codex-continuation-handoff.md`
permits `M0-F1`-`M0-F5` only after exact frozen packet path, revision, and SHA-256 binding."
Reinforced at `:19` and mirrored into the authority document at `owner-alignment-record.md:75`.

Against `m0-codex-continuation-handoff.md:70-72`: "Active-time cap: this single non-recurring task
execution only. A second task, resumed task after finalization, or scope extension requires a new
Owner authorization and handoff", and `:86-87` "Expiry: after this task's one
implementation-continuation run". That run completed:
`m0-codex-continuation-status.json:4` records "The one-run execution cap is exhausted", `:16`
accounts for 12 full-suite invocations, and `:19` states "Stop this task. A new Owner authorization
and handoff are required for any resumed or second task."

**Consequence.** Read literally, the frozen packet says the only remaining precondition for starting
`M0-F1`-`M0-F5` is a digest binding. It is not — the cited handoff's authority is spent. On
acceptance, the digest binding arrives and an implementer has packet text telling them they may
proceed. This is the exact silent-renewal wording the review handoff's question 10 directs me to
reject; it does not convert into the four-to-six-week program budget, which is correctly
firewalled at section 9.1, but it does renew a consumed local cap.

**Minimal fix.** In candidate `:7` and `:19`, and in `owner-alignment-record.md:75`, replace the
"permits ... only after ... binding" construction with: "The `m0-codex-continuation-20260817`
authorization is exhausted. `M0-F1`-`M0-F5` require a new Owner authorization and start receipt
that binds the accepted packet path, revision label, and SHA-256, plus its own active-time,
run/read/tool cap, expiry, and halt owner." One sentence in each of the three places.

### BLOCKER-2 — `directional_only` has no reachable trigger except the runtime check, and its contract permission is undefined

**Evidence.** Candidate section 5.3:121 defines `blocked + directional_only` as "the preregistered
runtime **or another frozen sufficiency rule** is incomplete". No other frozen sufficiency rule
exists. The 18 checks in section 5.2 contain no power, MDE, or precision check; across the whole
controlling corpus `grep -i 'underpowered|MDE|minimum detectable|statistical power'` returns exactly
two hits — `final-architecture-spec.md:469` and `enterprise-experiment-post-analysis-profile.md:386`.

Separately, `spec:469` still reads: "A valid-but-underpowered read may be labeled `directional_only`
**only when the ExperimentReadContract permits it**." Candidate section 5.1:63-76 does not define
any such permission field. `SEAM-M0-04-CONTRACT-FIELDS` (`alignment/seams.py:140-141`) names this
exact gap: "the directional_only permission field proposed by C2 ... is not frozen."

**Consequence.** A read that is valid on all 18 checks but statistically underpowered, with the
preregistered runtime complete, has every check `PASS`. Under section 5.3's closed combination table
the only remaining state is `eligible + decision_grade`. An underpowered read is therefore silently
promoted to decision-grade — the failure mode M7 and the Owner's own ceiling at `profile:121` exist
to prevent. Implementer A reads section 5.3 and ships runtime-only directionality; implementer B
reads `spec:469`, looks for the permission field, cannot find it, and either invents one or refuses
to emit `directional_only` at all. That is candidate stop condition 9 firing at freeze time.

**Minimal fix.** Choose one and state it in sections 5.2 and 5.3: either (a) add a 19th check —
"preregistered power/MDE sufficiency for the decision metric" — whose material failure maps to
`blocked + directional_only` when no other blocker applies, and add the corresponding contract
field to section 5.1; or (b) state explicitly that M0 performs no power assessment, that
`directional_only` is reachable **only** through the preregistered-runtime check, and amend
`spec:469` to match by deleting the "only when the ExperimentReadContract permits it" clause. Either
resolves it; leaving both texts standing does not.

### BLOCKER-3 — `spec:271` requires two `ExperimentReadContract` fields the candidate omits, and no M0 check consumes arm parity

**Evidence.** `final-architecture-spec.md:271` enumerates the `ExperimentReadContract` as including
"... CUPED identity; **arm parity fields**; compositional-SRM plan; ... **legal readiness-combination
policy**; and named Experiment Owner...". Candidate section 5.1:63-76 omits both.
`grep -ci 'arm parity'` returns 0 for the candidate, 0 for `seq` rows `M0-F1`/`M0-F3`, and 2 for the
spec (`:271`, `:414`). `spec:414` makes arm parity across "index generation/serving alias/ACL
snapshot/effective pipeline" a required G1 validity input whose divergence "caps Cause at
`suspected` and blocks query comparability".

**Consequence.** The freeze binds `M0-F1` to a contract field list that contradicts the controlling
spec, and binds `M0-F3` to an 18-check inventory with no arm-parity check. Arm parity is a search
relevance-specific validity trap — treatment and control served by different index generations or
ACL snapshots produce a real metric delta with no product cause — and it is exactly the class M0 is
supposed to catch before M1 starts. This is the same failure shape as B11: the control exists in the
spec and does not bind the funded slice.

**Minimal fix.** Decide whether arm parity is M0 or M1, once, and make both documents say it. If
M0: add "arm parity fields (index generation, serving alias, ACL snapshot, effective pipeline)" to
candidate section 5.1, and add arm parity to check 5 or as check 19; add "legal
readiness-combination policy" to section 5.1. If M1: delete "arm parity fields" from `spec:271` and
record the deferral in candidate section 6, so the M0 contract stops claiming a field nothing reads.

## Major findings

### MAJOR-1 — Every alignment seam points at the superseded draft's section numbers

`alignment/seams.py` `packet_reference` values track `m0-build-alignment-packet-draft.md`, which the
review handoff declares superseded. Draft structure: 3 User Job and Decision, 4 Required Input,
5 Required M0 Checks, 6 Required Output, 7 Proposed First-Screen Contract, 8 First Vertical
Spike, 9 Acceptance Scenarios, 11 Owner Decisions. Candidate structure: 3 Flight and
Decision Metric, 4 Human Responsibility, 5.1 input, 5.2 checks, 5.3 readiness, 5.4 output,
8 Production Authority, 9 Build Envelope, 11 Acceptance Scenarios, 12 Stop Conditions.

Eight of ten misdirect: `seams.py:112` (3 -> should be 5.3), `:143` (4 -> 5.1), `:153` (6 ->
5.4), `:163` (9 -> 11), `:173` (7 -> absent), `:195` (11 -> the Owner record), `:205` (8 -> 12).
`:122` (5) survives only because 5.2 is nested under 5. `seams.py:119` also still says "The draft
lists 14 checks", which is stale — the candidate has 18 — and `:160-161` still describes the
acceptance-ID collision that C1 resolved.

**Consequence.** The seam registry is the mechanism Phase B follows to fill each decision against
the frozen digest. Freezing the packet without correcting it hands the implementer a map whose
section numbers resolve to the wrong content in the very document they are told is authoritative.
Phase A was correctly forbidden to *fill* a seam; updating a stale cross-reference is not filling
one.

**Minimal fix.** In the same change that records the accepted `FrozenPacketBinding`, update all ten
`packet_reference` strings to the accepted packet's section numbers, correct "14 checks" to 18 at
`:119`, and rewrite `:160-161` to state that the registry is now unified on `VAL-*` and that what
remains open is which IDs bind which `M0-F*` unit.

### MAJOR-2 — The first-screen contract was dropped but is still referenced as accepted

Draft section 7 "Proposed First-Screen Contract" has no successor in the candidate. Yet candidate
section 13:319 lists "first-screen hierarchy" among the changes that force a new packet revision,
and `VAL-UI-101` (section 11:251) reads "**The accepted** first-screen hierarchy and review behavior
are bound to a named live-review receipt". Nothing in the candidate accepts one.
`SEAM-M0-07-FIRST-SCREEN` (`seams.py:173`) cites "alignment packet section 7", which is now
Production Authority and Old SMA.

**Consequence.** Change control protects an artifact the packet does not contain, and an acceptance
scenario asserts an accepted hierarchy that does not exist. `M0-F4` (`seq:59`) must render a
packet-centered projection with no frozen hierarchy to render.

**Minimal fix.** Either restore a short first-screen subsection to the candidate, or add one line to
section 11 stating that the first-screen hierarchy is deliberately held at
`wayfinder/prototype-observability-first-review-surface.md:23` and `spec:581-587` and is P3-gated,
and retarget `SEAM-M0-07` there. Then change `VAL-UI-101`'s "The accepted" to "The P3-accepted".

### MAJOR-3 — Phase A code cites acceptance IDs that no longer exist

`adapters/outcomes.py:44-46`: "the alignment packet **draft** (`M0-SEC-001`) and the CE plan
(`M0-READ-001`, `M0-SEC-001`) state it independently and agree."
`core/identity.py:72-73` cites the same three strings.

None of `M0-SEC-001`, `M0-READ-001` exists in `docs/plans/2026-08-12-001-...-greenfield-plan.md` any
more; C1 renumbered that registry to `VAL-*`. The code's justification for a security invariant
therefore points at a superseded document and two dangling identifiers.

**Consequence.** The no-retained-body rule is correct and mechanically enforced
(`adapters/fixture.py:308-312`, proven by mutation probe M10), so behavior is right. But its stated
authority is unreachable, and the next reader cannot verify the invariant against a live document.

**Minimal fix.** Repoint both docstrings at `VAL-SEC-001` and `VAL-M0-002` in the accepted packet
section 11, in the same change that records the binding.

### MAJOR-4 — `CoverageGapKind` exceeds the frozen taxonomy and was neither seamed nor reported

`core/coverage_gap.py:26-37` defines nine kinds. `freeze:61` — authority 3, above the spec — glosses
Coverage Gap as "Missing authority, timeout, unavailable source, unknown mapping, or unchecked
evidence plane": five. The four additions (`PARTIAL_READ`, `STALE_READ`, `CONFLICTING_SOURCES`,
`REDACTION_FAILURE`) are supported by `spec:829` and `spec:156`, so this is defensible rather than
reckless — but the continuation handoff section B directed exactly this case: "If the controlling
documents do not define an exact Coverage Gap enum, do not invent one. Preserve the behavior behind
an explicit alignment seam and report the unresolved contract." No seam exists and
`m0-codex-continuation-receipt.md` section 6 does not report it.

**Consequence.** These values are digest-bound: `CoverageGap.to_canonical()` includes `kind.value`
and `gap_id` is a `stable_id` over it (`coverage_gap.py:77-87`). Every sealed Phase A digest already
commits to a taxonomy the packet never froze. If Phase B adopts a different enum, every existing
digest changes.

**Minimal fix.** Add `SEAM-M0-11-COVERAGE-GAP-TAXONOMY` naming `freeze:61` versus `spec:829` as the
unresolved authority, or freeze the nine-value enum explicitly in candidate section 5.2 and
reconcile `freeze:61`.

### MAJOR-5 — Three Phase A guards are not proven by the 225-case suite

From the 22-probe mutation battery (each probe removes one guard on an isolated copy and re-runs the
full suite; a guard is proven only if the suite turns red):

| Probe | Mutation | Suite | Meaning |
| --- | --- | --- | --- |
| M04 | delete the repeated-receipt-identity rejection at `runner/hermetic.py:148-150` | **225 passed** | Receipt defect 7 claims the runner was corrected to "correlate adapter results to issued requests **or reject repeated receipt identities**". The correlation half is proven (probe M03 -> red). The duplicate-receipt half is not tested at all. |
| M13 | delete `self.verify_chain()` from `RevisionLog.seal()` at `core/revisions.py:184` | **225 passed** | "seal() verifies the chain" is unproven. `run_foundation` happens to call `verify_chain()` separately at `hermetic.py:156`, so the runner path is safe today; any other caller that seals without that line gets no chain check. |
| M22 | make `scan_package` return `()` before its loop (`tests/_import_graph.py:288`) | **225 passed** | The two "package is clean" assertions pass vacuously if the scanner stops walking files. The planted-violation tests exercise `scan_source` directly and `test_the_package_contains_no_python_files_outside_the_scanned_set` anchors `python_files`, but nothing anchors the step that applies the scanner to those files. |

**Consequence.** These are latent, not live: probes M17-M21 planted real violations (a `socket`
import, a `datetime.now()` call, a `write_text` call, an `adapters/production/` directory, an
unscanned `.py` file) into the runtime package and **all five were caught**, so the capability
control genuinely works right now. The risk is a future edit that breaks the scanner's file walk, or
an adapter that repeats a receipt identity, landing green.

**Minimal fix.** Three tests: one asserting a stub adapter returning a duplicate receipt is
rejected; one asserting `RevisionLog.seal()` raises on a hand-broken chain; and one asserting
`scan_package` returns at least one finding when applied to a root containing a deliberately
violating module — or, since tests cannot write files under this capability policy, inject the
per-file scanner into `scan_package` and assert it is invoked once per `python_files` entry.

### MAJOR-6 — B3's reuse inventory still does not exist, and it gates `M0-F1`

`grep -rn 'metric_registry|schema_catalog|basis-table'` across the canonical documents returns only
generic "basis-table" mentions in `enterprise-experiment-post-analysis-profile.md:34,95,112`. No
document names one row per asset with a `read-only reference` / `clean-room reimplement` /
`direct reuse pending review` disposition. `SEAM-M0-08-FIXTURE-BASELINES` honestly records that
"whether fixtures may derive from protected domain assets is an open Owner decision", which is the
right handling — but the adjudication's required action was to write the inventory **before**
`M0-F1`, and `M0-F1` is precisely what the freeze unblocks.

**Consequence.** M0's metric-registration check (check 3) and independent recomputation (check 14)
are the work the Owner indicated is already validated through basis-table routing. Starting `M0-F1`
without the inventory means re-deriving assets that exist, or reusing them without the interface,
provenance, test, security, and license review O6 requires.

**Minimal fix.** One page, one row per asset, three possible dispositions, plus the Owner's answer
on whether M0 fixtures may be derived from those files. Prerequisite for `M0-F1`, not for accepting
the packet.

### MAJOR-7 — 20 of 22 shared `VAL-*` IDs bind to no sequencing unit

`implementation-sequencing.md` references `VAL-UI-001` and `VAL-UI-101` (seq:59) and no other
`VAL-*` ID; `eval-acceptance-plan.md` and `final-architecture-spec.md` reference none. Candidate
section 13 freeze requirement 3 is "Codex maps every active requirement to a startable unit and
acceptance scenario."

**Consequence.** As written, requirement 3 cannot be evidenced for 20 of the 22 scenarios. The
mapping exists implicitly through the `M0-F*` exit-evidence prose, but not by identifier, so drift
between a scenario and its unit is undetectable.

**Minimal fix.** Add a `VAL-*` column to the `M0-F0`-`M0-F5` rows in `seq:53-58`, or one table in
the freeze record mapping each `VAL-*` to its owning unit.

## Phase A independent verification

### Reproduction

`225 passed in 0.21s` from the repository root, independently, matching
`m0-codex-continuation-receipt.md` section 2. The package aggregate before and after was
`2f1001b93b19b2318c4c6419205ed2f7778ac23c02533e78a0c0899f15bf7d1e`, identical to the receipt's
value, so the suite writes nothing into the package.

### Mutation battery — 22 probes, 19 caught

Caught (guard proven by the suite): deep-freeze no-op (4 failed); readiness-seam construction
unblocked (1); request-correlation removed (1); manifest/outcome binding removed (1); manifest
membership removed (1); sentinel-provenance relaxed (1); materiality-policy guard removed (2);
`gap_id` made caller-suppliable (1); `_enforce_body_policy` **unwired from its call site** (2);
`validate_case_id` **unwired from `_case_path`** (6); Coverage-Gap requirement unwired (2);
seal-mutation guard removed (1); `"now"` dropped from the forbidden clock calls (1); `"read_bytes"`
dropped from forbidden filesystem reads (2); and five end-to-end plants into real runtime files —
`import socket` (3), `datetime.now()` (1), `path.write_text()` (1), an `adapters/production/`
directory (1), an unscanned `.py` file (3).

The two unwiring probes matter most: they prove the guards are *reached*, not merely that they
reject when called directly. Survivors are MAJOR-5.

### Runtime probes beyond static AST

The continuation receipt correctly concedes that "static AST enforcement is not a runtime sandbox".
I closed part of that gap with a real `sys.addaudithook` over the full hermetic path across three
processes:

```text
audit_write_events      : 0
audit_network_events    : 0
audit_subprocess_events : 0
audit file reads        : stdlib/bytecode loading, the 8 fixture files, and manifest.json only —
                          no path outside the package
case_count              : 8   (all eight manifest cases reachable)
outcome_counts          : each of the 8 typed read outcomes exactly once
coverage_gap_count      : 7   (every non-trusted outcome)
readiness               : <ALIGNMENT_PENDING>
```

### Deterministic replay

Three clean processes at `PYTHONHASHSEED=0`, `1`, `99991` over identical frozen input produced
byte-identical results:

```text
run digest        sha256:20e95ae095db7e3d54d9d8dfab2f95deebd6be9c0347bf9cacec67f7bce78b3b
revision log      sha256:fde4b4c469e65cee89e05289b8337470a0515fd64a62d65d55e423480ad288c4
build receipt     rcpt-e4efd395da2cd5ba
serialized bytes  47092
```

These digests differ from the receipt's because the run input differs (`run_id`, `recorded_at`); the
determinism claim is equality across processes and seeds, and it holds.

### Object-level fault injection — all blocked

Sentinel provenance: an application dict `{"__kdd__": "UNKNOWN"}` is rejected at serialization
rather than decoding as absence; an unregistered sentinel name is rejected on decode; sentinel
truthiness raises; duplicate JSON keys, `NaN`, sets, bytes, and non-string keys are all rejected.
Path traversal: `../../etc/passwd`, `..`, `a/b`, `A-UPPER`, a NUL-suffixed id, and
`load_raw("../manifest")` are all rejected by pattern before any path is built. Materiality:
classifying a gap `material` or `non_material` without a versioned `rule_source` raises;
`gap_id` is not an accepted constructor argument. Append-only: append after seal, resetting
`_sealed`, mutating the sealed tuple or mappingproxy, mutating a frozen revision payload, and
overwriting `revision_digest` all raise. All ten seams still raise `AlignmentPendingError`;
`decide_readiness()` raises; `FrozenPacketBinding` rejects a malformed digest, uppercase hex, and an
empty revision label.

### Verdict on review question 11 — has Phase A silently chosen an unfrozen meaning?

**No.** `FoundationRunResult.__post_init__` (`hermetic.py:99-100`) makes any readiness other than
`ALIGNMENT_PENDING` unconstructible; every fixture and manifest entry is forced to
`expected_final_readiness = "alignment_pending"` (`fixture.py:154-159`, `:193-197`);
`adapters/outcomes.py:9-11` explicitly refuses to map outcomes to readiness; `CoverageGap`
materiality defaults to `UNKNOWN` and refuses classification without a versioned rule. The one place
Phase A did take an unratified decision is the nine-value `CoverageGapKind` (MAJOR-4).

### Untested boundaries — stated, not waved away

Static AST scanning is not an OS or interpreter sandbox; my audit-hook probe covers the hermetic
path as executed, not all reachable code. Fixture-directory symlink replacement retains an
environment-dependent TOCTOU residual if an attacker controls the synthetic fixture directory. No
production adapter, live company data, external service, host sandbox, cross-language digest
implementation, UI, or M1/M2 path exists or was tested. The canonical JSON deviates from RFC 8785
on key sort order (code point vs UTF-16 code unit), which is documented at `canonical_json.py:21-24`
and harmless for ASCII keys but is a real cross-language boundary. `manifest.json` is re-read once
per case (`fixture.py:208-211`) — correct, but O(n) reads where one would do.

## Packet sections eligible for freeze

Freezable as written, on this digest: 1 Purpose; 2 Product Outcome; 3 Flight and Decision Metric
Contract; 4 Human Responsibility Contract; 5.2 Required checks; 6 M1; 7 M2; 8 Production
Authority and Old SMA; 9.2 Continuity Checkpoint; 10 Implementation Slices; 11 Acceptance
Scenarios; 11.1 M0 fixture controls; 11.2 Gate map; 12 Stop Conditions; 13 Three-Party Review
and Freeze; 14 Explicit Non-Authorization.

Not eligible until the named blocker closes:

| Section | Blocker |
| --- | --- |
| Header line 7, section 1:19 | BLOCKER-1 — spent authorization presented as live |
| 5.1 Required input | BLOCKER-2 (permission field), BLOCKER-3 (arm parity, readiness-combination policy) |
| 5.3 Readiness outcome contract | BLOCKER-2 — `directional_only` unreachable except via runtime |
| 5.2 check inventory | BLOCKER-3 — no arm-parity check, if arm parity is ruled M0 |
| 9.1 Staffing and active-time budget | BLOCKER-1 — the named cap is exhausted |
| 11 `VAL-UI-101`, 13 change control | MAJOR-2 — first-screen hierarchy referenced but absent |

Answers to the two questions the handoff asked me to challenge directly. **Is
`blocked + directional_only` right for a valid pre-runtime read?** Yes. Separating eligibility from
use is a better design than a third enum value, it prevents a renderer or a Committee outcome from
promoting a directional read, and `eligible + directional_only` is correctly illegal. The
contradiction is not the mapping, it is that the state has only one reachable trigger (BLOCKER-2).
**Is the three-state materiality contract sound?** Yes. Unknown and unclassified defaulting to
material, `non_material` requiring a preregistered versioned rule, `NOT_APPLICABLE` requiring a
versioned applicability rule, and runtime insufficiency staying material while directional are
mutually consistent and propagate identically to `spec:272`, `seq:56`, `CE:198`, and `eval:`
section 8.M0. `core/coverage_gap.py:71-75` already enforces the rule-source requirement
mechanically.

## Four proofs, kept separate

1. **Phase A foundation — proven, with gaps.** 225 cases reproduced independently; 19 of 22
   mutation probes caught; zero write, network, or subprocess events under a runtime audit hook;
   determinism across three hash seeds; every object-level fault injection blocked. Gaps: MAJOR-4,
   MAJOR-5, and the untested boundaries above. This is a foundation, not an M0.
2. **Local fixture-backed M0 MVP — not proven and not started.** All ten `SEAM-M0-*` still raise.
   No readiness outcome, check inventory, materiality policy, contract field set, packet field set,
   acceptance-ID binding, first-screen behavior, fixture baseline, or stop policy is implemented.
   `M0-F1`-`M0-F5` have not begun, and per BLOCKER-1 they need a new Owner authorization, not only
   a digest binding.
3. **Production authorization — absent.** No adapter, credential, tenant, ACL, retention, load
   ceiling, or halt owner exists. P2 is untouched. Nothing in this review moves it.
4. **Experiment Review Committee acceptance — absent and not substitutable.** A green suite is not
   technical completion; technical completion is not review-readiness; review-readiness is not
   Committee Acceptance. Candidate section 11 `VAL-APR-001` and section 11.2 state this correctly,
   and I found no place where the package conflates them.

## Proposed signoff row

To be recorded against the reviewed digest, not the filename:

| Field | Value |
| --- | --- |
| `frozen_artifact` | `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` |
| `reviewed_sha256` | `40c7234f3c0d85f18ebfba656e7aec2ab5ab71b86451a077ecad340eac779396` |
| `revision` | not yet assigned; proposed `m0-alignment-v1` **after** BLOCKER-1/2/3 close, which produces a new digest that supersedes the one reviewed here |
| `party` | Claude Opus 5 (`claude-opus-5`), session `session_01YAshweqBjaqSc7S2SfufFS` |
| `verdict` | `accept_with_changes` |
| `sections_reviewed` | 1-14 in full, plus C1-C9 propagation into `spec`, `seq`, `eval`, `planning-decision-packet`, `profile`, `freeze`, and the CE plan |
| `required_changes` | BLOCKER-1, BLOCKER-2, BLOCKER-3 before freeze; MAJOR-1 through MAJOR-4 and MAJOR-7 in the binding change; MAJOR-5 before `M0-F1` exit; MAJOR-6 before `M0-F1` start |
| `unresolved_gates` | P2, P3, P4, Committee Acceptance; `profile:446-455` decisions 1-3 and 5-9; the four unapplied adjudicated actions B3, M18, M19, M20 |
| `conflicts_of_interpretation` | `spec:469` vs candidate section 5.3 (BLOCKER-2); `spec:271` vs candidate section 5.1 (BLOCKER-3); `owner-alignment-record.md:75` vs `m0-codex-continuation-handoff.md:70-72` (BLOCKER-1); `freeze:61` vs `core/coverage_gap.py:26-37` (MAJOR-4) |
| `timestamp` | 2026-08-18T02:27:48Z |
| `note` | A verdict recorded against a digest other than `reviewed_sha256` does not count. This review does not freeze the packet; only Codex writes the freeze record after the accepted findings are applied. |

## Boundaries observed

No canonical planning document was modified. No `.agents/skills/kdd_data_agent/` source file, test,
or fixture was modified: the package source aggregate is
`2f1001b93b19b2318c4c6419205ed2f7778ac23c02533e78a0c0899f15bf7d1e`, identical to the receipted value,
and `git status` shows the same four modified tracked files as at session start
(`.omc/project-memory.json`, `BACKLOG.md`, `CHANGELOG.md`, `CONTEXT.md`), none of them touched by me.
The one unintended write is the two OMC harness state files disclosed in the artifact-binding section
above; they are harness state, not package content, and I could not remove them because the
environment denied the deletion.

Every mutation ran on an isolated byte-identical copy under the job scratch directory. No commit,
push, PR, dependency install, production access, deployment, external message, or protected-path
change occurred. The packet is not declared frozen. `M0-F1` through `M0-F5` were not implemented. No
Owner decision was inferred from reviewer preference. Unrelated dirty-worktree changes are preserved.
