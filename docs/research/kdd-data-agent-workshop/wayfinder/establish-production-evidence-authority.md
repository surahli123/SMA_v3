# Establish Production Evidence Authority and Access Boundaries

Type: `wayfinder:task`
Status: open
Claim: 019ff4cf-3c9f-7661-9a30-51c1cd2c3536
Blocked by: none

## Question

In the real enterprise-search production environment, which systems are authoritative for metric, experiment, runtime identity, deploy, repo/symbol, config, flag, model, data/index, connector, ACL, and query/result evidence? Who owns mapping, access, retention, and redaction decisions?

Current funded priority: M0 requires authority only for experiment identity, the primary metric read, the independent recomputation/basis-table path, metric definitions, assignment/exposure, joins, freshness, and the applicable tenant/role/region scope. Code/deploy/change/query/replay authority remains direction-only until M1/M2 is funded. P2 must not force the broader inventory into the M0 build slice.

## Inputs

- [Research synthesis](../research-synthesis.md)
- [Enterprise-search experiment failure practices](../enterprise-search-experiment-failure-practices.md)
- [Primary-source audit](../primary-source-audit.md)
- A real source inventory supplied by production owner, Eng, and security/privacy. Do not infer it from old SMA.

## Resolution must define

- Canonical source, owner, stable identity, snapshot/freshness, and fallback for each evidence class.
- Proof for deployed SHA/config/flag/model/data/index/connector identity.
- Ownership, precedence, conflict, and cardinality for metric → surface/component → runtime → repo/symbol mappings.
- Tenant/source/role scope and authorization, redaction, retention, and packet boundaries for raw queries, results, and screenshots.
- Required read-only, pagination, partial/error, and receipt behavior for adapters.
- Per-source physically write-incapable credentials, constrained-broker enforcement, egress limits, and real-credential denial receipts.
- Identity model, synthetic-principal and aggregate-only boundaries, render-time recipient authorization, approver, and expiry.
- Typed redaction-failure behavior, artifact-tier retention, erasure/tombstone proof, diagnostic Trace retention, and confidential-content digest rules.
- Per-case/per-window load ceilings, named halt authority, tested disable path, and E15 judgment/offline-evaluation authority or explicit unavailability.

## Invariants and failure behavior

- A commit in a repository does not prove production is running it.
- Access cannot exceed the most sensitive source. Expanding tenant, source, or sensitive access requires human approval.
- Unknown mappings or unavailable sources produce explicit Coverage Gaps. Broad repository keyword search cannot masquerade as deployed proof.
- This ticket freezes an authority contract only. It does not connect to production or read unauthorized sensitive data.

## Acceptance scenarios

- The same query has different eligible corpora for different tenants/roles; scopes do not collapse.
- An interleaver change declares Confluence as its target but can affect Jira/3P placement; the mapping expresses one-to-many indirect impact.
- Deployed SHA differs from repository HEAD; runtime/deploy receipts remain authoritative.

## Human gate

Production owner, Eng, and security/privacy must confirm the sources, access, and retention boundaries they own. The Agent cannot answer for them.

## Prepared Asset

- [Production Evidence Authority and Access Boundary Intake](production-evidence-authority-intake.md)

## Current blockers

- No acknowledged production source inventory or accepted redacted proof set has been supplied.
- Source authority, ownership, access, retention, redaction, mapping, and fallback decisions remain unresolved.

## Required human participants

- Production Owner
- Engineering Technical Owners for proposed sources and mappings
- Security/Privacy Owner
- Experiment Owner or On-call/Incident Commander where applicable

## Next HITL step

Facilitate the linked intake, collect approved redacted proof locators and role acknowledgements, and keep this ticket open until its closure gate is satisfied.
