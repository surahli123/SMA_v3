"""Exact input bindings for the fixture-only M0 review surface.

Every tool in this prototype recomputes these digests before it does semantic
work and halts on drift. The values are the ones carried by the canonical M0
freeze record, the repository provenance file, and the Round 5 independent
review; nothing here re-derives or relaxes them.

This module reads repository files. It never writes to them, never reaches the
network, and never imports anything outside the Python standard library.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
"""Repository root, resolved from this file so any working directory works."""

PROTOTYPE_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / ".agents" / "skills"
PACKAGE_ROOT = SKILLS_ROOT / "kdd_data_agent"

PACKAGE_AGGREGATE_SUFFIXES = (".py", ".json", ".md")
PACKAGE_AGGREGATE_EXCLUDED_DIRS = ("__pycache__", ".pytest_cache", ".omc")
PACKAGE_AGGREGATE_RECIPE = (
    "sha256 over the concatenation of '<sha256>  <repository-relative-path>\\n' lines, "
    "ascending by path, for every .py, .json and .md file below "
    ".agents/skills/kdd_data_agent/, excluding __pycache__, .pytest_cache and .omc"
)


class BindingDrift(RuntimeError):
    """Raised when a bound input no longer matches its accepted digest."""


@dataclass(frozen=True)
class FileBinding:
    role: str
    path: str
    revision: str
    sha256: str


FILE_BINDINGS = (
    FileBinding(
        role="M0 build contract",
        path="docs/research/kdd-data-agent-workshop/reviews/2026-08-16-opus5-m0-alignment/m0-m2-build-alignment-packet.md",
        revision="m0-alignment-v1",
        sha256="82747da96d66dd8851c03edc837f38597264a07794a2b145cd530ca0a5f07b19",
    ),
    FileBinding(
        role="Architecture",
        path="docs/research/kdd-data-agent-workshop/final-architecture-spec.md",
        revision="kdd-data-agent-architecture-v1",
        sha256="9508b42979b5f708d3b0be7016ed414fd0b4c28d531b75fd0a4710eb46df8fc1",
    ),
    FileBinding(
        role="CE plan",
        path="docs/plans/2026-08-12-001-feat-kdd-data-agent-greenfield-plan.md",
        revision="observed supporting plan",
        sha256="2b4bbd3583e2f289303b8e47b255e3b53bd0f3307f0b699b33299b57aa9e1daf",
    ),
    FileBinding(
        role="Sequencing",
        path="docs/research/kdd-data-agent-workshop/implementation-sequencing.md",
        revision="observed supporting sequence",
        sha256="8fec2f8c3c3d22aa9dc1b762769673789d007fd74dbbed9c34e5ea88fcd4725b",
    ),
)

ACCEPTED_PACKAGE_AGGREGATE = "9eea3014cb74acc48e9bbd24a486d2b6a5a4a4f57ae76191f42d037a5988b19a"
ACCEPTED_PACKAGE_FILE_COUNT = 59
ACCEPTED_PACKAGE_VERDICT = "ACCEPT_LOCAL_M0_EVIDENCE"


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def package_manifest_lines() -> list[str]:
    """The exact `<sha256>  <path>` manifest the accepted aggregate hashes."""
    files: list[str] = []
    for candidate in PACKAGE_ROOT.rglob("*"):
        if not candidate.is_file() or candidate.suffix not in PACKAGE_AGGREGATE_SUFFIXES:
            continue
        if any(part in PACKAGE_AGGREGATE_EXCLUDED_DIRS for part in candidate.parts):
            continue
        files.append(candidate.relative_to(REPO_ROOT).as_posix())
    files.sort()
    return [f"{file_sha256(REPO_ROOT / name)}  {name}\n" for name in files]


def package_aggregate() -> tuple[str, int]:
    lines = package_manifest_lines()
    return hashlib.sha256("".join(lines).encode("utf-8")).hexdigest(), len(lines)


def verify_bindings() -> dict[str, object]:
    """Recompute every bound input. Raise `BindingDrift` on any mismatch."""
    observed: list[dict[str, str]] = []
    drift: list[str] = []
    for binding in FILE_BINDINGS:
        target = REPO_ROOT / binding.path
        if not target.is_file():
            drift.append(f"{binding.path}: file is absent")
            continue
        digest = file_sha256(target)
        observed.append(
            {
                "role": binding.role,
                "path": binding.path,
                "revision": binding.revision,
                "expected_sha256": binding.sha256,
                "observed_sha256": digest,
            }
        )
        if digest != binding.sha256:
            drift.append(f"{binding.path}: expected {binding.sha256}, observed {digest}")

    aggregate, count = package_aggregate()
    observed.append(
        {
            "role": "Accepted M0 package",
            "path": ".agents/skills/kdd_data_agent/",
            "revision": ACCEPTED_PACKAGE_VERDICT,
            "expected_sha256": ACCEPTED_PACKAGE_AGGREGATE,
            "observed_sha256": aggregate,
        }
    )
    if aggregate != ACCEPTED_PACKAGE_AGGREGATE:
        drift.append(f"accepted package aggregate: expected {ACCEPTED_PACKAGE_AGGREGATE}, observed {aggregate}")
    if count != ACCEPTED_PACKAGE_FILE_COUNT:
        drift.append(f"accepted package file count: expected {ACCEPTED_PACKAGE_FILE_COUNT}, observed {count}")

    if drift:
        raise BindingDrift("bound inputs drifted; halting before semantic work:\n  " + "\n  ".join(drift))

    return {
        "recipe": PACKAGE_AGGREGATE_RECIPE,
        "package_file_count": count,
        "bindings": observed,
    }


if __name__ == "__main__":  # pragma: no cover - operator entry point
    import json

    print(json.dumps(verify_bindings(), indent=2, sort_keys=True))
