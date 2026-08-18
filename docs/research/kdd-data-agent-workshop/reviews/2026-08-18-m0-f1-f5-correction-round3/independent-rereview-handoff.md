# Independent Rereview Handoff — M0 Correction Round 3

## Requested review

Perform a fresh, report-only independent rereview of exactly `IR-M0-01-RR` and `IR-M0-TEST-RR`. Do not adopt this implementation owner's conclusions. Preserve the accepted nineteen-validator evaluator behavior and the prior dispositions for `IR-M0-02`, `IR-M0-03-RR`, `IR-M0-04`, `IR-M0-05` plumbing, and `IR-M0-06`, but probe them if the new bytes could have regressed them.

This handoff does not start a reviewer.

## Hard binding

Independently recompute the sorted `.py`/`.json`/`.md` package manifest below `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`. Require exact aggregate:

`sha256:f32404705d3c32a9b1e09ba932db080ae1b1e63b6a55132c526457cec9e7c8ab`

Stop `BLOCKED_BY_DRIFT` if it differs. Independently verify the unchanged frozen packet, architecture, CE plan, and sequencing hashes recorded in the receipt and status.

## Required adversarial probes

1. Call `FlightReadinessPacket.deserialize` without `expected_packet_digest` and with a mismatched digest. Both must fail before returning a document.
2. Fully reseal the blocked CHK-05 packet into PASS: reseal the validator receipt, check evidence, check digest, readiness fields, gap inventory, and outer packet digest. Supply the original trusted packet digest out of band and require rejection.
3. Supply the attacker's new outer digest while independently mutating each relational field. Require rejection for a present-but-wrong validator receipt, validator actor, validator ID, outcome, reason, contract digest, source receipt, source-body digest, derivation inputs, and arbitrary evidence lineage.
4. Confirm the check evidence identity is recomputed from the exact typed actor, validator ID, outcome, reason, contract digest, source receipt, source-body digest, observation digest, and derivation inputs.
5. Reseal a gap whose check prefix remains CHK-05 but whose reason, evidence references, materiality, rule source, or next-safe-check differs. Require exact one-to-one correspondence rejection.
6. Confirm every check binds exactly one source receipt and one unique validator receipt and that no validator receipt proves multiple checks.
7. Re-run all nineteen semantic validators, the nineteen-case corpus, both trivial baselines, three decoys, reviewer conflict, six hard vetoes, unauthorized/no-body evidence, typed comparison disagreement, and `same_pipeline`.
8. Repeat the copied-package mutations that disable the trusted digest comparison, relation verifier, and gap verifier. The regression suite must kill all three.

## Expected local evidence

- Full suite from repository root, package root, and unrelated `/private/tmp`: `358 passed` each.
- Capability suite: `61 passed`; `adapters/production` absent.
- Seeds `0`, `1`, `42`, `99991`, and `random` all report:
  - serialized byte count: `46628`;
  - serialized-byte SHA-256: `47a3e56a7de91895087d2a7ce4437aae48daf39b2abdaf027390d4cc44676ddd`; and
  - internal packet digest: `sha256:9a421e1c3d003db70e14c6c9a0f4cc0263111e5c31c926b269b2948a8ebf4838`.

## Proof boundary

The trusted expected digest is an out-of-band local integrity binding, not a signature, secret, credential, production authorization, or Committee decision. An independent green rereview may accept only corrected local fixture-backed integrity evidence. It must not promote Phase A, establish production authorization or production-backed capability, close P2/P3/P4, authorize or complete M1/M2, deploy, publish, or establish Experiment Review Committee Acceptance.
