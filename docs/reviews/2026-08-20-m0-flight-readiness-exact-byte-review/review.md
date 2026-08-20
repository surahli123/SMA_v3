# Independent Exact-Byte Review — M0 Flight Readiness Review Surface

Handoff: `m0-flight-readiness-exact-byte-review-20260820`
Reviewed: `2026-08-20T00:35:27-07:00` → `2026-08-20T00:46:12-07:00` (America/Los_Angeles)
Verdict: **`ACCEPT_EXACT_BYTES`**

## 1. Reviewer independence

I did not author the implementation, its continuation, or any prior review of it.
I did not participate in either the implementing session
(`be43cb18-7161-44ea-9bb0-d8660934113e`) or the audit session
(`eb52e32f-64d7-4858-945d-2cbcf60182e8`). Every prior claim was treated as
untrusted until reproduced from the live bytes.

Where practical I did not run the package's own tooling as my evidence. I wrote
an independent aggregate implementation, an independent DOM assertion suite
against the real unmodified `app.js`, an independent forbidden-API scan, and an
independent WCAG contrast recomputation, and used the package's own tools only
as a cross-check afterwards. I spawned no subagent and no workflow. I made no
commit, push, merge, PR, deployment, publication or production access.

I wrote exactly two files, both new, both outside every reviewed root:
`docs/reviews/2026-08-20-m0-flight-readiness-exact-byte-review/review.md` and
`.../status.json`. `handoff.md` was not modified.

**One capability note that matters to this review.** The audit session recorded
that it could not read the twelve PNG captures and could confirm only that they
decode as genuine distinct pages. I can read images. I opened and read all
twelve directly. That closes the package's third recorded Coverage Gap, which is
the single largest thing a prior session could not attest to.

## 2. Exact reviewed identity

| Field | Value |
| --- | --- |
| Worktree | `/private/tmp/SMA_v3-opus-m0` |
| Branch | `codex/m0-flight-readiness-review` |
| HEAD | `5a04097565cce140dcccd3427234582ef00208da` |
| Output aggregate | `sha256:7a860b034edc15774ad59f2a678d2ca081003482da614f6bd313bba4edd4324d` |
| Output file count | 36 |
| Accepted-M0 aggregate | `sha256:9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a` |
| Accepted-M0 file count | 59 |
| Package state | uncommitted, as required |

Both aggregates were computed twice by my own implementation — once before any
semantic work, once after every check and immediately before this verdict was
written — and were identical both times. No reviewed-root byte changed during
the review. `git status --porcelain` returned a byte-identical dirty set before
and after.

## 3. Fail-closed byte gate

I did not use `tools/output_aggregate.py` to establish the digest. I wrote a
separate implementation of the documented recipe (sha256 over
`<sha256>  <repository-relative-path>\n` lines, ascending by path, over
`prototypes/m0-flight-readiness-review/` and
`docs/reviews/2026-08-18-m0-flight-readiness-review-surface/`, excluding
`__pycache__`, `.pytest_cache`, `.omc`, `.chrome-profile`, `.DS_Store`, and the
two self-referential outputs `evidence-receipt.md` and `status.json`) and
enumerated the manifest myself.

- 36 files, `7a860b03…4324d` — **MATCH**
- 59 files, `9eea3014…b19a` — **MATCH**
- `tools/output_aggregate.py` cross-check afterwards — same digest, same count

The manifest is exactly the 36 deliverable files: 18 under the prototype root
(shell, styles, renderer, two fixture payloads, eight tools, three test files)
plus twelve PNGs, plus six records under the review root. The three gitignored
directories the receipt discloses (`prototypes/.../.omc/`,
`docs/reviews/.../.omc/`, `tools/__pycache__/`) are excluded by the recipe and
by `.gitignore` lines 6 and 12, which I confirmed. Their exclusion is disclosed
rather than silent.

## 4. Frozen input bindings

Recomputed directly with `shasum -a 256`, independently of `tools/bindings.py`.
Five of five matched:

