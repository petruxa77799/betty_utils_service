from datetime import datetime
from uuid import UUID

from ..base import KafkaBaseModel


class UserCallbackModel(KafkaBaseModel):
    user_id: int
    partner_id: int
    last_login_dt: datetime | None
    is_new_user: bool
    invite_uuid: UUID | None


__all__ = [
    "UserCallbackModel",
]
