# Independent Rereview — M0 Correction Round 2

## Verdict

`REJECT_LOCAL_M0_EVIDENCE`

The required package aggregate and all frozen/supporting bindings reproduce exactly. The live evaluator now executes nineteen named check-specific validators, fails closed for contradictory, absent, malformed, unauthorized, and typed-disagreement inputs, restores the nine previously removed semantic cases, runs the nineteen-case sealed corpus and all hard vetoes, reproduces the canonical packet under five hash seeds, and remains inside its declared local-only capability boundary.

The package is nevertheless not acceptable local M0 evidence. `FlightReadinessPacket.deserialize` validates independently recomputable content hashes and identifier presence, but it does not validate the semantic relation between a check, its validator receipt, its source receipt, and its evidence identity. A blocked packet was promoted to `decision_grade` by changing CHK-05 from `FAIL` to `PASS`, recomputing the check digest and outer packet digest, removing the CHK-05 gap, and updating the readiness projection. Deserialization returned the promoted document even though the still-bound validator receipt said `CHK-05:FAIL`. Fully resealed validator-source lineage, validator identity, and evidence-lineage mutations were also accepted.

This verdict rejects only the corrected local fixture-backed M0 evidence claim. Phase A remains separate. Production authorization and capability, P2/P3/P4, M1/M2, deployment, publication, and Experiment Review Committee Acceptance remain open, unestablished, or unauthorized.

## Independence and scope

- The reviewer did not author the implementation or correction bytes and treated receipts, planted truth, and pass counts as unverified claims.
- No subagent or second reviewer was started. No external or production system, credential, network source, Git mutation, commit, push, deployment, publication, or other external action was used.
- Regression and adversarial work used disposable copies under `/private/tmp`.
- The only repository outputs written are this report and `independent-rereview-status.json`.

## Exact-byte binding

| Item | Independently recomputed SHA-256 | Result |
| --- | --- | --- |
| Round 2 rereview handoff | `e0e275f087a6bad19b648c4c18c2e53f3cdd8286d42be37cfbf484ab59ccb490` | observed current handoff |
| Sorted 59-file package aggregate | `52d4c82e2a80ffc5a42bc80918165b33ebed0b03256a27c7c7bc78bd8046d2f6` | exact required match; generated manifest byte-identical to `source-manifest-after.sha256` |
| Frozen packet | `82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` | exact match |
| Controlling architecture | `9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` | exact match |
| CE plan | `2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` | exact match |
| Sequencing plan | `8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` | exact match |

The package aggregate was recomputed from sorted repository-relative `.py`, `.json`, and `.md` paths below `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`. No drift block applies.

## Required verification

### Three-directory suite and five-seed builder

| Verification | Independent result |
| --- | --- |
| Repository root | `344 passed in 0.84s` |
| Package root | `344 passed in 0.87s` |
| Unrelated `/private/tmp` with explicit `PYTHONPATH` | `344 passed in 0.87s` |
| Seeds `0`, `1`, `42`, `99991`, `random` | identical on every run |
| Serialized byte count | `44044` |
| Serialized-byte SHA-256 | `cea0119be0588fe5746c2d6bd2da57c577332952c8ec17cf86171d9e8176dc4f` |
| Internal packet digest | `sha256:4135a724d70e0300d44ee431d1299fcdb9882b67a144b72e7cdaa4f88594c076` |

### Evaluator API, validators, and fail-closed behavior

- `.agents/skills/kdd_data_agent/m0/evaluator.py:1-21` is the public typed API and delegates to the internal implementation in `corrected_evaluator.py`.
- All nineteen named validators execute through the public evaluator. Replacing all nineteen observations with contradictory garbage produced zero `PASS` outcomes and `not_permitted`. The nineteen-case per-check contradiction matrix made each named check `FAIL`; removing an observation produced `MISSING`; a malformed observation produced materiality `unknown` and `not_permitted`.
- The trusted packet contains nineteen unique evidence identities and nineteen unique validator receipt identities. In the packet produced directly by the evaluator, every validator receipt binds the source receipt and contract digest, carries a unique observation digest, and binds the source body digest. This correct construction does not cure the deserialization finding below.
- The real unauthorized/no-body fixture produces CHK-16 `FAIL` and `not_permitted`. A typed reported/recomputed disagreement produces CHK-14 `FAIL`, remains visible, and is compared internally under `m0-comparison-rule/v1`. `same_pipeline` produces materiality-`UNKNOWN` and `not_permitted`. Public reconstruction with `dataclasses.replace` cannot promote a blocked typed packet.

### Sealed corpus, baselines, decoys, conflict, vetoes, and drift

All nineteen sealed cases executed through the public evaluator: one `decision_grade`, one `directional_only`, and seventeen `not_permitted`. Both trivial baselines were contradicted. The metric-version, CUPED-mode, and source-identity decoys, reviewer conflict, and all six typed hard vetoes reached their planted fail-closed outcomes through the same evaluator.

In disposable copies, changing a trusted fixture byte without updating the corpus pin failed with `fixture bytes drifted for m0-read-trusted-001`. Changing only planted truth for `m0-trusted` failed with `real evaluator contradicted planted truth for m0-trusted`. Fixture bytes and planted truth therefore cannot drift independently without detection.

### Test-count reconciliation

An exact Round 1 package was reconstructed in `/private/tmp` by matching all 59 files byte-for-byte to the Round 2 before-manifest. Normalized collected node-ID comparison against current bytes found exactly 31 additions and zero removals, explaining `313 -> 344`.

