# M0 Flight Readiness Review Surface — Evidence Receipt

Completed: `2026-08-20T00:05-07:00` (America/Los_Angeles)
Handoff: `opus5-m0-review-surface-20260818`, continued under
`opus5-m0-review-surface-continuation-20260819`
Branch: `codex/m0-flight-readiness-review`
Base commit: `5a04097565cce140dcccd3427234582ef00208da`
Verdict: **`COMPLETE_LOCAL_PROTOTYPE`**

`COMPLETE_LOCAL_PROTOTYPE` means one thing: a local fixture-only review artifact
exists, is mechanically verified, and is ready for a separate independent
exact-byte review. It is not production capability, not authorization, not P3
closure, and not Committee Acceptance.

## 1. Run authority and the expiry overrun

This run must be read with its custody history, not as a single clean pass.

The original handoff expired at `2026-08-19T02:33:32-07:00`. Work continued past
that point in wall-clock terms, the overrun was detected at
`2026-08-19T22:33:56-07:00`, and the run halted at that moment, reported the
overrun, and wrote a `PARTIAL_WITH_GAPS` ledger, README and status rather than
continue without authority. The Owner then authorized continuation through the
main orchestrator in `opus5-m0-review-surface-continuation-20260819`, which
replaced the expired cap with `2026-08-20T06:59:21-07:00` and set additional
requirements. Work resumed under that authority and completed inside it.

An independent reviewer should treat the following as a recorded Coverage Gap
rather than as a clean single-cap execution: **part of the implementation was
produced after the original cap expired and before the replacement cap was
issued.** Every artifact was re-verified after the replacement authority
arrived, and no completion claim from the partial state was carried forward
untested, but the sequencing is a fact of custody and is stated here rather than
smoothed over.

The superseded partial ledger's digest is recorded in `completion-ledger.md` so
the earlier state is auditable.

### Two sessions, and a concurrent-writer window

A second custody fact belongs here. Two sessions touched this package.
`be43cb18-7161-44ea-9bb0-d8660934113e` implemented it. A separate audit session,
`eb52e32f-64d7-4858-945d-2cbcf60182e8`, re-verified it and wrote the final
corrections, this receipt and the status. They overlapped: between `23:15` and
`23:24` on `2026-08-19` the implementing session was still writing into both
owned roots while the audit session was reading them, and it wrote a terminal
`COMPLETE_LOCAL_PROTOTYPE` status inside that window. An exact-byte package
cannot be produced while a second writer is mutating it, so the audit session
halted rather than racing it. The Owner then confirmed the implementing session
had been stopped and no writers remained. Byte stability was re-established by
two identical full-tree hashes of all 39 non-transient owned files, taken at
`23:34:28` and `23:39:19`, before any correction was written.

Every mechanical claim in this receipt was then re-executed by the audit session
against the live bytes. The single claim it cannot personally attest to is the
direct visual reading of the captures: that session has no image-viewing
capability. It confirmed instead, by decoding each PNG, that all twelve are
genuine, complete, byte-distinct rendered pages. §6 states both halves
separately, and `completion-ledger.md` carries the full attribution table.

## 2. Exact input bindings

Recomputed before semantic work and again after every write. Both times, five of
five matched.

| Role | Path | Revision | SHA-256 | Result |
| --- | --- | --- | --- | --- |
| M0 build contract | `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `m0-alignment-v1` | `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` | MATCH |
| Architecture | `docs/research/kdd-data-agent-workshop/final-architecture-spec.md` | `kdd-data-agent-architecture-v1` | `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` | MATCH |
| CE plan | `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | observed supporting plan | `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` | MATCH |
| Sequencing | `docs/research/kdd-data-agent-workshop/implementation-sequencing.md` | observed supporting sequence | `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` | MATCH |
| Accepted M0 package | `.agents/skills/kdd_data_agent/`, 59 files | `ACCEPT_LOCAL_M0_EVIDENCE` | `9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a` | MATCH |

The accepted package aggregate recipe was not documented in a single place in
the repository, so it was recovered by reproducing the published digest: sha256
over the concatenation of `<sha256>  <repository-relative-path>\n` lines,
ascending by path, for every `.py`, `.json` and `.md` file below
`.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache` and
`.omc`. `tools/bindings.py` implements it and halts on drift.

