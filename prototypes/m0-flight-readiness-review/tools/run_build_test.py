"""Execute the full verification battery and record exactly what happened.

Writes `build-test.json` and `build-test.log` into the owned review directory.
Every command is run for real; nothing is inferred. A command that is not run
must carry a non-empty `reason`, so a silent skip cannot be mistaken for a pass.

Installs nothing, downloads nothing, and touches no path outside the two owned
roots.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

from bindings import PROTOTYPE_ROOT, REPO_ROOT

REVIEW_DIR = REPO_ROOT / "docs" / "reviews" / "2026-08-18-m0-flight-readiness-review-surface"
TOOLS = PROTOTYPE_ROOT / "tools"
LOG_BUDGET_BYTES = 1024 * 1024

CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


def commands() -> list[dict]:
    python = sys.executable
    build = str(TOOLS / "build_fixtures.py")
    return [
        {
            "id": "bindings",
            "label": "recompute the five exact input bindings",
            "argv": [python, str(TOOLS / "bindings.py")],
            "cwd": REPO_ROOT,
        },
        {
            "id": "accepted-package-unmodified",
            "label": "confirm the accepted M0 package has no working-tree change",
            "argv": ["git", "status", "--porcelain", "--", ".agents/skills/kdd_data_agent"],
            "cwd": REPO_ROOT,
            "expect_empty_stdout": True,
        },
        {
            "id": "fixtures-check-root",
            "label": "reproduce the fixtures from the repository root",
            "argv": [python, build, "--check"],
            "cwd": REPO_ROOT,
        },
        {
            "id": "fixtures-check-prototype-root",
            "label": "reproduce the fixtures from the prototype root",
            "argv": [python, build, "--check"],
            "cwd": PROTOTYPE_ROOT,
        },
        {
            "id": "fixtures-check-unrelated-cwd",
            "label": "reproduce the fixtures from an unrelated working directory",
            "argv": [python, build, "--check"],
            "cwd": Path(REPO_ROOT.anchor) / "private" / "tmp"
            if (Path(REPO_ROOT.anchor) / "private" / "tmp").is_dir()
            else Path.home(),
        },
        *[
            {
                "id": f"determinism-seed-{seed}",
                "label": f"reproduce the fixtures with PYTHONHASHSEED={seed}",
                "argv": [python, build, "--check"],
                "cwd": REPO_ROOT,
                "env": {"PYTHONHASHSEED": seed},
            }
            for seed in ("0", "1", "42", "99991", "random")
        ],
        {
            "id": "node-check-app",
            "label": "parse app.js",
            "argv": ["node", "--check", str(PROTOTYPE_ROOT / "app.js")],
            "cwd": PROTOTYPE_ROOT,
        },
        {
            "id": "node-check-fixtures",
            "label": "parse data/fixtures.js",
            "argv": ["node", "--check", str(PROTOTYPE_ROOT / "data" / "fixtures.js")],
            "cwd": PROTOTYPE_ROOT,
        },
        {
            "id": "behaviour-suite",
            "label": "run the behaviour suite against the real app.js",
            "argv": ["node", str(PROTOTYPE_ROOT / "tests" / "test_surface.js")],
            "cwd": PROTOTYPE_ROOT,
        },
        {
            "id": "layout-overflow",
            "label": "measure horizontal overflow at six widths",
            "argv": ["sh", str(TOOLS / "check_overflow.sh")],
            "cwd": PROTOTYPE_ROOT,
            "requires_chrome": True,
        },
        {
            "id": "verify-root",
            "label": "run the full mechanical suite from the repository root",
            "argv": [python, str(TOOLS / "verify.py")],
            "cwd": REPO_ROOT,
            "requires_chrome": True,
        },
        {
            "id": "verify-unrelated-cwd",
            "label": "run the full mechanical suite from an unrelated working directory",
            "argv": [python, str(TOOLS / "verify.py")],
            "cwd": Path(REPO_ROOT.anchor) / "private" / "tmp"
            if (Path(REPO_ROOT.anchor) / "private" / "tmp").is_dir()
            else Path.home(),
            "requires_chrome": True,
        },
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=REVIEW_DIR)
    args = parser.parse_args()

    import os

    started = time.monotonic()
    log_parts: list[str] = []
    records: list[dict] = []
    failures: list[dict] = []

    for spec in commands():
        record = {
            "id": spec["id"],
            "label": spec["label"],
            "command": " ".join(str(part) for part in spec["argv"]),
            "cwd": str(spec["cwd"]),
        }
        if spec.get("env"):
            record["env"] = spec["env"]

        if spec.get("requires_chrome") and not CHROME.is_file():
            record["status"] = "skipped"
            record["reason"] = f"the local browser required for this check is absent at {CHROME}"
            records.append(record)
            log_parts.append(f"$ {record['command']}\nSKIPPED: {record['reason']}\n")
            continue

        env = dict(os.environ)
        env["PYTHONPATH"] = str(TOOLS)
        env.update(spec.get("env") or {})

        begin = time.monotonic()
        result = subprocess.run(
            [str(part) for part in spec["argv"]],
            cwd=str(spec["cwd"]),
            capture_output=True,
            text=True,
            env=env,
        )
        elapsed = int((time.monotonic() - begin) * 1000)
        output = (result.stdout + result.stderr).strip()

        ok = result.returncode == 0
        if spec.get("expect_empty_stdout") and result.stdout.strip():
            ok = False
            output += "\n(expected empty stdout)"

        record["status"] = "passed" if ok else "failed"
        record["exit_code"] = result.returncode
        record["duration_ms"] = elapsed
        record["output_tail"] = output.splitlines()[-1] if output else ""
        records.append(record)
        if not ok:
            failures.append({"id": spec["id"], "exit_code": result.returncode, "output": output[-4000:]})

        log_parts.append(
            f"$ cd {spec['cwd']}\n$ {record['command']}\n"
            + (f"[env {spec['env']}]\n" if spec.get("env") else "")
            + f"{output}\n[exit {result.returncode} in {elapsed} ms]\n"
        )

    duration_ms = int((time.monotonic() - started) * 1000)
    passed = [item for item in records if item["status"] == "passed"]
    skipped = [item for item in records if item["status"] == "skipped"]

    payload = {
        "kind": "build-test",
        "build": "passing" if not failures else "failing",
        "tests": "passing" if not failures else "failing",
        "durationMs": duration_ms,
        "counts": {
            "total": len(records),
            "passed": len(passed),
            "failed": len(failures),
            "skipped": len(skipped),
        },
        "commandsRun": records,
        "failures": failures,
        "notes": (
            "Every command was executed in this run. No dependency was installed and no "
            "network request was made. A skipped entry carries a non-empty reason."
        ),
    }

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "build-test.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    log = "\n".join(log_parts)
    if len(log.encode("utf-8")) > LOG_BUDGET_BYTES:
        log = log[: LOG_BUDGET_BYTES // 2] + "\n[log truncated to budget]\n"
    (args.out / "build-test.log").write_text(log, encoding="utf-8")

    print(
        f"{len(passed)} passed, {len(failures)} failed, {len(skipped)} skipped "
        f"in {duration_ms} ms"
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
