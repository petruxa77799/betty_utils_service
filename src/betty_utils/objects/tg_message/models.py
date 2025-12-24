from pydantic import constr

from .enums import MessageTypes
from ..base import KafkaBaseModel


class TGMessageModel(KafkaBaseModel):
    text: str
    image_url: str | None
    link: str | None
    link_text: constr(min_length=1, max_length=32) | None
    type: MessageTypes
    telegram_id: int
    partner_id: int


__all__ = [
    "TGMessageModel",
]