The additions are nineteen public-evaluator contradiction cases, the restored unknown-materiality ceiling, arbitrary-present and absent-observation regressions, and ten serialized-boundary cases. The eight previously removed named failures for CHK-03, CHK-05, CHK-06, CHK-08, CHK-11, CHK-12, CHK-15, and CHK-16 now have public-evaluator contradiction cases, and the ninth removed unknown-materiality case is restored. These are behavior assertions, not metadata-only inflation. The restored count is valid, but it omits the fully resealed relational attacks reproduced below.

### Frozen and capability boundary

The frozen packet, architecture, CE plan, and sequencing-plan digests remain invariant. Capability/import/no-write/no-network tests passed in the full suite and in the targeted 136-test M0/capability run. `.agents/skills/kdd_data_agent/core/capabilities.py:18-26` declares only `fixture_read`, `local_deterministic_compute`, and `in_memory_append`; `adapters/production` is absent. This is local capability evidence only, not production authorization or production-backed capability.

## Findings

### IR-M0-01-RR — BLOCKER: fully resealed checks and validator lineage can promote a blocked serialized packet

**Current anchors:** `.agents/skills/kdd_data_agent/m0/packet.py:314-365`; `.agents/skills/kdd_data_agent/m0/packet.py:555-617`; `.agents/skills/kdd_data_agent/m0/packet.py:618-681`; `.agents/skills/kdd_data_agent/m0/corrected_evaluator.py:458-490`.

`_verify_serialized_checks` recomputes each check's unkeyed digest and requires evidence strings to look like digests and receipt IDs to exist. It does not require the bound validator receipt's `outcome`, `validator_id`, actor, reason, observation digest, source-body digest, or derivation inputs to agree with the check. Receipt verification independently recomputes the receipt ID/digest, but does not enforce those cross-record relations. Readiness is then derived from the attacker-resealed check fields.

Fresh adversarial results:

```text
ACCEPTED_INVALID_FULLY_RESEALED_CHECK_PROMOTION:decision_grade
ACCEPTED_INVALID_RESEALED_VALIDATOR_SOURCE_LINEAGE
ACCEPTED_INVALID_RESEALED_CHECK_EVIDENCE_LINEAGE
ACCEPTED_INVALID_RESEALED_VALIDATOR_IDENTITY
```

**Impact:** untrusted serialized bytes can rewrite a validator failure into a pass and expose a blocked fixture packet as decision-grade. Check-specific evidence and receipt lineage are present in evaluator-created packets but are not enforced at the public deserialization boundary.

**Minimal correction:** deserialize into and validate the complete typed relational graph. For each check, require the exact source/validator receipt pair; require validator actor, ID, outcome, reason, contract digest, source receipt, source-body digest, and observation digest to agree; recompute the check evidence identity from those fields; and require exact gap/check correspondence. If a fully self-consistent reseal must be distinguishable from the original creator, bind deserialization to an external trusted expected digest or authenticated seal, because self-contained unkeyed content hashes alone cannot provide that authenticity. Add the exact fully resealed CHK-05 promotion and all three lineage probes as regressions.

### IR-M0-TEST-RR — MAJOR: serialized-boundary tests stop at stale or nonexistent bindings

**Current anchors:** `.agents/skills/kdd_data_agent/tests/test_m0_packet.py:71-102`; `.agents/skills/kdd_data_agent/tests/test_m0_packet.py:105-133`; `.agents/skills/kdd_data_agent/m0/packet.py:351-365`.

The new tests correctly reject a stale check digest, stale nested identities, a resealed noncanonical inventory, a frozen-binding mutation, and a nonexistent receipt ID. The check/receipt/evidence rebinding test changes the receipt reference to `rcpt_missing`; it does not replace it with a fully resealed, present validator receipt or recompute a plausible evidence identity. Consequently all 344 tests pass while the four attacks above are accepted.

**Impact:** the suite proves content-address and inventory checks but overstates complete nested identity-graph verification. It cannot prevent regression to false serialized readiness when an attacker reseals the linked records.

**Minimal correction:** add public-deserializer tests for a fully resealed blocking-check promotion; a present but wrong validator receipt; altered validator source derivation; recomputed arbitrary evidence lineage; and exact gap/check correspondence. Each must be rejected before a document is returned.

## Round 2 disposition and preserved boundaries

| Item | Independent disposition | Basis |
| --- | --- | --- |
| `IR-M0-01-RR` | `REJECTED` | stale digest is closed, but fully resealed check promotion and lineage mutation remain open |
| `IR-M0-03-RR` | `CORRECTED_IN_LIVE_EVALUATOR` | all nineteen semantic validators and absent/malformed/garbage ceilings pass; serialized proof remains unsafe through `IR-M0-01-RR` |
| `IR-M0-TEST-RR` | `REJECTED` | restored semantic cases are valid, but full-reseal attacks are untested |
| `IR-M0-02` | `PRESERVED_CORRECTED` | unauthorized/no-body fixture fails closed |
| `IR-M0-04` | `PRESERVED_CORRECTED` | typed outputs are compared internally under the versioned rule |
| `IR-M0-05` | `PLUMBING_PRESERVED_WITH_REJECTING_SERIALIZATION_DEPENDENCY` | corpus, baselines, decoys, conflict, vetoes, and drift checks execute correctly |
| `IR-M0-06` | `PRESERVED_CORRECTED` | named five-seed builder reports both digest namespaces truthfully |

No part of this rereview promotes Phase A evidence, establishes production authorization or production-backed M0 capability, closes P2/P3/P4, authorizes or completes M1/M2, deploys, publishes, or establishes Experiment Review Committee Acceptance.
