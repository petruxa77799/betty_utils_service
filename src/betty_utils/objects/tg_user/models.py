from uuid import UUID

from ..base import KafkaBaseModel


class TGUserModel(KafkaBaseModel):
    telegram_id: int
    username: str | None
    partner_id: int
    invite_uuid: UUID | None
    registration_qr_uuid: UUID | None


class TGLostUserModel(KafkaBaseModel):
    telegram_id: int
    partner_id: int


__all__ = [
    "TGUserModel",
    "TGLostUserModel",
]
