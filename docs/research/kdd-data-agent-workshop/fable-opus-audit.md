# Fable / Opus Evidence and Spec Audit

Date: 2026-08-11
Status: research review closed out. This is not a final engineering spec and does not authorize implementation.

> [!IMPORTANT]
> **Historical review snapshot; not current authority.** Fable/Opus served only as an adversarial reviewer and is not a fact source. The P0 gaps and final-spec NO-GO below describe the package at the time of this review. The four named P0 contract gaps were subsequently resolved by the closed [`freeze-canonical-domain-policy-contracts.md`](wayfinder/freeze-canonical-domain-policy-contracts.md) ticket and incorporated into [`final-architecture-spec.md`](final-architecture-spec.md). Current product meaning comes from those artifacts and [`planning-decision-packet.md`](planning-decision-packet.md), not from this audit's older lifecycle, single-axis, or gate vocabulary. Production authority, calibrated evaluation, and live review-surface acceptance remain open.

## 1. Scope and execution boundary

This round used one Fable session to perform an independent review of the existing research.

- Lead model: `claude-fable-5`.
- Evidence auditors: three `claude-opus-5` agents, each read-only and limited respectively to the workshop, Team 1286, and Team 1401.
- Session: `b83fbf4a-d66b-4c8e-9a02-3136d2d35406`.
- Auditor outputs: `a1217384c880ac9b5`, `aacf1c61c63014c8f`, `ab278e057c24b0607`.
- Input: a manually copied minimal evidence bundle (`local evidence bundle, not included`).
- Boundary: read-only; no repo writes, Git mutation, production access, or additional fan-out.
- Subsequent boundary: no further Fable tasks will be dispatched after this research closes out. Existing results are only a one-time review input.

Fable/Opus is not a new source of fact. Competition practices may enter the target design only through `Adopt / Adapt / Reject`. The old SMA, KDD repo, workshop, and winning entries impose neither compatibility nor architecture constraints.

## 2. GO / NO-GO

### Current conclusion

The label “Current conclusion” is historical to this audit date, not current package status.

- **Research evidence audit: GO.** Three material evidence errors were corrected and rechecked.
- **Freeze the final engineering spec directly: NO-GO at the time of this review.** Four executable P0 contracts were then missing: case lifecycle, append-only invalidation, runtime matcher, and derivation obligation. They are no longer current gaps; the closed canonical policy ticket and final architecture specification resolve them.
- **Continue planning / contract design: GO.** Planning may begin for vendor-neutral schemas, state transitions, matcher fixtures, and gate fixtures; this task neither freezes the spec nor authorizes implementation.

The direction is not wrong. The clean target is basically sound, but its prose principles must first become deterministic contracts.

## 3. Verified findings

### Workshop

Corrected in the primary evidence:

- Slide-only content is no longer described as a speaker audio claim. [meeting-audio-alignment.md:12,132](./meeting-audio-alignment.md)
- The `01:17:20–01:23:40` wall-clock interval was realigned with screenshots 39–45. [meeting-audio-alignment.md:130-132](./meeting-audio-alignment.md)
- The audio-only negative result remains: after removing the eligibility guard, all three paths still consistently accepted the biased answer. Consensus cannot replace a deterministic guard. [meeting-audio-alignment.md:141-146](./meeting-audio-alignment.md)
- Two failures were restored: the SQL approach for a complex hard join performed poorly; full pre-indexing was not completed and was changed to evidence retrieval on demand. [meeting-audio-alignment.md:131-132](./meeting-audio-alignment.md)
- `100%` audio coverage and `73/73` screenshot/topic mapping were verified by the primary task against the original local assets. The minimal Fable packet did not independently recheck the original M4A metadata; this limitation is recorded in the primary document. [meeting-audio-alignment.md:26-36,175-200](./meeting-audio-alignment.md)

### Team 1286

- In one complete demo, `solution.py` directly constructs an answer literal; the screen does not show source data being read, yet the shape validator and semantic reviewer still accept it. The correct bounded conclusion is: **deterministic code + review is insufficient to prove that a numeric value was derived from its source**. This must not be generalized into a claim that every solve was hard-coded. [creative-team1286-practices.md:71-80](./creative-team1286-practices.md)
- The Human wall's `fallback=continue` adopts the default value and continues after five minutes. This is fail-open, not human approval. [creative-team1286-practices.md:82-91](./creative-team1286-practices.md)
- Two production contracts were therefore added: numeric execution must have a nonzero source-read receipt; a material human gate must fail closed and follow an explicit escalation path. [creative-team1286-practices.md:225-238](./creative-team1286-practices.md)
- Paper claims, speaker claims, visual-only observations, and this report's inferences are separated. The paper claims grounding; the demo screen exposes an unexplained tension. Neither side should be promoted into a global fact.

