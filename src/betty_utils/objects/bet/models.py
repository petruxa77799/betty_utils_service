from ..base import KafkaBaseModel
from .enums import AnswerChoice, BetState


class CreateBetModel(KafkaBaseModel):
    wallet_id: int
    market_id: int
    answer: AnswerChoice


class CreateBetBackgroundModel(CreateBetModel):
    state: BetState
    result: int


class WsBetMessageModel(KafkaBaseModel):
    wallet_id: int
    bet_id: int
    profit: int
    right_answer: str | None = None
    state: BetState


__all__ = [
    "CreateBetModel",
    "CreateBetBackgroundModel",
    "WsBetMessageModel",
]
