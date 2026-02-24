from typing import Self

from pydantic import BaseModel
from .enums import PrizeType


class Prize(BaseModel):
    id: int | None = None
    title: str
    image_url: str
    image_detail_url: str
    type: PrizeType
    description: str | None = None


__all__ = [
    "Prize",
]
