"""Mechanical capability check over the package's own source.

Greps prove nothing about reachability, and a docstring promising "no network"
is not a control. This walks the AST of every file in the package and reports
any import or call shape that would give the slice a capability it is not
allowed to have.

It lives under `tests/` on purpose: the shipped runtime carries no code
inspection machinery, and `ast` never enters the runtime import graph.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path

from kdd_data_agent.core.capabilities import (
    ALLOWED_RUNTIME_IMPORTS,
    ALLOWED_TEST_IMPORTS,
    FORBIDDEN_ATTRIBUTE_CALLS,
    FORBIDDEN_ATTRIBUTE_REFERENCES,
    FORBIDDEN_BUILTIN_CALLS,
    FORBIDDEN_FILESYSTEM_READ_CALLS,
    FORBIDDEN_GLOBAL_REFERENCES,
    FORBIDDEN_IMPORT_PREFIXES,
    FORBIDDEN_IMPORTS,
)

EXCLUDED_DIR_NAMES = frozenset({"__pycache__"})
TEST_DIR_NAME = "tests"


@dataclass(frozen=True)
class Finding:
    """One capability violation, located precisely enough to fix."""

    label: str
    line: int
    kind: str
    detail: str

    def __str__(self) -> str:
        return f"{self.label}:{self.line} [{self.kind}] {self.detail}"


def python_files(root: Path, *, tests: bool) -> tuple[Path, ...]:
    """Runtime files, or test files, under `root`. Never both at once."""
    symlinked_directories = tuple(
        path for path in root.rglob("*") if path.is_symlink() and path.is_dir()
    )
    if symlinked_directories:
        names = ", ".join(str(path.relative_to(root)) for path in symlinked_directories)
        raise ValueError(f"symlinked package directories are forbidden: {names}")
    found: list[Path] = []
    for path in sorted(root.rglob("*.py")):
        parts = set(path.relative_to(root).parts)
        if parts & EXCLUDED_DIR_NAMES:
            continue
        is_test = TEST_DIR_NAME in path.relative_to(root).parts
        if is_test == tests:
            found.append(path)
    return tuple(found)


def scan_source(source: str, label: str, *, allowed_imports: frozenset[str]) -> tuple[Finding, ...]:
    """Scan one module's source text and return every capability violation."""
    findings: list[Finding] = []
    tree = ast.parse(source, filename=label)
    parents = {child: parent for parent in ast.walk(tree) for child in ast.iter_child_nodes(parent)}

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                findings.extend(_check_module(alias.name, node.lineno, label, allowed_imports))
        elif isinstance(node, ast.ImportFrom):
            if node.level and node.level > 0:
                package_parts = ["kdd_data_agent", *Path(label).with_suffix("").parts[:-1]]
                keep = len(package_parts) - (node.level - 1)
                base = package_parts[: max(keep, 0)]
                if node.module:
                    base.extend(node.module.split("."))
                candidates = [".".join(base)]
                candidates.extend(".".join([*base, alias.name]) for alias in node.names)
                for candidate in candidates:
                    findings.extend(_check_module(candidate, node.lineno, label, allowed_imports))
                continue
            findings.extend(_check_module(node.module or "", node.lineno, label, allowed_imports))
        elif isinstance(node, ast.Call):
            findings.extend(_check_call(node, label))
        elif isinstance(node, ast.Attribute) and (
            node.attr in FORBIDDEN_ATTRIBUTE_CALLS
            or node.attr in FORBIDDEN_ATTRIBUTE_REFERENCES
            or node.attr in FORBIDDEN_FILESYSTEM_READ_CALLS
        ):
            # Catch capability extraction before a later aliased call, for
            # example ``writer = path.write_text`` or ``clock = datetime.now``.
            # Direct calls are intentionally also reported by ``_check_call``.
            parent = parents.get(node)
            fixture_read = (
                label == "adapters/fixture.py"
                and node.attr == "read_text"
                and isinstance(parent, ast.Call)
                and parent.func is node
            )
            if label.startswith(f"{TEST_DIR_NAME}/") or fixture_read:
                continue
            kind = "module_table_write" if node.attr == "modules" else "forbidden_capability_reference"
            findings.append(
                Finding(
                    label,
                    node.lineno,
                    kind,
                    f"reference to .{node.attr}",
                )
            )
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            # `_o = open` then `_o("f", "w")` never appears as a call to a
            # forbidden name, so the bare reference is the thing to catch.
            if node.id in FORBIDDEN_BUILTIN_CALLS:
                findings.append(
                    Finding(label, node.lineno, "forbidden_builtin", f"reference to {node.id}")
                )
            elif node.id in FORBIDDEN_GLOBAL_REFERENCES:
                findings.append(
                    Finding(label, node.lineno, "forbidden_builtin", f"reference to {node.id}")
                )
            elif node.id in DYNAMIC_ATTRIBUTE_BUILTINS:
                parent = parents.get(node)
                if not (isinstance(parent, ast.Call) and parent.func is node):
                    findings.append(
                        Finding(
                            label,
                            node.lineno,
                            "dynamic_attribute_access",
                            f"aliased reference to {node.id}",
                        )
                    )
        elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
            findings.extend(_check_assignment(node, label))
        elif isinstance(node, ast.Delete):
            findings.extend(_check_module_table_targets(node.targets, node.lineno, label))

    return tuple(findings)


