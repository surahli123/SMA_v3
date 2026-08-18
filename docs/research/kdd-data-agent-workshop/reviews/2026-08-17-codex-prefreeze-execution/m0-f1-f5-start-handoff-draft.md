---
handoff_id: TBD-M0-F1-F5-START-ID
status: DRAFT_NOT_AUTHORIZED
scope: one bounded local hermetic M0-F1-F5 run
expires_at: TBD-ONE-RUN-EXPIRY
---

# Draft Start Handoff: M0-F1 through M0-F5

## Authority state

This is a draft only. It does not start M0-F1 through M0-F5 and does not authorize production access, M1/M2 work, mutation, commit, push, pull request creation, deployment, external messaging, publication, or Committee Acceptance.

The run may start only after every placeholder and gate below is resolved against the same immutable packet/spec bytes. A prepared patch, passing dry-run, green Phase A suite, or historical verdict is not sufficient authority.

## Whole goal and bounded run

- **Whole goal:** complete the fixture-backed M0 Flight Readiness MVP for one frozen contract while preserving the separate gates for production evidence, live review, calibrated evaluation, M1/M2, and Committee Acceptance.
- **Current bounded run:** implement only M0-F1 through M0-F5 against hermetic fixtures and the accepted exact packet/spec binding.
- **Stop boundary:** stop after the one authorized run or immediately on any halt condition. Preserve reviewable partial evidence and do not renew or expand the budget by inference.

## Exact accepted bindings — required before start

| Binding | Required value |
| --- | --- |
| Final packet path | `TBD-ABSOLUTE-FINAL-PACKET-PATH` |
| Final packet revision label | `TBD-FINAL-PACKET-REVISION` |
| Final packet SHA-256 | `sha256:TBD-64-LOWERCASE-HEX` |
| Controlling architecture-spec path | `TBD-ABSOLUTE-FINAL-SPEC-PATH` |
| Controlling architecture-spec revision label | `TBD-FINAL-SPEC-REVISION` |
| Controlling architecture-spec SHA-256 | `sha256:TBD-64-LOWERCASE-HEX` |
| CE plan SHA-256 observed at authorization | `sha256:TBD-64-LOWERCASE-HEX` |
| Sequencing SHA-256 observed at authorization | `sha256:TBD-64-LOWERCASE-HEX` |
| Phase A package aggregate SHA-256 | `sha256:TBD-64-LOWERCASE-HEX` |
| Authorized branch and HEAD | `TBD-BRANCH` / `TBD-40-HEX-HEAD` |

Changing any bound packet or spec byte invalidates this draft and requires a superseding exact-digest review and Owner acknowledgement.

## Required review and acknowledgement receipts

| Receipt | Required value |
| --- | --- |
| Independent packet/spec reviewer identity | `TBD-INDEPENDENT-REVIEWER` |
| Independent verdict | `TBD-accept-or-accept_with_changes-with-zero-unresolved-material-ambiguity` |
| Independent verdict timestamp | `TBD-ISO-8601` |
| Independent verdict packet/spec digests | `TBD-EXACT-DIGEST-PAIR` |
| Independent Phase A verdict | `TBD-PASS-OR-PASS_WITH_GAPS-WITH-DISPOSITION` |
| Phase A verdict package aggregate | `sha256:TBD-64-LOWERCASE-HEX` |
| Owner acknowledgement identity | `TBD-OWNER` |
| Owner acknowledgement | `TBD-ACKNOWLEDGED-EXACT-BINDING-AND-START` |
| Owner acknowledgement timestamp | `TBD-ISO-8601` |
| Start receipt ID | `TBD-START-RECEIPT-ID` |

Historical verdicts remain bound to their historical digests and must not be copied onto the final bytes.

## One-run execution budget — all fields required

| Budget field | Required value |
| --- | --- |
| Implementation lead | `TBD-NAMED-LEAD` |
| Active-time cap | `TBD-DURATION` |
| Full-suite invocation cap | `TBD-NONNEGATIVE-INTEGER` |
| Source-read cap | `TBD-NONNEGATIVE-INTEGER; expected 0 production reads` |
| Tool-call cap | `TBD-NONNEGATIVE-INTEGER` |
| Allowed file roots | `TBD-EXACT-LOCAL-PACKAGE-AND-FIXTURE-ROOTS` |
| Allowed commands | `TBD-EXACT-HERMETIC-COMMANDS` |
| Start time | `TBD-ISO-8601` |
| Expiry | `TBD-ISO-8601-OR-ONE-RUN-TERMINAL-EVENT` |
| Halt owner | `TBD-NAMED-HALT-OWNER` |
| Partial-result path | `TBD-RECEIPT-OR-HANDOFF-PATH` |

No missing or exceeded budget field may be repaired by silently consuming more time, reads, runs, or tools.

## Authorized work

1. **M0-F1:** encode the accepted M0 contracts, including one stored `analysis_use` state, derived render-time eligibility, declared `runtime_only | runtime_and_sample` sufficiency, fail-closed arm-parity applicability, typed next safe action, and immutable packet fields.
2. **M0-F2:** implement fixture-only reads, admission, independent recomputation receipts, partial/error/pagination behavior, and typed no-body redaction failure.
3. **M0-F3:** implement the exact frozen deterministic check inventory and D1/D2 failure mappings without post-hoc power computation.
4. **M0-F4:** seal the immutable packet and render the synthetic packet-centered review projection without persisting derived eligibility or introducing M1/M2 content.
5. **M0-F5:** implement threshold-free fixtures, trivial baselines, adversarial decoys, reviewer-conflict evidence, and hard vetoes.

## Required halt conditions

Halt immediately and preserve a partial receipt if:

- the live packet/spec digest differs from the authorized binding;
- any unresolved semantic choice would require inventing Owner meaning;
- a fail-closed default, closed enum, derived-readiness rule, or materiality ceiling can be bypassed;
- any production adapter, network socket, secret, production credential, external message, publication path, or mutation capability becomes reachable;
- identical frozen inputs produce different packet bytes or digests;
- a required arm-parity, sufficiency, SRM, CUPED, metric-version, unit/estimator, redaction, or authorization fixture cannot produce its declared failure state;
- the exact run/read/tool/active-time cap or expiry is missing or exceeded; or
- the work would cross into M1/M2, P2/P3/P4 closure, production authorization, or Committee Acceptance.

## Exit evidence

The run is complete only when the companion completion ledger has observable evidence for every M0-F1-F5 row and the final receipt records:

- exact packet/spec/revision/digest binding used by every semantic unit;
- changed files and proof that changes stayed within the authorized roots;
- exact hermetic commands and results within the one-run budget;
- deterministic packet/check digest reproduction;
- fixture, baseline, decoy, hard-veto, capability-isolation, and no-network/no-write evidence;
- unresolved gaps and next safe action; and
- explicit separation of local M0 verification, local MVP completion, production authorization, and Committee Acceptance.

## Terminal status vocabulary

- `COMPLETE_LOCAL_M0_EVIDENCE`: every in-scope ledger item is verified; no broader gate is implied.
- `PARTIAL_HALTED`: at least one in-scope item is incomplete and a halt condition fired; preserve exact evidence and blocker.
- `NOT_STARTED`: any binding, independent verdict, Owner acknowledgement, or one-run budget field is missing.

