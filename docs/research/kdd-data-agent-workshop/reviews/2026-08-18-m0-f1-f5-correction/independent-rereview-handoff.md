# Independent Rereview Handoff — M0 IR-M0-01 through IR-M0-06 Correction

Review target aggregate: `sha256:c9c2d30fe588ce68fa1f45f93b83df768090f3ce7c0992516e8d31b224d4c901`  
Input rejected aggregate: `sha256:30d6b47ca55f1444ef8ba596aedabd90db5f21af58e60d53ad2320a5fc94c196`  
Source manifests: `source-manifest-before.sha256` and `source-manifest-after.sha256`

## Required fresh reproduction

1. Recompute the sorted `.py`/`.json`/`.md` aggregate under `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`; require the exact review target above.
2. Recompute all frozen/supporting bindings in `correction-receipt.md`; any mismatch is `BLOCKED_BY_DRIFT`.
3. Run the full suite from repository root, package root, and unrelated `/private/tmp` with explicit `PYTHONPATH`.
4. Run the named canonical builder under at least five fresh hash seeds. Distinguish raw serialized-byte SHA-256 from the packet's internal identity digest.
5. Independently reproduce the original `dataclasses.replace` readiness promotion and unauthorized fixture path; both must fail closed.
6. Remove or bypass one validator result/evidence binding for each check class and verify no absent check becomes `PASS`.
7. Attempt to restore caller-controlled D4/D6 comparison truth; typed output disagreement must still be derived internally and block.
8. Mutate a pinned fixture byte, planted truth, decoy, reviewer conflict, trivial baseline, and each hard-veto route in disposable copies. The corpus must reject drift or contradict the mutation through the public evaluator.
9. Reinspect capability/import/no-write/no-network boundaries and confirm no production adapter or external-action surface exists.

Do not inherit this implementation owner's conclusion. Report exact aggregate binding, commands, mutation results, conflicts, remaining gaps, and one independent verdict. Keep corrected local fixture evidence separate from Phase A evidence, production authorization/capability, P2/P3/P4, M1/M2, deployment/publication, and Committee Acceptance.
