from .enums import BetState, AnswerChoice
from ..base import KafkaBaseModel


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
