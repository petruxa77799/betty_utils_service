from enum import StrEnum


class KafkaTopics(StrEnum):
    TG_USERS_TOPIC = "dev.tg_users_topic"
    TG_LOST_USERS_TOPIC = "dev.lost_users_topic"
    TG_MESSAGES_TOPIC = "dev.messages_topic"
    USERS_CALLBACK_TOPIC = "dev.user_callback_topic"
    MARKET_RESOLVE_TOPIC = "dev.market_resolve_topic"
    CREATE_BET_TOPIC = "dev.create_bet_topic"
    WS_WALLET_TOPIC = "dev.ws_wallet_topic"
    PROMO_ANSWER_TOPIC = "dev.promo_answer_topic"
    ENTER_EVENT_TOPIC = "dev.enter_event_topic"
    INVITE_REWARD_TOPIC = "dev.invite_reward_topic"
