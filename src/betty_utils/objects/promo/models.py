from ..base import KafkaBaseModel


class PromoAnswerModel(KafkaBaseModel):
    promo_id: int
    user_id: int


__all__ = [
    "PromoAnswerModel",
]
