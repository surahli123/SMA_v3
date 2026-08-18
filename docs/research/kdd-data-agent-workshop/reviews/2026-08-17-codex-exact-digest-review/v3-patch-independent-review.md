# Independent Review of the Exact Round 3 Candidate Patch

Date: 2026-08-17  
Handoff: `kdd-m0-v3-patch-independent-review-20260817`  
Review mode: bounded, report-only, fresh disposable-copy only  
Authority label: `CODEX_ADVISORY_ONLY`

## Verdict

**REJECT_CANDIDATE**

The exact v3 patch applies cleanly and all five claimed disposable post-apply digests are reproducible. It corrects every exact v2 rejection anchor, makes Check 14 a pending non-conformant seam, preserves D1-D3 and the exact 26-ID registry, and keeps the named open gates open. The candidate is nevertheless rejected because one post-apply packet sentence still presupposes a live, separate local fixture-backed M0 authorization. That semantic variant contradicts the packet's own exhausted-receipt state and the other four candidate documents.

This verdict is advisory only. It is not a freeze, Owner approval, Opus/Fable verdict, Phase A acceptance, implementation authorization, production authorization, or Committee Acceptance. The patch was not applied to live canonical documents, and no M0 unit was started.

## Exact patch and application evidence

| Item | Result |
| --- | --- |
| Exact patch | `docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/candidate-canonical-writeback-v3.patch` |
| Patch SHA-256 | `f85cae49ad6c3b1b2d24b7c217c54c9b4c204fabd111668a76447b31f1f24407` |
| Patch shape | 804 lines; 5 files; 167 insertions; 125 deletions |
| Live `git apply --check --whitespace=error-all` | **PASS** |
| Fresh disposable-copy strict check | **PASS** |
| Fresh disposable-copy application | **PASS** |
| Review environment | Five live source files copied to a new `/private/tmp` directory; no Git worktree, network, credentials, production access, or mutation authority |

## Disposable post-apply digest manifest

| Disposable candidate file | Independently recomputed SHA-256 | Round 3 claim |
| --- | --- | --- |
| `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | `e8b97b9224c39bbfd2ee1ec25059556febc0cc529e95e4244e6a338c3366b6c4` | match |
| `docs/research/kdd-data-agent-workshop/eval-acceptance-plan.md` | `2785fc7f9eab6c20dd030b1b6ab9c0f89a768a2163b52e3884b27fd8db535516` | match |
| `docs/research/kdd-data-agent-workshop/final-architecture-spec.md` | `75bf5f12463e7c686e2bae737754b9437d54600e870b67d634ddadbe93d87507` | match |
| `docs/research/kdd-data-agent-workshop/implementation-sequencing.md` | `311a4a4aa781029253f764847189b817e9a05d973ce9245035b00001f12bc109` | match |
| `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `4b3c5293a79536f2a75f7070d4de700a21c507a5e6eb86058357f183f559affc` | match |

## Rejection finding

### P0 — Explicit non-authorization text still presupposes a live M0 authorization

The disposable post-apply packet says at `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md:337`:

> This packet does not broaden the separate local fixture-backed M0 authorization.

In present-tense, unqualified wording, “the separate ... authorization” presupposes that such an authorization is live. It conflicts with the same packet's corrected statements at `:7`, `:19`, `:33`, and `:204` that the prior authorization is exhausted and `M0-F1`-`M0-F5` require a new exact-digest Owner start receipt. It also conflicts with the other four candidate documents' planning-only state.

An implementer could cite the explicit non-authorization section as evidence that a separate local M0 authorization still exists, even though this packet merely does not broaden it. This fails the handoff's requirement that no semantic live-M0-authority variant remain.

Minimal correction: replace the sentence with an explicit non-grant and exhausted-receipt statement, without implying any current separate authorization. A superseding patch must receive another exact-digest disposable-copy review.

## Nine-area verification matrix

| # | Required verification | Result | Evidence |
| --- | --- | --- | --- |
| 1 | Every v2 rejection anchor fixed; no semantic live-M0-authority variant | **FAIL** | The exact v2 anchors are corrected at CE plan `:9,20-21,27,38-40`, architecture `:38,798,1002`, sequencing `:205,553-555`, and evaluation `:148,218-220`. Packet `:337` still presupposes “the separate local fixture-backed M0 authorization.” |
| 2 | Check 14 pending everywhere; only a replaceable, explicitly non-conformant seam; no topology selected | **PASS** | All five documents name the pending Owner/Fable ruling, the candidate-recomputation seam, and explicit non-conformance. Architecture `:798` and evaluation `:148,218-220` no longer assert a settled fixture or independence measurement. No source- or transform-independence topology is selected. |
| 3 | D1, D2, and D3 coherent across all five documents | **PASS** | Each document contains `runtime_only | runtime_and_sample`, preregistered inputs, no post-hoc/achieved power, the missing-input branch, arm-parity `MISSING`/versioned `NOT_APPLICABLE`/material `FAIL` behavior, and stored `analysis_use` with derived non-settable eligibility. |
| 4 | Exactly 26 active `VAL-*` IDs mapped once | **PASS** | Packet acceptance table: 26 rows / 26 unique IDs. Sequencing ownership table: 26 rows / 26 unique IDs. Exact set match; missing `[]`; extra `[]`; duplicate ownership IDs `[]`. |
| 5 | B3, M18, M19, and M20 explicitly open | **PASS** | CE plan `:337,341-343` labels each item `OPEN`; no closure or resolution claim was found in the five candidate documents. |
| 6 | Historical `2f1001...` is not a verified current binding | **PASS** | Occurrence count across the five disposable candidate files: `0`. No replacement aggregate is represented as verified current truth. |
| 7 | No M0-F1-F5, production, M1/M2, mutation, deployment, publication, or Committee authority | **FAIL** | Production, M1/M2, mutation, deployment, publication, and Committee boundaries remain closed, but packet `:337` semantically preserves a separate local fixture-backed M0 authorization and therefore fails the all-authority condition. |
| 8 | Planning-only wording preserves the Owner-aligned goal, M0 main-deliverable status, and a future bounded exact-digest receipt | **PASS** | CE plan `:16-21,317`, architecture `:36-40,1002`, sequencing `:7,51,652`, evaluation `:4,29`, and packet `:7,19,33,204` preserve the goal and future receipt mechanism without starting work. |
| 9 | Links, headings, metadata, and terminology mechanically and semantically usable | **FAIL** | All 69 local Markdown links checked resolve, including the authoritative-registry anchor; headings and CE-plan frontmatter are mechanically usable. Cross-document authority terminology is not semantically coherent because packet `:337` conflicts with the exhausted-receipt state. |

## Preserved non-authorizations and open state

- Check 14 remains an unresolved Owner/Fable architecture decision; this review does not answer it.
- B3, M18, M19, M20, P2, P3, and P4 remain open.
- The historical Phase A aggregate beginning `2f1001` is absent from candidate canonical bytes.
- Production access, M1/M2 execution, mutation, commit, push, PR, deployment, rollback, publication, and Committee Acceptance remain ungranted except for the contradictory M0-authorization presupposition identified above.
- No canonical document, Phase A artifact, patch, prior review artifact, code, test, fixture, or Git state was modified by this review.

## Next lawful step

Prepare a superseding unapplied patch against the same live base that removes the packet's remaining semantic live-authorization presupposition. Then rerun exact-digest review in a new disposable copy. Do not apply canonical writeback or start `M0-F1`-`M0-F5` from this rejected candidate.

This bounded run stops after writing this report and its status JSON.