`git status --porcelain -- .agents/skills/kdd_data_agent` is empty. The accepted
package was read, never written.

## 3. Exact-byte output binding

| Field | Value |
| --- | --- |
| Aggregate | `7a860b034edc15774ad59f2a678d2ca081003482da614f6bd313bba4edd4324d` |
| File count | 36 |
| Tool | `prototypes/m0-flight-readiness-review/tools/output_aggregate.py` |
| Cross-check | reproduced independently by shell pipeline, same digest |

Algorithm: sha256 over the concatenation of
`<sha256>  <repository-relative-path>\n` lines, ascending by path, for every
file under `prototypes/m0-flight-readiness-review/` and
`docs/reviews/2026-08-18-m0-flight-readiness-review-surface/`, excluding
`__pycache__`, `.pytest_cache`, `.omc`, `.chrome-profile` and `.DS_Store`, and
excluding the two self-referential outputs that record the digest itself:
`evidence-receipt.md` and `status.json`. This is deliberately the same recipe as
the accepted package aggregate. Run
`python3 tools/output_aggregate.py --manifest` for the per-file listing.

## 4. Changed files

Every path below is new in this run. Nothing outside the two owned roots was
written, and nothing was committed.

`prototypes/m0-flight-readiness-review/`
: `README.md`, `index.html`, `styles.css`, `app.js`,
  `data/fixtures.json`, `data/fixtures.js`,
  `tools/bindings.py`, `tools/build_fixtures.py`, `tools/verify.py`,
  `tools/capture.sh`, `tools/check_overflow.sh`, `tools/narrow-frame.html`,
  `tools/run_build_test.py`, `tools/output_aggregate.py`,
  `tests/dom.js`, `tests/test_surface.js`, `tests/overflow.html`,
  and twelve PNGs under `evidence/`.

`docs/reviews/2026-08-18-m0-flight-readiness-review-surface/`
: `completion-ledger.md` (second revision), `evidence-receipt.md`,
  `visual-critique.md`, `design-critique.md`, `critique.json`,
  `build-test.json`, `build-test.log`, `status.json`.

`opus5-continuation-handoff.md` in that directory was written by the Owner-side
orchestrator, not by this run, and was left untouched.

An earlier revision of this receipt claimed that the repository `README.md` and
a `docs/archive/` addition had been changed outside the owned roots by another
concurrently active worker. **That claim is withdrawn.** At audit time
`git status --porcelain` reports no dirty path outside the two owned roots;
those files belong to base commit `5a04097` and were never touched by this work.

The only tracked file this run modified is
`docs/reviews/2026-08-18-m0-flight-readiness-review-surface/status.json`, which
is inside an owned root. Everything else listed above is untracked and new.

Three gitignored directories exist inside the owned roots and are **not**
deliverable bytes: `prototypes/m0-flight-readiness-review/.omc/`,
`docs/reviews/2026-08-18-m0-flight-readiness-review-surface/.omc/` and
`prototypes/m0-flight-readiness-review/tools/__pycache__/`. They are agent-hook
state and Python bytecode, matched by `.gitignore` lines 12 and 6, so they
cannot enter a commit, and the aggregate recipe in §3 excludes them by name, so
they cannot enter the digest. They are recorded here rather than deleted.

## 5. Commands executed

Recorded mechanically in `build-test.json` and `build-test.log`. Those records
are the audit session's re-execution of the whole battery against the final
bytes, not the implementing session's earlier run. Summary: 16 commands,
**16 passed, 0 failed, 0 skipped**, 14,707 ms total.

