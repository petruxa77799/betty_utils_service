from logging import Logger
import os
import sys

from ujson import dumps

from .mapping import exception_mapping_dict


__all__ = ["log_exception", "get_handler", "get_body"]


def get_body(error_code: str, exc: Exception | dict | list) -> str:
    return dumps(
        {
            "payload": {},
            "error_code": error_code,
            "error": str(exc),
            "warning": "",
        }
    )


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


def get_pretty_traceback(exc: Exception) -> str:
    exc_type, value, traceback = sys.exc_info()
    exc_str = (
        f"Error: {exc_type} {exc}\n"
        f"Module: {traceback.tb_frame.f_globals['__name__']}\n"
        f"Lineno: {traceback.tb_lineno}\n"
        f"Service: {os.getenv('SERVICE')}"
    )
    return exc_str


def get_handler(
    exc: Exception,
    logger: Logger,
    method: str,
    url: str,
    request_body: str,
    headers: dict,
) -> (int, str):
    status_code, error_code = exception_mapping_dict.get(type(exc))
    if not status_code:
        exc_str = get_pretty_traceback(exc)  # noqa: F841
        # TODO: Add logs to kafka here
        status_code, error_code = exception_mapping_dict.get(Exception)
    body = get_body(error_code, exc)
    log_exception(
        logger, status_code, method, url, request_body, headers, body, str(exc)
    )
    return {
        "content": body,
        "status_code": status_code,
        "media_type": "application/json",
    }
