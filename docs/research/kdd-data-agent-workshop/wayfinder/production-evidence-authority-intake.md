# Production Evidence Authority and Access Boundary Intake

Status: preparation asset for a human-in-the-loop decision; no production answers are recorded here.
Prepared for: [Establish Production Evidence Authority and Access Boundaries](establish-production-evidence-authority.md)
Policy context: [Freeze the Canonical Domain and Policy Contracts](freeze-canonical-domain-policy-contracts.md)
Planning context: [Data Agent Redesign Planning Decision Packet](../planning-decision-packet.md)

## Purpose and non-authority statement

This asset prepares the production owner, Engineering, security/privacy, and applicable experiment owner or on-call representative to establish an evidence-authority contract. It does not assert that any source is canonical, that any person owns a source, or that any access, retention, redaction, tenant, freshness, mapping, or fallback policy exists.

Repository research can establish required questions and fail-closed behavior. It cannot establish production facts. Every proposed answer below remains `UNKNOWN` until an authorized human supplies a redacted proof reference and each required role acknowledges the row.

This intake is research and design only. It authorizes no production access, source connection, raw-data read, credential handling, deployment, rollback, or mutation.

## Intake rules

1. Use role names in this document and keep personal contact details in an approved internal directory.
2. Record only redacted locators and digests. Never paste credentials, tokens, raw queries, raw results, user identifiers, tenant names, incident payloads, screenshots containing sensitive content, or access-control membership.
3. A source name is not proof of authority. Attach an accepted proof example and record its stable, redacted locator.
4. A repository commit is not proof of deployed runtime identity. Runtime or deploy evidence must bind environment, effective interval, rollout scope, and deployed artifact.
5. Missing access, zero reads, timeout, partial pages, stale evidence, and unresolved conflicts are Coverage Gaps, not negative evidence.
6. The narrowest source's authorization and sensitivity ceiling governs any combined packet. Tenant or source expansion requires explicit human approval and a new authorization receipt.
7. Do not enter real answers during an unapproved meeting recording or in this repository. Use the approved internal evidence register and copy only redacted references here.

## Safe redacted placeholder format

Use this format for every proposed answer. Angle-bracket values are labels, never real secrets or raw values.

```text
answer_state: UNKNOWN | PROPOSED | CONFLICTED | ACKNOWLEDGED
evidence_class: <class-label>
source_alias: SRC-<opaque-id>
source_kind: <generic-kind>
decision_owner_role: <role-only>
technical_owner_role: <role-only>
stable_identity_scheme: <field-names-and-version-only>
snapshot_or_interval: <ISO-8601-bounded-window-or-snapshot-rule>
scope: <environment/surface/component/tenant-class/role-class; no real tenant or user>
authorization_receipt: AUTH-<opaque-id>
credential_capability_ref: CAP-<opaque-id> | UNKNOWN
identity_model_ref: IDN-<opaque-id> | UNKNOWN
redaction_profile: REDACT-<opaque-id>
redaction_failure_ref: RFAIL-<opaque-id> | UNKNOWN
retention_policy_ref: RET-<opaque-id>
erasure_proof_ref: ERASE-<opaque-id> | UNKNOWN
load_ceiling_ref: LOAD-<opaque-id> | UNKNOWN
halt_authority_role: <role-only> | UNKNOWN
source_receipt: RCPT-<opaque-id>
content_digest: sha256:<digest-of-approved-redacted-artifact>
fallback_alias: SRC-<opaque-id> | NONE | UNKNOWN
conflict_rule_ref: CONFLICT-<opaque-id> | UNKNOWN
proof_locator: <approved-internal-redacted-locator>
acknowledgements: [<required-role>: PENDING | ACKNOWLEDGED | REJECTED]
notes: <no-sensitive-values>
```

Forbidden examples include passwords, API keys, bearer tokens, cookies, raw SQL containing sensitive literals, raw query strings, result text, screenshots of private content, user or group membership, tenant identifiers, and unredacted incident logs.

## Common question contract for every evidence class

Each inventory row must answer all fields below. `UNKNOWN` is acceptable during intake; omission is not.

