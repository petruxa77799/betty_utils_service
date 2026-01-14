from pydantic import BaseModel


class Marketing(BaseModel):
    id: int
    erid: str
    title: str


__all__ = [
    "EnterEventModel",
    "WalletModel",
    "WsResultUpdateMessageModel"
]
