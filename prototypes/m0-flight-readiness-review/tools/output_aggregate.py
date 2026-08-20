"""Compute the exact-byte aggregate over the two owned output roots.

Algorithm, stated so an independent reviewer can reproduce it byte for byte:

  1. Collect every regular file under `prototypes/m0-flight-readiness-review/`
     and `docs/reviews/2026-08-18-m0-flight-readiness-review-surface/`.
  2. Drop any path containing `__pycache__`, `.pytest_cache`, `.omc`,
     `.DS_Store`, or a `.chrome-profile` directory. These are runtime or tool
     state, never deliverable bytes.
  3. Drop the two self-referential outputs that record this digest:
     `evidence-receipt.md` and `status.json`. A digest cannot contain itself.
  4. Sort the remaining repository-relative POSIX paths ascending by code point.
  5. Build one line per file: the file's lowercase hex SHA-256, two spaces, the
     repository-relative path, and a newline.
  6. The aggregate is the SHA-256 of the UTF-8 concatenation of those lines.

This is the same recipe the accepted M0 package aggregate uses, so a reviewer
who can reproduce `9eea3014...b19a` can reproduce this with the same procedure.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from bindings import REPO_ROOT, file_sha256

OWNED_ROOTS = (
    "prototypes/m0-flight-readiness-review",
    "docs/reviews/2026-08-18-m0-flight-readiness-review-surface",
)

EXCLUDED_PARTS = ("__pycache__", ".pytest_cache", ".omc", ".chrome-profile")
EXCLUDED_NAMES = (".DS_Store",)
SELF_REFERENTIAL = (
    "docs/reviews/2026-08-18-m0-flight-readiness-review-surface/evidence-receipt.md",
    "docs/reviews/2026-08-18-m0-flight-readiness-review-surface/status.json",
)

RECIPE = (
    "sha256 over the concatenation of '<sha256>  <repository-relative-path>\\n' lines, "
    "ascending by path, for every file under prototypes/m0-flight-readiness-review/ and "
    "docs/reviews/2026-08-18-m0-flight-readiness-review-surface/, excluding __pycache__, "
    ".pytest_cache, .omc, .chrome-profile and .DS_Store, and excluding the two "
    "self-referential outputs evidence-receipt.md and status.json"
)


def owned_files() -> list[str]:
    names: list[str] = []
    for root in OWNED_ROOTS:
        base = REPO_ROOT / root
        if not base.is_dir():
            continue
        for candidate in base.rglob("*"):
            if not candidate.is_file():
                continue
            if any(part in EXCLUDED_PARTS for part in candidate.parts):
                continue
            if candidate.name in EXCLUDED_NAMES:
                continue
            relative = candidate.relative_to(REPO_ROOT).as_posix()
            if relative in SELF_REFERENTIAL:
                continue
            names.append(relative)
    names.sort()
    return names


def aggregate() -> dict[str, object]:
    names = owned_files()
    entries = [{"path": name, "sha256": file_sha256(REPO_ROOT / name)} for name in names]
    manifest = "".join(f"{item['sha256']}  {item['path']}\n" for item in entries)
    return {
        "recipe": RECIPE,
        "file_count": len(entries),
        "aggregate_sha256": hashlib.sha256(manifest.encode("utf-8")).hexdigest(),
        "excluded_self_referential": list(SELF_REFERENTIAL),
        "files": entries,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", action="store_true", help="print every file and digest")
    args = parser.parse_args()

    result = aggregate()
    if args.manifest:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"file_count       {result['file_count']}")
        print(f"aggregate_sha256 {result['aggregate_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