### Team 1401

- The Autopilot prompt already specifies the DB, two-table join, `qty * price`, output columns, and sort order. This run cannot prove that the agent autonomously discovered the complete decomposition or join. [creative-team1401-practices.md:104-105](./creative-team1401-practices.md)
- The Event Log shows only one `execute_context_sql`. The Summary's “4 tables” does not prove that this specific run traversed a four-table path; the direct check also has no independent receipt. [creative-team1401-practices.md:112,136-142](./creative-team1401-practices.md)
- The KG screen independently proves only a page pointer, not a complete verbatim quote. [creative-team1401-practices.md:219-225](./creative-team1401-practices.md)
- The cross-DB fixture was constructed for the ER demo and shares `customer_id`. A successful link does not prove that the heuristic generalizes. [creative-team1401-practices.md:230-240](./creative-team1401-practices.md)
- `execute_python` is enabled by default and described as executing arbitrary Python in the task context directory. The A/B production lane must deny it by default; if necessary, it may run only in an isolated environment with no credentials, no network, read-only mounts, and a short lifetime. [creative-team1401-practices.md:150-160](./creative-team1401-practices.md)

## 4. Difference between the Fable synthesis and primary evidence

| Item | Status | How to use it |
| --- | --- | --- |
| Direct workshop, paper, video, and source-frame content | `observed` | May serve as research evidence, still constrained to the specific time, page, and frame ranges |
| Adopt / Adapt / Reject in the three corrected documents | `audited judgment` | May serve as design input, not production proof |
| Fable architecture, P0/P1, ticket order, and pre-mortem | `reviewer inference` | Use for planning and destructive testing; it cannot rewrite primary evidence retroactively |
| M4A hash, ffprobe output, and 73/73 mapping not rechecked by the Fable packet | `outside packet` | Rely on the primary task's local verification; do not say Fable independently confirmed it |
| Team 1286 hollow determinism | `single-demo bounded finding` | Use to require a derivation receipt; do not say all Team 1286 solves failed |
| Team 1401 production capability not shown | `not observed` | Say only “not proven by this video,” not “does not exist” |

Do not adopt numeric defaults without independent support from Fable, such as requiring a baseline failure rate fixed at `30–40%`. Eval thresholds should be determined by real risk and calibration data.

## 5. P0 gaps

> [!NOTE]
> The four subsections below are retained as historical reviewer findings. They are resolved in the closed canonical policy ticket and final architecture specification; they must not be read as current missing contracts. This does not close the separate production-authority, evaluation/calibration, or observability-review gates.

### P0-1 — Case lifecycle / state machine

The requirements already have A/B stages, but lack complete create, freeze, blocked, resume, reopen, handoff, and close contracts. Lifecycle and verdict must remain separate.

Minimum contract:

```text
DRAFT -> FROZEN -> COLLECTING -> VALIDATING
      -> INVESTIGATING -> REVIEW_READY -> CLOSED

side states: WAITING_FOR_INPUT | BLOCKED | FAILED_RETRYABLE
```

- `resume`: continue unfinished work in the same generation.
- `reopen`: create a new generation without overwriting the old packet.
- Human approval timeout: remain blocked/waiting; never auto-release.
- `recovered`, `cause_confirmed`, and `case_closed` are distinct states.

### P0-2 — Append-only evidence, invalidation, and partial recompute

Evidence nodes, derived results, claims, gate results, and packets must never be overwritten in place.

Minimum contract:

- An update creates a new node/revision linked with `supersedes`.
- Every derived node stores `depends_on[]` and `producer_version`.
- New evidence marks only the dependency closure as `stale`.
- `recompute_from_stage` reruns only the affected closure.
- A closed packet is immutable; a new packet links through `supersedes_packet_id`.

### P0-3 — `scope × interval × rollout` matcher

A “recent change” may only generate a candidate. Whether it entered the affected runtime scope must be computed by a deterministic matcher.

Minimum contract:

- Scope: set intersection over environment, region, tenant/cohort, service, and route.
- Interval: normalize to UTC and specify half-open intervals, clock-skew tolerance, and rollback interval.
- Rollout: separate planned from observed; support mixed fleets, percentage rollout, and unknown coverage.
- Output at least `in | partial | out | unknown`, with numerator, denominator, and source receipt.
- `out` may exclude a candidate; `unknown` can produce at most `suspected`.