| Role | Result |
| --- | --- |
| M0 build contract `82747da9…7b19` | MATCH |
| Architecture `9508b429…8fc1` | MATCH |
| CE plan `2b4bbd35…1daf` | MATCH |
| Sequencing `8fec2f8c…4725b` | MATCH |
| Accepted M0 package, 59 files `9eea3014…b19a` | MATCH |

`git status --porcelain -- .agents/skills/kdd_data_agent` is empty. The accepted
package was read and never written, before and after my review.

## 5. Checks executed, and what each returned

Every recorded battery command was re-executed by me against the live bytes, and
extended where the recorded coverage was the minimum rather than the maximum.
**37 checks run, 36 passed, 1 failed as written, 0 skipped.** No check was
skipped for any reason, explained or otherwise.

The single failure is one of **my own** assertions, not an artifact check. Every
check belonging to the package — bindings, fixtures, determinism, both syntax
checks, the behaviour suite, the overflow measurements and all three mechanical
suite runs — passed. My assertion G, which demanded that no `<form>`, `<input>`,
`<textarea>` or `<select>` appear anywhere, failed because the Checks route
renders three view-filter controls. That failure is the finding recorded as NB-1
in §7. Investigating it did not reveal a read-only violation, and the verdict
does not turn on it, but it failed and it is counted as failed here rather than
folded into a clean number.

### Reproduction and determinism

| Check | Outcome |
| --- | --- |
| `bindings.py` from repo root | exit 0, five of five bindings match |
| `git status --porcelain -- .agents/skills/kdd_data_agent` | exit 0, empty |
| `build_fixtures.py --check` from repo root, prototype root, `/private/tmp`, `$HOME` | exit 0 ×4, identical model digest |
| `PYTHONHASHSEED` ∈ {0, 1, 42, 99991, random, 7, 12345, 987654321} | exit 0 ×8, identical model digest |
| Independent rebuild into a fresh temp dir, byte-compared to the committed payloads | `fixtures.json` and `fixtures.js` **byte-identical** |

The handoff required at least three `PYTHONHASHSEED` values; the record claimed
five; I ran eight, adding three the package never tried. All eight reproduce
`0c1ec29129a534b9b72948560437fe6487e375994e2b2630b7da89f97b8884c7` over a
580,239-byte model. The unrelated-cwd requirement was tested from two distinct
outside directories, not one. The rebuilt `fixtures.js` hash
`1fdb9851…ea4a` equals its manifest entry exactly, so the generator, the
committed bytes and the aggregate all agree.

### Provenance — the claim I most expected to fail

The durable record asserts that all seven scenarios are packets emitted by
`kdd_data_agent.m0.evaluator.evaluate_flight`, not hand-authored. A static read
is not proof of that: `emitted_by` is a hardcoded string in
`tools/build_fixtures.py`, and `m0/evaluator.py` is a 21-line re-export shim with
no function definitions of its own, so a shallow grep makes the claim look false.

I tested it at runtime instead. I wrapped the real `evaluate_flight` in
`m0/corrected_evaluator.py` with a spy and rebuilt the model:

- **7 invocations** of the genuine function during the build
- every return value a real `FlightReadinessPacket`
- 7 of 7 scenarios carry `evidence_class = fixture`, and `fixture` is the only
  value that appears anywhere in the model

`build_fixtures.py` imports `canonical_json`, `identity`, `unknown`, `checks`,
`contracts`, `evaluator`, `packet` and `tests/_m0_fixtures` from the accepted
package. The provenance claim is true, and it is true for the reason claimed.

### Behaviour, independently asserted

I wrote my own suite against the package's `tests/dom.js` shim, executing the
real unmodified `app.js` — not the package's `test_surface.js`. **21 of my 22
assertions passed; assertion G failed as written.**

