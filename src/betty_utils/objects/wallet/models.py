from ..base import KafkaBaseModel
from ..bet.enums import BetState
from .enums import ResultUpdateType


class EnterEventModel(KafkaBaseModel):
    wallet_id: int | None = None
    event_id: int
    user_id: int


class WalletModel(KafkaBaseModel):
    id: int
    result: int | None = None
    update_type: ResultUpdateType


class WsResultUpdateMessageModel(KafkaBaseModel):
    wallet_id: int
    bet: dict | None = None
    profit: int
    right_answer: str | None = None
    state: BetState | None
    invite: dict | None = None
    update_type: ResultUpdateType


__all__ = [
    "EnterEventModel",
    "WalletModel",
    "WsResultUpdateMessageModel"
]
