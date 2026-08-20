# M0 Flight Readiness review surface

A local, static, dependency-free, read-only review artifact for fixture-class
`FlightReadinessPacket` projections. Open `index.html` in a browser. There is no
build step, no server, no package to install and no network request.

**This is a pre-P3 local prototype.** It is fixture-only. It establishes no
production capability, no production authorization, no cause, no M1/M2
recommendation, no win/loss judgement, no P3 closure and no Experiment Review
Committee decision. Live review-surface acceptance remains the open external
gate `VAL-UI-101`.

## What it shows

Seven scenarios, every one of them a real packet **emitted by the accepted M0
package** (`kdd_data_agent.m0.evaluator.evaluate_flight`) against synthetic
reads. No readiness field is hand-authored.

| Scenario | Stored `analysis_use` | What it demonstrates |
| --- | --- | --- |
| `trusted-decision-grade` | `decision_grade` | a trusted read with no material blocker |
| `pre-runtime-directional` | `directional_only` | runtime below the preregistered threshold |
| `recomputation-disagreement` | `not_permitted` | reported and independently recomputed values disagree |
| `unauthorized-read` | `not_permitted` | an unauthorized read, no body retained |
| `redaction-blocked-read` | `not_permitted` | a redaction failure, no body retained |
| `stale-superseded-read` | `not_permitted` | a stale read, a superseding packet, an invalidated acknowledgement |
| `incomplete-observations` | `not_permitted` | absent observations and a non-independent recomputation, as typed Coverage Gaps |

Five routes: **Readiness** (the decision, why it is limited, the next safe
action, the receipt reach, the ordered material-check summary), **Checks** (the
sealed nineteen-check set with read-only view filters), **Receipts** (source
read, the D4/D6 recomputation, and one validator receipt per check),
**Gaps & state** (Coverage Gaps, disagreements, staleness, supersession,
acknowledgement) and **Boundaries** (what this surface is not, plus the exact
input bindings).

Deep links are read-only: `index.html#/<scenario_id>/<route_id>`.

## Layout

```
index.html            the shell and its mount points
styles.css            the visual contract; no remote asset, no @import
app.js                the renderer; builds DOM with textContent only
data/fixtures.json    the generated render model, canonical JSON
data/fixtures.js      the same payload, loadable over file://
tools/bindings.py     recomputes the five exact input bindings; halts on drift
tools/build_fixtures.py  projects accepted-package packets into the render model
tools/verify.py       the mechanical check suite
tools/capture.sh      desktop and true-390px visual evidence
tools/check_overflow.sh  horizontal-overflow measurement across six widths
tools/narrow-frame.html  hosts the surface at a genuinely narrow viewport
tools/run_build_test.py  runs the whole battery; writes build-test.json/.log
tools/output_aggregate.py  the exact-byte aggregate over the owned outputs
tests/test_surface.js behaviour suite; executes the real app.js
tests/dom.js          the minimal document the suite runs app.js against
tests/overflow.html   the layout probe
evidence/             rendered PNG evidence
```

## Regenerate and verify

From the repository root, or from any other directory:

```
PYTHONPATH=prototypes/m0-flight-readiness-review/tools \
  python3 prototypes/m0-flight-readiness-review/tools/build_fixtures.py --check

PYTHONPATH=prototypes/m0-flight-readiness-review/tools \
  python3 prototypes/m0-flight-readiness-review/tools/verify.py
```

`verify.py` recomputes the exact input bindings, confirms the accepted M0
package is unmodified, reproduces the fixtures, checks HTML/CSS/JavaScript
structure and offline-only guarantees, measures WCAG AA contrast for every
palette pair, runs the behaviour suite, and measures horizontal overflow at six
widths. Add `--skip-layout` where Chrome is unavailable.

The behaviour suite alone: `node tests/test_surface.js`.

## Design and safety properties

- Read-only. No control writes, applies, approves, acknowledges or re-evaluates.
  The view filters state so on screen.
- Model values are written with `textContent`; nothing reaches `innerHTML`, so a
  value in the data can never become markup.
- Fail-closed. An absent, foreign-schema, empty or truncated model renders a
  refusal rather than a partial page. A typed absence renders as `UNKNOWN` or
  `MISSING`, never as blank, `null` or a dash.
- No graph diagram. Every relationship is a table row that names its inputs.
- No Trace store exists in M0, and none is rendered.
- The visual baseline is the owner-selected design contract. The critique
  against it lives in three files under
  `docs/reviews/2026-08-18-m0-flight-readiness-review-surface/`:
  `visual-critique.md` (defects D1–D8), `design-critique.md` (which design-skill
  rules were adopted, which were rejected and why, defects D9–D12, and the
  residual AI-slop risks) and `critique.json` (the five-axis panel score).

## Bound inputs

This projection is bound to the four frozen documents and the accepted 59-file
M0 package aggregate `9eea3014…b19a` (`ACCEPT_LOCAL_M0_EVIDENCE`). A byte change
to any of them invalidates it; `tools/bindings.py` halts rather than emitting a
projection against drifted inputs. The Boundaries route lists all five with
their digests.
