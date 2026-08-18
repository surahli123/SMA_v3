# Prototype the Observability-First Review Surface

Type: `wayfinder:prototype`
Status: open
Claim: `019ff4cf-be73-7381-a086-6425c2a0bdf2`
Blocked by: none

## Question

For the current fixture-backed M0 slice, how should a packet-centered first screen let reviewers decide whether the Experiment setup and decision-metric read are trustworthy, inspect blockers, disagreements, Coverage Gaps, source/recomputation receipts, and the typed next safe action without implying an M1 cause? For the separately gated M1 continuation, how should a later screen combine a conclusion summary and a local evidence graph without turning the graph into decoration?

Scope update: the 2026-08-16 owner decision makes M0 Flight Readiness the only first build/funding slice. The existing Evidence Room remains useful M1 research, but it cannot by itself satisfy M0 interaction acceptance.

## Inputs

- Owner-confirmed graph/observability decisions in the [planning decision packet](../planning-decision-packet.md)
- [Team 1286 practices](../creative-team1286-practices.md)
- [Team 1401 practices](../creative-team1401-practices.md)
- [Research synthesis graph section](../research-synthesis.md)

## Resolution must define

- M0 packet hierarchy: `post_analysis_eligibility + analysis_use`, blocking checks, primary/scorecard-or-UI/recomputed disagreement, Coverage Gaps, receipts, typed next safe action, and named human state.
- A hard visual and semantic boundary preventing M1 Claims, candidate ranking, diffs, or Trace facts from appearing as M0 conclusions.
- First-screen hierarchy, local/full graph switching, coverage, and competing-claim entry.
- Separate Evidence Graph and Trace tabs with cross-links.
- Typed edges and representations for node/edge details, conflict, stale, invalidated, superseded, and incomplete states.
- Review tasks best served by graph, table, timeline, diff, or receipt.
- Summary, locator, authorized expansion, and redacted-revision handling for sensitive evidence.
- A shared A/B substrate with different default views; validate M0 first. M1 graph interactions remain separately gated until their implementation start and P3 path are authorized.

## Invariants and failure behavior

- The UI cannot create or write back source facts, claim state, verdict, or readiness.
- Tool logs, narration, static architecture diagrams, and arbitrary relations cannot masquerade as evidence.
- Every node/edge affecting verdict/readiness exposes source, scope, time, authorization, receipt, validator, freshness, and invalidation reason.
- HIGH contradictions must be prominent and must block a misleading confirmed/publishable reading.

## Acceptance scenarios

- An M0 reviewer can determine why a flight is `ready`, `blocked`, or incomplete from the sealed packet and reach the exact source/read/recomputation receipt without encountering an unsupported cause.
- A material primary-versus-recomputed disagreement and an unauthorized or partial read remain prominent and prevent a misleading readiness interpretation.
- A reviewer reaches exact code-line/config proof and its validator receipt from a Cause Verdict within two interactions.
- A reviewer can see two conflicting claims without the default local graph hiding one side.
- When the graph grows, coverage, filters, groups, and non-graph views still support review.

## Human gate

Owner/reviewers must review a rough prototype live. The Agent cannot decide whether observability is sufficient for them.

## Prototype handoff

- Prototype: [Observability-First Review Surface](../prototypes/observability-review-surface/)
- Review notes: [README](../prototypes/observability-review-surface/README.md)
- Run from the repository root: `python3 -m http.server 8765 --directory docs/research/kdd-data-agent-workshop/prototypes/observability-review-surface`
- Review URLs: `http://localhost:8765/?view=review`, `?view=claims`, `?view=verify`, and `?view=trace`.
- The former `?variant=A|B|C` surfaces are a rejected prototype iteration and are not part of the current UI contract.
- The current Evidence Room is an M1 research artifact, not the M0 review surface. An M0 packet-centered prototype and live reviewer receipt are still required.
- Human gate: pending. The Claim remains retained and this ticket remains open until the owner/reviewers confirm that the M0 interaction improves observability and review efficiency without implying an M1 cause.
