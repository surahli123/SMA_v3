# SMA v3 Pre-Push Verification Receipt

Verified: 2026-08-18 (America/Los_Angeles)

Terminal state: `READY_TO_PUSH_PRIVATE_MAIN`

## Repository Authority

- Authenticated GitHub account: `surahli123`.
- Target: `surahli123/SMA_v3`.
- GitHub state at verification: private, empty, viewer permission `ADMIN`.
- Target branch for the initial publication: `main`.

## Evidence Bindings

| Evidence | Fresh verification |
| --- | --- |
| Local M0 package | 59 files; aggregate `sha256:9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a` |
| Independent verdict | `ACCEPT_LOCAL_M0_EVIDENCE` |
| Frozen M0 packet | `sha256:82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19` |
| Frozen architecture | `sha256:9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1` |
| CE plan | `sha256:2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf` |
| Sequencing plan | `sha256:8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b` |
| Fable v3 draft custody | ledger `9ecd416d…7167`; design `ef51b40f…da4a`; overview `6b25d122…ea6`; flow `dae33ad6…e4d` |

## Mechanical and Safety Checks

- Three test invocations from the repository root, package root, and unrelated `/private/tmp`: `370 passed` each.
- Five `PYTHONHASHSEED` runs (`0`, `1`, `42`, `99991`, `random`) produced identical 47,075-byte evidence, serialized SHA-256 `7327bdb9…c9cc`, and internal digest `sha256:652a3d9…aa0`.
- Markdown: 168 files, 815 relative links, zero missing targets, zero unbalanced fences.
- JSON: 66 files, zero parse errors.
- Prototype JavaScript: syntax check passed.
- Gitleaks: no leaks over approximately 4.76 MB scanned.
- No `.omc`, `.workflow`, pytest cache, bytecode, `.env`, private audio/video/HEIC, or file over 10 MB.
- Exactly one non-English collaboration artifact remains: the Owner-requested six-question Chinese HTML. Durable Markdown is English.
- Source papers: PiTrace report SHA-256 `1114180…a572`; Cordiverse paper SHA-256 `4d48478d…b97f`.

## Proof Boundary

This receipt validates a private-repository export of research and accepted local fixture-backed evidence. It does not establish production M0 capability or authorization, close P2/P3/P4, implement M1/M2, authorize deployment or public release, or establish Experiment Review Committee Acceptance.

This is a pre-push receipt. The initial commit and remote `main` history are the authoritative proof of publication.
