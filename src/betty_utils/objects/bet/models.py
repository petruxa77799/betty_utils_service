from pydantic import constr

from ..base import KafkaBaseModel
from .enums import AnswerChoice, BetState


class CreateBetModel(KafkaBaseModel):
    wallet_id: int
    market_id: int
    answer: AnswerChoice
    answer_text: constr(to_lower=True, min_length=1, max_length=27) | None = None


class CreateBetBackgroundModel(CreateBetModel):
    state: BetState
    result: int


__all__ = [
    "CreateBetModel",
    "CreateBetBackgroundModel",
]
