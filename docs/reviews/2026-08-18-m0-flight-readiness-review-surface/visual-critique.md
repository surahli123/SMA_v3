# Visual and Observability Critique

Subject: `prototypes/m0-flight-readiness-review/`
Baseline: `owner-selected-design-contract.md`, `award-ui-narrative-contract.md`, and the
four owner-selected screenshots under
`docs/research/kdd-data-agent-workshop/prototypes/observability-review-surface/reference-assets/owner-selected-iteration/`
Method: build, render headless at 1440px and a true 390px viewport, read the
captures, name the defects, fix, re-render, re-read.

## 1. Conformance to the owner-selected contract

| Contract clause | How the surface meets it | Verdict |
| --- | --- | --- |
| A compact dark identity block anchors an otherwise light forensic workspace | 56px dark `M0` mark against `--paper #fbfaf7`; no other dark field on the page | met |
| Stable case rail, top route navigation, central task workspace, persistent right inspector | Scenario rail (232px), five-route tablist, workspace, packet-identity inspector | met |
| Thin rules and aligned rows carry hierarchy; elevation reserved for a selected record or permission boundary | Every separator is a 1px `--line`; no `box-shadow` anywhere; selection is a 3px left rule plus a wash | met |
| Orange identifies selection, contradiction, and blocked state; green is reserved for validated records; neither is decorative | Orange appears only on the selected rail row, the active tab underline, `not_permitted`/`blocked`, an unauthorized or stale state, and a `FAIL` outcome. Green appears only on `decision_grade`/`eligible` and `PASS` | met, after fix 4 below |
| Technical sans for navigation and explanation; monospace for identifiers, timestamps, locators, receipts, code, raw output | Every digest, receipt id, rule source, gap id, interval and enum is monospace; every sentence is sans | met |
| Tables, code, graph paths and provenance are primary; narrative explains authority but never replaces proof | Prose appears only in the decision explanation, the authority note, and the boundary statements. Everything else is a table, a definition list, or a verbatim receipt dump | met |
| No marketing AIDA, hero composition, CTA, stock imagery, scroll choreography or perpetual motion | None present; the page has no animation at all and honours `prefers-reduced-motion` regardless | met |

Interaction grammar carried over from the narrative contract: the reviewer's
question leads, the answer path stays visible, source detail opens beside it,
and the exact proof is within two interactions. The M1-specific parts of that
contract — competing claims, typed graph, deployed-code diff — are deliberately
absent, because M0 has no cause, no candidate and no Trace store to project.

## 2. Defects found in the first render, and what was done

Each was found by reading the captured evidence, not by inspection of the code.

**D1 — the frozen contract revision rendered as `not recorded`.** The inspector
read `frozen_binding.packet_revision`, but the packet nests it at
`frozen_binding.packet.revision`. A required first-screen field was therefore
silently absent. Fixed, and the frozen contract digest was added beside it so
the binding is legible without leaving the first screen. This was a real
correctness defect: the surface claimed a field was unrecorded when the packet
recorded it.

**D2 — the exact proof sat below nineteen table rows.** On the readiness route
the source-read and D4/D6 receipt cards were rendered after the material check
summary, so a reviewer looking for the proof scrolled past the whole check set
to reach it. The receipt reach now sits directly under the decision, before the
table. The two-interaction budget was always met; the reading order was not.

**D3 — the Gaps route buried its own answer.** Its question is which packet is
current and what happened to the earlier acknowledgement, and that answer sat
below twenty Coverage Gap rows. Panel order is now state, then acknowledgement,
then disagreements, then the gap table.

**D4 — orange had been spent on every absence.** `UNKNOWN` and `MISSING`
sentinels rendered in the warn colour, so a blocked packet showed dozens of
orange tokens and the accent stopped meaning anything. A typed absence is a fact
the packet records, not an alarm: sentinels are now muted monospace with a
dotted underline, and orange is reserved for blocked state and contradiction as
the contract requires.

**D5 — the rail repeated a derived fact seven times.** Every scenario row showed
`analysis_use · post_analysis_eligibility`, which is the same fact twice, since
eligibility is mechanically derived from the stored decision and already sits in
the authority strip. Five consecutive rows read `NOT_PERMITTED · BLOCKED`, which
is the repeated-badge pattern the contract warns against. The rail now carries
the stored decision only.