| Assertion | Result |
| --- | --- |
| Both receipts are top-level `<details>` + `<summary>` on the readiness route, no nesting, for all 7 scenarios | pass ×7 |
| `eligible` renders **iff** stored `analysis_use` is `decision_grade`, all 7 scenarios | pass ×7 |
| No `null`, `undefined`, bare dash, em dash, `NaN` or `[object Object]` text node in any of 35 route-views | pass |
| Fail-closed: absent model, foreign `schema_version`, empty scenario list, scenario missing its packet digest — each refuses, names what it saw, and mounts no route and no tab | pass ×4 |
| Read-only: model serialization byte-identical after 35 navigations | pass |
| No affirmative authority claim (cause, recommendation, win/loss, production, deploy, Committee, P3) across 35 route-views | pass |
| G: no `<form>`, `<input>`, `<textarea>`, `<select>` or write-verb button across 35 route-views | **FAILED as written** — three view-filter controls found; see NB-1 |

Assertion G is the one that failed. It found
`<select id="filter-outcome">`, `<select id="filter-materiality">` and
`<input type="checkbox" id="filter-core">` on the Checks route. I wrote the
assertion at maximum strictness deliberately, to see whether the receipt's claim
that "there is no form and no data-entry control" was literally true. It is not.
What the failure does **not** show is a read-only violation: there is no `<form>`,
no text entry and no submit; all three are label-associated view filters carrying
an on-screen disclosure; and the separate read-only assertion proves the model is
byte-identical after 35 navigations. So the artifact's behaviour is sound and the
receipt's sentence is wrong, which is exactly what NB-1 records.

The package's own suites were then run as a cross-check: `test_surface.js`
22/22, `check_overflow.sh` 120/120, `verify.py` 46/46 from the repo root and
46/46 from each of two unrelated working directories, `node --check` clean on
both scripts.

**A correction on my own method.** My first run of this suite reported 18
failures. That was a defect in my harness — I queried `children`/`tag`/`value`
instead of the shim's `childNodes`/`tagName`/`textContent`, so my text
extraction returned empty strings and several assertions passed or failed
vacuously. I found it because the passing assertions printed empty values. The
corrected run is the one reported above. No artifact defect was involved, and I
record it so this review's numbers are not read as a reproduction of a failure.

### Receipt reach within two interactions

From a cold load with no hash at all, the surface lands on **Readiness** with
`aria-selected="true"`, and both receipts are already present on that first
screen as closed native `<details>`: `Source read — exact retained receipt` and
`Independent recomputation — D4/D6 receipt`. Neither is nested inside another
`<details>`. Opening either is one native `<summary>` activation — Tab to reach,
Enter or Space to open, no scripting involved.

**0 navigations + 1 activation = 1 interaction, against a budget of 2.** Asserted
for all seven scenarios and confirmed visually in every readiness capture.

Supporting keyboard and landmark structure verified in source: `role="tablist"`
on `#route-tabs` in `index.html`, `aria-selected`, roving `tabindex`
(`0,-1,-1,-1,-1`), explicit `ArrowRight`/`ArrowLeft`/`Home`/`End` handling in
`app.js`, a skip link to the packet decision, `header`/`main`/`nav`/`aside`
landmarks, `<noscript>` fallback, `lang="en"`, `:focus-visible`, and a
`prefers-reduced-motion` block.

### Offline, read-only and injection safety

An independent scan over comment-stripped `app.js` for 23 forbidden APIs —
`fetch`, `XMLHttpRequest`, `WebSocket`, `EventSource`, `sendBeacon`,
`localStorage`, `sessionStorage`, `document.cookie`, `indexedDB`, `eval`,
`new Function`, `innerHTML`, `outerHTML`, `document.write`, `pushState`,
`replaceState`, `location.assign`, `location.replace`, `import()`, `require()`,
`serviceWorker`, `postMessage`, `Worker` — returned **zero hits**. Comment
stripping matters here: `app.js` names several of these in prose to say it
refuses them.

