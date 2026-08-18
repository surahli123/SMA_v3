# Independent Review of the Exact Round 4 Candidate Patch

Date: 2026-08-17  
Handoff: `kdd-m0-v4-patch-independent-review-20260817`  
Review mode: bounded, report-only, fresh disposable-copy only  
Authority label: `CODEX_ADVISORY_ONLY`

## Verdict

**ACCEPT_CANDIDATE_FOR_OWNER_WRITEBACK_REVIEW**

The exact v4 patch applies cleanly to a fresh disposable copy and all five claimed post-apply digests are reproducible. Independent v3-versus-v4 disposable-tree comparison shows exactly one replaced sentence in the alignment packet and no other changed candidate byte. The replacement removes the v3 live-authorization presupposition while preserving every v3 passing area.

This verdict is advisory only. It accepts v4 only as a candidate for Owner writeback review. It is not a freeze, canonical writeback, Owner approval, Opus/Fable verdict, Phase A acceptance, implementation start, production authorization, or Committee Acceptance. No M0 unit was started.

## Exact patch and application evidence

| Item | Result |
| --- | --- |
| Exact patch | `docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/candidate-canonical-writeback-v4.patch` |
| Patch SHA-256 | `348252dcbd22d814fec8af4c6a441f46a9ba42b116fe2a895c16882fe489fa3c` |
| Patch shape | 809 lines; 5 files; 168 insertions; 126 deletions |
| Live `git apply --check --whitespace=error-all` | **PASS** |
| Fresh v4 disposable strict check | **PASS** |
| Fresh v4 disposable application | **PASS** |
| Independent comparison basis | Separate fresh disposable trees created from the same five live source files; exact v3 and v4 patches applied independently |

## Disposable post-apply digest manifest

| Disposable candidate file | Independently recomputed SHA-256 | Round 4 claim |
| --- | --- | --- |
| `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | `e8b97b9224c39bbfd2ee1ec25059556febc0cc529e95e4244e6a338c3366b6c4` | match |
| `docs/research/kdd-data-agent-workshop/eval-acceptance-plan.md` | `2785fc7f9eab6c20dd030b1b6ab9c0f89a768a2163b52e3884b27fd8db535516` | match |
| `docs/research/kdd-data-agent-workshop/final-architecture-spec.md` | `75bf5f12463e7c686e2bae737754b9437d54600e870b67d634ddadbe93d87507` | match |
| `docs/research/kdd-data-agent-workshop/implementation-sequencing.md` | `311a4a4aa781029253f764847189b817e9a05d973ce9245035b00001f12bc109` | match |
| `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `30723c521e5ee67596af56ef2b2bfcb8b71cd2b069b6627fe28f5acf91912009` | match |

## Exact v3-versus-v4 disposable-tree comparison

Exactly one file differs: `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md`. The only diff is one removed line and one replacement line at disposable candidate `:337`.

Removed v3 sentence:

> This packet does not broaden the separate local fixture-backed M0 authorization. It does not grant production access, start M1/M2 implementation, approve a source, close P2/P3/P4, approve a Flight, establish a deadline, commit code, push a branch, open a PR, deploy, roll back, send a message, publish a document, or apply a candidate diff.

Replacement v4 sentence:

> This packet itself grants no implementation authority. The prior continuation authorization is exhausted, and any future local fixture-backed M0 slice requires a new exact-digest Owner start receipt. It does not grant production access, start M1/M2 implementation, approve a source, close P2/P3/P4, approve a Flight, establish a deadline, commit code, push a branch, open a PR, deploy, roll back, send a message, publish a document, or apply a candidate diff.

The first four post-apply file digests are identical between v3 and v4. Only the packet digest changes, from `4b3c5293a79536f2a75f7070d4de700a21c507a5e6eb86058357f183f559affc` to `30723c521e5ee67596af56ef2b2bfcb8b71cd2b069b6627fe28f5acf91912009`.

## Verification matrix

| # | Required verification | Result | Evidence |
| --- | --- | --- | --- |
| 1 | Remove the v3 rejection sentence without an equivalent live-authorization presupposition | **PASS** | Packet `:337` now explicitly grants no implementation authority, declares the prior authorization exhausted, and requires a future exact-digest Owner receipt. Broad scans of current, live, existing, separate, authorized, and executable M0 variants found only negative, exhausted, planned-only, future-receipt, or unrelated production-scope uses. |
| 2 | v3-versus-v4 tree differs by exactly one replaced packet sentence | **PASS** | Recursive byte comparison found one differing file. Unified diff contains one removed line and one replacement line at packet `:337`; no other file or byte differs. |
| 3 | D1, D2, and D3 remain coherent across all five documents | **PASS** | Every document retains `runtime_only | runtime_and_sample`, preregistered inputs, no post-hoc/achieved power, the missing-input branch, arm-parity `MISSING`/versioned `NOT_APPLICABLE`/material `FAIL`, and stored `analysis_use` with derived non-settable eligibility. |
| 4 | Check 14 remains pending and non-conformant without selecting a topology | **PASS** | All five documents retain the Owner/Fable-pending state, replaceable candidate-recomputation seam, and explicit non-conformance. No source- or transform-independence topology is selected. This review does not answer Check 14. |
| 5 | Exactly 26 active `VAL-*` IDs map once | **PASS** | Packet table: 26 rows / 26 unique IDs. Sequencing registry: 26 rows / 26 unique IDs. Exact set match; missing `[]`; extra `[]`; duplicate ownership IDs `[]`. |
| 6 | B3, M18, M19, and M20 remain explicitly open | **PASS** | CE plan `:337,341-343` retains explicit `OPEN` labels; no closing claim was found. |
| 7 | Historical `2f1001...` is not a current verified binding | **PASS** | Occurrence count across all five v4 disposable candidate files: `0`. |
| 8 | Owner-aligned M0-M2 goal, M0 main-deliverable status, and future exact-digest receipt mechanism remain intact | **PASS** | These bytes are identical to the corresponding accepted v3 candidate bytes. The five documents preserve the full program goal, M0 first-gate/main-deliverable status, and receipt path while keeping current execution disabled. |
| 9 | No M0-F1-F5, production, M1/M2, mutation, deployment, publication, or Committee authority is granted | **PASS** | Packet `:337` closes the last semantic ambiguity. Other candidate language requires new bounded receipts and named gates and preserves explicit non-authorizations. |
| 10 | Links, headings, metadata, and terminology are mechanically and semantically usable | **PASS** | All 69 local Markdown links checked resolve, including the authoritative-registry anchor. Headings and CE-plan frontmatter remain usable. Cross-document authority wording is now coherent. |

## Preserved boundaries

- Check 14 remains pending the Owner/Fable architecture ruling.
- B3, M18, M19, M20, P2, P3, and P4 remain open.
- The historical Phase A aggregate beginning `2f1001` is absent from candidate canonical bytes.
- Canonical writeback, `M0-F1`-`M0-F5`, production access, M1/M2 execution, mutation, commit, push, PR, deployment, rollback, publication, and Committee Acceptance remain unauthorized.
- No canonical document, Phase A artifact, patch, prior artifact, code, test, fixture, or Git state was modified by this review.

## Next lawful step

The Owner may review the exact v4 candidate for canonical writeback. Any writeback requires separate Owner authority and exact-file review. Even after writeback, `M0-F1`-`M0-F5` still require a new bounded exact-digest Owner start receipt, and Check 14 remains unresolved.

This bounded run stops after writing this report and its status JSON.
