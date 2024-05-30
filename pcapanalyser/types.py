"""Custom Types for type annotations."""

from typing import TypeAlias, TypedDict

import dpkt


Conversations: TypeAlias = dict[tuple[str, str], list[dpkt.ip.IP]]


class Packets(TypedDict):
    """Custom Type for type annotation."""

    raw: dict[float, bytes]
    count: dict[str, int]


class Emails(TypedDict):
    """Custom Type for type annotation."""

    From: list[str]
    To: list[str]
