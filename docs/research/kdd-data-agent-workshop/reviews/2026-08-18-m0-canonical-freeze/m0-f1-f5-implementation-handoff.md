---
handoff_id: kdd-m0-f1-f5-local-build-20260818-r1
status: AUTHORIZED_ONE_RUN
scope: one bounded local hermetic M0-F1-F5 run
expires_at: 2026-08-18T08:00:00-07:00-or-first-terminal-result
---

# M0-F1 through M0-F5 Implementation Handoff

## Goal and proof boundary

Complete the fixture-backed local M0 Flight Readiness MVP against the exact frozen packet and architecture bytes below. First close the material Phase A implementation gaps, then implement M0-F1 through M0-F5 and return independent-review-ready evidence.

This run may establish `COMPLETE_LOCAL_M0_EVIDENCE`. It cannot establish production-backed M0 capability, production authorization, M1/M2 completion, deployment authority, or Committee Acceptance.

## Exact binding

| Role | Path | Revision label | SHA-256 |
| --- | --- | --- | --- |
| Packet | `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md` | `m0-alignment-v1` | `sha256:82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` |
| Architecture | `docs/research/kdd-data-agent-workshop/final-architecture-spec.md` | `kdd-data-agent-architecture-v1` | `sha256:9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` |
| CE plan observed at start | `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | `ce-unified-plan/v1` | `sha256:2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` |
| Sequencing observed at start | `docs/research/kdd-data-agent-workshop/implementation-sequencing.md` | `m0-m2-sequencing-v1` | `sha256:8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` |
| Phase A input aggregate | `.agents/skills/kdd_data_agent/` | `phase-a-pass-with-gaps-20260818` | `sha256:2f1001b93b19b2318c4c6419205ed2f7778ac23c02533e78a0c0899f15bf7d1e` |

Freeze record: `docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-canonical-freeze/m0-canonical-freeze-record.md`.

Changing either frozen packet/spec byte halts the run. The Phase A aggregate is an input receipt, not an expected final package digest.

## Owner authorization and budget

- Owner acknowledgement: main-orchestrator closure on `2026-08-18`, authorizing the reviewed reconciliation, M0 prototype, independent verification, packaging, commit, and push sequence.
- Implementation lead: Codex Sol medium or an equivalent Codex continuation explicitly bound to this handoff.
- Active implementation cap: four hours.
- Expiry: `2026-08-18T08:00:00-07:00` or the first terminal result, whichever occurs first.
- Full-suite invocation cap: 12.
- Production source-read cap: 0. Fixture reads are allowed only through the fixture adapter and hermetic tests.
- Tool-call cap: 240 for this implementation run.
- Halt owner: the main orchestrator; the Owner may halt at any time.
- Partial-result root: `docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-f1-f5-execution/`.

Missing or exceeded budget fields do not renew themselves. Stop with `PARTIAL_HALTED` and preserve exact evidence.

## File ownership

The implementation task owns only:

- `.agents/skills/kdd_data_agent/**`; and
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-f1-f5-execution/**`.

It must not edit the frozen packet/spec, other planning or research documents, `.agents/skills/sma/**`, `.agents/skills/sma_rewrite/evals/**`, Git configuration, unrelated user files, or external systems. It is not alone in the worktree and must preserve all concurrent/user-owned changes.

## Required Phase A corrections before semantic completion

Close every BLOCKER and MAJOR from the independent Phase A report, or stop with exact evidence. At minimum:

1. Require registry-resolving versioned materiality/applicability rule sources; empty, whitespace, arbitrary, or wrong-type values fail closed.
2. Add golden receipt/run vectors and mutation coverage so every receipt-identity field is test-reachable.
3. Add fail-open and malformed authorization parser tests.
4. Keep authorization and redaction as orthogonal typed axes.
5. Replace accidental `CoverageGapKind` enum authority with an explicit versioned registry; do not invent unapproved kinds.
6. Repoint every seam and comment to current headings and sole-owner `VAL-*` IDs, and mechanically test those references.
7. Wire seal/predecessor-chain verification and lock it with mutations.
8. Close relative-import, symlink-directory, scanner non-vacuity, fixture-containment, duplicate-receipt, and body-policy reachability gaps.

The independent report at `docs/research/kdd-data-agent-workshop/reviews/2026-08-17-phase-a-independent-verification/phase-a-independent-review.md` is the finding authority for this correction set.

## M0-F1 through M0-F5 deliverables

- **M0-F1:** exact typed `ExperimentReadContract`, one stored `analysis_use`, derived eligibility, declared sufficiency, arm parity, materiality, typed next action, immutable packet envelope, and exact frozen binding.
- **M0-F2:** fixture-only reads, typed outcomes, no-false-Evidence behavior, D4/D6 independent recomputation receipts, append-only isolation, and orthogonal authorization/redaction.
- **M0-F3:** all nineteen deterministic checks with fixed-floor sealing, rule sources, fail-closed mappings, Query Success union/component integrity, and byte-stable reproduction.
- **M0-F4:** immutable fixture-class `FlightReadinessPacket` plus a synthetic packet-centered projection; no M1/M2 object, causal conclusion, product-logic candidate, Win/Loss label, or automation-consumable diff.
- **M0-F5:** threshold-free fixtures, always-ready/always-blocked baselines, adversarial decoys, fixture-author/reviewer conflict receipts, and hard vetoes for false readiness, leakage, unsafe redaction, write reachability, or unauthorized delivery.

Use `docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/m0-f1-f5-completion-ledger.md` as the minimum acceptance ledger. Copy its rows into the execution receipt and mark each with observable evidence; do not edit historical ledger rows in place.

## Allowed verification

- `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider .agents/skills/kdd_data_agent/tests -q`
- The same suite from the package root and from a clean `/private/tmp` working directory with explicit `PYTHONPATH`.
- Fresh-process deterministic probes over identical frozen inputs and multiple `PYTHONHASHSEED` values.
- Isolated fault-injection/mutation copies under a fresh `/private/tmp` root.
- Static capability/import scanning and runtime audit of the exercised hermetic path.

No network, dependency installation, production adapter, secret, credential, subprocess workflow, external message, deployment, or Git mutation is authorized.

## Halt conditions

Stop immediately if:

- any frozen digest drifts;
- implementation requires inventing product meaning or a production binding;
- a fail-closed default, closed registry, derived readiness rule, or materiality ceiling can be bypassed;
- production/network/write/external-delivery capability becomes reachable;
- identical frozen inputs produce different bytes or digests;
- a required invalid/directional/decision-grade fixture cannot reach its declared state;
- the budget or expiry is exceeded; or
- the task crosses into production, M1/M2, P2/P3/P4 closure, deployment, publication, or Committee authority.

## Required outputs

Write English-only durable outputs under the authorized execution-review root:

- `implementation-receipt.md`;
- `implementation-status.json`;
- `completion-ledger.md`;
- exact before/after source manifests and digests; and
- an independent-review handoff bound to the final package digest.

Terminal status is exactly `COMPLETE_LOCAL_M0_EVIDENCE` or `PARTIAL_HALTED`. A green suite alone is insufficient.

