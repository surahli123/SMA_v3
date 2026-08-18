# Independent Review Handoff — Local M0-F1 through M0-F5

Review target aggregate: `sha256:30d6b47ca55f1444ef8ba596aedabd90db5f21af58e60d53ad2320a5fc94c196`  
Source manifest: `source-manifest-after.sha256`  
Implementation terminal claim: `COMPLETE_LOCAL_M0_EVIDENCE`

## Required independent reproduction

1. Recompute the sorted `.py`/`.json`/`.md` aggregate under `.agents/skills/kdd_data_agent/`, excluding `__pycache__`, `.pytest_cache`, and `.omc`; require the target digest above.
2. Recompute the packet and architecture SHA-256 values from `implementation-receipt.md`.
3. Run `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider .agents/skills/kdd_data_agent/tests` from repository root, package root, and an unrelated temporary working directory with explicit `PYTHONPATH`.
4. Reproduce packet serialization across fresh processes and multiple `PYTHONHASHSEED` values; require 18,740 bytes and packet digest `sha256:51b7bc3bdeebb9422d022dcf293b63bb29d10d21a34b305bbc7a6a8e44a4f0f9` for the canonical trusted fixture builder.
5. Independently mutate receipt identity fields, authorization fail-open handling, rule resolution, seal verification, relative production imports, symlink scanning, fixture containment, seam authority, and body policy.
6. Adversarially inspect the nineteen-check registry, fixed floor, readiness mapping, declared sufficiency, arm parity, D4/D6 independence, Query Success union, material ceiling, packet contamination barrier, fixture matrix, decoys, reviewer provenance, and hard vetoes.

The reviewer must not treat the implementation receipt or green suite as an independent verdict. Report exact digest binding, conflicts of interest, commands, mutations, findings, and one verdict. Keep local M0 completion separate from production authorization, P2/P3/P4, M1/M2, deployment, and Committee Acceptance.