| Field | Question that must be answered | Required form |
| --- | --- | --- |
| Canonical source | Which source is authoritative for this fact, and for which fact fields is it not authoritative? | Redacted source alias plus authority statement |
| Decision owner | Which role decides authority, precedence, policy, and exceptions? | Role and escalation role; no inferred person |
| Technical owner | Which role maintains the source, adapter semantics, schema, and incident response? | Role and service ownership reference |
| Stable identity | Which immutable or versioned key identifies the entity and revision? | Field names, namespace, uniqueness rule, version |
| Snapshot/time | Is evidence point-in-time, interval-effective, event-time, ingestion-time, or query-time? How is timezone handled? | Timestamp semantics and bounded interval |
| Scope | Which environment, surface/component, region, tenant class, role class, cohort, and rollout does it cover? | Explicit included and excluded dimensions |
| Freshness | What is the source-specific freshness/expiry rule, who owns it, and how is stale evidence represented? | Policy reference and observable timestamp; no invented SLO |
| Pagination/partial/error | How are cursors, total/read counts, truncation, timeouts, per-shard or per-source failures, retries, and zero reads represented? | Deterministic status and completeness receipt |
| Authorization | Which read-only purpose, identity class, attributes, approval, and expiry permit access? Are per-source credentials physically incapable of writes, brokered outside model execution, and covered by a real-credential denial receipt? | Authorization receipt, constrained-broker boundary, capability reference, and denial proof |
| Identity and render authorization | Which synthetic or service principal model is permitted, which cross-user comparisons are aggregate-only, and which live recipient entitlements are rechecked at each render? | Versioned identity model, named approver, expiry, and render-time denial receipt |
| Redaction | Which fields are removed, tokenized, bucketed, summarized, or forbidden from packets and model context? What typed no-body result, blocked coverage, and dependent publish barrier follow redaction failure? | Versioned redaction profile and failure receipt |
| Retention | How long may raw, redacted, derived, cached, packet, and diagnostic Trace evidence persist, and who may delete or extend it? How are erasure-eligible content, tombstones, key destruction, backups, and deletion proof handled without rewriting history? | Policy reference by artifact tier and erasure-proof contract |
| Load and stop authority | What per-case/per-window limits apply to reads, rows, bytes, pages, retries, and concurrent workers? Which named role can halt the path and how is disablement tested? | Versioned ceiling, halt role, escalation path, and denial/stop receipt |
| Receipt/digest | What proves the exact read, query, version, page set, result count, and content integrity without exposing content? | Immutable receipt ID and digest semantics |
| Fallback | If canonical evidence is unavailable, what source, if any, is permitted; what ceiling applies; and when must the system abstain? | Named alias or `NONE`, precedence, ceiling |
| Conflicts | How are contradictory sources detected, retained, escalated, and resolved without overwriting history? | Precedence rule, resolver role, resolution receipt |
| Cardinality | Is the relationship one-to-one, one-to-many, many-to-one, or many-to-many; are indirect and conditional edges explicit? | Cardinality and edge semantics |

## Evidence-class inventory and tailored questions

The prompts below specialize the common contract. Each row still requires every common field above.

