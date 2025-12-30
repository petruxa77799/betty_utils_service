from enum import StrEnum


class BetState(StrEnum):
    CREATED = "CREATED"
    RESOLVED = "RESOLVED"
    CANCELLED = "CANCELLED"


class AnswerChoice(StrEnum):
    ANSWER_A = "answer_a"
    ANSWER_B = "answer_b"
    ANSWER_ANY = "answer_any"
    ANSWER_TEXT = "answer_text"


__all__ = [
    "BetState",
    "AnswerChoice",
]
