"""Append-only revision tests.

The point of these is not that append works — it is that overwrite, delete,
fork, and clock-dependent ordering all fail.
"""

from __future__ import annotations

import dataclasses

import pytest

from kdd_data_agent.core.identity import (
    Actor,
    ActorKind,
    AuthorizationState,
    TimeInterval,
    TimestampError,
)
from kdd_data_agent.core.revisions import AppendOnlyViolation, Revision, RevisionLog

ACTOR = Actor(actor_id="test-validator", actor_kind=ActorKind.DETERMINISTIC_VALIDATOR)
T0 = "2026-08-16T00:00:00+00:00"
T1 = "2026-08-16T01:00:00+00:00"


def append(log: RevisionLog, entity_id: str, payload: dict, recorded_at: str = T0) -> Revision:
    return log.append(
        entity_id=entity_id,
        entity_kind="test_entity",
        actor=ACTOR,
        authorization_state=AuthorizationState.NOT_EVALUATED,
        recorded_at=recorded_at,
        payload=payload,
    )


def test_first_revision_supersedes_nothing_and_later_ones_chain():
    log = RevisionLog()
    first = append(log, "e1", {"v": 1})
    second = append(log, "e1", {"v": 2}, recorded_at=T1)

    assert first.revision_index == 0
    assert first.supersedes is None
    assert second.revision_index == 1
    assert second.supersedes == first.revision_id
    assert log.head("e1") is second
    assert log.history("e1") == (first, second)
    log.verify_chain()


def test_history_is_never_overwritten_by_a_correction():
    log = RevisionLog()
    first = append(log, "e1", {"v": 1})
    append(log, "e1", {"v": 2}, recorded_at=T1)

    assert len(log) == 2
    assert log.history("e1")[0].payload == {"v": 1}
    assert first.payload == {"v": 1}


def test_revisions_are_frozen():
    log = RevisionLog()
    revision = append(log, "e1", {"v": 1})
    with pytest.raises(dataclasses.FrozenInstanceError):
        revision.payload_digest = "sha256:" + "0" * 64


def test_revision_payload_is_detached_and_deeply_frozen():
    payload = {"nested": {"items": [1, 2]}}
    revision = append(RevisionLog(), "e1", payload)
    original_digest = revision.payload_digest

    payload["nested"]["items"].append(3)

    assert revision.payload_digest == original_digest
    assert revision.payload["nested"]["items"] == (1, 2)
    with pytest.raises(TypeError):
        revision.payload["nested"]["new"] = "mutation"


def test_log_exposes_no_update_or_delete_path():
    log = RevisionLog()
    for forbidden in ("delete", "remove", "update", "pop", "clear", "truncate", "set"):
        assert not hasattr(log, forbidden), f"RevisionLog must not expose .{forbidden}()"


def test_a_sealed_log_rejects_further_appends():
    log = RevisionLog()
    append(log, "e1", {"v": 1})
    log.seal()

    assert log.is_sealed is True
    with pytest.raises(AppendOnlyViolation, match="sealed"):
        append(log, "e2", {"v": 2})


def test_a_sealed_log_freezes_and_protects_its_internal_snapshot():
    log = RevisionLog()
    append(log, "e1", {"v": 1})
    original_digest = log.digest()
    log.seal()

    with pytest.raises(AttributeError):
        log._revisions.clear()
    with pytest.raises(AttributeError):
        log._heads.clear()
    with pytest.raises(AppendOnlyViolation, match="cannot be mutated"):
        log._revisions = ()
    assert log.digest() == original_digest


def test_entity_kind_cannot_change_between_revisions():
    log = RevisionLog()
    append(log, "e1", {"v": 1})
    with pytest.raises(AppendOnlyViolation, match="not"):
        log.append(
            entity_id="e1",
            entity_kind="other_kind",
            actor=ACTOR,
            authorization_state=AuthorizationState.NOT_EVALUATED,
            recorded_at=T1,
            payload={"v": 2},
        )


def test_a_later_revision_that_supersedes_nothing_is_rejected():
    with pytest.raises(AppendOnlyViolation, match="must name the revision"):
        Revision(
            entity_id="e1",
            entity_kind="test_entity",
            revision_index=1,
            supersedes=None,
            actor=ACTOR,
            authorization_state=AuthorizationState.NOT_EVALUATED,
            recorded_at=T0,
            derivation_inputs=(),
            payload={"v": 1},
        )


def test_a_first_revision_that_supersedes_something_is_rejected():
    with pytest.raises(AppendOnlyViolation, match="cannot supersede"):
        Revision(
            entity_id="e1",
            entity_kind="test_entity",
            revision_index=0,
            supersedes="rev-0000000000000000",
            actor=ACTOR,
            authorization_state=AuthorizationState.NOT_EVALUATED,
            recorded_at=T0,
            derivation_inputs=(),
            payload={"v": 1},
        )


def test_verify_chain_detects_a_broken_chain():
    log = RevisionLog()
    first = append(log, "e1", {"v": 1})
    forged = Revision(
        entity_id="e1",
        entity_kind="test_entity",
        revision_index=1,
        supersedes="rev-ffffffffffffffff",
        actor=ACTOR,
        authorization_state=AuthorizationState.NOT_EVALUATED,
        recorded_at=T1,
        derivation_inputs=(),
        payload={"v": 2},
    )
    log._revisions.append(forged)
    assert forged.supersedes != first.revision_id
    with pytest.raises(AppendOnlyViolation, match="supersedes"):
        log.verify_chain()


def test_seal_recomputes_payload_and_revision_digests():
    log = RevisionLog()
    revision = append(log, "e1", {"v": 1})
    object.__setattr__(revision, "payload_digest", "sha256:" + "0" * 64)
    with pytest.raises(AppendOnlyViolation, match="payload digest mismatch"):
        log.seal()
    assert log.is_sealed is False


def test_verify_chain_rejects_a_tampered_revision_content_address():
    log = RevisionLog()
    revision = append(log, "e1", {"v": 1})
    object.__setattr__(revision, "revision_digest", "sha256:" + "0" * 64)
    with pytest.raises(AppendOnlyViolation, match="content address mismatch"):
        log.verify_chain()


def test_identical_logs_produce_identical_digests():
    def build() -> RevisionLog:
        log = RevisionLog()
        append(log, "e1", {"v": 1})
        append(log, "e2", {"v": 2})
        append(log, "e1", {"v": 3}, recorded_at=T1)
        return log

    assert build().digest() == build().digest()


def test_revision_ids_are_content_addressed_not_random():
    def build() -> str:
        log = RevisionLog()
        return append(log, "e1", {"v": 1}).revision_id

    assert build() == build()


@pytest.mark.parametrize("bad", ["2026-08-16T00:00:00", "not-a-timestamp", "2026-08-16"])
def test_naive_or_malformed_timestamps_are_rejected(bad):
    log = RevisionLog()
    with pytest.raises(TimestampError):
        append(log, "e1", {"v": 1}, recorded_at=bad)


def test_interval_endpoints_must_be_ordered():
    with pytest.raises(TimestampError, match="after end"):
        TimeInterval(start=T1, end=T0)
