from uuid import UUID
from datetime import datetime
from ..base import KafkaBaseModel


class DistributionModel(KafkaBaseModel):
    distribution_id: int
    version_key: UUID
    send_at: datetime


__all__ = [
    "DistributionModel",
]
