from pydantic import BaseModel, model_validator
import ujson


class KafkaBaseModel(BaseModel):
    @model_validator(mode="before")
    def json_validate(cls, value):
        if isinstance(value, (str, bytes)):
            return ujson.loads(value)
        return value


__all__ = [
    "KafkaBaseModel",
]
