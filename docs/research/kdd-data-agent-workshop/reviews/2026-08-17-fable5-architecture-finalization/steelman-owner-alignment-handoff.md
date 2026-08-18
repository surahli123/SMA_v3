---
handoff_id: kdd-m0-steelman-owner-alignment-20260818
created_at: 2026-08-18T00:14:20-07:00
source_thread: 019ff3f9-ee51-7e32-937a-85fd9be2226a
target_thread: 05b209ef-e51c-459b-8646-0b3a5fd69cd1
status_path: /Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/steelman-owner-alignment-status.json
expires_at: after one Fable decision run
---

# Cross-Thread Handoff: Integrate the Owner's Steelman Decisions

## Current Blocker

The architecture-finalization job resumed after the Claude quota reset, but its existing evidence packet predates a high-leverage Owner discussion. The Owner has now resolved the product-level questions that determine what M0 proves, how the online search-success metric is treated, and when the Data Agent may challenge the official decision metric.

Do not return to production field, table, event-name, or threshold-value elicitation. Those bindings exist only on the company laptop and must remain typed production-binding requirements. Continue only with architecture-changing questions.

## Read First

- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/architecture-decision-ledger.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/architecture-finalization-status.json`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-fable5-architecture-finalization/owner-check14-decision-handoff.md`
- `/Users/surahli/Documents/projects/SMA_v2/docs/research/kdd-data-agent-workshop/reviews/2026-08-17-codex-prefreeze-execution/candidate-canonical-writeback-v4.patch`
- X steelman source: `https://x.com/Khazix0918/status/2089514899504607342`

## New Owner Decisions

Treat these as Owner authority, not reviewer inference.

1. **Production-backed M0 Definition of Done.** M0 MVP is not complete on fixtures alone. It must run one real, authorized production Flight end to end on the company laptop and produce a reviewer-auditable `FlightReadinessPacket`. The preregistered core material checks must execute against real evidence. Every unresolved item remains a typed Coverage Gap. A correctly blocked packet may prove M0 product capability, but only a packet satisfying all applicable material checks may be `decision_grade` or proceed to M1.
2. **Environment boundary.** The first real Flight can be validated only on the company laptop. Local fixtures, contracts, adapters, and deterministic replay remain pre-production evidence and cannot be called production validation. Actual table names, event schemas, threshold values, catalog identities, owners, ACLs, and retention policy remain `PRODUCTION_BINDING_REQUIRED` until that environment is available.
3. **Decision-metric shape.** The main decision metric is online behavioral `Query Success`, a union of `TraditionalResultSuccess` and `AIAnswerSuccess`. `TraditionalResultSuccess` requires a result click whose click-to-next-click duration reaches a fixed threshold. `AIAnswerSuccess` requires an AI-answer link click or sufficient AI-answer dwell. Thresholds are fixed within a Flight and identical across treatment and control for the corresponding policy. The precise production values and remaining timer bindings are deferred to the company laptop.
4. **M0/M1 semantic boundary.** M0 validates the registered union formula, component instrumentation, common grain/population/window, overlap handling, production definition, source reads, and reproducibility. M1 explains component movement, substitution, mix shift, and user-value semantics. Component-direction conflict is not by itself an M0 validity failure.
5. **No component guardrails yet.** The union is the sole decision metric. Its components are diagnostic. No component-level guardrail or threshold is preregistered; the Experiment Review Committee currently makes contextual trade-off rulings. The Agent must not invent a hidden guardrail after observing results.
6. **Explicit non-binding advisory.** When components conflict, the Data Agent must issue an explicit advisory: `recommend_pass | recommend_change | recommend_block | insufficient_evidence`. The Agent may issue `recommend_change` or `recommend_block` even when official Query Success improves and M0 confirms the calculation is valid. The official metric result and Agent advisory remain separate. The Experiment Review Committee retains final authority.
7. **Evidence floor for challenging an improving official metric.** Component divergence alone triggers mandatory M1 investigation but cannot justify `recommend_change` or `recommend_block`. At least one valid, scope-matched outcome-evidence stream not mechanically derived from the same union metric is required. Examples include reformulation, abandonment, session/task outcome, downstream user action, reviewed query/result evidence, human usefulness judgment, or direct user feedback. Missing evidence produces `insufficient_evidence`, not inferred absence of harm.
8. **M1 does not wait for M2.** Valid orthogonal behavioral evidence is sufficient for M1 to issue the non-binding advisory. Query/result examples from M2 may strengthen or falsify the advisory but are not mandatory before M1 publishes it.
9. **M0 blocking constrains M1 claims; it does not forbid M1 investigation.** Once the M0 packet is sealed, the case may enter M1 even when M0 is blocked. Publication authority is evaluated per M1 claim against its evidence dependencies. A `blocked + not_permitted` Flight may support validity, instrumentation, data-quality, and remediation analysis, but it cannot support treatment-causal or production-change claims that depend on the invalid comparison. A `blocked + directional_only` Flight may support explicitly directional component and orthogonal-outcome analysis. A local Coverage Gap blocks only claims that depend on the missing evidence. Every M0 blocker remains visible and cannot be waived by entering M1.
10. **An invalid Flight produces a scoped, non-binding block advisory.** When M0 is `blocked + not_permitted` because the experiment is invalid, M1 emits `recommend_block` with `target = use_of_this_flight_as_decision_evidence`, `basis = invalid_experiment`, and scope bound to the exact Flight generation. It advises the Committee not to rely on that Flight for the launch decision; it does not block the product launch, authorize rollback, or request a production mutation. This validity-based advisory does not require an orthogonal user-outcome stream because it does not challenge the decision metric's user-value semantics. It must include the validity remediation or rerun as the next safe action, and Committee authority remains final.
11. **M0 material checks use a fixed core plus preregistered Flight-specific applicability.** Every Flight runs the fixed core covering authorization and identity; assignment, exposure, and arm parity; metric formula, components, and symmetric threshold policy; population, grain, and window; source authority, freshness, and coverage; independent recomputation and registered statistical method; and preregistered runtime/sample sufficiency. Flight-specific checks and `NOT_APPLICABLE` decisions are selected before outcome reads, bound to a version and digest, and justified by a versioned applicability rule. Unknown applicability defaults material. Checks may not be removed after outcomes are observed; a change requires a new generation that preserves the prior record.

