from datetime import datetime

from ..base import KafkaBaseModel
from .enums import AnswerTypes


class WSEventMarketModel(KafkaBaseModel):
    id: int
    title: str
    image_url: str | None
    answer_type: AnswerTypes
    answer_a: str | None
    answer_b: str | None
    expired_at: datetime
    profit: int
    timer: int
    enable_skip: bool
    one_time_bet: bool
    rank: int
    event_id: int
    action: str  # ToDo: implement enum
