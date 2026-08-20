"""Mechanical verification for the M0 Flight Readiness review surface.

Runs the checks that do not need a browser: input bindings, fixture
determinism, HTML/CSS/JavaScript structure, offline-only guarantees, colour
contrast, and the behaviour suite. Installs nothing, downloads nothing, and
writes nothing outside the report it prints.

Exit status is 0 only when every check passes.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

from bindings import PROTOTYPE_ROOT, REPO_ROOT, BindingDrift, verify_bindings

TOOLS = PROTOTYPE_ROOT / "tools"
VOID_ELEMENTS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

NETWORK_TOKENS = (
    "fetch(", "XMLHttpRequest", "WebSocket", "EventSource", "sendBeacon",
    "http://", "https://", "//cdn.", "@import",
)

STORAGE_TOKENS = ("localStorage", "sessionStorage", "document.cookie", "indexedDB")
EXECUTION_TOKENS = ("eval(", "new Function", "innerHTML", "outerHTML", "document.write")

# Foreground/background pairs that must clear WCAG AA. Small text needs 4.5:1;
# the large-text allowance is only claimed where the rule sets >= 18.66px bold
# or >= 24px.
CONTRAST_PAIRS = (
    ("--ink", "--paper", 4.5, "body text on the workspace ground"),
    ("--ink", "--panel", 4.5, "body text on a panel"),
    ("--muted", "--paper", 4.5, "secondary label on the workspace ground"),
    ("--muted", "--panel", 4.5, "secondary label on a panel"),
    ("--muted", "--soft", 4.5, "secondary label on a hovered row"),
    ("--accent", "--paper", 4.5, "blocked state on the workspace ground"),
    ("--accent", "--panel", 4.5, "blocked state on a panel"),
    ("--accent", "--accent-wash", 4.5, "blocked state on its own wash"),
    ("--ok", "--panel", 4.5, "validated state on a panel"),
    ("--ok", "--ok-wash", 4.5, "validated state on its own wash"),
    ("--warn", "--panel", 4.5, "unknown or missing state on a panel"),
    ("--warn", "--warn-wash", 4.5, "unknown or missing state on its own wash"),
)


class Report:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, str]] = []
        self.failed = 0

    def add(self, name: str, ok: bool, detail: str = "") -> None:
        self.rows.append(("PASS" if ok else "FAIL", name, detail))
        if not ok:
            self.failed += 1

    def render(self) -> str:
        width = max(len(name) for _, name, _ in self.rows)
        lines = [f"{status}  {name.ljust(width)}  {detail}" for status, name, detail in self.rows]
        lines.append("")
        lines.append(f"{len(self.rows) - self.failed} passed, {self.failed} failed, {len(self.rows)} total")
        return "\n".join(lines)


class Balance(HTMLParser):
    """Verify tag nesting closes exactly, and collect a few required facts."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.errors: list[str] = []
        self.tags: list[str] = []
        self.attrs: dict[str, list[dict[str, str]]] = {}

    def handle_starttag(self, tag: str, attrs) -> None:
        self.tags.append(tag)
        self.attrs.setdefault(tag, []).append({key: (value or "") for key, value in attrs})
        if tag not in VOID_ELEMENTS:
            self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID_ELEMENTS:
            return
        if not self.stack:
            self.errors.append(f"</{tag}> closes nothing")
        elif self.stack[-1] != tag:
            self.errors.append(f"</{tag}> closes <{self.stack[-1]}>")
            self.stack.pop()
        else:
            self.stack.pop()


def channel(value: float) -> float:
    value = value / 255.0
    return value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4


def luminance(hex_colour: str) -> float:
    raw = hex_colour.lstrip("#")
    if len(raw) == 3:
        raw = "".join(part * 2 for part in raw)
    red, green, blue = (int(raw[index:index + 2], 16) for index in (0, 2, 4))
    return 0.2126 * channel(red) + 0.7152 * channel(green) + 0.0722 * channel(blue)


def contrast(foreground: str, background: str) -> float:
    first, second = luminance(foreground), luminance(background)
    lighter, darker = max(first, second), min(first, second)
    return (lighter + 0.05) / (darker + 0.05)


