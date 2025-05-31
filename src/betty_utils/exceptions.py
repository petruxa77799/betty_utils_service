__all__ = (
    "EventNotFound",
    "LeaderboardNotFound",
    "AuthRequiredException",
    "EnterEventException",
    "UserNotAvailable",
    "WalletNotFound",
    "WalletNotAvailable",
    "PartnerNotFound",
    "UserNotFound",
    "UserAlreadyExists",
)


class PartnerNotFound(Exception): ...


class EventNotFound(Exception): ...


class LeaderboardNotFound(Exception): ...


class AuthRequiredException(Exception): ...


class UserNotAvailable(Exception): ...


class EnterEventException(Exception): ...


class WalletNotFound(Exception): ...


class WalletNotAvailable(Exception): ...


class UserNotFound(Exception): ...


class UserAlreadyExists(Exception): ...
