import os
from functools import wraps

import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, UTC

from .exception import AuthRequiredException

__all__ = ["AuthorizationTools", "user_exists"]


class AuthorizationTools:
    secret = os.getenv("AUTH_SECRET_SALT")
    algorithm = "HS256"
    access_token_second = 900
    refresh_token_second = 3600 * 24 * 90

    @classmethod
    def get_token_pair(cls, user_id: int) -> (str, str, int, int):
        created_at = int(datetime.now(UTC).timestamp())
        access_expires_at = created_at + cls.access_token_second
        refresh_expires_at = created_at + cls.refresh_token_second
        access_payload = {
            "user_id": user_id,
            "expires_at_t": access_expires_at,
            "is_refresh": False,
        }
        access_token = jwt.encode(access_payload, cls.secret, algorithm=cls.algorithm)
        refresh_payload = {
            "user_id": user_id,
            "expires_at_t": refresh_expires_at,
            "is_refresh": True,
        }
        refresh_token = jwt.encode(refresh_payload, cls.secret, algorithm=cls.algorithm)
        return access_token, refresh_token, access_expires_at, refresh_expires_at

    @classmethod
    def validate_token(cls, token: str, is_refresh: bool = False) -> int | None:
        try:
            data = jwt.decode(token, cls.secret, algorithms=cls.algorithm)
        except InvalidTokenError:
            user_id = None
        else:
            user_id = data.get("user_id")
            refresh = data.get("is_refresh")
            if user_id and is_refresh != refresh:
                user_id = None
            if user_id and data.get("expires_at_t") < datetime.now(UTC).timestamp():
                user_id = None

        return user_id


def user_exists(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if not kwargs["request"].state.user_id:
            raise AuthRequiredException()
        return await func(*args, **kwargs)

    return wrapper
