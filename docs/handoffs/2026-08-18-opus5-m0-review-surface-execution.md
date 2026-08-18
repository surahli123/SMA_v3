---
handoff_id: opus5-m0-review-surface-20260818
created_at: 2026-08-18T14:33:32-07:00
source_thread: 019ff3f9-ee51-7e32-937a-85fd9be2226a
target_thread: Claude Code Opus 5 max-effort implementation session
status_path: /private/tmp/SMA_v3-opus-m0/docs/reviews/2026-08-18-m0-flight-readiness-review-surface/status.json
expires_at: after one Claude Code execution run or 2026-08-19T02:33:32-07:00, whichever occurs first
---

# Cross-Thread Handoff: Build the Fixture-Only M0 Flight Readiness Review Surface

## Current Blocker

The fixture-backed M0 evaluator and its synthetic `VAL-UI-001` projection are independently accepted, but the repository does not yet contain a polished packet-centered review artifact for an Owner/reviewer to inspect. P3 live interaction acceptance remains open and must not be implied.

## Whole Goal and Current Slice

- **Whole goal:** deploy an enterprise Data Agent that produces an auditable `FlightReadinessPacket`, then continues through separately authorized M1 and M2 analysis for one A/B Flight.
- **Current slice:** implement only a dependency-free, fixture-only, read-only, pre-P3 M0 Flight Readiness review surface. This is a local review artifact and mechanical projection proof, not a production adapter, causal analysis, recommendation engine, final UI contract, or Committee workflow.

## Exact Input Bindings

Recompute these before and after semantic work. Halt on any mismatch.

| Role | Path | Revision | SHA-256 |
| --- | --- | --- | --- |
| M0 build contract | `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `m0-alignment-v1` | `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` |
| Architecture | `docs/research/kdd-data-agent-workshop/final-architecture-spec.md` | `kdd-data-agent-architecture-v1` | `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` |
| CE plan | `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | observed supporting plan | `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` |
| Sequencing | `docs/research/kdd-data-agent-workshop/implementation-sequencing.md` | observed supporting sequence | `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` |
| Accepted M0 package | `.agents/skills/kdd_data_agent/` over the accepted 59-file aggregate definition | `ACCEPT_LOCAL_M0_EVIDENCE` | `9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a` |

Read these first:

1. `README.md`
2. `PROVENANCE.md`
3. `docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-canonical-freeze/m0-canonical-freeze-record.md`
4. the four exact-bound inputs above
5. `.agents/skills/kdd_data_agent/tests/test_m0_review_projection.py`
6. `.agents/skills/kdd_data_agent/m0/packet.py`, especially `synthetic_review_projection`
7. `docs/research/kdd-data-agent-workshop/prototypes/observability-review-surface/owner-selected-design-contract.md`
8. `docs/research/kdd-data-agent-workshop/prototypes/observability-review-surface/award-ui-narrative-contract.md`
9. the owner-selected screenshots under `docs/research/kdd-data-agent-workshop/prototypes/observability-review-surface/reference-assets/owner-selected-iteration/`
10. `docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/deliverable-alignment-review.md`

## Ownership

You own only:

- `prototypes/m0-flight-readiness-review/**`
- `docs/reviews/2026-08-18-m0-flight-readiness-review-surface/**`

Do not edit `.agents/skills/kdd_data_agent/**`, canonical architecture/planning/research files, repository publication files, or any other path. Other workers may be active; do not revert or overwrite their changes.

## Product Contract

Build a static, dependency-free artifact that renders synthetic fixture-class packet projections. It must make these facts clear without requiring explanation outside the artifact:

1. Flight identity and evidence class.
2. Stored `analysis_use` and separately labelled derived `post_analysis_eligibility`.
3. Typed `next_safe_action` and reopen condition.
4. Ordered material-check summary with outcome, materiality, rule source, evidence IDs, and validator/receipt IDs.
5. Coverage Gaps, disagreements, authorization/redaction state, staleness, invalidation, supersession, and incomplete-state behavior.
6. Exact source-read and D4/D6 independent-recomputation receipts reachable within two read-only interactions.
7. Packet digest, frozen contract revision, core-check-set revision, expiry, and supersession link.
8. Explicit boundaries: fixture-only; no production capability; no cause; no M1/M2 recommendation; no win/loss; no P3 closure; no Committee decision.

Provide at least these local scenarios:

