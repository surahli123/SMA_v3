"""Single named builder/command for the canonical trusted fixture packet."""

from __future__ import annotations

import hashlib
import json

from ._m0_fixtures import packet_for


def canonical_packet_evidence() -> dict[str, object]:
    packet = packet_for()
    serialized = packet.serialize()
    return {
        "builder": "kdd_data_agent.tests.canonical_packet_builder:canonical_packet_evidence",
        "serialized_byte_count": len(serialized),
        "serialized_byte_sha256": hashlib.sha256(serialized).hexdigest(),
        "internal_content_digest": packet.packet_digest,
        "digest_namespaces": {
            "serialized_byte_sha256": "raw canonical serialized bytes",
            "internal_content_digest": "FlightReadinessPacket identity payload",
        },
    }


def main() -> None:
    print(json.dumps(canonical_packet_evidence(), sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