| ID | Evidence class | Canonical source, ownership, and identity questions | Time, scope, freshness, and completeness questions | Access, lifecycle, proof, fallback, conflict, and cardinality questions |
| --- | --- | --- | --- | --- |
| E01 | Metric | Which registry defines metric name, version, formula, numerator, denominator, unit, guardrails, and allowed dimensions? Which role decides semantics, and which role owns computation? What stable ID binds definition and revision? | Which event-time and processing-time windows apply? Which population, surface/component, experiment/incident, tenant class, and role class are included? How are freshness, completeness, joins, late events, pagination, zero rows, and partial recomputation represented? | Which aggregates or row-level reads are authorized? Which dimensions require suppression? What are raw/aggregate retention tiers and query receipts? What is an allowed fallback, if any? How are definition-vs-pipeline conflicts resolved? Can one metric map to multiple surfaces, components, runtimes, and symbols? |
| E02 | Experiment | Which system defines experiment, variants, assignment, exposure, trigger, ramp, allocation, holdout, status, and owner? What IDs version assignment and analysis plans? | What are assignment, exposure, observation, and analysis intervals? Which tenants, roles, surfaces, components, cohorts, and exclusions apply? How are delayed exposures, missing pages, SRM inputs, partial exports, and freshness represented? | Who may read assignment and exposure data? Which identifiers must be tokenized? What is retained? What receipts bind snapshot and query? Is any fallback acceptable? How are experiment registry, telemetry, and owner records reconciled? Can one experiment affect multiple flags, components, metrics, and runtimes? |
| E03 | Runtime identity | Which runtime inventory proves the executable artifact, image/package digest, process, environment, service, cluster, and effective dependency set? Who decides what counts as runtime identity and who operates the inventory? | What observation time or effective interval proves what was running? Which environment, region, tenant class, surface/component, route, and replica set are covered? How are mixed versions, partial fleet visibility, stale heartbeats, and unavailable instances represented? | What read-only identity can inspect runtime metadata? What fields are sensitive? What retention and attestations apply? What receipt binds observed runtime to artifact? Is deploy history an allowed fallback and with what ceiling? How are runtime/deploy disagreements handled? Can one runtime serve many components and one component span many runtimes? |
| E04 | Deploy | Which release/deploy control plane records artifact, environment, start/end/effective time, rollout, rollback, actor class, and outcome? Who owns deploy truth and pipeline semantics? What immutable event ID and artifact digest are used? | Which regions, cells, services, tenant cohorts, traffic percentages, and time intervals were reached? How are progressive rollout, pause, rollback, failed wave, partial success, missing page, and stale export recorded? | Who may read deployment metadata and audit history? What actor fields are redacted and retained? What receipt proves each rollout wave? What fallback is allowed if the deploy control plane is unavailable? How are declared, reachable, and observed deployment states reconciled? Can one deploy contain many artifacts and one artifact appear in many deploys? |
| E05 | Repo/symbol | Which source-control and code-ownership records are authoritative for owner/repo, commit, file, symbol, line range, generated source, and ownership? Who resolves repo and symbol identity? | Which commit/tree snapshot is examined, and how is it related to the affected interval and deployed artifact? Which service, component, surface, branch/tag, and generated-vs-source scope apply? How are shallow history, missing submodules, renamed symbols, pagination, and indexing lag represented? | Which repositories and metadata may be read? What code or ownership data is restricted? What retention and diff digests apply? Is code search a fallback only for discovery? How are ownership and symbol-index conflicts resolved? Can a metric map to many symbols and a symbol affect many metrics/surfaces? |
| E06 | Config | Which configuration registry or runtime snapshot defines effective values, inheritance, defaults, overlays, schema, and provenance? Who decides semantic ownership and who operates distribution? What identifies config object and revision? | When did each value become effective, where, and for which component, tenant class, role class, or cohort? How are propagation delay, mixed revision, omitted default, stale cache, pagination, and partial reads represented? | Who may read values versus only digests? Which values are secret or sensitive and must never enter evidence? What retention and change receipts apply? What fallback is allowed? How are desired-state and observed-effective-state conflicts resolved? Can one revision affect many runtimes and one runtime combine many revisions? |
| E07 | Flag | Which feature-management source defines flag schema, rule revision, evaluation logic, prerequisites, targeting, ramp, and kill state? Who owns business intent and technical evaluation? What IDs identify flag and rule revision? | What evaluation time, effective interval, environment, tenant/role cohort, surface/component, and rollout percentage apply? How are propagation, evaluation failure, default branch, missing exposure, pagination, and partial cohort coverage represented? | Who may inspect rules and evaluation receipts? Which targeting attributes must be redacted? What retention applies? What receipt proves effective evaluation without exposing identity? Is runtime telemetry a fallback? How are declared targeting and observed exposure conflicts handled? Can one flag gate many components and one request evaluate many flags? |
| E08 | Model | Which registry and serving control plane define model artifact, digest, lineage, feature/preprocess schema, endpoint, routing, and deployment? Who approves semantic use and who owns serving? What stable model and deployment revision IDs exist? | Which model was effective for each time, environment, route, cohort, tenant class, and surface? How are canaries, vendor-managed changes, routing fallback, mixed versions, missing metadata, and stale registry data represented? | Which model metadata, prompts/features, or outputs are authorized? What requires redaction? What retention and attestation receipts apply? Is endpoint observation a fallback and with what ceiling? How are registry and serving conflicts resolved? Can one endpoint route many models and one model serve many components? |
| E09 | Data/index | Which lineage catalog, dataset snapshot store, index control plane, and serving alias define source version, schema/mapping, generation, shards, embedding generation, and alias? Which roles own data truth and serving-index truth? | What snapshot/effective interval, environment, source, tenant class, language, shard, alias, and coverage apply? How are refresh lag, backfill, deletes, duplicates, mixed generation, missing shards, pagination, and partial failures represented? | Who may read metadata, samples, counts, or content? What fields/content are forbidden? What separate retention applies to source, index, sample, and receipt? What fallback is allowed? How are source-lineage-index-serving conflicts resolved? Can one dataset feed many indexes and one index combine many datasets/models? |
| E10 | Connector | Which connector registry and run ledger define connector type, source alias, config digest, checkpoint/high-water mark, run, schema/parser/chunker, and per-source outcome? Who owns source relationship and connector operation? | Which run/effective interval, environment, tenant class, source partition, content type, and index target apply? How are retries, skipped/deleted items, throttling, pagination, checkpoint gaps, partial failure, and freshness represented? | Who may inspect connector metadata or sampled payload? Which source fields are sensitive? What retention and receipts prove page/checkpoint coverage? What fallback is allowed? How are source, connector, and index counts reconciled? Can one connector feed many indexes and one index receive many connectors? |
| E11 | ACL/identity | Which identity, group, entitlement, source ACL, indexed ACL, and query-time enforcement records are authoritative for each stage? Which security/privacy role decides policy and which Eng role operates propagation? What versioned identities exist without exposing principals? | Which identity/ACL snapshot and effective interval apply to environment, tenant boundary, role class, source, document class, and index generation? How are propagation lag, nested groups, partial expansion, deny errors, pagination, and stale snapshots represented? | Which authorized test identities or aggregate counts may be used? Which principal, group, document, and tenant fields are forbidden? What retention applies to raw, tokenized, and aggregate receipts? Is any fallback permitted for authorization facts? How are source ACL and indexed/effective ACL conflicts handled? What are user-group-document-tenant cardinalities? |
| E12 | Query/result/session | Which telemetry and rendering records define request, normalized query, eligible corpus, candidate stages, ranked results, rendered results, interactions, and session boundaries? Who owns semantic definitions and collection correctness? What pseudonymous IDs bind stages without exposing content? | Which event/query/session time, environment, tenant/role class, locale, device, surface/component, pipeline, index, and model scope apply? How are sampling, late events, dropped stages, pagination, truncation, timeout, cache, fallback, and partial results represented? | Under what purpose may raw content ever be read, by whom, and through which approved interface? What must be tokenized, summarized, bucketed, or excluded from model context and packets? What separate retention tiers apply? What digests prove joins and rendered-list identity? What fallback is allowed? How are trace, render, and interaction conflicts resolved? What are query-request-result-session cardinalities? |
| E13 | Incident | Which incident system defines incident ID, severity, onset, affected scope, timeline, mitigations, recovery, monitoring, and closure? Which IC/on-call role owns operational state and which role owns evidence integrations? | Which event time, declared and observed intervals, environment, region, tenant class, service, and surface are covered? How are evolving scope, missing timeline events, linked sub-incidents, partial exports, and stale status represented? | Who may read incident metadata, restricted notes, or customer-impact fields? What is redacted and retained? What timeline/event receipts are accepted? What fallback is allowed? How are incident declaration and telemetry conflicts handled? Can one incident affect many components and one change participate in many incidents? |
| E14 | Mapping | Which versioned catalog establishes metric -> surface/component -> runtime -> repo/symbol and related config/flag/model/data/index/connector dependencies? Who decides mapping semantics and who maintains each edge? What stable IDs identify nodes, edges, revisions, and provenance? | For what interval, environment, tenant/role class, surface, rollout, and topology revision is each edge valid? How are unknown, indirect, conditional, partial, stale, paginated, or conflicting edges represented? | Who may read sensitive topology and ownership metadata? What is redacted and retained? What receipt proves edge provenance? May heuristics create candidates only, and what ceiling applies? How are conflicts and precedence resolved? Cardinality must explicitly support one-to-many and many-to-many, including declared, reachable, and observed impact as separate edges. |
| E15 | Judgment/offline evaluation | Which rubric, query set, judge class, judgment date, and evaluation revision may be used, and who owns their semantic and production applicability? | Which tenant/query class, locale, surface, model/index generation, and observation interval are covered? How are sampling, stale judgments, missing classes, and offline-online divergence represented? | Which judgment details may be read or modeled? What redaction, retention, independence, conflict, and receipt rules apply? E15 is unavailable until P2/P4 authority acknowledges the exact source and use. |