def _check_module(
    module: str,
    line: int,
    label: str,
    allowed_imports: frozenset[str],
) -> tuple[Finding, ...]:
    if not module:
        return ()
    top = module.split(".")[0]
    if module.startswith(FORBIDDEN_IMPORT_PREFIXES) or top in FORBIDDEN_IMPORT_PREFIXES:
        return (Finding(label, line, "forbidden_import", f"import of forbidden path {module!r}"),)
    if top in FORBIDDEN_IMPORTS:
        return (Finding(label, line, "forbidden_import", f"import of {module!r}"),)
    if top == "kdd_data_agent":
        return ()
    if top not in allowed_imports:
        return (
            Finding(
                label,
                line,
                "disallowed_import",
                f"{module!r} is not in the positive import allowlist",
            ),
        )
    return ()


DYNAMIC_ATTRIBUTE_BUILTINS = frozenset({"getattr", "setattr", "delattr"})


def _check_call(node: ast.Call, label: str) -> tuple[Finding, ...]:
    func = node.func
    if isinstance(func, ast.Name):
        if func.id in FORBIDDEN_BUILTIN_CALLS:
            return (Finding(label, node.lineno, "forbidden_builtin", f"call to {func.id}()"),)
        if func.id in DYNAMIC_ATTRIBUTE_BUILTINS:
            return _check_dynamic_attribute(node, func.id, label)
    if isinstance(func, ast.Attribute) and func.attr in FORBIDDEN_ATTRIBUTE_CALLS:
        return (
            Finding(
                label,
                node.lineno,
                "forbidden_mutation_call",
                f"call to .{func.attr}()",
            ),
        )
    if isinstance(func, ast.Attribute) and func.attr in FORBIDDEN_FILESYSTEM_READ_CALLS:
        if label.startswith(f"{TEST_DIR_NAME}/"):
            return ()
        if func.attr == "read_text" and label == "adapters/fixture.py":
            return ()
        return (
            Finding(
                label,
                node.lineno,
                "forbidden_filesystem_read",
                f"call to .{func.attr}() outside the fixture read seam",
            ),
        )
    if (
        isinstance(func, ast.Attribute)
        and isinstance(func.value, ast.Attribute)
        and func.value.attr == "modules"
        and func.attr in {"__delitem__", "__setitem__", "clear", "pop", "popitem", "setdefault", "update"}
    ):
        return (
            Finding(
                label,
                node.lineno,
                "module_table_write",
                f"call to sys.modules.{func.attr}()",
            ),
        )
    return ()


def _check_dynamic_attribute(node: ast.Call, builtin: str, label: str) -> tuple[Finding, ...]:
    """`getattr(obj, "write_text")()` reaches a forbidden shape without ever
    naming it as an attribute, and `getattr(obj, name)` hides the target
    entirely. A literal, non-forbidden name is the only accepted form."""
    if len(node.args) < 2:
        return ()
    attribute = node.args[1]
    if not isinstance(attribute, ast.Constant) or not isinstance(attribute.value, str):
        return (
            Finding(
                label,
                node.lineno,
                "dynamic_attribute_access",
                f"{builtin}() with a non-literal attribute name",
            ),
        )
    if (
        attribute.value in FORBIDDEN_ATTRIBUTE_CALLS
        or attribute.value in FORBIDDEN_ATTRIBUTE_REFERENCES
        or attribute.value in FORBIDDEN_BUILTIN_CALLS
        or attribute.value in FORBIDDEN_GLOBAL_REFERENCES
        or attribute.value in FORBIDDEN_FILESYSTEM_READ_CALLS
    ):
        return (
            Finding(
                label,
                node.lineno,
                "forbidden_mutation_call",
                f"{builtin}() reaching .{attribute.value}",
            ),
        )
    return ()


def _check_assignment(node: ast.AST, label: str) -> tuple[Finding, ...]:
    """Catch `sys.modules["socket"] = ...`, which installs a capability without
    importing anything."""
    targets = getattr(node, "targets", None) or [getattr(node, "target", None)]
    return _check_module_table_targets(targets, node.lineno, label)


def _check_module_table_targets(
    targets: list[ast.expr] | tuple[ast.expr, ...],
    line: int,
    label: str,
) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    for target in targets:
        base = target.value if isinstance(target, ast.Subscript) else target
        if isinstance(base, ast.Attribute) and base.attr == "modules":
            findings.append(
                Finding(
                    label,
                    line,
                    "module_table_write",
                    "assignment to or deletion from sys.modules",
                )
            )
    return tuple(findings)


def scan_package(root: Path, *, tests: bool) -> tuple[Finding, ...]:
    """Scan every runtime (or test) module under the package root."""
    allowed = ALLOWED_TEST_IMPORTS if tests else ALLOWED_RUNTIME_IMPORTS
    findings: list[Finding] = []
    for path in python_files(root, tests=tests):
        label = str(path.relative_to(root))
        findings.extend(scan_source(path.read_text(encoding="utf-8"), label, allowed_imports=allowed))
    return tuple(findings)


def imported_modules(root: Path, *, tests: bool) -> tuple[str, ...]:
    """Every absolute module name the scanned files import, sorted."""
    modules: set[str] = set()
    for path in python_files(root, tests=tests):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                modules.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and not node.level:
                modules.add(node.module or "")
    return tuple(sorted(item for item in modules if item))
