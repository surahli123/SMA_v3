# Evidence Room — Observability Review Prototype

> PROTOTYPE / THROWAWAY. Synthetic, read-only, dependency-free, and not connected to production systems. This is M1 research, not the current M0 Flight Readiness deliverable or its packet-centered review surface.

## Question

Which first-screen and evidence-navigation structure lets a reviewer verify the current conclusion, expose counterevidence and gaps, and locate exact deployed proof without mistaking Trace for Evidence?

## Run

From the repository root:

```bash
python3 -m http.server 8765 --directory docs/research/kdd-data-agent-workshop/prototypes/observability-review-surface
```

Routes:

- `http://127.0.0.1:8765/?view=review`
- `http://127.0.0.1:8765/?view=claims`
- `http://127.0.0.1:8765/?view=verify`
- `http://127.0.0.1:8765/?view=trace`
- Prototype states append `&state=loading|empty|error|permission`.
- Physical keyboard shortcuts are `F1` through `F4` for Review, Claims, Verify, and Trace.

The former `?variant=A|B|C`, Evidence Dossier, and Case Ledger surfaces are rejected iterations. Evidence Room replaces their information architecture; it is not a reskin.
Legacy `?variant=` URLs are normalized in place to `?view=review` so the browser cannot imply that rejected A/B/C variants remain current.

## Owner-selected design iteration

The current rebuild uses the owner-selected Verify and Trace screens as the primary product-language contract. The new route references derived from that shared system are:

- [Review route reference](reference-assets/owner-selected-iteration/review.png)
- [Claims route reference](reference-assets/owner-selected-iteration/claims.png)
- [Verify route reference](reference-assets/owner-selected-iteration/verify.png)
- [Trace route reference](reference-assets/owner-selected-iteration/trace.png)

The shared geometry, product-fit decisions, and route mapping are recorded in [Owner-Selected Design Contract](owner-selected-design-contract.md). The earlier `unified-*.png` set and every prior self-score are superseded iteration evidence, not owner acceptance.

## Current design direction

The four owner-selected route references are the hard composition contract. The current implementation reconstructs their light forensic shell and route-specific review grammar instead of reinterpreting them as an editorial page or a generic dashboard.

- Review reproduces the conclusion row, 2×2 evidence matrix, Case Facts sidebar, and Persistent Proof Dock. Exact deployed proof is one interaction from the next safe action.
- Claims reproduces the competing-claims list, grouped horizontal Evidence Graph, typed directional relations, controls, legend, and adjacent Evidence Inspector.
- Verify reproduces the breadcrumb, authority and receipt strips, detailed applied-vs-`not_applied` code comparison, evidence summary, verification log, provenance, and permission-redacted ACL sidebar.
- Trace reproduces the dense execution table, evidence cross-links, raw-output inspector, status legend, footer facts, and explicit not-Evidence boundary.

The narrative was drafted with `comms-draft` and passed through `comms-polish`. It keeps the conclusion, contradiction, gap, proof, and safe next action concrete without strengthening uncertainty into a causal fact.

## Superseded reference images

The following earlier images remain for rejected-iteration comparison only. They are not the current implementation contract.

- [Review reference](reference-assets/unified-review.png) — receipt `exec-2572a33c-ac80-47d7-9049-ab9774f5bd3a`
- [Claims reference](reference-assets/unified-claims.png) — receipt `exec-af8b1edf-918e-4cd8-9719-9a3f2850616b`
- [Verify reference](reference-assets/unified-verify.png) — receipt `exec-a48704f8-55cf-4d04-9b4f-056582d00e2c`
- [Trace reference](reference-assets/unified-trace.png) — receipt `exec-846934ba-ce37-4677-bd4a-ff99271011c6`

