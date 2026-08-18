# Phase A Independent Verification Handoff

Created: 2026-08-17  
Repository: `/Users/surahli/Documents/projects/SMA_v2`  
Expected branch: `codex/kdd-data-agent-practices-research`  
Mode: independent adversarial review; read-only except for the two review outputs named below  
Reviewer: fresh Claude Opus 5 at high effort

## Mission

Independently answer review questions Q11 and Q12 for the current Phase A package. Do
not review or freeze the architecture packet as a substitute for this task. Determine
whether Phase A remains semantics-independent and replaceable, and independently test
its mechanical claims without trusting any self-authored receipt or a prior reviewer
verdict.

The reviewer must not have authored the Phase A implementation, the Codex continuation,
the Phase A receipts, or the earlier Opus freeze review. This session is intended to be
that fresh third reviewer.

## Current binding to verify before review

- Freeze-candidate packet:
  `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md`
- Expected post-edit packet SHA-256:
  `67c844d10dcafcf2637388bf579dfcd9866d7d69ea6f4d3b456fd6b6b15dfcfa`
- Controlling architecture spec:
  `docs/research/kdd-data-agent-workshop/final-architecture-spec.md`
- Expected post-edit spec SHA-256:
  `3b20c93859b78074b653d375fc29f60bd40993b3f3bcb4ee2ff481e8ba8706b8`
- Phase A package: `.agents/skills/kdd_data_agent/`
- Previously receipted package aggregate, excluding caches and `.omc` harness state:
  `2f1001b93b19b2318c4c6419205ed2f7778ac23c02533e78a0c0899f15bf7d1e`

Recompute all three values. If any value differs, bind findings to the observed bytes
and report the mismatch. Do not silently reuse a historical digest.

### Main-orchestrator observation after the first rate-limited review attempt

At `2026-08-17T20:03-07:00`, the live package excluding `.omc`, bytecode, and pytest
caches was `diff -qr` identical to the isolated review copy retained at
`/Users/surahli/.claude/jobs/671d8db1/tmp/mut1/kdd_data_agent`. However, the aggregate
claim above was not reproducible from the command later published by that review:

- from the repository root, the published `find ... | sort | xargs shasum | shasum`
  shape with `.omc` excluded produced
  `28276ec2d15af6f66d58472056d04357b1d16aa6c99b25c3aed7fef00e3806ad`;
- from the package root, using relative paths and the same exclusions produced
  `a38474375ed8f0a5ea6aa72dc1594388f7293881391dbd7db20c0d07bfc1df20`
  for both the live package and the retained isolated copy;
- the live package now also contains
  `.omc/state/sessions/61ce23e2-d4b8-468a-aec2-7188ad6714f5/pre-tool-advisory-throttle.json`.
  Including harness-state JSON makes the aggregate drift again and is not a valid
  source binding.

Treat this as a digest-contract question to resolve independently, not as proof that
the source changed. Define and report a reproducible manifest algorithm with explicit
root-relative paths, file extensions, directory exclusions, and ordering. Report both
the stable source-manifest digest and any historical aggregate mismatch. Do not force
the result to equal `2f1001...`.

## Authority and evidence discipline

Treat implementation receipts and earlier reviews as claims to test, not as authority.
The current alignment packet and controlling architecture spec define the candidate
semantics, but neither constitutes a freeze record. Owner decisions and the closed
canonical policy contract outrank reviewer preferences.

Do not copy the earlier Opus Phase A verdict. That reviewer later declined Q11 and Q12
for conflict of interest, and Codex is also not independent because it authored the
continuation. The earlier probes are useful test ideas only.

Read first:

1. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-freeze-codex-fix-handoff.md`
2. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-freeze-codex-disposition.md`
3. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-freeze-opus5-review-handoff.md`, especially Q11 and Q12
4. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-freeze-opus5-adversarial-review.md`, especially section `Phase A independent verification`; use as hypotheses, not acceptance
5. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-multiagent-review-consolidated.md`
6. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-prealignment-foundation-receipt.md`
7. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-codex-continuation-receipt.md`
8. `docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-codex-continuation-status.json`
9. The current packet, controlling spec, closed policy contract, and the complete Phase A package and tests.

## Q11: semantic independence

Determine whether Phase A has silently selected any meaning that the current packet,
Owner record, or closed policy contract has not frozen. At minimum examine:

- readiness, check-inventory, materiality, packet, acceptance-ID, UI, fixture-baseline,
  and budget seams;
- the current `CoverageGapKind` taxonomy and its mapping to canonical policy dimensions;
- `AuthorizationState` versus redaction-failure state;
- stale `packet_reference` values and removed acceptance IDs;
- no-retained-body comments and receipts that cite the former colliding
  `M0-READ-001` / `M0-SEC-001` identifiers as independent authority;
- whether any provisional Python mechanism or fixture vocabulary has become an
  accidental product contract;
- whether the post-edit coordinated readiness fields, legal pair policy,
  preregistered power/MDE sufficiency, and arm-parity contract are still blocked at
  the seams rather than pre-decided by Phase A.

Classify every semantic issue as one of:

- `semantics_independent`;
- `stale_reference_only`;
- `unratified_semantic_choice`;
- `contradicts_current_packet`;
- `requires_owner_or_policy_ruling`.

## Q12: independent mechanical verification

Run fresh tests and adversarial probes. Do not treat the existing 225-pass count,
mutation results, or receipts as sufficient. Use isolated copies under a fresh
temporary directory for every mutation or fault injection. Do not mutate the live
package.

At minimum verify:

1. Complete test-suite result from the repository root and at least one alternate
   working directory, with caches and bytecode disabled.
2. Deterministic serialized bytes and digests across fresh processes and multiple
   `PYTHONHASHSEED` values using identical frozen inputs.
3. Deep immutability, append-only revision behavior, duplicate-receipt handling,
   seal-chain verification, and build-receipt binding.
4. Receipt identity sensitivity to source, actor, authorization state, observation
   interval, detail, Coverage Gaps, and derivation inputs.
5. Fail-closed parsing of invalid authorization values and exact-key fixture/manifest
   validation.
6. Canonical JSON behavior for reserved-sentinel smuggling on decode, duplicate keys,
   non-finite numbers, floats including `1.0` and `-0.0`, lone surrogates, non-string
   keys, sets, bytes, and cross-process byte stability. Distinguish documented
   protocol deviations from bugs.
7. Coverage Gap materiality rule-source validation, including empty, whitespace-only,
   arbitrary, sentinel, and versioned rule-source shapes; verify the default mapping.
8. Static capability scanner reachability and non-vacuity, including planted forbidden
   imports/calls, unscanned Python files, symlinks, aliases, and dynamic-call limits.
9. Runtime audit evidence for the exercised hermetic path: filesystem writes, network,
   subprocess, credential access, wall-clock reads, and reads outside the expected
   package/fixture surface. Clearly state that this is not an OS sandbox proof.
10. Test reachability through isolated mutation probes, especially the previously
    reported live defects: receipt-identity field removal, fail-open authorization
    parsing, seal-chain guard removal, forbidden-clock/read scanner removal, body-policy
    and case-ID call-site unwiring, and build-receipt assertions.

If a probe is unsafe, nondeterministic, or not feasible, report it as an untested
boundary rather than inferring a pass.

## Verdict and proof boundaries

Return exactly one Phase A verdict:

- `PASS`: all material Phase A claims independently hold and no unratified semantic
  choice remains;
- `PASS_WITH_GAPS`: the foundation is usable but named gaps remain, with an explicit
  statement of which gaps block M0-F1 start or M0-F0 acceptance;
- `FAIL`: a material claim is false or the package has chosen a contradictory semantic
  contract.

Keep these separate in the report:

1. Phase A foundation verification;
2. local fixture-backed M0 MVP completion;
3. production authorization;
4. Experiment Review Committee acceptance.

A Phase A pass cannot freeze the packet, authorize M0-F1 through M0-F5, prove the local
M0 MVP, authorize production access, or stand in for Committee acceptance.

## Output contract

Write only:

- `docs/research/kdd-data-agent-workshop/reviews/2026-08-17-phase-a-independent-verification/phase-a-independent-review.md`
- `docs/research/kdd-data-agent-workshop/reviews/2026-08-17-phase-a-independent-verification/phase-a-independent-status.json`

The Markdown report must include:

- exact reviewed path/digest bindings;
- reviewer identity, model, session ID, timestamp, and conflict-of-interest statement;
- commands and observable results;
- Q11 classification table;
- Q12 claim/probe/result/evidence table;
- findings ordered by `BLOCKER`, `MAJOR`, then `MINOR`, each with exact file/line
  evidence, consequence, and minimal correction;
- mutation/fault-injection matrix including survivors;
- untested boundaries;
- one Phase A verdict and the four separated proof states;
- a statement of whether M0-F1 may start from the Phase A evidence alone. The expected
  authority answer is no unless a separate accepted freeze binding and fresh Owner
  authorization exist.

The JSON status must include the same digests, verdict, severity counts, commands,
test counts, mutation totals/survivors, runtime-event counts, untested boundaries,
and output-file digests.

## Boundaries and stop conditions

- Review-only. Do not edit Phase A source, tests, fixtures, canonical docs, packets,
  plans, ADRs, or any prior receipt/review.
- Do not write a freeze record or implementation handoff.
- Do not commit, push, open a PR, install dependencies, access production, deploy,
  send messages, or modify external systems.
- Preserve the dirty worktree and all user-owned changes.
- You may write temporary isolated test copies only under a fresh `/private/tmp`
  directory and remove only that exact directory when finished.
- No subagents or workflows for this review; independence belongs to this fresh Opus
  context. Stop after one complete report plus one mechanical self-check of the two
  output files.
- If the live package changes during review, stop and report byte drift instead of
  mixing findings across versions.
