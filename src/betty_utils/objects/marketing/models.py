from ..base import KafkaBaseModel


class MarketingModel(KafkaBaseModel):
    id: int
    erid: str
    title: str | None = None


__all__ = ["MarketingModel"]