| Command | Exit | Result |
| --- | --- | --- |
| `python3 tools/bindings.py` (repo root) | 0 | five of five bindings match |
| `git status --porcelain -- .agents/skills/kdd_data_agent` | 0 | empty; accepted package unmodified |
| `python3 tools/build_fixtures.py --check` (repo root) | 0 | model sha256 `0c1ec291…84c7` |
| `python3 tools/build_fixtures.py --check` (prototype root) | 0 | identical digest |
| `python3 tools/build_fixtures.py --check` (unrelated cwd) | 0 | identical digest |
| the same, with `PYTHONHASHSEED` `0`, `1`, `42`, `99991`, `random` | 0 each | identical digest all five |
| `node --check app.js` | 0 | parses |
| `node --check data/fixtures.js` | 0 | parses |
| `node tests/test_surface.js` | 0 | 22 passed, 0 failed |
| `sh tools/check_overflow.sh` | 0 | 120 passed, 0 failed |
| `python3 tools/verify.py` (repo root) | 0 | 46 passed, 0 failed |
| `python3 tools/verify.py` (unrelated cwd) | 0 | 46 passed, 0 failed |

Additionally, `sh tools/capture.sh` produced the twelve evidence PNGs, and
`python3 tools/run_build_test.py` produced the build-test records above.

## 6. What was verified

**Determinism.** Five `PYTHONHASHSEED` values, including `random`, all reproduce
the same 580,239-byte model with sha256 `0c1ec29129a534b9b72948560437fe6487e375994e2b2630b7da89f97b8884c7`.
The generator reads no clock and no randomness.

**Provenance of every scenario.** All seven scenarios are packets emitted by
`kdd_data_agent.m0.evaluator.evaluate_flight` against the accepted package's own
fixtures. No readiness field is hand-authored. `evidence_class` is `fixture` on
every one, enforced by the packet type itself.

**First-screen contract.** For all seven scenarios, the readiness route carries
the stored `analysis_use` with its origin, the derived
`post_analysis_eligibility` with its derivation rule and a statement that it is
never stored, one sentence naming the check that limits the Flight, and the
typed next safe action with guidance, reopen condition and blockers.

**Receipt reach.** Both the exact source-read receipt and the D4/D6
independent-recomputation receipt are on the first screen as `<details>`
elements. Opening either is one activation, reachable by Tab and triggered by
Enter or Space with no scripting involved — inside the two-interaction budget
with one to spare. Asserted for all seven scenarios.

**Prohibited authority.** Two independent tests. One scans every authored
paragraph across five routes and seven scenarios and requires any sentence
raising cause, recommendation, candidate diff, win/loss, production capability,
Committee, P3, acceptance, launch, deploy or rollback to be a negation. The
other bans affirmative claim phrases outright. Eight explicit boundaries are
rendered on the Boundaries route.

**Fail-closed behaviour.** An absent model, a foreign `schema_version`, an empty
scenario list and a scenario missing its packet digest each render a refusal
naming what was seen, and mount no route at all. A typed absence renders as its
token (`UNKNOWN` or `MISSING`); no authored field can render blank, `null`,
`undefined` or a bare dash. No scenario other than `decision_grade` can display
`eligible`. An unauthorized or redaction-blocked read states that no body is
retained instead of showing an empty panel.

**Read-only guarantees.** No control offers a write, apply, approve, acknowledge
or re-evaluate action; there is no form and no data-entry control. Scenario and
route selection and the view filters leave the model byte-identical, asserted by
comparing serialized state before and after. The filter states on screen that it
changes no packet, check, evidence or source state.

**Offline and injection safety.** `app.js` contains no `fetch`,
`XMLHttpRequest`, `WebSocket`, `EventSource`, `sendBeacon`, `localStorage`,
`sessionStorage`, `document.cookie`, `indexedDB`, `eval`, `new Function`,
`innerHTML`, `outerHTML`, `document.write`, `history.pushState`,
`history.replaceState`, `location.assign`, `location.replace`, `import()` or
`require()` — checked over code with comments stripped, since the file names
several of these in prose to say it refuses them. `index.html` loads exactly two
local scripts and references no remote origin. `styles.css` has no `@import` and
no remote `url()`. `data/fixtures.js` parses as inert JSON.

**Accessibility.** Twelve foreground/background pairs measured against WCAG AA:
lowest is 4.76:1, highest 15.83:1, all above the 4.5:1 floor for small text.
Visible `:focus-visible` outline; skip link to the packet decision; `header`,
`main`, `nav` and `aside` landmarks; `noscript` fallback pointing at the same
payload; a `role="tablist"` with `aria-selected`, roving `tabindex` and
Arrow/Home/End handling, asserted by test; `prefers-reduced-motion` honoured,
though the stylesheet contains no animation to reduce.

