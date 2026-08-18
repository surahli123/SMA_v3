# Architecture Finalization Coordination Update

Status: `ACTIVE_REVIEW_INPUT`  
Date: 2026-08-17  
Audience: Fable 5 architecture facilitator, job `05b209ef`

## Byte-level state change

The architecture handoff's starting packet digest is superseded. Do not cite
`40c7234f3c0d85f18ebfba656e7aec2ab5ab71b86451a077ecad340eac779396`
as the current candidate or transfer its Opus verdict to the new bytes.

Current post-edit candidate bindings:

| Artifact | SHA-256 |
| --- | --- |
| `m0-m2-build-alignment-packet.md` | `67c844d10dcafcf2637388bf579dfcd9866d7d69ea6f4d3b456fd6b6b15dfcfa` |
| `final-architecture-spec.md` | `3b20c93859b78074b653d375fc29f60bd40993b3f3bcb4ee2ff481e8ba8706b8` |
| `docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md` | `52ce2763a365eb35ea884dfbc7f19b8b3d012b85edac544a21b356638126499c` |

Recompute before use because this worktree is active.

## Applied review corrections

The main orchestrator applied all eight edits from
`m0-freeze-codex-fix-handoff.md` after validating them against the live bytes. The
durable disposition is
`docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-freeze-codex-disposition.md`.

Architecture-relevant results:

- readiness uses two coordinated stored fields; only three exact pairs are legal;
  an illegal pair is rejected, not interpreted or repaired, and neither field has
  precedence;
- triage uses `analysis_use` plus `next_safe_action.kind`, never eligibility alone;
- unknown materiality remains stored as `unknown`, while the applied ceiling treats it
  as material until a versioned ruling supersedes it;
- a pre-runtime directional packet's reopen trigger and expiry bind to the
  preregistered runtime end;
- the M0 contract now includes treatment/control arm parity for index generation,
  serving alias, ACL snapshot, and effective pipeline;
- preregistered power/MDE sufficiency is explicit and is check 19; arm parity is part
  of check 5;
- the former implementation-continuation authorization is exhausted. M0-F1 through
  M0-F5 require a fresh Owner authorization and bounded start receipt even after a
  freeze is accepted;
- the freeze record must bind both the packet and controlling architecture-spec
  revision labels and SHA-256 values.

## Evidence conflict and current gate state

The surviving fix handoff says `zero blockers`, but the full review and status JSON it
cites list three blockers against the old digest. The current edits closed the three
failure shapes in the candidate documents, but no old verdict may be copied to the new
digest.

Current state:

- packet and spec: post-review candidates, not frozen;
- full 30-finding reconciliation: `PARTIAL`, not cleared;
- B3, M18, M19, and M20 required actions: not cleared;
- Phase A: not independently cleared;
- M0-F1 through M0-F5: not authorized and not started;
- production access, M1/M2 implementation, and Committee Acceptance: not authorized or
  proven.

A fresh third Opus 5 reviewer is being routed to Q11/Q12 under:

`docs/research/kdd-data-agent-workshop/reviews/2026-08-17-phase-a-independent-verification/handoff.md`

Do not finalize canonical writeback or produce a `FROZEN` record until that result, a
fresh exact-digest packet/spec review, and explicit Owner acknowledgement of the final
bindings are reconciled. Continue Owner discussion and draft-only architecture work;
mark any final-shaped output `APPROVED_PENDING_GATE` if design discussion concludes
before those gates close.

