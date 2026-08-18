# Faithful Reconstruction Receipt

PROTOTYPE / THROWAWAY. Synthetic, read-only, dependency-free, and not connected to production systems. This receipt prepares the prototype for another owner review; it is not owner acceptance.

## Why the prior implementation failed

The rejected implementation treated the generated mockups as loose inspiration. It kept the product facts but replaced the mockups' dense forensic composition with editorial headings, sparse space, generic cards, and simplified graph and proof structures. That was a failure to follow the owner's selected design contract. The reconstruction instead treats the four owner-selected route images as hard geometry and composition contracts.

## Hard visual contract

- `reference-assets/owner-selected-iteration/review.png`
- `reference-assets/owner-selected-iteration/claims.png`
- `reference-assets/owner-selected-iteration/verify.png`
- `reference-assets/owner-selected-iteration/trace.png`

The four routes share one 220 px case rail, one 64 px route masthead, separate Cause Verdict and Recommendation Readiness axes, thin rule-based grouping, compact technical sans and monospace typography, and sparse orange state accents.

## Screen-by-screen correction

| Route | Rejected mismatch | Reconstructed contract |
|---|---|---|
| Review | Editorial conclusion page with loose evidence blocks and weak proof continuity. | Compact conclusion strip, 2x2 evidence matrix, Case Facts inspector, and full-width Persistent Proof Dock. |
| Claims | Loose card grid that obscured the answer path and reduced the inspector. | Competing-claims rail, four grouped evidence bands, fifteen typed nodes, explicit directional edges, controls, legend, and full Evidence Inspector. |
| Verify | Simplified code view without the mockup's full authority and provenance hierarchy. | Breadcrumb, deployed authority strip, receipt and validator metadata, deployed-versus-candidate code panes, literal `not_applied`, verification log, provenance, ACL, and redaction boundary. |
| Trace | Sparse editorial timeline with too little event density. | Explicit not-Evidence boundary, dense event table, evidence links, raw-output inspector, state legend, and trace facts footer. |

## Browser revision cycles

### Cycle 1

Screenshots: `review-artifacts/reconstruction-cycle-1-{review,claims,verify,trace}.png`.

Finding: the route anatomy was present, but proof density, graph grouping, and inspector hierarchy remained weaker than the owner-selected images. Review lacked enough proof rows; Claims needed a clearer banded path; Verify needed stronger deployed-versus-candidate authority; Trace needed a denser event ledger.

Revision: expanded the Proof Dock, rebuilt the graph as grouped typed evidence bands, restored the detailed code and receipt hierarchy, and rebuilt Trace around a full event table and raw-output inspector.

### Cycle 2

Screenshots: `review-artifacts/reconstruction-cycle-2-{review,claims,verify,trace}.png` and `review-artifacts/reconstruction-cycle-2b-{review,claims,verify,trace}.png`.

Finding: a browser cache mixed the new CSS with an older JavaScript payload, creating false visual drift. Source and server hashes matched, so the document now uses revisioned asset URLs. After the corrected reload, desktop composition matched the selected shell and route geometry. Mobile still required a complete vertical evidence path and bottom navigation clearance.

Revision: added revisioned static asset URLs, completed the mobile graph reflow, preserved all evidence states, and reserved bottom space for fixed route navigation.

### Final inspection

Desktop renders at 1586x992:

- `review-artifacts/reconstruction-final-desktop-review.png`
- `review-artifacts/reconstruction-final-desktop-claims.png`
- `review-artifacts/reconstruction-final-desktop-verify.png`
- `review-artifacts/reconstruction-final-desktop-trace.png`

Mobile renders at 390x844:

- `review-artifacts/reconstruction-final-mobile-review.png`
- `review-artifacts/reconstruction-final-mobile-claims.png`
- `review-artifacts/reconstruction-final-mobile-verify.png`
- `review-artifacts/reconstruction-final-mobile-trace.png`

Same-aspect side-by-side comparisons:

- `review-artifacts/reconstruction-comparison-review.png`
- `review-artifacts/reconstruction-comparison-claims.png`
- `review-artifacts/reconstruction-comparison-verify.png`
- `review-artifacts/reconstruction-comparison-trace.png`

The final critique uses observable composition deltas rather than an agent taste score. The owner-rejected score is superseded and is not acceptance evidence.

## Skill applicability

- `gpt-taste` removed generic AI dashboard defaults and forced a single focal hierarchy per review task.
- `design-taste-frontend` established the disciplined rule grid, restrained accent, typography roles, focus treatment, responsive reflow, and reduced-motion behavior.
- `open-design-critique-theater` made the owner-visible render, not source intent, the critique target and replaced self-score claims with route-specific evidence.
- `imagegen-frontend-web` produced the horizontal route references that were inspected as one product system.
- `image-to-code` changed the references from inspiration into hard composition contracts and drove the DOM and information-architecture reconstruction.
- `open-design-build-test` required truthful skips for absent project commands and equivalent static and real-browser checks.
- `comms-draft` and `comms-polish` tightened conclusion, contradiction, gap, proof, and next-action copy without overstating causal certainty.

Marketing AIDA, landing-page hero/footer structure, stock imagery, GSAP scroll choreography, conversion CTAs, and perpetual animation were not applied because they conflict with a forensic review workspace. Their anti-slop, hierarchy, typography, and rhythm principles were retained.

## Functional review evidence

- One real click on `Open deployed proof` navigates from Review to Verify.
- Selecting `EV-DEP-17` in Claims updates the Evidence Inspector with exact deployed support details.
- One real click on `Back to evidence in graph` navigates from Trace to Claims.
- Real physical-key automation with `F1` through `F4` navigates Review, Claims, Verify, and Trace.
- Loading, empty, error, and permission states fail closed and do not strengthen a verdict.
- Desktop and 390 px mobile routes have no horizontal document overflow.
- Reduced-motion mode computes zero animation duration.
- Focus indicators and the skip link are visible.
- No code or tool-output pane renders a literal backslash-n sequence.

## Honest remaining deviations

- The implementation uses available system font equivalents rather than the mockup's exact proprietary font files.
- Lightweight inline SVG and text primitives replace unavailable source icon assets.
- Claims graph routing is faithful in hierarchy and function but not pixel-identical in every Bezier path.
- Synthetic timestamps and prose differ where required to preserve the current Scenario A evidence contract.
- Mobile is an intentional task-preserving reflow, not a scaled copy of the desktop image.
- Fixed mobile navigation clearance still requires owner validation during real Claims and Trace scrolling.

## Gate

P3 remains open with Claim `019ff4cf-be73-7381-a086-6425c2a0bdf2`. Only explicit owner live acceptance can close it.
