"""Positive capability allowlist for the M0 slice.

The rule is inverted from the usual denylist: a capability is unavailable
unless it is named here. A denylist can only forbid the risks somebody already
thought of; an allowlist forbids everything nobody has justified.

This module holds only declarations — no filesystem walk, no `ast`, no
execution. The mechanical check that the runtime package actually stays inside
these bounds lives in `tests/_import_graph.py` and `tests/test_capability_allowlist.py`,
so the shipped package carries no code-inspection machinery of its own.
"""

from __future__ import annotations

from enum import Enum


class Capability(str, Enum):
    """Every capability any M0 component is allowed to hold."""

    FIXTURE_READ = "fixture_read"
    LOCAL_DETERMINISTIC_COMPUTE = "local_deterministic_compute"
    IN_MEMORY_APPEND = "in_memory_append"


ALLOWED_CAPABILITIES = frozenset(Capability)

FORBIDDEN_CAPABILITY_NAMES = (
    "production_read",
    "network",
    "credential_access",
    "subprocess",
    "arbitrary_execution",
    "filesystem_write",
    "external_publication",
    "mutation",
    "legacy_runtime_import",
)
"""Named for tests and receipts. Deliberately absent from `Capability`: they
have no representation, so no component can request one.
"""

ALLOWED_RUNTIME_IMPORTS = frozenset(
    {
        "__future__",
        "collections",
        "dataclasses",
        "datetime",
        "enum",
        "hashlib",
        "hmac",
        "json",
        "math",
        "pathlib",
        "re",
        "types",
        "typing",
    }
)
"""Stdlib modules the runtime package may import. Nothing else, no third party."""

ALLOWED_TEST_IMPORTS = ALLOWED_RUNTIME_IMPORTS | frozenset(
    {
        "ast",
        "itertools",
        "pytest",
        "sys",
    }
)
"""Tests may inspect the package, so they get `ast` and `sys`. They still get no
network, subprocess, or credential module.
"""

FORBIDDEN_IMPORTS = frozenset(
    {
        "asyncio",
        "ctypes",
        "ftplib",
        "http",
        "imaplib",
        "multiprocessing",
        "os",
        "pickle",
        "requests",
        "shutil",
        "smtplib",
        "socket",
        "socketserver",
        "ssl",
        "subprocess",
        "telnetlib",
        "tempfile",
        "urllib",
        "webbrowser",
        "xmlrpc",
    }
)
"""Explicitly named so a violation reads as a policy breach, not a typo.

`os` is here on purpose: `pathlib` covers every path need in this slice without
also handing over `os.system`, `os.remove`, and the environment.
"""

FORBIDDEN_IMPORT_PREFIXES = (
    "sma",
    "sma_rewrite",
    "kdd_data_agent.adapters.production",
)
"""Legacy runtime and the pre-P2 production adapter path are unreachable."""

FORBIDDEN_BUILTIN_CALLS = frozenset(
    {
        "__import__",
        "breakpoint",
        "compile",
        "eval",
        "exec",
        "globals",
        "input",
        "locals",
        "open",
        "vars",
    }
)
"""`open` is forbidden even for reading: `Path.read_text` is the single read
seam, which keeps every file access in one auditable call shape.
"""

FORBIDDEN_ATTRIBUTE_CALLS = frozenset(
    {
        # filesystem mutation
        "chmod",
        "copy",
        "copy_into",
        "hardlink_to",
        "link_to",
        "lchmod",
        "mkdir",
        "move",
        "move_into",
        "rename",
        "replace",
        "rmdir",
        "rmtree",
        "symlink_to",
        "touch",
        "truncate",
        "unlink",
        "write",
        "write_bytes",
        "write_text",
        "writelines",
        # ambient user/environment state
        "expanduser",
        "home",
        # file handles: `Path.open` reaches a write mode without the `open`
        # builtin, so blocking the builtin alone is not enough
        "open",
        # subprocess
        "popen",
        "run",
        "system",
        # wall clock: `datetime` is an allowed import, so the no-clock rule
        # needs its own call-shape guard or it is only a grep-verified state
        "monotonic",
        "now",
        "perf_counter",
        "today",
        "utcnow",
        "fromtimestamp",
    }
)
"""Mutation, subprocess, and wall-clock call shapes. None appear in the runtime
package or in its tests.

Deliberately over-matching: this is name-based, not type-aware, so `str.replace`
and a method legitimately named `run` or `write` would also be flagged. A lint
false positive is a conversation; a false negative is a capability leak. If a
legitimate use appears, widen it explicitly rather than by accident.
"""

FORBIDDEN_GLOBAL_REFERENCES = frozenset({"__builtins__"})
"""Ambient access to the builtin table can recover ``open``, ``exec``, or
``__import__`` without spelling any forbidden call. It is therefore forbidden
as a value, not only when called directly.
"""

FORBIDDEN_ATTRIBUTE_REFERENCES = frozenset(
    {
        "__bases__",
        "__builtins__",
        "__closure__",
        "__code__",
        "__dict__",
        "__getattribute__",
        "__globals__",
        "__mro__",
        "__subclasses__",
        "modules",
    }
)
"""Reflection and module-table handles that can recover a forbidden callable
or install a module without spelling the eventual capability at the call site.
"""

FORBIDDEN_FILESYSTEM_READ_CALLS = frozenset(
    {
        "cwd",
        "glob",
        "iterdir",
        "lstat",
        "read_bytes",
        "read_text",
        "readlink",
        "rglob",
        "stat",
    }
)
"""Filesystem reads outside the fixture adapter's two ``read_text`` calls.

Tests may inspect their own package and fixtures. Runtime code gets exactly one
auditable source-read seam and no ambient-directory or enumeration access.
"""

FORBIDDEN_PACKAGE_PATHS = ("adapters/production",)
"""Directories that must not exist before P2 closes."""


class CapabilityError(PermissionError):
    """Raised when a component declares a capability outside the allowlist."""


def assert_capabilities(declared: frozenset[Capability], owner: str) -> None:
    """Raise unless every declared capability is in the positive allowlist."""
    if not isinstance(declared, frozenset):
        raise TypeError("declared capabilities must be a frozenset")
    unknown = {item for item in declared if not isinstance(item, Capability)}
    if unknown:
        raise CapabilityError(f"{owner} declares non-capability values: {sorted(map(str, unknown))}")
    outside = declared - ALLOWED_CAPABILITIES
    if outside:
        raise CapabilityError(f"{owner} declares capabilities outside the M0 allowlist: {sorted(outside)}")