## Steelman Method

For each remaining architecture-changing disagreement:

1. Restate the real decision, not its surface wording.
2. Steelman the strongest case for the current direction.
3. Steelman the strongest opposing case.
4. Identify the one or two variables that change the answer.
5. Ask the Owner exactly one decisive question, in Chinese, and wait.
6. After the answer, give a clear judgment, reasons, and next action.

Do not ask implementation-detail questions that can be represented by a production-binding placeholder.

## Task

1. Integrate the eight Owner decisions into the English architecture decision ledger and final design drafts without editing canonical documents or candidate v4.
2. Perform a blind-spot pass and pre-mortem against the target system, concentrating on the remaining high-level attacks:
   - whether one real blocked packet is sufficient proof of M0 capability;
   - how the first-Flight core material-check set is selected without weakening fail-closed safety;
   - whether the one-orthogonal-evidence floor is strong enough to prevent post-hoc metric cherry-picking;
   - how M1 recommendation authority remains independent without becoming unaccountable product policy;
   - whether making M2 optional for the advisory undermines falsification or Committee usability;
   - how the company-laptop-only production boundary affects handoff, deterministic replay, and evidence retention.
3. Lead with product and architecture decisions. Keep production-specific field bindings as open gates.
4. Use Fable 5 for synthesis and arbitration. Reuse current evidence. If delegation is useful, remain within five total lanes and do not use agents for code writing.
5. Preserve the distinction among fixture readiness, production-backed M0 product capability, Flight eligibility, M1 advisory readiness, and Committee Acceptance.

## Output Required

- Update `architecture-decision-ledger.md` with the new Owner decisions and their consequences.
- Update `architecture-finalization-status.json`.
- Complete the already-promised English architecture/design-flow artifacts in this directory.
- Write the JSON status at `status_path`.
- In the Chinese Owner conversation, report only the next architecture-changing question or the final synthesis. Avoid field-level elicitation.

## Done When

- All eight new Owner decisions appear without semantic drift.
- The architecture explicitly requires one real authorized Flight for M0 MVP completion.
- Fixture evidence cannot be mistaken for production validation.
- The official metric result, Agent advisory, and Committee ruling remain separate.
- The evidence floor and M1-without-M2 sequencing are testable and fail closed.
- Remaining unknowns are true Owner decisions or production-binding gates, not implementation trivia.

## Red Lines

- Do not modify product code, tests, fixtures, Phase A, candidate v4, canonical architecture, plan, sequencing, or evaluation documents.
- Do not freeze or apply any candidate.
- Do not start `M0-F1`-`M0-F5`, access production, or claim Phase A cleared.
- Do not commit, push, open a PR, deploy, install, publish, or send external messages.
- Do not use Fable or any subagent to write code.
- Do not spawn more than five total subagents/workflow lanes.
- Do not expose company data or invent production bindings.

## Status Writeback

Write JSON to `status_path` with:

```json
{
  "handoff_id": "kdd-m0-steelman-owner-alignment-20260818",
  "status": "done|blocked|skipped",
  "summary": "",
  "evidence": [],
  "remaining_owner_questions": [],
  "production_binding_gates": [],
  "next_step": "",
  "updated_at": ""
}
```
