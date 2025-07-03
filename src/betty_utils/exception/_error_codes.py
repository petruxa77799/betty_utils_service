from enum import StrEnum

__all__ = [
    "ErrorCode",
    "EventErrorCode",
    "AuthErrorCode",
    "UserErrorCode",
    "WalletErrorCode",
    "PartnerErrorCode",
    "LeaderboardErrorCode",
]


class AuthErrorCode(StrEnum):
    CODE_EXPIRED_ERROR = "AU_001"
    CODE_NOT_FOUND = "AU_002"
    UNAUTHORIZED = "AU_003"
    TELEGRAM_VALIDATION_FAIL = "AU_004"


class ErrorCode(StrEnum):
    PROCESS_VALIDATION_ERROR = "VA_001"
    UNHANDLED_ERROR = "CR_001"


class LeaderboardErrorCode(StrEnum):
    LEADERBOARD_NOT_FOUND = "LB_001"


class EventErrorCode(StrEnum):
    EVENT_NOT_FOUND = "EV_001"
    ENTER_EVENT_EXCEPTION = "EV_002"


class UserErrorCode(StrEnum):
    USER_NOT_FOUND = "US_001"
    USER_ALREADY_EXISTS = "US_002"
    USER_NOT_AVAILABLE = "US_003"


class WalletErrorCode(StrEnum):
    WALLET_NOT_FOUND = "WA_001"
    WALLET_NOT_AVAILABLE = "WA_002"


class PartnerErrorCode(StrEnum):
    PARTNER_NOT_FOUND = "PS_001"
