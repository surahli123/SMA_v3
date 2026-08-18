# SMA v3 — Enterprise Experiment Post-Analysis Data Agent

SMA v3 is a clean, evidence-preserving handoff repository for a new enterprise Data Agent initiative. It combines KDD Data Agents workshop research, reverse audits of award-winning systems, owner decisions, architecture and implementation plans, adversarial reviews, a review-surface prototype, and an independently accepted **local fixture-backed M0 evidence package**.

This repository intentionally does not carry the legacy SMA application or its Git history. Legacy SMA assets were research inputs only; production metric definitions, schemas, catalogs, business tables, access policy, and source authority must be rebound to the real enterprise environment.

## Current State

- **Accepted local evidence:** `ACCEPT_LOCAL_M0_EVIDENCE` for package aggregate `sha256:9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a`.
- **Reproduction evidence:** 370 tests passed from the repository root, package root, and an unrelated temporary directory; five hash-seed runs matched.
- **Architecture review:** the recovered Fable 5 architecture draft is `ALIGNED_WITH_GAPS`. It is retained as a labelled historical draft with its errata, not promoted over the frozen packet/specification.
- **Not established:** production M0 capability, production authorization, P2/P3/P4, M1/M2 completion, deployment, publication approval, or Experiment Review Committee Acceptance.

## Start Here

1. [Deliverable index](docs/research/kdd-data-agent-workshop/deliverable-index.md)
2. [Planning decision packet](docs/research/kdd-data-agent-workshop/planning-decision-packet.md)
3. [Owner alignment record](docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/owner-alignment-record.md)
4. [Canonical M0 freeze record](docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-canonical-freeze/m0-canonical-freeze-record.md)
5. [Round 5 independent review](docs/research/kdd-data-agent-workshop/reviews/2026-08-18-m0-f1-f5-correction-round5/independent-review.md)
6. [Final architecture specification](docs/research/kdd-data-agent-workshop/final-architecture-spec.md)
7. [Implementation sequencing](docs/research/kdd-data-agent-workshop/implementation-sequencing.md)
8. [M0 package](.agents/skills/kdd_data_agent/README.md)
9. [Repository provenance and export receipt](PROVENANCE.md)

## Repository Map

- `docs/research/kdd-data-agent-workshop/` — research, evidence manifests, owner decisions, architecture, reviews, prototypes, receipts, Wayfinder tickets, and complete grill-session records.
- `docs/plans/` — the bounded engineering plan.
- `docs/adr/` — owner-aligned architectural decisions for the M0–M2 validation program.
- `.agents/skills/kdd_data_agent/` — fixture-only M0 implementation, fixtures, and tests.
- `sources/papers/` — owner-authorized research-source PDFs with immutable provenance.

## Product Boundary

The M0 product objective is an auditable `FlightReadinessPacket` for an A/B Flight. A correctly blocked real Flight may demonstrate that the Agent can detect invalid decision evidence, but it does not authorize or block product launch. The Data Agent is an independent consultant; the Experiment Owner runs the Flight and the Experiment Review Committee owns the decision.

`Query Success` is the decision metric. Its traditional-click and AI-answer-success components remain diagnostic. A component-divergence recommendation requires at least one independent outcome-evidence source; otherwise the Agent must expose a Coverage Gap or insufficient-evidence result.

## Safety and Continuation

- Read-only by design: no apply, commit, PR, deploy, rollback, or production mutation capability is granted to the Agent.
- Candidate diffs may be syntactically valid and independently reviewable, but must remain unapplied and human-only.
- Do not infer production table, metric, ACL, catalog, threshold, or owner bindings from fixtures or legacy SMA.
- Before changing accepted package bytes, create a new aggregate, rerun deterministic verification, and obtain a fresh independent review.
- Preserve historical receipts and drafts byte-for-byte; supersede them with new revisions rather than rewriting custody history.

## Source and Licensing Note

This is a private research and engineering handoff. Included third-party papers remain the property of their authors and are supplied only as owner-authorized source evidence; no relicensing or public redistribution right is asserted. See [sources/papers/README.md](sources/papers/README.md).
