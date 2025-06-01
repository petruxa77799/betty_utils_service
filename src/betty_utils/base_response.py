__all__ = ["BaseResponse", "with_ok"]


class BaseResponse:
    error: str
    error_code: str
    warning: str


def with_ok(payload: dict | list, warning: str = "") -> dict:
    body = {
        "payload": payload,
        "error_code": "",
        "error": "",
        "warning": warning,
    }
    return body
