# Independent Review of the Exact Round 2 Candidate Patch

Date: 2026-08-17  
Handoff: `kdd-m0-v2-patch-independent-review-20260817`  
Review mode: bounded, report-only, disposable-copy only  
Authority label: `CODEX_ADVISORY_ONLY`

## Verdict

**REJECT_CANDIDATE**

The exact v2 patch applies cleanly and its claimed disposable post-apply digests are reproducible. D1-D3 and the 26-ID ownership registry are materially improved. The candidate nevertheless fails the handoff's hard conditions because current implementation authority is still asserted in unpatched canonical text, and Check 14 is still represented as a current independent-recomputation fixture/measurement rather than only as a replaceable seam pending the Owner/Fable ruling.

This verdict is advisory only. It is not an Opus or Fable verdict, a freeze, Owner approval, implementation authorization, Phase A acceptance, production authorization, or Committee Acceptance. The patch was not applied to live canonical documents, and no M0 unit was started.

## Exact patch and application evidence

| Item | Result |
| --- | --- |
| Exact patch | `docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/candidate-canonical-writeback-v2.patch` |
| Patch SHA-256 at start and end | `54b386f12d0fc9fc80dbc263404db1bcc7796f030fddddb5fda53c827602286b` |
| Patch shape | 580 lines; 5 files; 126 insertions; 88 deletions |
| Live `git apply --check --whitespace=error-all` | **PASS** |
| Fresh disposable-copy `git apply --check --whitespace=error-all` | **PASS** |
| Fresh disposable-copy application with `--whitespace=error-all` | **PASS** |
| Live canonical inputs after review | unchanged at their pre-run SHA-256 values |

The disposable copy was created under `/private/tmp`; its contents were used only for this review. It was not a Git worktree and carried no production, credential, network, or mutation authority.

## Disposable post-apply digest manifest

| Disposable candidate file | Independently recomputed SHA-256 | Round 2 claim |
| --- | --- | --- |
| `reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `74d77bbb4fce84099d951c58f2f55cf695c3e9ffccb713e929e330e068ffd264` | match |
| `final-architecture-spec.md` | `04285c0eb0a008f573a5c8b872ca7b184182413ea3b7b7dfa356cd2c7b0d09fa` | match |
| `implementation-sequencing.md` | `ae8f935b24af65ef90b1a1a5e2d01e38c08bcb9dac1f6310f30c33151596e946` | match |
| `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | `da78980c2a1d5204c14e9f8ff824e60bd775cd12a0dcd604d813433c89e9d9d9` | match |
| `eval-acceptance-plan.md` | `ff01fcd439b482d752f5766d6560faad819e113bc5719b142fd18137b63f5b91` | match |

## Rejection findings

### P0 — Live M0 implementation authority remains asserted

The patch adds correct exhausted-receipt language, but it does not remove several semantically direct authorization claims:

- `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md:9` retains canonical frontmatter `authority_state: owner-aligned-m0-m2-program; local-fixture-m0-authorized`.
- The same plan says “the current M0 start receipt” at `:21` and refers to “the current M0 implementation authority” at `:38`, despite `:20` saying the prior receipt is exhausted and no implementation is authorized.
- `final-architecture-spec.md:38` states: “The currently executable scope is a local fixture-backed M0 MVP.”
- The specification closes at `final-architecture-spec.md:1002` with: “The current implementation authority is limited to the local fixture-backed M0 MVP.” This directly contradicts its corrected scope at `:5` and milestone text at `:890,940`.
- `implementation-sequencing.md:203` still refers to “the current fixture-backed M0 implementation authority,” and `:553` still says “The current fixture-backed M0 start receipt.” These contradict `:51,261,538,650`, which state that no qualifying receipt is live.

**Consequence:** an implementer can cite canonical metadata, the architecture outcome section, the architecture closing statement, or the sequencing halt contract as current authority to start fixture-backed M0 work. Exact-phrase tests missed these semantic variants.

**Minimal correction:** replace the listed live-authority phrases with one consistent state: the prior receipt is exhausted; the next fixture-backed M0 slice is planned only; `M0-F1`-`M0-F5` require a new exact-digest Owner authorization and bounded receipt. Update the CE-plan `authority_state` itself, not only its prose.

### P1 — Check 14 is not represented only by a replaceable seam

