# Chart the Greenfield Search Metric Data Agent Redesign

## Destination

Find an executable route to a problem-driven, implementation-ready greenfield redesign specification. Codex or Claude Code should be able to implement it directly or generate a reliable implementation plan. This map plans the work; it does not implement the agent.

## Notes

- This map remains a research/design tracker. A separate Owner start receipt now authorizes only the local fixture-backed M0 implementation; the map itself grants no implementation, commit, push, PR, deployment, rollback, or other mutation authority.
- M0 Flight Readiness is the first gate and main deliverable. M1/M2 belong to the same one-Flight validation program but require separate gates/start receipts; Scenario B follows only through a separate later decision.
- Scenarios A and B are the only sources of requirements. Old SMA, the KDD workshop, Champion, Fourth-place, Team 1286, and Team 1401 are rejectable references, not compatibility or migration constraints.
- Resolve at most one Wayfinder ticket per session. Claim it before work. The charting session resolved no ticket.
- Local Markdown tracker rule: an open, unclaimed ticket whose blockers are all closed is on the frontier.
- Owner decisions are in the [planning decision packet](../planning-decision-packet.md). Research routing is in the [research synthesis](../research-synthesis.md) and [source manifest](../source-manifest.md).
- Continue to use `grilling` and `domain-modeling`. Only owner-confirmed terms and decisions may become product contracts.
- Preserve existing untracked files. Do not touch `.agents/skills/sma/` or `.agents/skills/sma_rewrite/evals/`.

## Decisions so far

- [Freeze the Canonical Domain and Policy Contracts](freeze-canonical-domain-policy-contracts.md) — Frozen an orthogonal, append-only policy across eight state dimensions, the two-axis policy matrix, Gates 0–7, partial recomputation, and fail-closed human responsibilities.
- [Owner alignment record](../reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md) and [planning decision packet](../planning-decision-packet.md) — Freeze the M0-first one-Flight M0-M2 program boundary, deferred Scenario B boundary, read-only authority, Evidence Graph/Trace separation, review path, and human gates.
- [Final architecture specification](../final-architecture-spec.md) — Specifies the target ports, append-only Evidence and Claim substrate, typed changes, validators, mapping, Scenario A/B flows, packets, security, and renderer projections.
- [Implementation sequencing](../implementation-sequencing.md) and [CE plan](../../../plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md) — Define the currently authorized local fixture-backed `M0-F0`-`M0-F5` route and the separately gated `D0 + U1-U13` M1/M2 continuation.
- [Evaluation and acceptance plan](../eval-acceptance-plan.md) — Specifies threshold-free fixtures, blind adjudication, hard vetoes, replay/shadow boundaries, measurements, and the later pilot-calibration process.
- [Deliverable index](../deliverable-index.md) and [cloud/internal-agent handoff](../cloud-agent-handoff.md) — Provide the current package inventory, authority order, and safe continuation route.

## Remaining open frontier

- [P2 — Establish Production Evidence Authority and Access Boundaries](establish-production-evidence-authority.md) remains open. The logical read-only Adapter SDK contract is specified, but real source identities, owners, mappings, ACLs, credentials, retention/redaction, load limits, and fallback authority require named production, Engineering, and security/privacy evidence.
- [P3 — Prototype the Observability-First Review Surface](prototype-observability-first-review-surface.md) remains open. Evidence Room is mechanically validated M1 research; the current M0 slice still needs a packet-centered Flight Readiness prototype and live owner/reviewer evidence.
- [P4 — Freeze Evaluation Gold, Adjudication, and Calibration](freeze-evaluation-gold-and-calibration.md) remains open. The threshold-free evaluation contract is specified, but real blind-case adjudication, pilot distributions, numeric exits, human baseline, and named approvals are not yet available.
- Production access, M1/M2 implementation, replay/shadow-read, commit, push, PR, deployment, rollback, and publication each require separate later authorization. None is implied by this map or by the local fixture-backed M0 start receipt.

## Out of scope

- Modifying or migrating old SMA/KDD implementations, or preserving their modules, languages, storage, dependencies, or schemas.
- Executing a candidate diff, production write, deployment, rollback, Slack message, formal-document publication, commit, push, or PR.
- Promoting competition architecture, agent routing, heuristic joins, debug traces, static diagrams, or LLM narration directly into the target architecture.
- Guessing SLA, token, cost, top-k, case-count, or stability thresholds before production-complexity pilots.
