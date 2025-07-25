import asyncio
from datetime import datetime, timedelta, UTC

__all__ = ["ExpiredCachedDict"]


class ExpiredCacheDict:
    def __init__(self):
        self.__expire = {}
        self.__values = {}
        asyncio.create_task(self.__clear_expired_keys())
        self.__run = True

    @property
    def expire(self):
        return self.__expire

    @property
    def values(self):
        return self.__values

    def __setitem__(self, key, value):
        expired_sec = None
        if 1 < len(value) < 3:
            expired_sec = value[1]
            value = value[0]
        if expired_sec is not None and not isinstance(expired_sec, int):
            raise TypeError("expired_sec must be int or None")
        self.__values[key] = value
        if expired_sec is not None:
            self.__expire[key] = datetime.now(UTC) + timedelta(seconds=expired_sec)

    def __getitem__(self, key):
        expired_at = self.__expire.get(key)
        value = None
        if expired_at is None or expired_at > datetime.now(UTC):
            value = self.__values.get(key)
        return value

    def __del__(self):
        self.__run = False
        self.__expire.clear()
        self.__values.clear()

    async def __clear_expired_keys(self):
        await asyncio.sleep(10)
        while self.__run:
            need_remove = []
            for key in self.__expire:
                if datetime.now(UTC) > self.__expire[key]:
                    need_remove.append(key)
            for key in need_remove:
                self.__expire.pop(key)
                self.__values.pop(key)
            await asyncio.sleep(6)