## Role-specific questionnaire

### Production Owner

1. For E01–E15, which source aliases are proposed as canonical, and exactly which fields does each source govern?
2. Who is the decision owner role for each row, and what escalation role resolves absence or disagreement?
3. Which production environments, surfaces/components, tenant classes, role classes, regions, and scenarios are in initial scope? Which are explicitly excluded?
4. What business purpose permits each read, and what is the narrowest evidence needed for Scenario A and Scenario B?
5. Which source substitutions are allowed when canonical evidence is unavailable, and what Cause Verdict and Recommendation Readiness ceilings must follow?
6. Which mapping edges are declared by product ownership, which are maintained by Engineering, and which require observed runtime evidence?
7. Which source or mapping conflicts must block publication rather than be resolved by precedence?
8. Who serves as independent causal reviewer and separate action approver for later cases? This intake does not grant either authority.

### Engineering Technical Owners

1. For each proposed source, what immutable identifiers, revision identifiers, timestamps, effective intervals, and content digests exist?
2. How can a read-only adapter prove the complete page/read set, total/read counts, cursor termination, truncation, retries, timeouts, and per-partition failures?
3. What proves observed runtime identity independently of repository HEAD and desired deploy state?
4. How do deploy waves, config inheritance, flag evaluation, model routing, index aliases, connector checkpoints, and mixed fleet versions become effective over time?
5. What is the exact cardinality of metric -> surface/component -> runtime -> repo/symbol edges? How are indirect effects such as a declared Confluence target affecting Jira or third-party placement represented?
6. Which heuristic discoveries may create candidates only, and which authoritative evidence must validate them?
7. What source-specific freshness signals exist? Do not propose a freshness SLO without the accountable owner.
8. Which errors are retryable, which require query repair, which require a different source, and which must terminate as Coverage Gaps?
9. What proof can bind query/result/session stages to the same request without exposing raw content or identity?

### Security and Privacy Owner

1. For each row, what purpose limitation, data classification, least-privilege role, tenant boundary, source boundary, and approval/expiry apply?
2. Which metadata, aggregate evidence, tokenized evidence, authorized samples, or raw fields may be read by a human, an adapter, or a model? State prohibitions explicitly.
3. Which redaction profile applies before storage, model context, screenshots, review packets, exports, and logs?
4. What are the separate retention and deletion rules for raw, redacted, derived, cached, receipt, and immutable packet artifacts?
5. Are any fallbacks forbidden for ACL/identity or query/result/session evidence? What happens when the canonical source is inaccessible?
6. Which authorized test-identity procedure can validate allow/deny behavior without exposing real users, groups, tenants, or documents?
7. What new approval is required to add a tenant, source, role class, evidence field, raw-content view, or retention extension?
8. What security event or evidence state forces a HIGH risk flag, blocks Recommendation Readiness, or requires incident escalation?
9. Which digests or attestations are safe to retain when the underlying evidence must expire or be deleted?

### Experiment Owner

