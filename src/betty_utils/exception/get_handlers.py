from logging import Logger
from .mapping import exception_mapping_dict
from ujson import dumps


__all__ = ["log_exception", "get_handler", "get_body"]


def get_body(error_code: str, exc: Exception | dict | list) -> dict:
    return dumps({
        "payload": {},
        "error_code": error_code,
        "error": str(exc),
        "warning": "",
    })


def log_exception(
    logger: Logger,
    status_code: int,
    method: str,
    url: str,
    request_body: str,
    headers: dict,
    body: dict,
    exc_str: str,
) -> None:
    logger.warning(
        f"Fail request. {method} {url} {status_code}",
        {
            "method": method,
            "url": url,
            "request_body": request_body,
            "response_status": status_code,
            "response_body": body,
            "headers": headers,
            "exception": exc_str,
        },
    )


def get_handler(
    exc: Exception,
    logger: Logger,
    method: str,
    url: str,
    request_body: str,
    headers: dict,
) -> (int, str):
    status_code, error_code = exception_mapping_dict[exc]
    body = get_body(error_code, exc)
    log_exception(
        logger, status_code, method, url, request_body, headers, body, str(exc)
    )
    return {"content": body, "status_code": status_code, "media_type": "application/json"}
