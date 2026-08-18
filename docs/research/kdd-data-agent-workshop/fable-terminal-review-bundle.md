# Fable Terminal Review Bundle

Status: retained prepared input; the single authorized attempt was consumed and availability-blocked  
Scope: research and planning only; no implementation, production access, commit, push, PR, deploy, rollback, publication, or other mutation

## Review Objective

Adversarially review whether the greenfield Data Agent research, product contract, architecture specification, implementation sequence, evaluation design, and handoff package are logically coherent and ready for an implementation team to plan against.

This is a decision-layer review. Fable is not a fact source. Every factual challenge must return to the linked primary audit, fixed repository revision, or owner decision. A `GO` can mean only that the specification is suitable for separately authorized implementation planning; it cannot authorize implementation or production action.

## Start Gate

Start exactly one Fable session only if all conditions are true at execution time:

1. `claude-fable-5` is live and selectable in the actual Claude Code runtime.
2. The package checks in the [terminal-review readiness matrix](deliverable-readiness-matrix.md) still pass.
3. The [Evidence Room prototype handoff](prototypes/observability-review-surface/README.md) is the current P3 artifact.
4. No required research, owner decision, specification, sequence, evaluation, index, or handoff artifact is missing or materially contradictory.

If Fable is unavailable or disabled, fail closed. Do not substitute Opus, relabel another model as Fable, create a replacement session, or automatically reschedule. That condition occurred at 03:01 PDT and is recorded in the [availability receipt](fable-terminal-review-availability-receipt.md). This bundle must not be used again without fresh explicit owner authorization.

## Authority Order

Use this order when sources disagree:

1. [Planning decision packet](planning-decision-packet.md) for owner-confirmed product meaning.
2. [Closed canonical domain and policy contract](wayfinder/freeze-canonical-domain-policy-contracts.md) for state, gate, invalidation, and human-authority rules.
3. [Final architecture specification](final-architecture-spec.md) for the technology-neutral target design.
4. [Implementation sequencing](implementation-sequencing.md) for canonical `D0 + U1-U13` unit identity and dependencies.
5. [Evaluation and acceptance plan](eval-acceptance-plan.md) for evaluation rungs, vetoes, and calibration.
6. Primary research audits and their fixed source revisions for source claims.
7. [CE implementation plan](../../plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md) as a subordinate engineering proposal.

The older [greenfield requirements draft](greenfield-requirements.md) is research history, not the final specification.

## Proven Research Facts and Boundaries

- [Meeting alignment](meeting-audio-alignment.md) records full-duration historical coverage for both recordings and retains audio-only material. [Screenshot indexing](screenshot-index.md) covers 73/73 supplied images while explicitly treating them as partial slides, not a complete deck or verbatim transcript.
- [Qwen/Whisper comparison](qwen-whisper-asr-comparison.md) records HTTP 400 and zero Qwen transcripts. No dual-ASR corroboration exists.
- Unresolved source conflicts remain unknown: `0.65 / 0.69`, `25c / 35c`, the opening Qwen3.5 suffix, and Team 1401 `3-page PDF / graph 1 page`.
- [Team 1286](creative-team1286-practices.md) and [Team 1401](creative-team1401-practices.md) have observed graph UI. The [Champion audit](champion-repo-reverse-audit.md) and [Fourth-place audit](fourth-place-repo-reverse-audit.md) found no observed interactive Evidence Graph.
- No award work proves the target's complete production causal chain. Competition practices are evaluated through Adopt, Adapt, or Reject; they are not compatibility constraints or production truth.
- Old SMA and local KDD are audited in [primary-source-audit.md](primary-source-audit.md). Useful deterministic and evidence-handling practices may be adapted; legacy architecture, stages, schemas, thresholds, and routes are not inherited.
- The Champion Sol audit is the reverse-audit authority. Its Terra extractor was interrupted and produced no usable evidence packet. The Fourth-place Sol audit and owner-authorized Terra extraction completed; an interrupted derivative agent adds no evidence grade.

The [source manifest](source-manifest.md) and [cross-research consistency audit](cross-research-consistency-audit.md) keep `source fact | author or speaker claim | owner decision | reviewer inference | engineering proposal | unknown` distinct.

## Canonical Product Contract