Applicable to E01, E02, E07, E12, E14, and any row used for Scenario A.

1. Which versioned metric definition, analysis plan, assignment, exposure, trigger, ramp, population, and guardrail records are authoritative?
2. Which business-semantic checks require experiment-owner judgment, and which numeric/data-quality checks remain deterministic?
3. What proves treatment/control eligibility, same-window comparison, and the effective pipeline, corpus, ACL, and runtime for each arm?
4. Which experiment conflicts or missing receipts make G1 fail or inconclusive and prohibit a production-change Recommendation?
5. Which de-identified or aggregated evidence is sufficient for adjudication, and which raw evidence is not permitted?
6. Who acknowledges the experiment-specific inventory rows and the final authority decision without serving as the sole causal reviewer by default?

### On-call or Incident Commander

Applicable to E01, E03–E14 when Scenario B or incident evidence is in scope.

1. Which incident timeline and operational-health sources are authoritative, and who may set `recovered`, `stable`, or `closed`?
2. Which onset, affected-scope, mitigation, recovery, monitoring, and dependency receipts are required?
3. What is the safe read-only evidence path during an incident, including budgets, source-load limits, and escalation?
4. Which missing or conflicting sources block a rollback-ready packet, and which low-risk mitigation evidence may be independently sufficient while causation remains `suspected`?
5. How are recovery evidence and continuing RCA kept separate so recovery does not auto-confirm cause?

## Exact proof examples

The examples define evidence shape, not real source names.

| Evidence class | Accepted proof example | Insufficient proof |
| --- | --- | --- |
| Metric | Versioned metric-definition receipt plus immutable query/read receipt showing bounded window, dimensions, nonzero page set, row counts, freshness/completeness checks, and redacted digest | Dashboard screenshot, copied number, or query text without execution/read receipt |
| Experiment | Registry revision plus assignment/exposure/trigger/ramp receipts for the same interval and scoped cohorts | Experiment name, launch message, or owner recollection |
| Runtime identity | Read-only runtime attestation binding environment, observed time, service instance set, executable artifact/image digest, config/flag/model/index identities, and coverage status | Repository HEAD, branch name, image tag alone, or desired-state manifest |
| Deploy | Immutable deploy event and rollout-wave receipts binding artifact digest, environment, scope, start/end/effective time, outcome, and rollback state | CI success, merged PR, release note, or deploy announcement |
| Repo/symbol | Exact owner/repo plus commit/tree digest, file, symbol locator, ownership revision, and a verified binding from deployed artifact to commit | Broad keyword search, similar repository, default branch, or unbound code snippet |
| Config | Effective runtime snapshot or attestation showing config object/revision, inheritance resolution, scope, time, and redacted value digest | Config file in Git, desired value, or undocumented default |
| Flag | Rule revision and scoped evaluation receipt showing effective result, prerequisites, cohort/rollout, time, and redacted targeting digest | Flag UI screenshot, current global state, or experiment intent |
| Model | Registry artifact digest plus serving/routing attestation for endpoint, time, scope, preprocess/schema revision, and fallback state | Model display name, vendor announcement, or registry entry without serving proof |
| Data/index | Source/lineage snapshot, index generation/mapping digest, alias/serving receipt, shard/coverage status, and effective time | Source row exists, index name, latest generation, or document-count screenshot |
| Connector | Run/checkpoint receipt with page or partition coverage, success/error/skip/delete counts, parser/chunker revision, destination generation, and terminal status | Connector configured, last-success badge, or sampled document alone |
| ACL/identity | Authorized-test receipt binding pseudonymous identity class, group-expansion revision, source/index ACL versions, query-time policy, allow/deny assertions, and effective time | Real-user screenshot, group list, “access looks correct,” or rank result without ACL lineage |
| Query/result/session | Approved redacted request-chain receipt binding pseudonymous request/session IDs, pipeline/index/model revisions, per-stage counts, render digest, event joins, partial/fallback status, and scope | Raw query/result pasted into a ticket, final top-k screenshot, or trace without render/event linkage |
| Incident | Versioned incident event/timeline receipt linked to bounded telemetry reads, declared and observed scope, mitigation, recovery window, and human operational-state event | Chat transcript, status-page prose, or recovery claim without monitoring evidence |
| Mapping | Versioned edge records with node IDs, direction, edge type, cardinality, provenance receipt, effective interval, scope, and acknowledgements from responsible roles | Wiki diagram, naming similarity, inferred repository proximity, or unversioned ownership list |

## Canonical Gates 0–7 and dual-axis implications

This intake maps authority requirements to the already frozen policy; it does not claim that any gate can currently pass.

