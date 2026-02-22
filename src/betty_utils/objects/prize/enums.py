from enum import StrEnum


class PrizeType(StrEnum):
    TICKET="TICKET"
    SPIN="SPIN"
    REAL="REAL"


__all__ = [
    "PrizeType",
]
