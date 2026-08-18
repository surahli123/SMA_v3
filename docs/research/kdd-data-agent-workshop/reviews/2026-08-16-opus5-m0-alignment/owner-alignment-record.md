# Owner Alignment Record for the M0-M2 Validation Slice

Date: 2026-08-16  
Authority: Owner-confirmed product decisions  
Scope: Product authority for planning and the M0-M2 validation program; local fixture-backed M0 implementation is separately authorized, while production access and M1/M2 implementation are not

## Purpose

This record is the durable authority for the six product decisions resolved through the Owner grill. It supersedes contradictory planning statements that treated M1 and M2 as direction-only for the entire first implementation program. Historical review findings remain evidence, but they do not override these Owner decisions.

## Confirmed Decisions

### O1. Flight identity

A `Flight` is one A/B test and is equivalent to one `Experiment`. Rollout, exposure, analysis-window, and run-attempt details belong to that Flight. They are not separate Flights.

### O2. Decision metric policy

The target product supports multiple equally important decision metrics through a frozen metric set and decision policy. The first M0 implementation defaults to one decision metric. Co-primary metrics are allowed only as an approved, preregistered exception. Contracts must not encode singular cardinality as a permanent invariant.

### O3. Invalid Experiment Remediation

The target M0 capability may generate a correct, reviewable, unapplied candidate diff that is limited to validity, instrumentation, or data-quality remediation. The first vertical path starts with typed remediation guidance and a reopen condition. Guidance remains the permanent fallback whenever exact-target, authority, validation, or no-write delivery gates are incomplete. M0 must never infer a production cause, propose a product-logic optimization, or apply a mutation from an invalid experiment.

### O4. Production review and approval roles

Every real production Flight separates three responsibilities:

- The `Experiment Owner` designs and runs the Flight and prepares its evidence package.
- The `Independent DS Consultant` challenges methods, evidence, and risks but has no final approval authority.
- The `Experiment Review Committee` conducts Experimentation triage or review and makes the final pass, change, or block decision.

Fixture-only and local development work may use documented, time-bounded role overlap. That exception never extends to a production Flight.

### O5. Build slice, staffing, schedule, and acceptance boundary

The first implementation program is an M0-M2 Validation Slice for one real, authorized production Flight:

- M0 Flight Readiness remains the first gate and main deliverable.
- M1 Metric Movement and Production Grounding and M2 Win/Loss Evidence are implemented within the same validation slice. They are no longer direction-only for this slice.
- The planning envelope is two builders and four to six active engineering weeks, with part-time domain, DS, review, Engineering, and security/privacy support as required by the relevant gate.
- The primary builder's leave from 2026-08-24 through 2026-09-14 is excluded from active engineering time.
- End of September is a stretch target, not a promised completion or approval date.
- Technical completion means that one authorized Flight produces review-ready M0, M1, and M2 packets. It does not imply Experiment Review Committee acceptance.

A reproducible Continuity Checkpoint is required before 2026-08-24. It must let another builder continue without oral context or let the primary builder resume effective work within half a day on return. If nobody works during leave, calendar progress pauses; the checkpoint limits restart cost but cannot create progress without a builder.

### O6. Old SMA asset reuse and production authority

Old SMA metric definitions, schema catalogs, business-table routing, and fixture facts may be read as historical candidates. They may be transferred only after validation against current production sources and named owners for the Flight's scope and effective time. Old SMA may be stale or wrong and is never production truth.

Adopted facts must retain provenance, validation receipts, effective scope, and observed drift. The new Data Agent does not inherit old SMA runtime or architecture. Direct code reuse requires separate interface, provenance, test, security, and license review.

## Superseded Planning Statements

The following meanings are superseded wherever they appear in the current planning corpus:

- M1 and M2 receive no implementation work in the first program.
- `flight` remains undefined or is distinct from an Experiment.
- M0 permanently requires exactly one decision metric.
- An invalid experiment can never carry a bounded validity, instrumentation, or data-quality candidate diff.
- The Experiment Owner may approve their own production Flight.
- A DS reviewer owns final production approval.
- Old SMA domain definitions may act as an oracle or production authority.
- Technical completion, packet generation, review readiness, and Committee Acceptance are interchangeable.

## Authority Boundaries That Remain Open

These decisions do not invent production access or approval:

- P2 must name authoritative sources, owners, credentials, ACL/tenant boundaries, retention, redaction, load ceilings, and halt authority before the real production path runs.
- P3 must validate the live review interaction contract with actual users before final UI acceptance.
- P4 must govern sealed fixtures, blind evaluation, adjudication, calibration, and any numeric GO thresholds.
- The Experiment Review Committee alone owns Committee Acceptance for a real Flight.
- The completed pre-alignment and continuation handoffs no longer grant a live implementation capability. `M0-F1`–`M0-F5` require a new Owner authorization and start receipt binding the accepted packet path, revision label, SHA-256, active-time cap, run/read/tool cap, expiry, and halt owner. Production access and M1/M2 implementation still require their separate gate closure and start decisions.

## Change Control

Any later change to O1-O6 requires a superseding Owner decision that names the changed decision, reason, effective scope, and affected artifacts. Engineering convenience, reviewer preference, legacy behavior, or an implementation spike cannot silently revise this record.