| Gate | Authority rows needed from this intake | Missing or conflicting authority behavior |
| --- | --- | --- |
| G0 Claim contract | E01, E13, E14 plus the evidence classes named by the claim | Keep Cause Verdict=`unassessed`; Recommendation Readiness at most `blocked` |
| G1 Observation and validity | E01, E02 when applicable, E12, and their authorization/freshness/receipt fields | `inconclusive` when authority/coverage is missing; critical invalidity prohibits a production Recommendation |
| G2 Runtime identity and reachability | E03–E11 and E14, scoped by environment × tenant/role/surface × interval × rollout | `out` may rule a candidate out only with validated proof; `unknown` or conflict keeps Cause at most `suspected` and readiness=`blocked` |
| G3 Mechanism coherence | E03–E12 and E14 with a runtime observation matching a prediction | Missing authoritative intermediate evidence keeps Cause at most `suspected`; causally linked action at most `proposal_ready` |
| G4 Independent causal challenge | Applicable authoritative metric, experiment, runtime, data/index, query/result/session, and incident receipts | No complete independent challenge keeps Cause at most `suspected`; no human opinion substitutes for evidence |
| G5 Alternatives and counterevidence | Coverage receipts across E01–E15 as applicable | Open material source or owner conflict keeps Cause at most `suspected` and readiness=`blocked` |
| G6 Recovery, regression, recurrence | E01, E03–E14 as applicable; E13 is human-owned for incident health | Recovery alone does not confirm cause; missing regression/replay/monitoring evidence prevents confirmation and lowers readiness |
| G7 Promotion and independent review | Complete acknowledged authority rows, G0–G6 receipts, conflict registry, policy result, immutable packet digest | Missing reviewer, authority, or evidence blocks publication; Action Approval remains separate |

Cause Verdict (`unassessed | suspected | confirmed | ruled_out | inconclusive`) and Recommendation Readiness (`not_applicable | blocked | proposal_ready | action_ready | rejected`) remain independent. This intake cannot promote either axis. Even later, an authority acknowledgement is necessary metadata, not causal proof or action approval. HIGH security/privacy risk, a material contradiction, or expanded tenant/source scope forces fail-closed handling.

## Failure behavior

| Condition | Required behavior | Prohibited behavior |
| --- | --- | --- |
| Unknown answer | Record `UNKNOWN`, accountable role, affected rows/gates, and next safe human step | Guess a source, owner, policy, or mapping |
| Missing access | Record Coverage Gap and authorization request route; perform no read | Treat no access or zero reads as negative evidence |
| Conflicting owners | Preserve both proposals, mark `CONFLICTED`, name the decision-owner role and escalation, and block affected rows | Select the more convenient source or overwrite one view |
| Stale source | Retain historical receipt as stale, block current promotion, and request a fresh bounded snapshot | Present the old observation as current or silently refresh with broader access |
| Raw-sensitive evidence | Stop ingestion, do not copy it, follow the approved security handling path, and create only a safe incident/coverage reference if authorized | Paste, summarize into model context, screenshot, hash-and-retain without policy, or move it to this repository |
| Tenant or source expansion | Stop and require a new explicit authorization receipt defining purpose, scope, expiry, redaction, retention, and approver | Reuse an old approval, infer cross-tenant equivalence, or broaden a query/filter |
| Pagination or partial error | Preserve page/read counts, cursor state, failures, retry status, and completeness ceiling | Treat a partial result as complete or silently drop failed partitions |
| No canonical fallback | Mark the fact unavailable and apply the gate ceiling or abstain | Substitute logs, repo search, memory, or narration as authority |

## Unresolved decision ledger

All entries start unresolved. Add proposals only after authorized human intake; do not delete rejected alternatives.