### P0-4 — Derivation obligation

An exact query and shape validation can still pass a hard-coded result. Numeric execution must prove that it read the authoritative source.

Minimum contract:

- The execution receipt records source reads, query/locator, snapshot/version, input digest, and output digest.
- If the source-read set for a numeric derivation is empty, Gate 1 fails immediately.
- The independent validator uses an independent implementation and frozen input and checks the read set; it cannot reuse the same erroneous execution result.
- An open HIGH risk or contradiction must propagate to the publish gate; it cannot be displayed only as a badge.

## 6. P1 gaps

1. Adapter contract: `snapshot_token`, cursor, pagination, partial, truncation, dedupe, rate limit, timeout, auth subject, and typed error.
2. Mapping schema: metric segment → service/route/job → repo/file/symbol/owner; many-to-many, versioned, with conflict sets, and no last-write-wins.
3. Unified claim/verdict contract: the model submits only falsifiable claims; deterministic policy handles ranking and promotion.
4. Eval gold and thresholds: frozen fixtures, required/forbidden candidates, expected transitions, false-cause, abstention, provenance, and latency/cost gates.
5. Repeated-run stability: a deterministic layer ranks candidates for the same evidence; run a multi-run stability eval at minimum.
6. SLOs: A turnaround, B time-to-first-safe-check, and per-case tool/row/token/cost budgets.
7. Handoff: recipient, acknowledgement, expiry, stale marker, and close/reopen conditions.
8. Multiple-change cause: support `trigger`, `proximate mechanism`, `contributing factor`, and `systemic condition`; do not force a complex SEV into one root cause.

## 7. Proposed logical architecture

The diagram below is a clean-target recommendation supported by the evidence audit. It is planning input, not a final architecture spec. At that historical point, final boundaries, naming, and sequencing were still awaiting the owner grill and Wayfinder planning; later canonical artifacts now control them.

```text
Versioned Contracts
  -> Case Lifecycle + Append-only Evidence Graph
  -> Read-only Adapter Plane
  -> Deterministic Validators / Runtime Matcher / Mapping Resolver
  -> Semantic Workers submit falsifiable Claims
  -> Claim Registry
  -> Policy & Gate Engine
  -> Immutable Review Packet
  -> Human Review / Handoff
```

Boundaries:

- The evidence graph is the source of truth. The renderer cannot write back to evidence.
- The model does not write numeric or identity facts.
- A semantic worker neither decides a verdict nor publishes directly.
- Policy must fail closed; unknown does not automatically pass.
- Relevance affects only default presentation and does not delete underlying evidence.
- A/B share contracts; A optimizes for complete explanation and patch-ready direction, while B optimizes for time-to-first-safe-check and progressively higher confidence.
- Do not choose a language, vendor, storage system, or multi-agent framework yet, and do not inherit the old SMA/KDD module boundary.

## 8. Planning status

This section records planning status at the time of the audit. The owner grill later closed, the Wayfinder map and tickets were written, and the canonical final architecture specification now exists. This report remains non-canonical and does not supersede any later artifact.

Confirmed by the owner:

- The target is a problem-driven, deep, clear, implementation-ready redesign spec; planning includes architecture and sequencing, but there is no implementation now.
- The result is ranked production `code | config | flag | model | data` candidates, with complete evidence and an auditable reasoning path.
- A may generate an unapplied candidate diff; B generates a rollback-ready packet. Neither ever mutates, deploys, or rolls back.
- **Historical audit observation, now superseded:** this review recorded the then-current single-axis vocabulary as `observed | suspected | action-ready | confirmed`; no state authorized mutation.
- **Current owner-confirmed contract:** [planning-decision-packet.md](./planning-decision-packet.md) separates two independent axes. Cause Verdict is `unassessed | suspected | confirmed | ruled_out | inconclusive`. Recommendation Readiness is `not_applicable | blocked | proposal_ready | action_ready | rejected`. No state on either axis authorizes mutation.
- An invalid experiment yields only validity, instrumentation, and data-quality fixes; system hypotheses and production-change proposals are blocked.
- High-risk / large-blast-radius items cannot become `action-ready`; escalate to the IC + code owner.
- A human ruling does not replace evidence. A material gate fails closed; a packet has a named recipient, acknowledgement, expiry, escalation, and close/reopen behavior.
- After rollback, perform both recovery verification and continuing RCA; `recovered`, `stable`, and `close` are decided by the human on-call / IC.
- Do not set A/B SLAs yet; decide after benchmarking real production complexity.
- **Historical wording, superseded:** this audit said `confirmed` used stricter Gates 0–7 and that failure of a hard gate capped the result at `action-ready`. The current G0–G7 policy evaluates Cause Verdict and Recommendation Readiness independently; `action_ready` is never a Cause Verdict, and its exact ceilings come from the closed canonical policy ticket.
- Complex SEVs do not require a single root cause; model `trigger`, `proximate mechanism`, `contributing factor`, and `systemic condition`.
- A uses a layered causal chain and eight cause classes; it does not default to a code bug.

