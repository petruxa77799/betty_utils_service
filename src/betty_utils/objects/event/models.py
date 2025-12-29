from ..base import KafkaBaseModel


class WSEventModel(KafkaBaseModel):
    event_id: int
    action: str  # ToDo: implement enum
