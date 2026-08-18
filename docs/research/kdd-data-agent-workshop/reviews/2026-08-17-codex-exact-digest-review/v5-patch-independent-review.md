# Independent Exact-Byte Review — Candidate Canonical Writeback v5

Date: 2026-08-18

Handoff: `kdd-m0-canonical-candidate-v5-independent-review-20260818`

Verdict: **`REJECT_CANDIDATE`**

## Review boundary

This was one fresh, bounded, report-only review. I did not read the author task conversation, start another reviewer or model, modify the patch or any live target, touch Phase A or prior review artifacts, alter Git state, create a freeze/start receipt, or start `M0-F1`–`M0-F5`.

The exact patch was applied only under the fresh disposable root:

`/private/tmp/kdd-v5-independent-review.Z3mxOK`

The repository remained on branch `codex/kdd-data-agent-practices-research` at HEAD `28cbbda6e4d4d7f08134952d38433e52d3ee8768`.

## Exact-byte binding

Patch SHA-256:

`a2844d700c997f445532dad32807a5239e02f61ce9b080a555d00d46a085e03a`

The patch contains 268 insertions and 147 deletions across exactly seven targets.

| Target | Live input SHA-256 | Disposable post-apply SHA-256 |
| --- | --- | --- |
| `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | `52ce2763a365eb35ea884dfbc7f19b8b3d012b85edac544a21b356638126499c` | `e82779674e14013ed656d862877e7b2778b50fbd366f63960698d97e60ee19df` |
| `docs/research/kdd-data-agent-workshop/enterprise-experiment-post-analysis-profile.md` | `3da58196296c3eb164a598a67750e1d57bbc5936176edde2d743917b48d7f663` | `9a5823d02aa4d26f5fe472f0f90f2c07bc378d4ea745145f7494f749710cf77e` |
| `docs/research/kdd-data-agent-workshop/eval-acceptance-plan.md` | `5dce10ca451f7ccbbf5d86896cefed2b8dd8a5b5cae480da4d3ea030d5603194` | `2d4612e319e7c8dce209eeaee228638ec0abf69a0ee70a01697c30b96b40e965` |
| `docs/research/kdd-data-agent-workshop/final-architecture-spec.md` | `3b20c93859b78074b653d375fc29f60bd40993b3f3bcb4ee2ff481e8ba8706b8` | `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` |
| `docs/research/kdd-data-agent-workshop/implementation-sequencing.md` | `1d42e67c0ba5e2a1799960a3e151b12fa847a419f13b7a9f63362366dc3a29ee` | `5b71ac04d58201f36acef3bc39443e00b348fb794ea4b131d19d206eb7529a22` |
| `docs/research/kdd-data-agent-workshop/planning-decision-packet.md` | `7e68ad675b988f2dfc3f53cf13e6e5e4bbd24194ce896c38df395e62b06bd37c` | `1ba07b2587a491a3c6e3e45a3b9af2ef7f701f0de32674a74d2bcac6a8109497` |
| `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `67c844d10dcafcf2637388bf579dfcd9866d7d69ea6f4d3b456fd6b6b15dfcfa` | `9ab5097e31f3cd47fd6dc194a19aaa9af5ecf11fb18a7210bcbe523fca5e3761` |

All live inputs and all post-apply digests reproduce the Round 5 claims exactly. Both live and disposable `git apply --check --whitespace=error-all` succeeded without fuzz or whitespace errors.

## Rejecting findings

### V5-01 — The controlling alignment packet still forbids the blocked-Flight M1 investigation that S10 explicitly permits

- Exact disposable anchors:
  - `/private/tmp/kdd-v5-independent-review.Z3mxOK/docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md:29`
  - `/private/tmp/kdd-v5-independent-review.Z3mxOK/docs/research/kdd-data-agent-workshop/implementation-sequencing.md:72`
- Contradictory contract in the same disposable document: `/private/tmp/kdd-v5-independent-review.Z3mxOK/docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md:170`.
- Impact: line 29 says “M1 cannot start for a blocked Flight,” and the sequencing diagram requires “M0 pass” before M1. S10 instead permits M1 investigation for a correctly blocked real Flight under separate authority, with dependent claims capped by the applicable publication ceiling. The same alignment packet correctly states that rule at line 170. The candidate therefore weakens S10 and leaves the controlling documents internally contradictory, failing checks 1 and 12.
- Minimal correction: replace the absolute blocked-Flight prohibition with the S10 rule already used at line 170, and change the sequencing edge from “M0 pass” to a packet/authority/publication-ceiling condition that permits investigation while prohibiting causal promotion from failed or missing M0 evidence.

### V5-02 — The CE unified-plan frontmatter uses an undefined `artifact_readiness` value

