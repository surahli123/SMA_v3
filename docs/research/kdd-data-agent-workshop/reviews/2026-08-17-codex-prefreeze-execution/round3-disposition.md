# Round 3 Codex Disposition

Date: 2026-08-17  
Handoff: `kdd-m0-prefreeze-execution-round3-20260817`  
Branch / HEAD observed: `codex/kdd-data-agent-practices-research` / `28cbbda6e4d4d7f08134952d38433e52d3ee8768`

## Disposition

**BOUNDED ROUND 3 COMPLETE — UNAPPLIED CANDIDATE ONLY.**

`candidate-canonical-writeback-v3.patch` supersedes the rejected Round 2 candidate for review purposes. It is generated against the same unchanged five live canonical inputs and has not been applied to the repository. It is not a freeze, Owner approval, Opus/Fable verdict, Phase A acceptance, implementation start, production authority, P2/P3/P4 closure, M1/M2 approval, or Committee Acceptance.

## Round 3 corrections

The v3 candidate preserves the accepted Round 2 D1-D3 propagation, complete 26-ID ownership registry, open-gate states, and digest boundary. It additionally closes the two independent-review rejection classes:

1. **No live fixture-backed M0 authority remains.** The CE plan frontmatter is now planning-only, `execution` is disabled until a new receipt, and `authority_state` records the exhausted prior continuation and a planned-not-authorized local slice. All remaining “current start receipt,” “current implementation authority,” “currently executable,” current-fixture headings, milestone labels, package-boundary labels, and equivalent sequencing/specification variants were replaced. Every document now applies one rule: the prior continuation receipt is exhausted; the next local fixture-backed M0 slice is planned only; `M0-F1`-`M0-F5` require a new exact-digest Owner authorization and bounded start receipt.
2. **Check 14 is only a pending seam.** Every affected fixture, measurement, acceptance, projection, contract, and registry reference now describes only a replaceable, explicitly non-conformant candidate-recomputation seam. It cannot yield a check-14 pass, fail, materiality ruling, readiness transition, measurement, score, or conformance claim before the Owner/Fable ruling is digest-bound.
3. **No topology was selected.** The candidate explicitly leaves the Owner/Fable choice between source- and transform-independence models open and forbids implementation convention from resolving it.

## Preserved contracts and open actions

- **D1 preserved:** exactly `runtime_only | runtime_and_sample`; preregistered inputs only; no post-hoc or achieved power; exact N/A and missing-input branches.
- **D2 preserved:** missing arm-parity evidence is material `MISSING`, `blocked + not_permitted`, and `evidence_collection`; N/A requires a versioned rule; applicable divergence is material `FAIL`.
- **D3 preserved:** only `analysis_use` is stored; `post_analysis_eligibility` is a non-settable render-time derivation.
- **26-ID registry preserved:** all 26 active packet `VAL-*` IDs map exactly once to one `M0-F*`, later `U*`, or explicit external gate with proving evidence.
- **B3, M18, M19, and M20 remain explicitly open.**
- The historical Phase A aggregate beginning `2f1001` is absent from candidate canonical bytes and is not current verified truth. The future start binding remains unresolved pending Opus Q11/Q12 and an exact manifest algorithm.

## Exact live input binding

| Live input | SHA-256 before and after Round 3 |
| --- | --- |
| `reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `67c844d10dcafcf2637388bf579dfcd9866d7d69ea6f4d3b456fd6b6b15dfcfa` |
| `final-architecture-spec.md` | `3b20c93859b78074b653d375fc29f60bd40993b3f3bcb4ee2ff481e8ba8706b8` |
| `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | `52ce2763a365eb35ea884dfbc7f19b8b3d012b85edac544a21b356638126499c` |
| `implementation-sequencing.md` | `1d42e67c0ba5e2a1799960a3e151b12fa847a419f13b7a9f63362366dc3a29ee` |
| `eval-acceptance-plan.md` | `5dce10ca451f7ccbbf5d86896cefed2b8dd8a5b5cae480da4d3ea030d5603194` |

Prior artifacts remain unchanged. In particular, the v2 patch remains `54b386f12d0fc9fc80dbc263404db1bcc7796f030fddddb5fda53c827602286b`, the Round 2 disposition remains `c96904583b0ba836691cf77046aaa2499d376deb9140d79f16a4112067193d1d`, and `status-round2.json` remains `b2192c1cefc26ae751f1019e330c918733fcef95fa2807dc5cfb481755e1f51f`.

## Verification evidence

- `git apply --check --whitespace=error-all` against unchanged live bytes: **PASS**.
- Fresh disposable-copy application with `--whitespace=error-all`: **PASS**.
- Patch shape: 804 lines; 5 patched files; 167 insertions and 125 deletions.
- D1-D3 mechanical presence across all five post-apply documents: **PASS**.
- Active `VAL-*` proof: packet 26 unique IDs; authoritative mapping 26 unique rows; exact set match; no missing, extra, or duplicate ID: **PASS**.
- Semantic stale-authority scan: all independently identified phrases plus broader current-M0/current-fixture semantic variants absent: **PASS**.
- Check-14 scan: every post-apply document contains Owner/Fable pending state, candidate-recomputation seam, and explicit non-conformance; banned settled-fixture/measurement variants absent: **PASS**.
- B3/M18/M19/M20 explicit open-state scan: **PASS**.
- `2f1001` occurrence count across candidate canonical bytes: **0**.
- Live canonical and prior-artifact digests: **UNCHANGED**.
- Product tests were not run because this bounded task prohibited product, Phase A, test, and fixture changes and did not start an implementation unit.

## Disposable post-apply digest manifest

| Candidate file after fresh disposable application | SHA-256 |
| --- | --- |
| `reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `4b3c5293a79536f2a75f7070d4de700a21c507a5e6eb86058357f183f559affc` |
| `final-architecture-spec.md` | `75bf5f12463e7c686e2bae737754b9437d54600e870b67d634ddadbe93d87507` |
| `implementation-sequencing.md` | `311a4a4aa781029253f764847189b817e9a05d973ce9245035b00001f12bc109` |
| `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | `e8b97b9224c39bbfd2ee1ec25059556febc0cc529e95e4244e6a338c3366b6c4` |
| `eval-acceptance-plan.md` | `2785fc7f9eab6c20dd030b1b6ab9c0f89a768a2163b52e3884b27fd8db535516` |

## Next lawful step

Independently review the exact v3 patch and its post-apply digests. A passing advisory review would still not authorize canonical writeback or implementation. Owner/Fable must resolve Check 14, Opus Q11/Q12 must resolve the future Phase A digest contract, and the Owner must issue a new exact-digest bounded start receipt before `M0-F1`-`M0-F5`. This bounded run stops after the required status writeback.
