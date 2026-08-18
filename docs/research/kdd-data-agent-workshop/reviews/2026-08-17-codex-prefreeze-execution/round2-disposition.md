# Round 2 Codex Disposition

Date: 2026-08-17  
Handoff: `kdd-m0-prefreeze-execution-round2-20260817`  
Branch / HEAD observed: `codex/kdd-data-agent-practices-research` / `28cbbda6e4d4d7f08134952d38433e52d3ee8768`

## Disposition

**BOUNDED FOLLOW-UP COMPLETE — UNAPPLIED CANDIDATE ONLY.**

`candidate-canonical-writeback-v2.patch` supersedes the Round 1 candidate for review purposes. It is a patch against the unchanged live canonical bytes; it has not been applied to the repository. It is not a freeze, Owner authorization, Opus/Fable approval, Phase A verdict, P2/P3/P4 closure, implementation start, production authority, M1/M2 approval, or Committee Acceptance.

## Corrections in v2

The patch preserves the Round 1 D1-D3 corrections and closes the two Round 2 advisory classes:

1. All identified stale assertions that the exhausted Phase A/continuation authority remains live are replaced. The packet, architecture specification, CE plan, sequencing, and evaluation plan now state that the prior `m0-codex-continuation-20260817` authorization is exhausted and that `M0-F1`-`M0-F5` require a new exact-digest Owner authorization and bounded start receipt. The receipt must bind the accepted packet path, revision, SHA-256, active-time cap, run/read/tool cap, expiry, and halt owner.
2. `implementation-sequencing.md` now contains the single authoritative ownership registry for all 26 active packet `VAL-*` IDs. Every ID has exactly one owner: one `M0-F*` unit, later `U*` unit, or explicit external gate. Every row names its proving test/receipt or open-gate evidence. The packet references that registry and retains only scenario meanings.
3. The four packet-only planned IDs remain outside M0 ownership: `VAL-M1-001` and `VAL-M1-002` map to later `U8`; `VAL-M2-001` and `VAL-M2-002` map to later `U8` with their separate M2 start/replay authority still open.
4. Check 14 remains explicitly pending an Owner/Fable architecture ruling. The candidate introduces only a replaceable recomputation receipt seam and forbids any claim that the open independent-recomputation question has been resolved by implementation convention.

## Preserved Owner decisions

- **D1:** exactly `runtime_only | runtime_and_sample`; preregistered inputs only; no post-hoc or achieved power; versioned `NOT_APPLICABLE` under `runtime_only`; missing declared sample inputs are `MISSING`, `blocked + not_permitted`, and `contract_correction`.
- **D2:** missing required arm-parity evidence is material `MISSING`, `blocked + not_permitted`, and `evidence_collection`; `NOT_APPLICABLE` requires a versioned rule; applicable divergence is material `FAIL`.
- **D3:** only `analysis_use` is stored; `post_analysis_eligibility` is a non-settable render-time derivation.

## Open actions preserved

- **B3 remains open:** a per-asset reuse inventory and its interface, provenance, test, security, license, source, owner, and access evidence are required before direct reuse or `M0-F1`.
- **M18 remains open:** the affected external-sharing/security inventory must close before external distribution.
- **M19 remains open:** employee-endpoint collection stays off absent separate privacy/labor and query-authority receipts.
- **M20 remains open:** the required capture/pin predicate and fail-closed unsupported-host behavior still require implementation proof before dependent publication.
- **Check 14 remains open:** Owner/Fable must decide the independent-recomputation architecture.

## Digest-contract mismatch

The historical Phase A aggregate beginning `2f1001` is not recorded as current observed truth. The prior receipts' aggregate command is not reproducible as a current binding algorithm. The future start-handoff aggregate or manifest value remains unresolved pending Opus Q11/Q12 and a newly specified exact manifest algorithm. No `2f1001` value appears in the candidate canonical bytes.

## Exact input binding

| Live input | SHA-256 before and after this run |
| --- | --- |
| `reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `67c844d10dcafcf2637388bf579dfcd9866d7d69ea6f4d3b456fd6b6b15dfcfa` |
| `final-architecture-spec.md` | `3b20c93859b78074b653d375fc29f60bd40993b3f3bcb4ee2ff481e8ba8706b8` |
| `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | `52ce2763a365eb35ea884dfbc7f19b8b3d012b85edac544a21b356638126499c` |
| `implementation-sequencing.md` | `1d42e67c0ba5e2a1799960a3e151b12fa847a419f13b7a9f63362366dc3a29ee` |
| `eval-acceptance-plan.md` | `5dce10ca451f7ccbbf5d86896cefed2b8dd8a5b5cae480da4d3ea030d5603194` |

Round 1 artifacts were also preserved. The Round 1 patch remains `6c17123aacfff7d1c867f3fee33d9873cf3d13195b89328b846b67f2cc309845`; no Round 1 file was edited.

## Verification evidence

- `git apply --check --whitespace=error-all`: **PASS** against the unchanged live bytes.
- Disposable-copy application: **PASS**.
- Patch file: 580 lines; 5 patched files; 126 insertions and 88 deletions.
- Active-ID proof: **PASS** — packet registry 26 IDs / 26 unique; authoritative mapping 26 rows / 26 unique; exact set match; no missing, extra, or duplicate ID.
- Stale-authority proof: **PASS** — zero occurrences of the eight exact stale live-authorization phrases identified from the advisory anchors.
- Check-14 proof: **PASS** — the patched packet, architecture specification, CE plan, sequencing, and evaluation plan preserve the pending Owner/Fable state.
- Historical aggregate proof: **PASS** — no `2f1001` occurrence in the patched canonical candidate.
- Canonical/live input digests: **UNCHANGED**.
- Product tests: not run; this bounded task produced review-only documents and prohibited product, test, and fixture changes.

## Post-apply digest manifest

| Candidate file after disposable application | SHA-256 |
| --- | --- |
| `reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `74d77bbb4fce84099d951c58f2f55cf695c3e9ffccb713e929e330e068ffd264` |
| `final-architecture-spec.md` | `04285c0eb0a008f573a5c8b872ca7b184182413ea3b7b7dfa356cd2c7b0d09fa` |
| `implementation-sequencing.md` | `ae8f935b24af65ef90b1a1a5e2d01e38c08bcb9dac1f6310f30c33151596e946` |
| `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | `da78980c2a1d5204c14e9f8ff824e60bd775cd12a0dcd604d813433c89e9d9d9` |
| `eval-acceptance-plan.md` | `ff01fcd439b482d752f5766d6560faad819e113bc5719b142fd18137b63f5b91` |

## Next lawful step

Independent reviewers must evaluate these exact candidate bytes. Owner/Fable must resolve check 14, Opus Q11/Q12 must resolve the future Phase A digest/manifest contract, and the Owner must issue a new exact-digest bounded start receipt before any `M0-F1`-`M0-F5` implementation begins. This bounded Round 2 run stops here.
