# Mockup Fidelity Contract

PROTOTYPE / THROWAWAY. This receipt treats the four `unified-*.png` references as the chosen visual contract. Product authority, accessibility, and read-only semantics remain non-negotiable; they must fit the reference composition rather than replace it.

| Route | Mockup geometry | Current implementation | Exact mismatch | Planned correction |
|---|---|---|---|---|
| Review | 180 px dark rail; large case masthead; boxed verdict/readiness; horizontal mode tabs; conclusion plus narrow Case Facts rail; ruled 2×2 evidence matrix; full-width proof table. | Thin fixed app header, editorial headline, paired evidence blocks, authority trail, no case-facts rail. | Reads like an editorial web page. The case masthead, secondary navigation, fact rail, strict matrix, and proof-table proportions are missing. | Recreate the masthead, tabs, asymmetric conclusion/facts split, ruled evidence matrix, and persistent proof table with the same whitespace and type rhythm. |
| Claims | Narrow dark rail; case masthead; left claim list; dense toolbar; free graph topology grouped as Observation, Authority, and Judgment; right inspector; bottom legend. | Large editorial heading and a uniform 3×3 CSS grid of equal boxes. | The graph reads as a checklist, not a spatial investigation. Edge routing, node hierarchy, toolbar density, and inspector rhythm diverge from the reference. | Use absolute graph nodes and SVG typed edges in three spatial bands; reproduce the left list, toolbar, inspector, and legend proportions. |
| Verify | Dark rail; case masthead; proof breadcrumb; compact title; dense authority and receipt strips; two large light code panes; provenance rail; evidence summary and verification log. | Large editorial heading, sparse authority strip, dark code panes, small receipts column. | Proof authority is visually diluted. Breadcrumb, receipt row, summary, log, and the reference's light dossier material are absent. | Rebuild the complete authority hierarchy with light side-by-side code panes and literal `not_applied` candidate status. |
| Trace | Dark rail; case masthead; large left trace table; right output inspector and readable log; bottom trace summary. | Thin app header, oversized warning block, sparse ledger, small dark log, large unused lower space. | This is the largest fidelity failure: wrong masthead, density, title treatment, table geometry, inspector scale, and bottom summary. | Recreate the dense trace table, large inspector/log, legend, and trace summary while preserving the explicit not-Evidence boundary. |

## Product-fit decisions

- Marketing AIDA, hero/footer composition, conversion copy, GSAP, and perpetual motion are excluded because they obscure an investigation workflow and conflict with the dependency-free prototype boundary.
- The skills' anti-slop, typography, spacing, hierarchy, restrained motion, and composition guidance is applied directly.
- The graph is an interactive evidence projection, never decoration. Trace remains a separate execution projection and cannot change the verdict without a cross-linked validated evidence record.