- Exact disposable anchor: `/private/tmp/kdd-v5-independent-review.Z3mxOK/docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md:6`.
- Impact: the document declares `artifact_contract: ce-unified-plan/v1` but changes `artifact_readiness` to `planning-only-awaiting-exact-digest-start-receipt`. The unified-plan contract recognizes `requirements-only` and `implementation-ready`; execution/authorization is a separate dimension. This undefined value prevents deterministic document classification and can cause CE plan/review tooling to reject or misroute the canonical plan. Therefore the declared mechanical/document contract does not reproduce, failing check 14.
- Minimal correction: restore `artifact_readiness: implementation-ready` because the document contains the Planning Contract, implementation units, verification contract, and Definition of Done. Preserve the exhausted-receipt and no-current-authority facts in the existing `execution`, `authority_state`, Readiness, and Stop Conditions fields.

## Fourteen-check result

| # | Result | Independent evidence |
| --- | --- | --- |
| 1 | **FAIL** | D1–D8 and S1–S11 are substantially encoded, including preregistered sufficiency, parity, one stored readiness state, recomputation independence, clean-room fixtures, shared snapshot, fixed core floor, and D8. V5-01 nevertheless contradicts S10. |
| 2 | **PASS** | Disposable alignment packet lines 181–183 define an append-only, non-binding `FlightAdvisoryRevision` and separate it from Cause Verdict, Recommendation Readiness, Action Approval, and Incident State. |
| 3 | **PASS** | Alignment packet line 183 and evaluation plan lines 240–243 preserve selection timing/history and require independent confirmation before post-unblinding evidence can carry change/block; otherwise the state is `insufficient_evidence` with `urgent_investigation`. |
| 4 | **PASS** | Alignment packet lines 162–166 and evaluation plan line 224 keep program `m0_capability_state` separate from per-Flight `analysis_use`; a correctly blocked Flight can demonstrate capability only after real production execution and independent adjudication and remains non-decision-grade. |
| 5 | **PASS** | Alignment packet line 185 and evaluation plan lines 244–246 make `candidate_diff_eligibility` independent of advisory publication, require M2 for user-visible semantics, narrowly version N/A, and fail closed for HIGH risk or large blast radius. |
| 6 | **PASS** | Alignment packet lines 70 and 181–185 plus evaluation plan lines 240–245 cover the Query Success union/components, no-hidden-guardrail rule, challenge lineage, blind-rubric boundary, `query_evidence_state`, falsifier execution state, and supersession. |
| 7 | **PASS** | Alignment packet lines 75, 81, 106, 113–115, 145–146 and 166 cover `evidence_class`, sealed fixed-floor core checks, typed production bindings, Check-14/shared-snapshot semantics, and the laptop export/redaction manifest. |
| 8 | **PASS** | Alignment packet line 80 and architecture specification line 174 keep authorization/redaction orthogonal and require an explicit versioned Coverage Gap policy registry. |
| 9 | **PASS** | Alignment packet line 164 separates fixture evidence, program capability, Flight decision-grade status, P2/production authorization, launch approval, and Committee Acceptance. |
| 10 | **PASS** | Production definitions, sources, schemas, owners, thresholds, timers, retention, credentials, and rulings remain typed bindings or named gates; no invented production value or Committee decision was found. |
| 11 | **PASS** | The CE plan's Phase A evidence ceiling records `PASS_WITH_GAPS`, names the implementation-only controls, and denies M0 acceptance, production capability, and policy closure from Phase A evidence. |
| 12 | **FAIL** | The mechanical registry check found 26 unique `VAL-*` owners and 26 referenced IDs with no duplicates or unowned references, but V5-01 leaves controlling M1/blocked-Flight terminology contradictory. |
| 13 | **PASS** | The post-apply documents repeatedly state that no start receipt is live and grant no implementation, production, mutation, Git, deployment, messaging, publication, or Committee authority. |
| 14 | **FAIL** | Exact apply, post-apply digests, whitespace, seven-target scope, 26-ID ownership, and all local Markdown file links reproduced. V5-02 breaks the declared `ce-unified-plan/v1` metadata contract. |

## Mechanical verification and invariance

- `git apply --check --whitespace=error-all` succeeded against the live targets and again in the fresh disposable copy.
- All seven post-apply SHA-256 values match the Round 5 status exactly.
- Local Markdown file-link resolution found zero missing targets when resolved against the live repository.
- The authoritative acceptance registry has 26 rows, 26 unique owned IDs, and zero unowned touched-document references.
- Patch, Round 5 disposition/status, steelman records, architecture ledger, Fable review, and Phase A review digests were unchanged after review.
- Live target digests, branch, HEAD, index, and unrelated dirty-worktree state were unchanged. The only repository writes from this run are this report and its required status JSON.

## Disposition

The exact v5 patch is mechanically reproducible but is not a safe candidate for Owner writeback review because it retains a direct S10 contradiction and introduces invalid unified-plan metadata. Correct only those defects in a superseding exact patch, then run a new independent exact-byte review. This report grants no writeback, freeze, implementation, production, Git, deployment, or Committee authority.
