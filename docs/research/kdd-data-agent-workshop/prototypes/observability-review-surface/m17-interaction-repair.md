# M17 Interaction Repair

PROTOTYPE / THROWAWAY. Synthetic, read-only, dependency-free, and not connected to production systems.

## Scope

This bounded repair addresses Opus finding M17 in the Observability Review Surface. It does not change architecture, planning, evidence authority, production state, or the P3 human gate.

## Reproduction before repair

Source inspection found that `graphStage()` assigned `data-evidence="EV-DEP-17"` to every non-`EV-` graph node. A real browser click on Claim `C-09` therefore produced:

- clicked node dataset: `EV-DEP-17`
- selected records: deployed Evidence plus all three competing Claim nodes
- inspector: `Validated support / EV-DEP-17 / Deployed blend artifact`

The same browser session found no observable state change after activating `Show answer path`, Verify `Config`, or Trace `Status: All`.

Before screenshot: `review-artifacts/m17-before-claim-fallback.png`.

## Repair

- Added a dedicated synthetic model for `C-17`, `C-09`, and `C-22` with Claim state, review question, current basis, linked records, coverage, next review, and a Claim locator.
- Claim rail entries and graph nodes now use `data-claim`. Evidence nodes continue to use `data-evidence`.
- Selecting a Claim opens `CLAIM INSPECTOR` for that exact Claim. The Evidence Inspector no longer silently falls back to `EV-DEP-17` for an unknown identifier.
- `Show answer path` and `Show evidence path` now set an explicit pressed state, highlight deterministic node sets, and publish a live status message.
- Single-option Claims controls are visibly disabled. Contradiction, collapse, and re-layout controls retain deterministic behavior.
- Verify `Code`, `Diff`, and `Receipts` controls focus the corresponding real projection and publish a live status message. The unavailable standalone `Config` projection, single-option comparison selector, and authorized expansion are visibly disabled.
- Trace filters now support deterministic Time, Status, Tool category, Evidence link, search, reset, count, and empty-state behavior.

After screenshots:

- `review-artifacts/m17-after-claim-detail.png`
- `review-artifacts/m17-after-trace-filter.png`

## Browser evidence after repair

- `C-09`: `data-claim=C-09`, no `data-evidence`, inspector heading `CLAIM INSPECTOR`, state `Inconclusive`, and no deployed-artifact fallback.
- `C-22` from the rail: inspector heading `CLAIM INSPECTOR`, state `Ruled out`, active rail Claim `C-22`, and no deployed-artifact fallback.
- Answer path: `aria-pressed=true`, graph class `path-answer`, live status `Answer path highlighted · 6 review nodes.`
- Evidence path: answer path clears, evidence path becomes pressed, and the live status identifies the metric-to-Claim chain.
- Verify Config: visibly disabled as unavailable. Diff focuses `#verify-diff`; Receipts focuses `#verify-receipts`; authorized expansion is disabled as unavailable.
- Trace Status filter: label changes to `Status: Attention`, `aria-pressed=true`, and visible event count changes from 9 to 3.
- Trace Status plus linked-Evidence filters: event count becomes 0 and the explicit empty state appears.
- Trace search `retry`: one matching event remains. Reset restores 9 events and clears search.
- Claims, Verify, and Trace at 390x844: `innerWidth=390`, `scrollWidth=390`.
- Real Tab navigation reaches the skip link and interactive controls with a visible solid focus outline.
- Browser console and page errors: none.

## Mechanical checks

- `node --check app.js`: pass.
- `git diff --check`: pass.
- Durable artifact CJK scan: zero.
- Prohibited machine-local path scan: zero.
- JavaScript source contains no non-Claim fallback to `EV-DEP-17`.
- The `prefers-reduced-motion` CSS override is present. Runtime emulation is not claimed because the current browser command did not make `matchMedia` report `reduce`.

The prototype has no package manifest, project-declared build, lint, typecheck, or test command. Those checks remain skipped with that exact reason; static syntax and real-browser interaction checks are the truthful equivalents.

## Integration instructions

Review and integrate only these owned prototype files at the same repository-relative destination:

- `index.html`
- `app.js`
- `styles.css`
- `README.md`
- `build-test.json`
- `build-test.log`
- `m17-interaction-repair.md`
- `review-artifacts/m17-before-claim-fallback.png`
- `review-artifacts/m17-after-claim-detail.png`
- `review-artifacts/m17-after-trace-filter.png`

Do not edit the Wayfinder ticket, map, architecture, planning packet, implementation code, or protected agent paths. P3 remains open with its existing Claim until explicit owner live acceptance.

## Remaining P3 gaps

- Owner live acceptance is still pending.
- Mobile intentionally shows the critical typed path rather than all competing Claims at once; its review efficiency still needs owner validation.
- Nodes without a synthetic detail record now show an explicit unavailable inspector rather than fabricated detail.
- The prototype remains static and read-only; it does not prove production data authority or backend behavior.
