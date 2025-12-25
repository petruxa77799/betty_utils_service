from enum import StrEnum


class KafkaTopics(StrEnum):
    TG_USERS_TOPIC = "dev.tg_users_topic"
    TG_LOST_USERS_TOPIC = "dev.lost_users_topic"
    TG_MESSAGES_TOPIC = "dev.messages_topic"
    USERS_CALLBACK_TOPIC = "dev.user_callback_topic"
    MARKET_RESOLVE_TOPIC = "dev.market_resolve_topic"
    BETS_TOPIC = "dev.bets_topic"
    WS_WALLET_TOPIC = "dev.ws_wallet_topic"
    PROMO_ANSWER_TOPIC = "dev.promo_answer_topic"
    WALLETS_TOPIC = "dev.wallets_topic"
    WALLETS_CALLBACK_TOPIC = "dev.wallets_callback_topic"
