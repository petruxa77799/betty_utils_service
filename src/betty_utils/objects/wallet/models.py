from ..base import KafkaBaseModel


class EnterEventModel(KafkaBaseModel):
    event_id: int
    user_id: int


__all__ = [
    "EnterEventModel",
]
