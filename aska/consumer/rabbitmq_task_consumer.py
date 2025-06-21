from aska.client.pika_client import PikaClient
from aska.consumer.task_consumer import TaskConsumer


class RabbitMQTaskConsumer(TaskConsumer):
    def __init__(self, client: PikaClient):
        self._client = client
