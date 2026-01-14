from ..base import KafkaBaseModel


class MarketingModel(KafkaBaseModel):
    id: int
    erid: str
    title: str


__all__ = ["MarketingModel"]
