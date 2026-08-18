"""Mechanical capability evidence.

Two halves, and the second matters as much as the first: the package is clean,
AND the checker fails on planted violations. A scanner that always returns zero
findings would also report a clean package.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from kdd_data_agent.core.capabilities import (
    ALLOWED_CAPABILITIES,
    ALLOWED_RUNTIME_IMPORTS,
    ALLOWED_TEST_IMPORTS,
    FORBIDDEN_IMPORTS,
    FORBIDDEN_PACKAGE_PATHS,
    Capability,
    CapabilityError,
    assert_capabilities,
)

from ._import_graph import imported_modules, python_files, scan_package, scan_source


def test_runtime_package_has_no_capability_violations(package_root: Path):
    findings = scan_package(package_root, tests=False)
    assert findings == (), "\n".join(str(item) for item in findings)


def test_tests_have_no_capability_violations(package_root: Path):
    findings = scan_package(package_root, tests=True)
    assert findings == (), "\n".join(str(item) for item in findings)


def test_runtime_imports_are_stdlib_only_and_inside_the_allowlist(package_root: Path):
    modules = imported_modules(package_root, tests=False)
    outside = [
        name
        for name in modules
        if name.split(".")[0] not in ALLOWED_RUNTIME_IMPORTS
        and name.split(".")[0] != "kdd_data_agent"
    ]
    assert outside == [], f"runtime imports outside the allowlist: {outside}"


def test_no_legacy_sma_or_kdd_runtime_is_imported(package_root: Path):
    for tests in (False, True):
        for name in imported_modules(package_root, tests=tests):
            top = name.split(".")[0]
            assert top not in {"sma", "sma_rewrite"}, f"legacy import: {name}"


def test_no_network_credential_or_subprocess_module_is_imported(package_root: Path):
    for tests in (False, True):
        for name in imported_modules(package_root, tests=tests):
            assert name.split(".")[0] not in FORBIDDEN_IMPORTS, f"forbidden import: {name}"


@pytest.mark.parametrize("forbidden_path", FORBIDDEN_PACKAGE_PATHS)
def test_production_adapter_path_does_not_exist(package_root: Path, forbidden_path: str):
    assert not (package_root / forbidden_path).exists(), (
        f"{forbidden_path} must not exist before P2 closes"
    )


def test_the_package_contains_no_python_files_outside_the_scanned_set(package_root: Path):
    assert not [path for path in package_root.rglob("*") if path.is_symlink() and path.is_dir()]
    scanned = set(python_files(package_root, tests=False)) | set(python_files(package_root, tests=True))
    on_disk = {
        path
        for path in package_root.rglob("*.py")
        if "__pycache__" not in path.relative_to(package_root).parts
    }
    assert on_disk == scanned


PLANTED_VIOLATIONS = (
    ("import socket", "forbidden_import"),
    ("import subprocess", "forbidden_import"),
    ("from urllib.request import urlopen", "forbidden_import"),
    ("import os", "forbidden_import"),
    ("from sma.scripts import pipeline", "forbidden_import"),
    ("from kdd_data_agent.adapters.production import client", "forbidden_import"),
    ("from . import production", "forbidden_import"),
    ("from .production import client", "forbidden_import"),
    ("from ..adapters.production import client", "forbidden_import"),
    ("import numpy", "disallowed_import"),
    ("handle = open('f', 'w')", "forbidden_builtin"),
    ("eval('1+1')", "forbidden_builtin"),
    ("exec('x = 1')", "forbidden_builtin"),
    ("__import__('socket')", "forbidden_builtin"),
    ("path.write_text('x')", "forbidden_mutation_call"),
    ("path.unlink()", "forbidden_mutation_call"),
    ("subprocess_module.run(['ls'])", "forbidden_mutation_call"),
    ("os_module.system('ls')", "forbidden_mutation_call"),
    ("writer = path.write_text\nwriter('x')", "forbidden_capability_reference"),
    ("clock = datetime.now\nvalue = clock()", "forbidden_capability_reference"),
    ("home = Path.home()", "forbidden_mutation_call"),
    ("path = Path('~').expanduser()", "forbidden_mutation_call"),
    ("import importlib\nimportlib.import_module('socket')", "disallowed_import"),
    ("from importlib import import_module\nimport_module('socket')", "disallowed_import"),
    ("builtins_table = __builtins__", "forbidden_builtin"),
    ("import json\nreader = json.decoder.__builtins__['open']", "forbidden_capability_reference"),
    ("getattr(object, '__builtins__')", "forbidden_mutation_call"),
    ("getattr(object, '__subclasses__')()", "forbidden_mutation_call"),
    ("dynamic = getattr\ndynamic(path, name)", "dynamic_attribute_access"),
    ("sys.modules.pop('safe_name', None)", "module_table_write"),
    ("del sys.modules['safe_name']", "module_table_write"),
    ("sys.modules = {}", "module_table_write"),
    ("modules = sys.modules\nmodules['socket'] = fake", "module_table_write"),
    ("reader = object.__getattribute__\nreader(path, 'write_text')", "forbidden_capability_reference"),
    ("writer = path.__class__.__dict__['write_text']\nwriter(path, 'x')", "forbidden_capability_reference"),
    ("from ...sma import runtime", "forbidden_import"),
    ("from ...sma_rewrite import runtime", "forbidden_import"),
    ("from ... import sma", "forbidden_import"),
    ("import random", "disallowed_import"),
    ("import uuid", "disallowed_import"),
    ("path.copy(destination)", "forbidden_mutation_call"),
    ("path.move(destination)", "forbidden_mutation_call"),
    ("moment = datetime.fromtimestamp(0)", "forbidden_mutation_call"),
    ("Path('/etc/passwd').read_bytes()", "forbidden_filesystem_read"),
    ("reader = Path('/etc/passwd').read_text\ndata = reader()", "forbidden_capability_reference"),
    ("reader = Path('/etc/passwd').read_bytes\ndata = reader()", "forbidden_capability_reference"),
    ("Path.cwd()", "forbidden_filesystem_read"),
    ("Path('/').iterdir()", "forbidden_filesystem_read"),
    ("Path('/etc/passwd').stat()", "forbidden_filesystem_read"),
)


@pytest.mark.parametrize("source,expected_kind", PLANTED_VIOLATIONS)
def test_the_scanner_detects_planted_violations(source: str, expected_kind: str):
    label = "adapters/planted.py" if source.startswith("from .") else "planted.py"
    findings = scan_source(source, label, allowed_imports=ALLOWED_TEST_IMPORTS)
    kinds = {finding.kind for finding in findings}
    assert expected_kind in kinds, f"{source!r} produced {findings}"


def test_the_scanner_accepts_a_clean_module():
    clean = "from kdd_data_agent.core.digest import content_digest\nvalue = content_digest({'a': 1})\n"
    assert scan_source(clean, "clean.py", allowed_imports=ALLOWED_RUNTIME_IMPORTS) == ()


def test_symlinked_package_directory_is_rejected():
    class FakeSymlink:
        def is_symlink(self): return True
        def is_dir(self): return True
        def relative_to(self, _root): return Path("linked")

    class FakeRoot:
        def rglob(self, pattern): return [FakeSymlink()] if pattern == "*" else []

    with pytest.raises(ValueError, match="symlinked package directories"):
        python_files(FakeRoot(), tests=False)


def test_capability_allowlist_is_positive_and_small():
    assert ALLOWED_CAPABILITIES == frozenset(Capability)
    assert {item.value for item in Capability} == {
        "fixture_read",
        "local_deterministic_compute",
        "in_memory_append",
    }


def test_assert_capabilities_rejects_values_outside_the_enum():
    with pytest.raises(CapabilityError, match="non-capability values"):
        assert_capabilities(frozenset({"production_read"}), "TestComponent")


def test_assert_capabilities_accepts_the_allowed_set():
    assert_capabilities(frozenset({Capability.FIXTURE_READ}), "TestComponent")
