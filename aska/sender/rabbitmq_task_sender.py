from aska.client.pika_client import PikaClient
from aska.sender.task_sender import TaskSender


class RabbitMQTaskSender(TaskSender):
    def __init__(self, client: PikaClient):
        self._client = client
