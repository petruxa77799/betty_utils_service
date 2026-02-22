from typing import Self

from pydantic import constr, model_validator
from .enums import PrizeType


class Prize(BaseModel):
    title: str
    image_url: str
    image_detail_url: str
    type: PrizeType
    description: str | None = None


__all__ = [
    "Prize",
]
