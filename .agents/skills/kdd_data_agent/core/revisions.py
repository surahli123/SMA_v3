"""Append-only revision primitives.

Canonical rule this encodes (P1): Evidence, receipts, claims, verdicts, and
packets are append-only. History is never overwritten; a correction is a new
revision that `supersedes` the previous one.

The store here is generic on purpose. It knows nothing about experiments,
checks, or readiness. It knows that a record has an entity, a monotonic
revision index, an actor, an authorization state, a recorded time, derivation
inputs, a payload, and a digest — the fields that stay true regardless of how
the M0 alignment packet ends up defining a contract or a packet.

Determinism: revision ids are truncated content digests, not random UUIDs, and
`recorded_at` is supplied by the caller. A replay over identical frozen inputs
therefore produces identical ids and identical bytes.
"""

from __future__ import annotations

from collections.abc import Iterator, Mapping
from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any, Union

from .digest import content_digest, stable_id
from .identity import Actor, AuthorizationState, validate_timestamp
from .immutability import deep_freeze
from .unknown import Sentinel

MaybeStr = Union[str, Sentinel]


class AppendOnlyViolation(RuntimeError):
    """Raised on any attempt to overwrite, delete, or fork recorded history."""


@dataclass(frozen=True)
class Revision:
    """One immutable revision of one entity."""

    entity_id: str
    entity_kind: str
    revision_index: int
    supersedes: MaybeStr | None
    actor: Actor
    authorization_state: AuthorizationState
    recorded_at: MaybeStr
    derivation_inputs: tuple[str, ...]
    payload: Mapping[str, Any]
    payload_digest: str = ""
    revision_id: str = ""
    revision_digest: str = ""

    def __post_init__(self) -> None:
        if not isinstance(self.entity_id, str) or not self.entity_id.strip():
            raise ValueError("entity_id must be a non-empty string")
        if not isinstance(self.entity_kind, str) or not self.entity_kind.strip():
            raise ValueError("entity_kind must be a non-empty string")
        if self.revision_index < 0:
            raise ValueError("revision_index must be non-negative")
        if not isinstance(self.actor, Actor):
            raise TypeError("actor must be an Actor")
        if not isinstance(self.authorization_state, AuthorizationState):
            raise TypeError("authorization_state must be an AuthorizationState")
        validate_timestamp(self.recorded_at, "recorded_at")
        if self.revision_index == 0 and self.supersedes is not None:
            raise AppendOnlyViolation("the first revision of an entity cannot supersede anything")
        if self.revision_index > 0 and self.supersedes is None:
            raise AppendOnlyViolation("a later revision must name the revision it supersedes")

        object.__setattr__(self, "derivation_inputs", tuple(self.derivation_inputs))
        object.__setattr__(self, "payload", deep_freeze(self.payload))
        object.__setattr__(self, "payload_digest", content_digest(self.payload))
        identity = self._identity_payload()
        object.__setattr__(self, "revision_id", stable_id("rev", identity))
        object.__setattr__(self, "revision_digest", content_digest(identity))

    def _identity_payload(self) -> dict[str, Any]:
        # Nested values stay un-normalized; the top-level canonical pass owns
        # serialization.
        return {
            "entity_id": self.entity_id,
            "entity_kind": self.entity_kind,
            "revision_index": self.revision_index,
            "supersedes": self.supersedes,
            "actor": self.actor,
            "authorization_state": self.authorization_state.value,
            "recorded_at": self.recorded_at,
            "derivation_inputs": list(self.derivation_inputs),
            "payload_digest": self.payload_digest,
        }

    def to_canonical(self) -> dict[str, Any]:
        record = self._identity_payload()
        record["payload"] = dict(self.payload)
        record["revision_id"] = self.revision_id
        record["revision_digest"] = self.revision_digest
        return record

    def verify(self) -> None:
        """Recompute every content address and reject a tampered revision."""
        expected_payload_digest = content_digest(self.payload)
        if self.payload_digest != expected_payload_digest:
            raise AppendOnlyViolation(f"revision {self.revision_id!r} payload digest mismatch")
        identity = self._identity_payload()
        expected_id = stable_id("rev", identity)
        expected_digest = content_digest(identity)
        if self.revision_id != expected_id or self.revision_digest != expected_digest:
            raise AppendOnlyViolation(f"revision {self.revision_id!r} content address mismatch")