**D6 — the review question fought the facts grid.** A sentence was being squeezed
into an 88px label column and wrapping four words wide. It now has its own line
above the facts.

**D7 — the page scrolled sideways on narrow viewports.** Measured, not guessed:
a probe (`tests/overflow.html`) loads the surface at 390, 480, 760, 900, 1180
and 1440px across four scenarios and five routes and reports any element whose
right edge escapes the viewport without sitting inside a scrollable container.
The first run failed 20 of 120 cases. Two causes: grid children defaulting to
`min-width: auto` and refusing to shrink, and verbatim `<pre>` receipt dumps with
no `overflow-x`. Both fixed; label-above-value stacking was added below 760px so
an ISO interval no longer has to share a row with its label. The probe now
passes 120 of 120 and runs as part of `tools/verify.py`.

**D8 — the narrow evidence was not evidence.** The first "390px" captures showed
text truncated mid-word. The DOM measured no overflow, so one of the two was
lying. Headless Chrome clamps a window to 500px wide: `--window-size=390` laid
the page out at 500px and the screenshot merely cropped it. The page had never
been at fault. Narrow captures now render inside a fixed 390px iframe
(`tools/narrow-frame.html`), which gives a genuinely narrow layout viewport. The
lesson is recorded because a mobile screenshot from headless Chrome below 500px
is untrustworthy by default, and would have been reported as a product defect.

## 3. AI-design cliches checked for, and the result

| Cliche | Present |
| --- | --- |
| Gratuitous gradient | none; no `linear-gradient` in the stylesheet |
| Glowing or floating card | none; no `box-shadow`, no `border-radius` above 50% on anything but the focus ring |
| Generic chat bubble | none |
| Oversized empty hero | none; the first screen is a dense decision strip |
| Decorative sparkle, emoji or icon carrying meaning without text | none; the page contains no icon font, no SVG and no emoji |
| Unexplained confidence score | none; every value is a typed packet field with its rule source |
| Repeated pill badges | reduced to one bordered outcome tag per check row; the rail duplication was removed as D5 |
| Marketing copy | none; the prose is declarative and every sentence names a packet field or a limit |

## 4. Observability gaps that remain

These are genuine and unfixed. They are listed so a later reviewer does not have
to rediscover them.

1. **The route tablist scrolls horizontally below roughly 620px, and the fifth
   tab is off-screen with no affordance saying so.** The scroller is correct and
   keyboard navigation still reaches every route by arrow key, but a touch
   reviewer sees four of five tabs and no scroll hint.
2. **A blocked packet renders nineteen near-identical rows.** When the read is
   not admitted, eighteen checks share the reason "reported evidence was not
   admitted" and only `CHK-16` carries the substantive failure. The surface
   orders `CHK-16` first, and the decision explanation names it, but the table
   still asks the reader to scan eighteen consequences of one cause. Grouping
   consequential unknowns under their originating check would be an improvement
   and is a change to presentation only.
3. **Coverage Gap identity is shown but not cross-linked.** A gap names its
   `evidence_refs` as receipt ids, and the receipt index lists those ids, but the
   two are not linked: matching them is manual. Every relationship is present in
   a table, as required, but traversal is by eye.
4. **The check table sets a 720px minimum and scrolls inside its container on a
   phone.** This is deliberate — compressing it instead breaks identifiers
   mid-token — but it means a narrow reviewer scrolls a region rather than
   reading a reflowed layout.
5. **No live reviewer has used this.** Every accessibility property claimed here
   is either mechanically checked (contrast ratios, focus style, landmarks,
   tablist semantics, reduced motion) or structurally implemented. None of it is
   a substitute for the P3 live review-surface acceptance gate, which remains
   open.

## 5. What the critique does not establish

This critique covers a local fixture-only artifact. It does not establish
production M0 capability or authorization, close P2, P3 or P4, begin M1 or M2,
or carry any Experiment Review Committee decision. `VAL-UI-101` remains an open
external gate.