`index.html` loads exactly two local scripts and references no remote origin.
`styles.css` has no `@import` and no remote `url()`. `data/fixtures.js` is a
single inert assignment with no `function` and no arrow. The only `apply`
occurrences in `app.js` are `applyHash()`, read-only hash routing. Nodes are
built with `createElement` and `textContent` only, so a model value cannot become
markup. There is no persistence of any kind, so nothing here is an
automation-consumable apply surface.

### Visual evidence — read directly, not merely decoded

All twelve PNGs: valid `IEND`, expected 2× geometry (2880×2360 desktop,
840×3000 narrow), twelve distinct sha256s. The narrow width is 420 CSS px because
`capture.sh` adds 30px of window allowance around a fixed 390px iframe in
`narrow-frame.html`; the surface itself is at a true 390px, as documented in the
script.

I then opened and read every one. All twelve are real, dense, correctly rendered
pages, not blank or near-blank frames:

| Capture | What I actually saw |
| --- | --- |
| `trusted-desktop` | `decision_grade` with "stored on the packet", derived `eligible` separately labelled "never stored on the packet" with its rule, the why-limited sentence, typed next safe action with guidance/reopen/blockers, both receipts, ordered check table, full packet identity and expiry |
| `blocked-desktop` | `not_permitted`/`blocked`, authorization `unauthorized`, staleness `stale`, completeness `incomplete` 18 unresolved, "no source body is retained under this authorization and redaction state", CHK-16 FAIL ordered first |
| `invalidated-desktop` | Gaps & state: staleness, supersession digest, acknowledgement `acknowledged → invalidated`, one recorded disagreement with both receipt ids, 20 typed Coverage Gaps with materiality, rule source, reason and next safe check |
| `incomplete-desktop` | CHK-09 MISSING, CHK-17 MISSING, CHK-14 UNKNOWN ordered ahead of every PASS; blockers CHK-09, CHK-14, CHK-17 |
| `receipts-desktop` | Receipt index as a list, explicitly "There is no node diagram: each relationship below is a row, and each row names its inputs" — the graph-prohibition contract satisfied |
| `boundaries-desktop` | All eight boundaries rendered and numbered, Trace stated as not present in M0, provenance table with all five exact bindings and digests |
| six narrow captures | Correct single-column reflow at 390px, no horizontal document scroll, all first-screen fields preserved |

Ordering, labelling and typed-absence behaviour visible in the captures match
what my DOM assertions proved. Typed absence renders as `MISSING`,
`none recorded`, `not_recorded` or `UNKNOWN` — never blank, never a bare dash.

### Accessibility, recomputed rather than quoted

I recomputed WCAG contrast myself from the CSS custom properties, modelling each
pair as it is actually used (`.outcome.FAIL` puts `--accent` on `--accent-wash`;
`.outcome.MISSING/.UNKNOWN` puts `--warn` on `--warn-wash`). Fourteen real
text/background pairs:

- lowest **4.76:1** — `--accent` `#c3410f` on `--accent-wash` `#fff4ee`
- highest **15.83:1** — `--ink` `#1f2326` on `--panel` `#ffffff`
- all fourteen ≥ 4.5:1

That reproduces the receipt's stated bounds exactly. The receipt says twelve
pairs; I measured fourteen and got the same floor and ceiling.

### Fake-completion scan

Per my own completion discipline I scanned all owned source for `TODO`, `FIXME`,
`XXX`, `HACK`, `test.skip`, `it.skip`, `describe.skip`, `.only(`,
`NotImplementedError`, "placeholder", "not implemented". **No matches.** No
stubbed test, no disabled assertion, no unimplemented branch. `build-test.json`
records `skipped: 0` and the log contains no skip marker.

## 6. Blocking findings

**None.**

No finding falsifies the recorded verdict, and none required rejecting the exact
bytes. Every mechanical claim in the receipt, the ledger and the status that I
tested reproduced against the live bytes, and the two claims the earlier
revisions got wrong were already withdrawn and corrected in the record rather
than reproduced.

## 7. Non-blocking findings

