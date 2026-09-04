from __future__ import annotations

import socket
from dataclasses import dataclass


SUPPORTED = {"A", "AAAA", "MX", "NS", "TXT", "CNAME"}


@dataclass(frozen=True)
class Record:
    name: str
    type: str
    value: str


def lookup(name: str, record_type: str = "A") -> list[Record]:
    record_type = record_type.upper()
    if record_type not in SUPPORTED:
        raise ValueError(f"unsupported record type: {record_type}")
    family = socket.AF_INET6 if record_type == "AAAA" else socket.AF_INET
    if record_type not in {"A", "AAAA"}:
        return []
    answers = socket.getaddrinfo(name, None, family, socket.SOCK_STREAM)
    values = sorted({item[4][0] for item in answers})
    return [Record(name, record_type, value) for value in values]


def reverse_lookup(address: str) -> str:
    return socket.gethostbyaddr(address)[0]