The packet correctly marks Check 14 pending and permits only a replaceable receipt seam (`m0-m2-build-alignment-packet.md:103,110`). The candidate architecture still labels a fixed “Current M0 fixtures” set at `final-architecture-spec.md:793` and includes “Primary-source versus independent-recomputation disagreement” at `:798`. The evaluation plan also retains “independent numeric recomputability” as an unqualified required measurement at `eval-acceptance-plan.md:148`.

Those statements conflict with the candidate's own pending language at `final-architecture-spec.md:77,271,856,890` and `eval-acceptance-plan.md:10,218-220`, which says the Owner/Fable ruling is unresolved and only a replaceable candidate-recomputation seam may exist.

**Consequence:** a builder or evaluator can treat the independent-recomputation architecture and fixture as settled, then claim Check 14 conformance before the Owner/Fable ruling.

**Minimal correction:** change the architecture fixture to a planned candidate-recomputation disagreement exercised only through the replaceable seam, explicitly non-conformant until the ruling; qualify the evaluation measurement the same way. Do not choose the independent-recomputation topology in this patch.

## Eight-area verification matrix

| # | Required verification | Result | Evidence |
| --- | --- | --- | --- |
| 1 | D1, D2, and D3 propagate without a new Owner decision | **PASS** | D1 closed rule and failure branches appear in packet `:45,108,116`, spec `:271-272,469`, plan `:32,34,198`, sequencing `:56,58`, and evaluation `:212-215`. D2 preserves `MISSING`, material fail-closed behavior, versioned N/A, and divergence `FAIL`. D3 stores only `analysis_use` and derives non-settable eligibility in all five documents. |
| 2 | No wording claims the exhausted receipt still authorizes work | **FAIL** | CE plan `:9,21,38`; architecture spec `:38,1002`; sequencing `:203,553`. |
| 3 | All 26 active packet `VAL-*` IDs map exactly once | **PASS** | Packet registry: 26 unique IDs. Authoritative sequencing registry: 26 rows / 26 unique IDs. Exact set match; missing `[]`; extra `[]`; mapping duplicates `[]`. Repeated scenario references in the packet are not ownership rows. |
| 4 | B3, M18, M19, and M20 remain explicitly open | **PASS** | CE plan `:335,339-341` labels all four open and retains their required external or implementation evidence. No closure or authorization claim was found elsewhere in the candidate. |
| 5 | Check 14 remains pending and only a replaceable seam exists | **FAIL** | Pending/seam language exists, but spec `:793-798` still declares a current independent-recomputation fixture and evaluation `:148` retains an unqualified independent-recomputability measurement. |
| 6 | Historical `2f1001...` is not a verified current binding | **PASS** | Exact occurrence count across the five disposable candidate files: `0`. No replacement aggregate is represented as current truth. |
| 7 | No silent M0-F1-F5, production, M1/M2, mutation, deployment, or Committee authorization | **FAIL** | Production, M1/M2, mutation, deployment, and Committee boundaries remain closed, but the stale M0 authority claims listed above violate the all-authority condition. |
| 8 | Cross-document terms and readiness projections are coherent | **FAIL** | D1-D3 projections are coherent; authority state and Check-14 status are internally contradictory at the exact anchors above. |

## `VAL-*` exact-set result

The 26 unique active IDs in the packet exactly equal the 26 unique rows in the authoritative sequencing registry. The registry has no duplicate ownership row, missing ID, or extra ID. The four planned M1/M2 IDs remain outside M0 ownership: `VAL-M1-001`, `VAL-M1-002`, `VAL-M2-001`, and `VAL-M2-002` map to later `U8`, with their separate start and production/replay gates still open.

## Preserved non-authorizations

- B3, M18, M19, and M20 remain open.
- Check 14 remains an Owner/Fable decision despite the contradictory fixed fixture identified above.
- The historical Phase A aggregate beginning `2f1001` is not present in the candidate.
- P2, P3, P4, production access, M1/M2 implementation, mutation, commit, push, PR, deployment, rollback, publication, and Committee Acceptance remain ungranted.
- No Phase A artifact, patch, canonical document, prior review artifact, code, test, fixture, or Git state was modified by this review.

## Next lawful step

Prepare a superseding unapplied patch against the same live base that removes every stale M0-authority assertion and reduces all Check-14 fixtures/measurements to an explicitly replaceable, non-conformant seam pending the Owner/Fable ruling. Then repeat exact-digest disposable-copy review. Only after an advisory candidate passes may the Owner consider canonical writeback; writeback still would not authorize `M0-F1`-`M0-F5`.

This bounded run stops after writing this report and its status JSON.
