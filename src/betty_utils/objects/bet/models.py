from ..base import KafkaBaseModel
from .enums import AnswerChoice, BetState


class CreateBetModel(KafkaBaseModel):
    wallet_id: int
    market_id: int
    answer: AnswerChoice


class CreateBetBackgroundModel(CreateBetModel):
    state: BetState
    result: int


__all__ = [
    "CreateBetModel",
    "CreateBetBackgroundModel",
]