Scenario A is the MVP: a post-experiment search-metric miss becomes ranked deployed `code | config | flag | model | data` candidates with an auditable evidence packet and an optional candidate diff marked literally `not_applied`.

Scenario B is deferred: a SEV metric drop becomes ranked runtime-reached production changes and a rollback-ready human packet. The Agent never rolls back. It models trigger, proximate mechanism, contributing factor, and systemic condition rather than forcing one root cause.

Cause Verdict:

`unassessed | suspected | confirmed | ruled_out | inconclusive`

Recommendation Readiness:

`not_applicable | blocked | proposal_ready | action_ready | rejected`

The axes are independent. No state authorizes mutation. `confirmed` requires every applicable `G0-G7` condition and independent causal review. Invalid experiments may publish only validity, instrumentation, and data-quality fixes. HIGH-risk or large-blast-radius recommendations cannot become `action_ready`.

Evidence revisions and handoff packets are immutable. Invalidation triggers dependency-scoped recomputation. Evidence Graph and Trace are separate, cross-linked, read-only projections.

## Product-Flow Challenges

### Scenario A

Challenge whether the design can distinguish and rank failures across experiment validity, metric definition, sample ratio mismatch, query mix, tenant/role/locale/surface, ACL/corpus/index freshness, retrieval/fusion/rerank/render/session behavior, latency/fallback/cache, deployed identity, and the unapplied candidate diff.

### Scenario B

Challenge whether the shared substrate can support measurement incidents, change points, mixed rollout, unknown runtime reachability, multiple changes, multiple causal roles, rollback recovery verification, continuing RCA, and a rollback-ready packet without granting rollback authority.

### Review Surface

Use [Evidence Room](prototypes/observability-review-surface/README.md) only as the current rough P3 artifact. It replaces the owner-rejected Case Ledger baseline, uses exactly four unified references, and has static/browser receipts. Its final agent critique is not owner acceptance. P3 remains open.

## Adversarial Review Questions

1. Where does the package overclaim evidence, launder an author claim into fact, or cite a source that does not support the decision?
2. Where can hallucinated causality, retrieval blindness, metric/relevance confusion, stale deployed identity, or a wrong exact patch target survive the gates?
3. Can human gates become theater rather than enforceable, named, expiring authority receipts?
4. Do fail-closed behavior, abstention, contradiction handling, risk propagation, invalidation, recomputation, deterministic ranking, and repeated-run stability survive partial failure?
5. Does `D0 + U1-U13` preserve the canonical sequencing and isolate P2, P3, and P4 post-gate work?
6. Does the evaluation plan prioritize false `confirmed`, wrong target, and security/ACL failure; avoid invented thresholds; and measure human utility, latency, tokens, source load, and cost?
7. Perform a literal **blind spot pass** for **unknown unknowns**.
8. Assume the system failed 12-24 months after launch. For each likely failure, give the early signal, mitigation, and cheapest falsifier. Include vendor/framework lock-in and cost/latency runaway.

## Open Gates That Must Remain Open

- P2: production evidence authority and access boundaries.
- P3: owner/reviewer acceptance of review interactions and visual hierarchy.
- P4: real evaluation gold, adjudication, pilot calibration, and named approvals.

These gates can yield findings or owner questions. The terminal reviewer cannot close them.

## Required Output

Write English durable artifacts:

- `fable-final-review.md`: session/model/subagent provenance, readiness evidence, severity-ordered findings with source anchors, blind-spot pass, 12-24 month pre-mortem, and `GO | ITERATE | NO-GO` under the research/spec boundary.
- `fable-review-disposition.md`: one row per material finding with `accepted | rejected | needs source recheck | owner decision needed`, source-check evidence, change made or exact blocker, and remaining gate.

Use at most three independent Opus reviewers and require concise conclusions plus evidence, not hidden reasoning. Stop after one Fable session and one bounded disposition pass when no material new finding remains.

After disposition, refresh the [deliverable index](deliverable-index.md), [completion matrix](completion-matrix.md), [readiness matrix](deliverable-readiness-matrix.md), [research synthesis](research-synthesis.md), [cloud handoff](cloud-agent-handoff.md), [cross-research audit](cross-research-consistency-audit.md), and [objective completion audit](objective-completion-audit.md). Preserve P2, P3, and P4 honestly.