@dataclass
class RevisionLog:
    """An in-memory append-only log. It exposes no update or delete path."""

    _revisions: list[Revision] | tuple[Revision, ...] = field(default_factory=list)
    _heads: dict[str, Revision] | Mapping[str, Revision] = field(default_factory=dict)
    _sealed: bool = False

    def __setattr__(self, name: str, value: Any) -> None:
        if getattr(self, "_sealed", False) and name in {"_revisions", "_heads", "_sealed"}:
            raise AppendOnlyViolation("the sealed revision log cannot be mutated")
        super().__setattr__(name, value)

    def append(
        self,
        *,
        entity_id: str,
        entity_kind: str,
        actor: Actor,
        authorization_state: AuthorizationState,
        recorded_at: MaybeStr,
        payload: Mapping[str, Any],
        derivation_inputs: tuple[str, ...] = (),
    ) -> Revision:
        """Append the next revision of `entity_id` and return it."""
        if self._sealed:
            raise AppendOnlyViolation("the revision log is sealed")
        if not isinstance(self._revisions, list) or not isinstance(self._heads, dict):
            raise AppendOnlyViolation("the revision log storage is immutable")
        previous = self._heads.get(entity_id)
        if previous is None:
            index = 0
            supersedes: str | None = None
        else:
            if previous.entity_kind != entity_kind:
                raise AppendOnlyViolation(
                    f"entity {entity_id!r} is {previous.entity_kind!r}, not {entity_kind!r}"
                )
            index = previous.revision_index + 1
            supersedes = previous.revision_id

        next_payload_digest = content_digest(payload)
        if previous is not None and previous.payload_digest == next_payload_digest:
            raise AppendOnlyViolation(
                f"entity {entity_id!r} cannot append an identical payload as a correction"
            )

        revision = Revision(
            entity_id=entity_id,
            entity_kind=entity_kind,
            revision_index=index,
            supersedes=supersedes,
            actor=actor,
            authorization_state=authorization_state,
            recorded_at=recorded_at,
            derivation_inputs=derivation_inputs,
            payload=payload,
        )
        self._revisions.append(revision)
        self._heads[entity_id] = revision
        return revision

    def head(self, entity_id: str) -> Revision:
        try:
            return self._heads[entity_id]
        except KeyError:
            raise KeyError(f"no revision recorded for entity {entity_id!r}") from None

    def history(self, entity_id: str) -> tuple[Revision, ...]:
        return tuple(rev for rev in self._revisions if rev.entity_id == entity_id)

    def entity_ids(self) -> tuple[str, ...]:
        seen: dict[str, None] = {}
        for revision in self._revisions:
            seen.setdefault(revision.entity_id, None)
        return tuple(seen)

    def __iter__(self) -> Iterator[Revision]:
        return iter(tuple(self._revisions))

    def __len__(self) -> int:
        return len(self._revisions)

    @property
    def is_sealed(self) -> bool:
        return self._sealed

    def seal(self) -> None:
        """Verify the chain and permanently close the public append path."""
        self.verify_chain()
        self._revisions = tuple(self._revisions)
        self._heads = MappingProxyType(dict(self._heads))
        self._sealed = True

    def verify_chain(self) -> None:
        """Raise if any entity's revision chain is broken or out of order."""
        expected_index: dict[str, int] = {}
        last_id: dict[str, str] = {}
        for revision in self._revisions:
            revision.verify()
            entity = revision.entity_id
            index = expected_index.get(entity, 0)
            if revision.revision_index != index:
                raise AppendOnlyViolation(
                    f"entity {entity!r} revision index {revision.revision_index} breaks the chain "
                    f"(expected {index})"
                )
            if index > 0 and revision.supersedes != last_id[entity]:
                raise AppendOnlyViolation(
                    f"entity {entity!r} revision {revision.revision_id} supersedes "
                    f"{revision.supersedes!r}, expected {last_id[entity]!r}"
                )
            expected_index[entity] = index + 1
            last_id[entity] = revision.revision_id
        if set(self._heads) != set(last_id):
            raise AppendOnlyViolation("revision head registry does not match chain entities")
        for entity, revision_id in last_id.items():
            if self._heads[entity].revision_id != revision_id:
                raise AppendOnlyViolation(f"entity {entity!r} head does not match chain tail")

    def to_canonical(self) -> list[Any]:
        return list(self._revisions)

    def digest(self) -> str:
        """Digest of the whole log, in append order."""
        return content_digest(self.to_canonical())
