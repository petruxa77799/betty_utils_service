import asyncio
from typing import Optional

from aiokafka import AIOKafkaConsumer, TopicPartition, AIOKafkaProducer
from aiokafka.structs import ConsumerRecord

from betty_utils.logs import logger
from ujson import dumps


__all__ = [
    "BaseConsumer",
    "BaseProducer",
]


class BaseConsumer:
    def __init__(
        self,
        servers: list[str],
        client_id: str,
        topic: str,
        group_id: str,
        enable_auto_commit: bool = False,
        max_poll_records: Optional[int] = None,
        max_poll_interval_ms: int = 300000,
        session_timeout_ms: int = 45000,
        app=None,
        ws_data=None,
        consumer_timeout: int = 0,
    ):
        self._app = app
        self._topic = topic
        self._message_serializer = None
        self._consumer = None
        self._consume_task = None
        self._kafka_server = servers
        self._client_id = client_id
        self._group_id = group_id
        self._enable_auto_commit = enable_auto_commit
        self._max_poll_records = max_poll_records
        self._max_poll_interval_ms = max_poll_interval_ms
        self._session_timeout_ms = session_timeout_ms
        self._create_consumer()
        self._ws_data = ws_data
        self._consumer_timeout = consumer_timeout

    async def start(self):
        await self._consumer.start()
        self._consume_task = asyncio.create_task(self._consume_messages_from_kafka())

    async def close(self):
        self._consume_task.cancel()
        await self._consumer.stop()

    @staticmethod
    def _key_deserializer(msg_key):
        return msg_key.decode()

    def _create_consumer(self):
        self._consumer = AIOKafkaConsumer(
            self._topic,
            bootstrap_servers=self._kafka_server,
            group_id=self._group_id,
            client_id=self._client_id,
            max_poll_records=self._max_poll_records,
            enable_auto_commit=self._enable_auto_commit,
            max_poll_interval_ms=self._max_poll_interval_ms,
            session_timeout_ms=self._session_timeout_ms,
            isolation_level="read_committed",
        )

    @staticmethod
    def _parse_key(key):
        return key.split(".")

    async def process_msg(self, result: dict[TopicPartition, list[ConsumerRecord]]):
        raise NotImplementedError

    async def _consume_messages_from_kafka(self):
        await asyncio.sleep(5)
        while True:
            result = await self._consumer.getmany(timeout_ms=10000)
            try:
                await self.process_msg(result=result)
            except Exception as e:
                logger.exception(f"Problem with consumed message {e}")
            if self._consumer_timeout:
                await asyncio.sleep(self._consumer_timeout)


class BaseProducer:
    def __init__(self, servers: list[str], client_id: str):
        self._kafka_server = servers
        self._client_id = client_id

        self._producer = AIOKafkaProducer(
            bootstrap_servers=self._kafka_server,
            client_id=self._client_id,
            enable_idempotence=True,
        )

    async def start(self):
        await self._producer.start()

    async def close(self):
        await self._producer.stop()

    async def produce(self, data: dict, key: str, topic: str):
        try:
            await self._producer.send_and_wait(
                topic=topic, value=dumps(data).encode(), key=key.encode()
            )
        except Exception as ex:
            logger.exception(f"Problem with producer {ex}")