**NB-1 — `evidence-receipt.md` §6 understates the control inventory.**
*Surfaced by the one assertion of mine that failed (G, §5).* The receipt states:
"there is no form and no data-entry control." The Checks route renders three
native form controls: `<select id="filter-outcome">`,
`<select id="filter-materiality">` and `<input type="checkbox" id="filter-core">`,
each correctly associated by `<label for>`.

The substance of read-only is intact and I verified it independently: there is no
`<form>` element, no text entry, no submit, all three are view filters, they
carry the on-screen disclosure "View filter only — no packet, check, evidence or
source state changes", and the model is byte-identical after 35 navigations. The
sentence understates the surface in the safe direction, and it contradicts the
same document's own filter paragraph a few lines later; `README.md` states it
correctly ("The view filters state so on screen"). This is a wording defect in a
durable record, not a capability overstatement. Suggested correction: "no form
element and no data-entry control; the three view filters change only what is
displayed."

**NB-2 — `evidence-receipt.md` §6 offers an unobserved cause for the
`receipts-narrow` ink density.** The receipt attributes that capture's 28% row
ink, against roughly 40% elsewhere, to "the receipts route being shorter at
390px." Reading the capture shows a different cause: the receipt index is a
five-column table that scrolls horizontally inside its own container, so at 390px
only three columns are visible and every row carries a wide empty right region.
The audit session correctly logged this as an observation rather than a defect
and correctly declined to call it a failure, but it supplied an explanation it had
no capability to see. The behaviour itself is correct and is what the passing
overflow measurements describe: wide content scrolls inside its own container
while the document does not.

**NB-3 — Coverage Gap 5 understates its own consequence.** The gap reads: "Below
roughly 620px the fifth route tab is off-screen with no visible hint; keyboard
arrow navigation still reaches it." Reading `boundaries-narrow.png` shows a
stronger effect: when the fifth route is the *active* one, the tablist shows no
selected tab at all, because the active indicator is itself off-screen. At 390px
the narrow view therefore gives no visible indication of which route is being
displayed. The existence and the keyboard mitigation are disclosed; the severity
is not. Non-blocking because it is a disclosed layout gap on a local prototype
and keyboard reach is unaffected.

**NB-4 — Minor count discrepancy in the contrast claim.** The receipt says twelve
foreground/background pairs were measured; modelling the palette as used yields
fourteen. Both bounds the receipt states, 4.76:1 and 15.83:1, reproduce exactly.
Trivial, recorded for completeness.

## 8. Accepted disclosed gaps

Accepted per the handoff, which permits disclosed external gaps unless the
artifact falsely claims they passed or the gap invalidates the local
fixture-only result. None of these does either — each is stated plainly in §7
and §8 of the receipt and in `coverage_gaps` in the status.

1. **Expiry overrun.** Part of the implementation was produced after the original
   cap expired and before the replacement cap was issued. Disclosed as custody
   history rather than smoothed over. Work completed at `2026-08-20T00:05-07:00`,
   inside the replacement cap of `2026-08-20T06:59:21-07:00`.
2. **Concurrent-writer window.** Two sessions overlapped between 23:15 and 23:24
   on 2026-08-19 and the implementing session published a terminal status inside
   that window. The audit session halted rather than racing it, byte stability was
   re-established by two identical full-tree hashes, and every mechanical claim was
   re-executed afterwards. I re-executed them again from the live bytes; all hold.
3. **Split attestation on the captures — now closed.** This was the package's
   weakest attestation: the audit session had no image-viewing capability. I read
   all twelve captures directly and confirm real rendered content and the required
   desktop and narrow states. This gap no longer stands against the exact bytes.
4. **Consequential-row repetition.** A packet whose read was not admitted presents
   eighteen rows restating one cause. Visible in `blocked-desktop`; correctly
   ordered and explained. Disclosed, and reflected in the clarity score of 4.
5. **Tablist scroll affordance below ~620px.** See NB-3.
6. **Coverage Gap identifiers are not cross-linked** to the receipt index.
7. **No screen-reader and no cross-browser verification.** Assistive technology is
   unavailable and only Chrome is installed. The record does not claim either
   passed; it lists both as excluded with reasons. Structure and ARIA were verified
   in source; announced output was not.