**Layout.** 120 measurements — four scenarios, five routes, six widths from
390px to 1440px — confirm the document never scrolls horizontally. Wide content
scrolls inside its own container.

**Visual evidence.** Twelve PNGs: trusted, blocked, invalidated/superseded and
incomplete at both desktop and 390px, plus receipts and boundaries at both.

The implementing session opened and read each one, not merely checked it for
existence; twelve defects were found that way and fixed, logged as D1–D8 in
`visual-critique.md` and D9–D12 in `design-critique.md`.

The audit session cannot restate that reading — it has no image-viewing
capability — so it verified the captures a different way, by decoding every PNG
and measuring it. All twelve carry a valid `IEND` terminator, decode cleanly at
the expected 2× device-scale geometry (2880×2360 desktop, 840×3000 narrow), and
are byte-distinct from one another. Ink coverage ranges from 3.4% to 4.9% and
distinct-colour counts from 1,054 to 1,799, so each is a densely rendered page
rather than a blank or near-blank frame. The `receipts-narrow` capture carries
ink on 28% of its rows against roughly 40% for the other narrow captures, which
is consistent with the receipts route being shorter at 390px; no required test
covers row-ink density, and it is recorded as an observation, not a defect.

**Critique.** `critique.json` scores clarity 4, hierarchy 4, typography 5,
motion 5, brand 4, overall 4, converged at the `score >= 4` rule after two
passes.

## 7. Checks excluded, and why

| Excluded | Reason |
| --- | --- |
| Any production read | Prohibited by the handoff. Zero production reads occurred. |
| Any network request | Prohibited. Chrome ran headless against `file://` URLs with networking flags disabled and a throwaway profile. |
| Dependency installation | Prohibited. Only Python 3.14 stdlib, Node's stdlib and the locally installed Chrome were used. |
| Automated axe or Lighthouse audit | Both require an installed dependency. Contrast, focus, landmarks, tablist semantics and reduced motion were checked directly instead. |
| Screen-reader testing | Requires assistive technology not available in this environment. Structure and ARIA were verified; announced output was not. |
| Cross-browser rendering | Only Chrome is installed locally. The surface uses no vendor-specific feature beyond a `-webkit` marker reset. |
| Live reviewer acceptance | This is the P3 gate. It remains open by design and this run does not touch it. |
| Any commit, push, PR or merge | Prohibited. The package is left uncommitted so an independent reviewer can inspect the exact live bytes. |

## 8. Coverage Gaps

1. **Expiry overrun.** Part of the implementation was produced after the
   original cap expired and before the replacement cap was issued. See §1.
2. **Concurrent-writer window.** Two sessions wrote or read this package with an
   overlap, and the implementing session published a terminal status inside that
   overlap. Byte stability was re-established and every mechanical claim
   re-executed before this receipt was written, but the package was not produced
   by a single serialized run. See §1.
3. **Split attestation on the captures.** The reading of the twelve captures is
   the implementing session's evidence; the audit session could confirm only
   that each is a genuine, complete, distinct rendered page. See §6.
4. **Consequential-row repetition.** A packet whose read was not admitted
   presents eighteen rows restating one cause. Ordered correctly and explained,
   but still a wall of near-identical content.
5. **Tablist scroll affordance.** Below roughly 620px the fifth route tab is
   off-screen with no visible hint; keyboard arrow navigation still reaches it.
6. **Coverage Gap identifiers are not cross-linked** to the receipt index.
   Every relationship is a table row, but matching is manual.
7. **No screen-reader or cross-browser verification**, per §7.
8. **No live reviewer has used the surface.** P3 remains open.

## 9. Proof boundary

This receipt validates a local, fixture-only, read-only, pre-P3 review artifact
and the mechanical checks listed above. It does not establish production M0
capability, production authorization, source authenticity, P2/P3/P4 closure, M1
or M2 completion, deployment, publication, or Experiment Review Committee
Acceptance. It does not readjudicate Phase A and does not alter the accepted
local M0 evidence package or its `ACCEPT_LOCAL_M0_EVIDENCE` verdict. No real
Flight is described, and no result about any real Flight is implied.