At the time of this review, those questions were assigned to planning. The MVP boundary is now frozen in the final architecture specification. Authoritative production sources, mapping ownership, redaction/retention, calibrated evaluation, and live review-surface acceptance remain open and must not be presented as resolved.

## 9. Startable implementation outline

This is only the research reviewer's dependency sketch. It neither replaces the Wayfinder map/tickets nor indicates that the owner has accepted the sequencing, and it does not authorize implementation.

| Unit | Content | Acceptance evidence |
| --- | --- | --- |
| U0 | Evidence corrections | Three corrected documents are on disk; `git diff --check` passes |
| U1 | Contracts v0 | Versioned schemas, example instances, and round-trip/invalid fixture tests |
| U2 | Case lifecycle | blocked/resume/reopen/handoff/close transitions; illegal transitions rejected |
| U3 | Append-only graph | mutation fails; supersession is queryable; dependency closure and partial recompute are correct |
| U4 | Runtime matcher | time-zone, scope-mismatch, gradual-rollout, mixed-fleet, and rollback fixtures all pass |
| U5 | Adapter SDK + fake adapters | pagination, snapshot drift, partial, typed error, and receipt fixtures all pass |
| U6 | Deterministic validators | SRM/changepoint/decomposition and planted-defect fixtures pass |
| U7 | Claim registry + gates | zero-source-read result rejected; risk propagates; human timeout does not release |
| U8 | A/B walking skeleton | Frozen synthetic A/B cases; no false `confirmed`; correct abstention |
| U9 | Eval + stability | multi-run ranking stable; false-cause, provenance, and latency/cost receipts comparable |

Dependencies: `U1 -> U2/U3/U4/U5 -> U6/U7 -> U8 -> U9`. Defer UI, online memory, live learning, generic action tools, and broad voting.

## 10. Pre-mortem

| Failure after 12–24 months | Early signal | Countermeasure |
| --- | --- | --- |
| Production sources are incomplete, so the agent never advances beyond metric-level guesses | Many cases end with an inventory coverage gap | Start with a narrow service that has complete read-only sources; measure coverage gaps from day one |
| Validators degrade into shape checks | Pass rate approaches 100%, with almost no discrepancies | Maintain planted-defect evals; make the derivation receipt a hard gate |
| SEV pressure causes fail-open behavior | Provisional answers or timeout defaults enter the final packet | Material gates fail closed; fixed escalation; every denial/timeout has a receipt |
| The evidence graph is too heavy, and users return to bare SQL/chat | Case creation declines; conclusions circulate outside the system | Receipts create the graph automatically; prioritize reducing B time-to-first-safe-check |
| The top suspect differs between two runs of the same case | Repeated-run rankings are inconsistent | The LLM only generates candidates; a deterministic scorer ranks them and undergoes stability evals |
| Automatic memory/policy promotion contaminates decisions | Unreviewed rules enter live policy | Allow only offline, versioned, human-gated promotion |
| A recent deploy is treated as the cause | High-ranking candidate has timing only, without scope/mechanism | Make matcher, runtime identity, counterevidence, and independent validation hard promotion gates |
| The renderer states a conclusion stronger than the evidence | Packet claim has no graph edge or has a stale dependency | Renderer is a pure projection; rerun policy gates before packet build |

## 11. Evidence-audit recommendation

**Agree with modifications.** Retain evidence-first, typed production changes, runtime identity, read-only adapters, deterministic gates, and abstention. Add:

1. case lifecycle and generation;
2. append-only invalidation / partial recompute;
3. `scope × interval × rollout` matcher;
4. source-read derivation obligation;
5. fail-closed human gate + escalation;
6. deterministic ranking + repeated-run stability;
7. mandatory risk → publish-gate propagation.

Only after these contracts are complete and planning shared understanding is frozen should the work enter final engineering spec review. Research practice itself cannot prove production correctness.