| Decision ID | Decision required | Required roles | Current state | Evidence required to resolve | Downstream impact |
| --- | --- | --- | --- | --- | --- |
| D01 | Canonical source and field-level authority for E01–E15 | Production Owner; each row's Engineering Technical Owner; Security/Privacy Owner for sensitive rows | UNKNOWN | Accepted proof for every row plus acknowledgement matrix | All gates; adapter design |
| D02 | Decision-owner and technical-owner role for every source and mapping edge | Production Owner; Engineering Technical Owners | UNKNOWN | Service/ownership references and escalation path | Conflict resolution; incident routing |
| D03 | Stable identity, snapshot/time, and effective-interval semantics per class | Engineering Technical Owners | UNKNOWN | Versioned schema or redacted sample receipt | G1–G3; invalidation |
| D04 | Initial environment, surface/component, tenant/role class, region, and scenario scope | Production Owner; Security/Privacy Owner | UNKNOWN | Explicit inclusions/exclusions and authorization receipt | G0–G2; access boundary |
| D05 | Source-specific freshness and staleness policy | Decision owner for each row; Engineering Technical Owner | UNKNOWN | Observable freshness field and policy reference | Evidence state; gate reopening |
| D06 | Pagination, partial, error, retry, and zero-read semantics | Engineering Technical Owners | UNKNOWN | Redacted complete and partial read receipts | Adapter contract; coverage |
| D07 | Authorization purpose, least privilege, expiry, and tenant/source expansion workflow | Security/Privacy Owner; Production Owner | UNKNOWN | Authorization policy and redacted approval receipt shape | All production reads |
| D08 | Redaction and model-context policy per field and artifact tier | Security/Privacy Owner | UNKNOWN | Versioned redaction profile and approved examples | Evidence packets; UI; storage |
| D09 | Retention/deletion rules for raw, redacted, derived, receipt, cache, and packet tiers | Security/Privacy Owner; records owner if applicable | UNKNOWN | Policy references and deletion/extension authority | Storage and audit design |
| D10 | Receipt and digest semantics per source | Engineering Technical Owners; Security/Privacy Owner | UNKNOWN | Redacted accepted proof examples | Evidence validation; reproducibility |
| D11 | Permitted fallback, precedence, and verdict/readiness ceilings per row | Production Owner; Engineering Technical Owner; Security/Privacy Owner where sensitive | UNKNOWN | Source-outage scenario and policy acknowledgement | Fail-closed behavior |
| D12 | Conflict detection, resolver role, and append-only resolution receipt | Production Owner; Engineering Technical Owners; Security/Privacy Owner for policy conflicts | UNKNOWN | Conflict scenario and resolution format | G2, G5, G7 |
| D13 | Mapping ownership, edge semantics, precedence, indirect impact, and cardinality | Production Owner; Engineering mapping owners | UNKNOWN | Versioned mapping edge examples including one-to-many and many-to-many | Runtime/repo targeting |
| D14 | Experiment-specific authority and invalidity boundary | Experiment Owner; Production Owner; Engineering telemetry owner | UNKNOWN | Accepted E01/E02/E07/E12/E14 proofs | Scenario A G1 and proposal ceiling |
| D15 | Incident evidence authority and operational-state ownership | On-call/IC; Production Owner; relevant Engineering owners | UNKNOWN | Accepted E13 proof and linkage to other rows | Scenario B G6; handoff |
| D16 | Physically write-incapable credential and constrained-broker contract per source | Security/Privacy Owner; Engineering Technical Owner | UNKNOWN | Capability manifest plus real-credential denial receipt | Adapter admission; hard safety boundary |
| D17 | Synthetic/service identity model, aggregate-only comparisons, render-time entitlements, approver, and expiry | Security/Privacy Owner; Production Owner | UNKNOWN | Identity model and allow/deny render receipts | Tenant/ACL isolation; review surface |
| D18 | Typed redaction-failure behavior and erasure-eligible retention/deletion proof | Security/Privacy Owner; records owner if applicable | UNKNOWN | No-body failure receipt, tiered retention, tombstone/key-destruction proof | Evidence admission; publication; deletion |
| D19 | Per-case/per-window source-load ceilings and named halt authority | Engineering Technical Owner; On-call/IC; Production Owner | UNKNOWN | Load-limit policy, tested disable path, stop/escalation receipt | Replay/shadow safety; PROD-007/008 |
| D20 | E15 judgment/offline-evaluation authority and reviewer independence | Experiment Owner; Evaluation Owner; Security/Privacy Owner | UNKNOWN | Versioned rubric/query-set/judge-class receipt and scope | G1/G3/G4 evidence; offline-online divergence |

## Interview agenda

Recommended duration is set by the facilitator after participant availability is known; no duration is assumed here.

1. Reconfirm scope, non-access boundary, and the rule that repository research cannot answer production facts.
2. Confirm participating roles and identify missing decision authority before discussing sources.
3. Walk E01–E15, recording only proposed source aliases, field authority, owner roles, and safe proof locators.
4. For each row, test one complete-read scenario and one pagination/partial/error scenario.
5. Review authorization, redaction, retention, and tenant/source expansion with security/privacy.
6. Walk three identity chains: metric -> surface/component -> runtime -> repo/symbol; deploy -> runtime; query -> eligible corpus -> result -> session/metric.
7. Test conflict cases: repository HEAD differs from deployed SHA; desired config differs from observed config; source ACL differs from indexed/effective ACL; declared target has indirect one-to-many impact.
8. Review fallback behavior and explicit abstention/ceiling for every unavailable canonical source.
9. Map unresolved rows to G0–G7 and both policy axes without promoting any state.
10. Assign evidence follow-ups and acknowledgement owners; schedule a closure review only after proofs exist.

## Completion checklist for the HITL intake

- [ ] Production Owner, Engineering Technical Owners, Security/Privacy Owner, and applicable Experiment Owner or On-call/IC participated or explicitly delegated authority through an approved record.
- [ ] Every E01–E15 row answers every common question field or explicitly says `UNKNOWN`.
- [ ] Every proposed canonical source has an accepted redacted proof locator; no source is accepted by name or screenshot alone.
- [ ] Stable identities, timestamp/effective-interval semantics, included/excluded scope, and source-specific freshness are explicit.
- [ ] Pagination, page/read counts, partial/error/timeout, retry, and zero-read behavior are proven with redacted examples.
- [ ] Authorization, credential capability, constrained-broker boundary, identity model, render-time ACL, redaction failure, retention, erasure, and deletion/extension authority are explicit by evidence and artifact tier.
- [ ] Per-source load ceilings, named halt authority, tested disable path, and real-credential write-denial receipt are explicit.
- [ ] E15 judgment/offline-evaluation authority is acknowledged or explicitly unavailable; no screenshot or inferred component supplies it.
- [ ] Receipt/digest semantics are sufficient to reproduce or independently validate a read without retaining forbidden content.
- [ ] Every fallback is named or `NONE`, with precedence and policy ceiling; no silent substitution exists.
- [ ] Conflicts remain append-only and have a named resolver role, escalation, and resolution receipt.
- [ ] Mapping examples cover one-to-one, one-to-many, many-to-one, many-to-many, indirect impact, and declared/reachable/observed distinctions.
- [ ] The repository-HEAD-versus-deployed-runtime scenario resolves in favor of accepted runtime/deploy proof.
- [ ] Same-query/different-tenant-or-role eligibility remains separated and has no cross-tenant evidence leakage.
- [ ] D01–D20 are resolved or explicitly accepted as blockers; no blocking unknown is hidden.
- [ ] No secrets, raw sensitive values, real tenant/user/group identifiers, or unauthorized production evidence are present in this repository asset.

