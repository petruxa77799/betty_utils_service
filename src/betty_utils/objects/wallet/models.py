from ..base import KafkaBaseModel


class EnterEventModel(KafkaBaseModel):
    event_id: int
    user_id: int


class WalletModel(KafkaBaseModel):
    id: int
    result: int | None = None


__all__ = [
    "EnterEventModel",
]
