from enum import StrEnum


class KafkaTopics(StrEnum):
    TG_USERS_TOPIC = "dev.tg_users_topic"
    TG_LOST_USERS_TOPIC = "dev.lost_users_topic"
    TG_MESSAGES_TOPIC = "dev.messages_topic"