8. **No live reviewer has used the surface.** `VAL-UI-101` and P3 live interaction
   acceptance remain open external gates, stated on the Boundaries route itself.

## 9. Do the durable claims overstate the evidence?

No. This is the check most likely to fail on work of this kind, and it holds.

The strongest permitted result is a local, fixture-only, read-only, pre-P3
prototype, and that is exactly what every durable surface claims.
`COMPLETE_LOCAL_PROTOTYPE` is defined in the receipt's own opening as "a local
fixture-only review artifact… ready for a separate independent exact-byte
review. It is not production capability, not authorization, not P3 closure, and
not Committee Acceptance."

I searched for the opposite claim rather than trusting the disclaimer. Across all
35 route-views, no affirmative authority phrase appears — no cause, no
recommendation, no win/loss, no production readiness, no deploy or ship advice,
no P3 closure, no Committee acceptance. The Boundaries route renders all eight
negations explicitly. Every readiness view carries the sentence "A validity-based
block advises against using this Flight as decision evidence. It does not block,
approve, roll back, or otherwise gate a product launch," which refuses the
authority rather than merely omitting it. The rail badge reads
`evidence_class = fixture` and the footer reads "Fixture-only projection · pre-P3"
on every screen I inspected. No real Flight is described and no result about any
real Flight is implied.

The two claims that were overstated in earlier revisions — a battery duration
belonging to a superseded run, and an assertion that files outside the owned
roots had been changed by another worker — are both explicitly withdrawn and
corrected in `completion-ledger.md`, with the superseded ledger's digest
recorded. I verified the withdrawal is the correct one: `git status --porcelain`
shows no dirty path outside the two owned roots.

## 10. Proof boundary

This review establishes that the exact 36 uncommitted files aggregating to
`sha256:7a860b03…4324d`, on branch `codex/m0-flight-readiness-review` at HEAD
`5a04097`, are a local, fixture-only, read-only, pre-P3 review prototype whose
mechanical claims reproduce, whose bindings match, whose fixtures are
deterministic and genuinely emitted by the accepted M0 package, whose visual
evidence is real, and whose durable record does not overstate itself.

It establishes nothing further. It is not production M0 capability, not
production authorization, not source authenticity, not P2/P3/P4 closure, not M1
or M2 completion, not deployment, not publication, and not Experiment Review
Committee Acceptance. It does not readjudicate Phase A. It does not alter the
accepted local M0 evidence package or its `ACCEPT_LOCAL_M0_EVIDENCE` verdict,
which I confirmed unmodified before and after. `VAL-UI-101` and P3 live
interaction acceptance remain open. No screen-reader, cross-browser or
live-reviewer evidence exists, and this review asserts none.

The review covers the bytes as they stand. Any byte change to any reviewed root
invalidates it and requires a fresh gate.

## 11. Disposition

The exact reviewed bytes are accepted.

**Commit B may contain the exact reviewed implementation and evidence bytes** —
the 36 files under `prototypes/m0-flight-readiness-review/` and
`docs/reviews/2026-08-18-m0-flight-readiness-review-surface/` aggregating to
`sha256:7a860b034edc15774ad59f2a678d2ca081003482da614f6bd313bba4edd4324d`, plus
the two self-referential records `evidence-receipt.md` and `status.json` that the
recipe excludes by construction. The three gitignored state directories cannot
enter a commit and must not be added.

**Commit C may contain this independent review record** — `review.md` and
`status.json` under
`docs/reviews/2026-08-20-m0-flight-readiness-exact-byte-review/`, alongside the
orchestrator-owned `handoff.md`.

I created neither commit. Committing, pushing and publishing a first transferable
version remain the Owner's call. The four non-blocking findings are corrections
to English records, not to code; none of them blocks either commit, and applying
them would change bytes and therefore require a fresh gate.

---

**`ACCEPT_EXACT_BYTES`**