## Explicit ticket-closure gate

The ticket must remain open until all conditions below are met.

| Required acknowledgement | Rows or decisions that must be acknowledged | Evidence that must exist before acknowledgement counts |
| --- | --- | --- |
| Production Owner | E01–E15 field authority and scope; D01, D02, D04, D11–D20 | Accepted proof locators, explicit included/excluded scope, owner-role matrix, fallback/conflict policy, mapping examples |
| Engineering Technical Owner for each source | Their E-row; D02, D03, D05, D06, D10–D13 as applicable | Stable identity and schema semantics; complete and partial read receipts; freshness signal; runtime/deploy/config/flag/model/data binding where applicable |
| Security/Privacy Owner | E01, E02, E06–E12, E14 at minimum, plus any row classified sensitive; D04, D07–D12, D16–D20 | Purpose-bound read authorization; tenant/source boundary; versioned redaction and retention policies; safe proof/digest rules; expansion workflow |
| Experiment Owner, when Scenario A is in scope | E01, E02, E07, E12, E14; D14 | Versioned metric/experiment authority, assignment/exposure proof, business-semantic adjudication boundary, invalidity behavior |
| On-call/IC, when Scenario B or incident evidence is in scope | E01, E03–E14 as applicable; D15 | Incident/timeline authority, bounded telemetry linkage, operational-state ownership, recovery/monitoring evidence requirements |

Closure additionally requires:

1. every required row is `ACKNOWLEDGED`, not merely `PROPOSED`;
2. all accepted proof examples are represented by approved redacted locators and digests;
3. no unresolved conflict changes authority, access, retention, tenant boundary, mapping, or fallback behavior;
4. a complete acknowledgement matrix identifies the role, decision revision, time, and immutable intake digest;
5. local review confirms no raw sensitive data or secrets were copied into the repository;
6. the ticket receives a human-authored resolution based on the completed evidence register.

Until then, the ticket remains open and is not added to the map's **Decisions so far**.

## Handoff to an internal coding agent or cloud continuation

Do not begin adapter implementation from this preparation asset alone.

1. Read the ticket, this intake, the [map](map.md), the [planning decision packet](../planning-decision-packet.md), and the [frozen policy contract](freeze-canonical-domain-policy-contracts.md).
2. Verify the ticket is still open, its Claim is current, and no newer acknowledged intake supersedes this asset.
3. Obtain only the approved redacted authority register or contract revision. Do not request credentials, raw production exports, or broader tenant/source access.
4. Validate that every implementation input has `ACKNOWLEDGED` authority, a stable identity contract, time/scope semantics, authorization, redaction, retention, receipt, fallback, conflict, and cardinality rules.
5. Convert acknowledged rows into versioned read-only adapter requirements. Preserve `UNKNOWN`, partial, stale, conflict, zero-read, and no-authority as explicit outcomes.
6. Treat heuristics and repository search as candidate discovery only. Require accepted runtime/deploy proof for production identity.
7. Enforce least privilege, bounded reads, pagination completeness, source-load budgets, and no tenant/source expansion.
8. Keep Cause Verdict, Recommendation Readiness, Action Approval, and Incident State independent. No adapter result authorizes mutation.
9. If any required row is unresolved, stop that implementation slice and return a Coverage Gap with the exact accountable role and proof needed.
10. Preserve append-only revisions and link the implementation plan back to the acknowledged intake digest. Do not overwrite this preparation document with production facts.

## Research basis and limits

- [Research synthesis](../research-synthesis.md) identifies authoritative production sources, mapping ownership, retention/redaction, and tenant/ACL policy as still unknown.
- [Enterprise-search experiment failure practices](../enterprise-search-experiment-failure-practices.md) establishes why query context, eligible corpus, ACL, connector/index, model, pipeline, fallback/cache, render, and telemetry identities are required, while explicitly leaving enterprise-specific thresholds and policies undecided.
- [Primary-source audit](../primary-source-audit.md) shows that old SMA and KDD do not provide production change discovery, deploy-to-runtime verification, or metric-to-symbol mapping authority.
- [Freeze the Canonical Domain and Policy Contracts](freeze-canonical-domain-policy-contracts.md) provides the canonical Gate 0–7, dual-axis, Coverage Gap, append-only, and fail-closed behavior used here.

These sources justify the intake structure. They do not answer the intake.
