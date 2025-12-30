from pydantic import constr

from ..base import KafkaBaseModel
from .enums import AnswerChoice, BetState


class CreateBetModel(KafkaBaseModel):
    wallet_id: int
    market_id: int
    answer: AnswerChoice
    answer_text: constr(to_lower=True, min_length=1, max_length=27) | None = None

    @model_validator(mode="after")
    def validate_any_answer_exists(self) -> Self:
        if not any([self.answer, self.answer_text]):
            raise ValueError("Answer or answer_text are required")
        return self

    @property
    def answer_lower(self) -> str:
        return self.answer.lower() if self.answer else self.answer_text.lower()


class CreateBetBackgroundModel(CreateBetModel):
    state: BetState
    result: int


__all__ = [
    "CreateBetModel",
    "CreateBetBackgroundModel",
]