- `decision_grade` trusted fixture;
- `directional_only` pre-runtime/sufficiency fixture;
- `not_permitted` material-invalid fixture;
- unauthorized or redaction-blocked fixture;
- stale/invalidated/superseded fixture;
- incomplete fixture with typed Coverage Gaps.

Any scenario not representable from the accepted package must be labelled a projection fixture and must not be presented as an emitted production packet.

## Interaction and Visual Requirements

- Read-only navigation, filtering, expanding, and inspection only. No action changes packet, verdict, readiness, evidence, or source state.
- The packet decision, why it is limited, and `next_safe_action` form the first-screen hierarchy.
- Every graph-like relationship has an equivalent table/list path; a decorative node cloud is prohibited.
- Trace, if shown at all, is a separate diagnostic cross-link and never evidence authority.
- Use the owner-selected reference assets and design contract as the visual baseline. Preserve their dense analyst-workbench character, restrained palette, explicit hierarchy, and evidence-first interaction.
- Avoid AI-design cliches: no gratuitous gradients, glowing cards, generic chat bubbles, oversized empty hero areas, decorative sparkles, unexplained confidence scores, repeated pill badges, or marketing copy.
- Use semantic HTML, keyboard navigation, visible focus, sufficient contrast, responsive layout, and reduced-motion support.
- Do not copy third-party implementation code or add a dependency without a licence/security decision. Existing screenshots are design evidence, not reusable source code.

## Verification Required

Create an English completion ledger and evidence receipt. At minimum verify:

- clean static build/run from repository root and an unrelated working directory;
- deterministic fixture/render input bytes across at least three `PYTHONHASHSEED` values if Python is used;
- HTML, CSS, JavaScript, and fixture-data mechanical checks without installing dependencies;
- tests for every required first-screen field and prohibited authority claim;
- fail-closed rendering for blocked, stale, unauthorized, invalidated, and incomplete states;
- keyboard-only access to source and D4/D6 receipts within two interactions;
- no network requests, production reads, write/mutation action, secrets, external messages, or source-worktree writes;
- visual evidence at desktop and narrow/mobile widths for trusted, blocked, and invalidated/incomplete states;
- before/after critique against the owner-selected visual contract, including any remaining AI-slop or observability gaps.

The receipt must record all executed commands, exit status, excluded checks, changed files, exact input and output digests, and a final verdict of `COMPLETE_LOCAL_PROTOTYPE`, `PARTIAL_WITH_GAPS`, or `BLOCKED`.

## Stop Conditions

Stop and write `BLOCKED` or `PARTIAL_WITH_GAPS` if:

- any exact-bound input or accepted package aggregate drifts;
- the implementation would require editing the accepted M0 package;
- any semantic choice depends on P2, P3, P4, production data, a real Flight, a Committee ruling, or an unfrozen Owner decision;
- a required check needs network, credentials, production/company data, a new dependency, or access outside the repository and local temporary files;
- a read-only UI control would mutate canonical state or imply an action the Agent is not authorized to perform;
- the one-run cap or expiry is reached.

## Authority and Red Lines

- **Execution cap:** one Claude Code Opus 5 session, maximum effort, one bounded implementation run.
- **Read cap:** repository files and generated local fixture artifacts only; zero production reads.
- **Tool cap:** local read/edit/test/render tools only; no network, package installation, browser sign-in, or external service.
- **Halt owner:** `owner-main-orchestrator`.
- Do not spawn subagents or workflows in this implementation session.
- Do not commit, push, open a PR, deploy, publish, send messages, or modify production/external state.
- Do not start M1/M2, production adapters, P2/P3/P4 closure, Committee actions, or candidate-diff work.
- Do not claim P3, production M0 capability, production authorization, or Committee Acceptance.

## Status Writeback

Write JSON to the `status_path`:

```json
{
  "handoff_id": "opus5-m0-review-surface-20260818",
  "status": "done|blocked|partial",
  "verdict": "COMPLETE_LOCAL_PROTOTYPE|PARTIAL_WITH_GAPS|BLOCKED",
  "summary": "",
  "input_bindings": {},
  "output_digest": "",
  "changed_files": [],
  "verification": [],
  "coverage_gaps": [],
  "next_step": "",
  "updated_at": ""
}
```

## Done When

The bounded artifact, tests, desktop/mobile visual evidence, critique, completion ledger, receipt, and status writeback exist inside the owned paths; all exact-bound inputs still match; the accepted M0 aggregate is unchanged; and the result is ready for a separate independent exact-byte review. No broader gate is implied.