Consistency inspection: all four corrected references use Evidence Room, CASE A–017, Search experiment miss, Cause Verdict Suspected, Recommendation Readiness Blocked, SHA `9f71c2e`, artifact `blend_weights.bin v73`, the same four evidence IDs, the same dark rail and bone workspace, and the same orange risk accent. Unauthorized metrics, thresholds, timing claims, unrelated incidents, and ambiguous comparison copy were removed. Earlier generated images are superseded exploration and are not implementation references.

Superseded exploration is quarantined under `rejected-reference-assets/` or explicitly identified above. Current implementation references live under `reference-assets/owner-selected-iteration/`.

## Current review evidence

- [Owner-rejection critique](critique-owner-ai-slop-2026-08-12.json) — supersedes every earlier agent score.
- [Faithful reconstruction receipt](faithful-reconstruction-receipt.md) — records the hard-contract rebuild, review cycles, exact browser checks, and remaining deviations.
- [M17 interaction repair](m17-interaction-repair.md) — separates Claim and Evidence inspection and records honest control behavior.
- Current desktop renders: `review-artifacts/reconstruction-final-desktop-{review,claims,verify,trace}.png`
- Current mobile renders: `review-artifacts/reconstruction-final-mobile-{review,claims,verify,trace}.png`
- Side-by-side reference comparisons: `review-artifacts/reconstruction-comparison-{review,claims,verify,trace}.png`
- [Current build and interaction receipt](build-test.json)

M17 behavior: competing Claim nodes and rail entries open a Claim Inspector for that exact Claim. They never fall through to another Claim's supporting Evidence. Claims path controls and Trace filters have deterministic synthetic behavior. Verify `Code`, `Diff`, and `Receipts` controls focus their real projections; the absent standalone `Config` projection and authorized expansion are visibly disabled.

Older Case Ledger, Evidence Dossier, editorial award-language, and A/B/C artifacts are retained only as rejected iteration evidence. Screenshots and overlays are comparison evidence, not owner acceptance.

## Source-backed patterns and inference

Observed Team 1286 mechanics used here: source graph, answer path, grouping, node detail, re-layout, and separate Trace. Observed Team 1401 mechanics used here: typed relations, clusters, filters, collapse/expand, detail inspection, and exact source/page location. These are interaction precedents, not evidence that the teams solved production RCA.

The production review chain is a reviewer inference from the local contract: metric → surface → query/result → ACL/corpus → pipeline/runtime → typed deployed change → claim/contradiction → verification → recommendation. Graph is optional: Review uses a decision sequence, Verify uses code/diff/receipts, and Trace uses a timeline because each is clearer for its task.

## Review script

1. On Review, state the conclusion, strongest contradiction, and why Recommendation Readiness is blocked.
2. Reach exact SHA, repository, file, symbol, lines, and validator receipt in no more than two interactions.
3. On Claims, select the strongest contradiction and identify its source, scope, time, authorization, receipt, validator, freshness, and invalidation.
4. Filter contradictions, collapse context, re-layout, and distinguish the Evidence Graph from Trace.
5. Find stale, incomplete, invalidated, superseded, high-risk, permission-redacted, empty, loading, and error behavior.
6. Choose the clearer non-graph projection for code proof and execution replay.

## Measurable feedback

- Exact deployed proof reached within two interactions: yes / no; interaction count: ____
- Strongest contradiction found without prompting: yes / no; time: ____
- Stale or incomplete evidence and recompute impact identified: yes / no
- Trace distinguished from Evidence: yes / no
- Clearer non-graph projection selected: review sequence / code-diff / receipts / timeline
- Mobile Claims continuation and proof navigation are understandable: yes / no
- Most confusing element: ____
- One change that would reduce review time: ____

## Human gate

Owner live review is pending. The Wayfinder ticket remains open with its Claim retained. Closure requires owner/reviewer confirmation that the interaction improves observability and review efficiency; an agent critique score is not acceptance.

Mobile live-review limitation: mobile deliberately reflows the dense desktop graph and tables instead of scaling them. The fixed route navigation reserves bottom clearance, but the owner should still verify that it does not obscure a selected Claims node or Trace event during real scrolling.
