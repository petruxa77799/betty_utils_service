from .exceptions import (
    PartnerNotFound,
    EventNotFound,
    LeaderboardNotFound,
    AuthRequiredException,
    UserNotFound,
    UserNotAvailable,
    UserAlreadyExists,
    WalletNotAvailable,
    WalletNotFound,
    EnterEventException,
)
from ._error_codes import (
    ErrorCode,
    PartnerErrorCode,
    EventErrorCode,
    UserErrorCode,
    LeaderboardErrorCode,
    AuthErrorCode,
    WalletErrorCode,
)
from ._error_statuses import (
    BETTY_HTTP_400_BAD_REQUEST,
    BETTY_HTTP_401_UNAUTHORIZED,
    BETTY_HTTP_404_NOT_FOUND,
    BETTY_HTTP_500_INTERNAL_SERVER_ERROR,
)

__all__ = (
    "exception_mapping_dict",
)

exception_mapping_dict = {
    PartnerNotFound: (BETTY_HTTP_404_NOT_FOUND, PartnerErrorCode.PARTNER_NOT_FOUND),
    EventNotFound: (BETTY_HTTP_404_NOT_FOUND, EventErrorCode.EVENT_NOT_FOUND),
    LeaderboardNotFound: (
        BETTY_HTTP_404_NOT_FOUND,
        LeaderboardErrorCode.LEADERBOARD_NOT_FOUND,
    ),
    AuthRequiredException: (BETTY_HTTP_401_UNAUTHORIZED, AuthErrorCode.UNAUTHORIZED),
    UserNotAvailable: (BETTY_HTTP_400_BAD_REQUEST, UserErrorCode.USER_NOT_AVAILABLE),
    EnterEventException: (
        BETTY_HTTP_400_BAD_REQUEST,
        EventErrorCode.ENTER_EVENT_EXCEPTION,
    ),
    WalletNotFound: (BETTY_HTTP_404_NOT_FOUND, WalletErrorCode.WALLET_NOT_FOUND),
    WalletNotAvailable: (
        BETTY_HTTP_400_BAD_REQUEST,
        WalletErrorCode.WALLET_NOT_AVAILABLE,
    ),
    UserNotFound: (BETTY_HTTP_404_NOT_FOUND, UserErrorCode.USER_NOT_FOUND),
    UserAlreadyExists: (BETTY_HTTP_400_BAD_REQUEST, UserErrorCode.USER_ALREADY_EXISTS),
    Exception: (BETTY_HTTP_500_INTERNAL_SERVER_ERROR, ErrorCode.UNHANDLED_ERROR),
}