def css_tokens(css: str) -> dict[str, str]:
    block = re.search(r":root\s*\{(.*?)\}", css, re.S)
    if not block:
        return {}
    return {
        name: value.strip()
        for name, value in re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", block.group(1))
    }


def run(command: list[str], cwd: Path) -> tuple[int, str]:
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    return result.returncode, (result.stdout + result.stderr).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-behaviour", action="store_true", help="skip the Node behaviour suite")
    parser.add_argument(
        "--skip-layout",
        action="store_true",
        help="skip the headless-browser horizontal-overflow measurement",
    )
    args = parser.parse_args()

    report = Report()

    # 1. Exact input bindings.
    try:
        bindings = verify_bindings()
        report.add(
            "exact input bindings",
            True,
            f"{len(bindings['bindings'])} bound inputs match; package is {bindings['package_file_count']} files",
        )
    except BindingDrift as error:
        report.add("exact input bindings", False, str(error).splitlines()[0])
        print(report.render())
        return 1

    # 2. The accepted package is untouched by this prototype.
    code, output = run(["git", "status", "--porcelain", "--", ".agents/skills/kdd_data_agent"], REPO_ROOT)
    report.add("accepted M0 package unmodified", code == 0 and output == "", output or "no working-tree change")

    # 3. Fixtures reproduce from the accepted package.
    code, output = run(
        [sys.executable, str(TOOLS / "build_fixtures.py"), "--check"],
        REPO_ROOT,
    )
    report.add("fixtures reproduce from the accepted package", code == 0, output.splitlines()[-1] if output else "")

    html_path = PROTOTYPE_ROOT / "index.html"
    css_path = PROTOTYPE_ROOT / "styles.css"
    js_path = PROTOTYPE_ROOT / "app.js"
    data_js = PROTOTYPE_ROOT / "data" / "fixtures.js"
    data_json = PROTOTYPE_ROOT / "data" / "fixtures.json"

    html = html_path.read_text(encoding="utf-8")
    css = css_path.read_text(encoding="utf-8")
    javascript = js_path.read_text(encoding="utf-8")

    # 4. HTML structure.
    parser_state = Balance()
    parser_state.feed(html)
    report.add(
        "HTML tags balance",
        not parser_state.errors and not parser_state.stack,
        "; ".join(parser_state.errors) or (f"unclosed: {parser_state.stack}" if parser_state.stack else "balanced"),
    )

    html_attrs = parser_state.attrs
    report.add("HTML declares a document language", html_attrs.get("html", [{}])[0].get("lang") == "en")
    report.add("HTML declares a viewport", any(
        item.get("name") == "viewport" for item in html_attrs.get("meta", [])
    ))
    report.add("HTML provides a skip link", 'class="skip"' in html and 'href="#packet-decision"' in html)
    report.add("HTML uses landmark elements", all(
        tag in parser_state.tags for tag in ("header", "main", "aside", "nav")
    ))
    report.add("HTML provides a noscript fallback", "noscript" in parser_state.tags)

    scripts = [item.get("src", "") for item in html_attrs.get("script", [])]
    report.add(
        "HTML loads only its own local scripts",
        scripts == ["data/fixtures.js", "app.js"],
        ", ".join(scripts),
    )

    # 5. CSS structure.
    report.add("CSS braces balance", css.count("{") == css.count("}"), f"{css.count('{')} open, {css.count('}')} close")
    report.add("CSS honours reduced motion", "prefers-reduced-motion" in css)
    report.add("CSS provides a visible focus style", ":focus-visible" in css)
    report.add("CSS defines responsive breakpoints", css.count("@media (max-width") >= 3)

    tokens = css_tokens(css)
    report.add("CSS exposes its palette as tokens", len(tokens) >= 12, f"{len(tokens)} custom properties")

    for foreground, background, floor, label in CONTRAST_PAIRS:
        if foreground not in tokens or background not in tokens:
            report.add(f"contrast {foreground} on {background}", False, "token missing")
            continue
        ratio = contrast(tokens[foreground], tokens[background])
        report.add(
            f"contrast {foreground} on {background}",
            ratio >= floor,
            f"{ratio:.2f}:1 (needs {floor}:1) — {label}",
        )

    # 6. JavaScript.
    code, output = run(["node", "--check", str(js_path)], PROTOTYPE_ROOT)
    report.add("app.js parses", code == 0, output)
    code, output = run(["node", "--check", str(data_js)], PROTOTYPE_ROOT)
    report.add("data/fixtures.js parses", code == 0, output)

    # 7. Offline-only and read-only guarantees, over code rather than comments.
    stripped = re.sub(r"/\*.*?\*/", "", javascript, flags=re.S)
    stripped = re.sub(r"^\s*//.*$", "", stripped, flags=re.M)
    html_stripped = re.sub(r"<!--.*?-->", "", html, flags=re.S)

    for label, text in (("app.js", stripped), ("index.html", html_stripped), ("styles.css", css)):
        hits = [token for token in NETWORK_TOKENS if token in text]
        report.add(f"{label} makes no network reference", not hits, ", ".join(hits))

    hits = [token for token in STORAGE_TOKENS if token in stripped]
    report.add("app.js touches no client storage", not hits, ", ".join(hits))
    hits = [token for token in EXECUTION_TOKENS if token in stripped]
    report.add("app.js builds no markup from data", not hits, ", ".join(hits))

    # The generated loader must be inert data, not a program.
    loader = data_js.read_text(encoding="utf-8")
    body = loader.split("=", 1)[1].strip().rstrip(";\n")
    try:
        json.loads(body)
        report.add("data/fixtures.js is inert data", True, "payload parses as JSON")
    except json.JSONDecodeError as error:
        report.add("data/fixtures.js is inert data", False, str(error))

    # 8. The render model itself.
    model = json.loads(data_json.read_text(encoding="utf-8"))
    report.add("model schema is the expected revision", model["schema_version"] == "m0-review-surface-projection/v1")
    report.add("model carries the required scenario classes", {
        item["decision"]["analysis_use"]["value"] for item in model["scenarios"]
    } == {"decision_grade", "directional_only", "not_permitted"})
    report.add("every scenario is fixture class", all(
        item["flight"]["evidence_class"] == "fixture" for item in model["scenarios"]
    ))
    report.add("every scenario carries a packet digest", all(
        item["identity"]["packet_digest"].startswith("sha256:") for item in model["scenarios"]
    ))
    report.add("every scenario reaches a source and a D4/D6 receipt", all(
        item["receipts"]["source_read"] and item["receipts"]["recomputation_d4_d6"]
        for item in model["scenarios"]
    ))
    report.add("every D4/D6 receipt names its decision bindings", all(
        receipt["decision_bindings"] == ["D4", "D6"]
        for item in model["scenarios"]
        for receipt in item["receipts"]["recomputation_d4_d6"]
    ))
    report.add("no scenario carries a cause, recommendation or diff field", all(
        not ({"cause", "recommendation", "candidate_diff", "win_loss"} & set(item))
        for item in model["scenarios"]
    ))
    report.add("the accepted package projection is preserved verbatim", all(
        item["accepted_package_projection"]["scenario_id"] == "VAL-UI-001"
        and item["accepted_package_projection"]["live_review_scenario"] == "VAL-UI-101:open_external_P3_gate"
        for item in model["scenarios"]
    ))
    report.add("boundaries are stated", len(model["boundaries"]) >= 8, f"{len(model['boundaries'])} statements")

    # 9. Behaviour suite.
    if not args.skip_behaviour:
        code, output = run(["node", str(PROTOTYPE_ROOT / "tests" / "test_surface.js")], PROTOTYPE_ROOT)
        summary = output.splitlines()[-1] if output else ""
        report.add("behaviour suite", code == 0, summary)

    # 10. Layout: the page itself must never scroll sideways at any width.
    if not args.skip_layout:
        code, output = run(["sh", str(TOOLS / "check_overflow.sh")], PROTOTYPE_ROOT)
        summary = output.strip().splitlines()[-1] if output.strip() else ""
        report.add("no horizontal page overflow at any width", code == 0, summary)

    print(report.render())
    return 1 if report.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
