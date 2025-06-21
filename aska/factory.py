from aska.client.pika_client import PikaClient
from aska.consumer.rabbitmq_task_consumer import RabbitMQTaskConsumer
from aska.sender.rabbitmq_task_sender import RabbitMQTaskSender


class AskaFactory:
    @classmethod
    def make_client(cls) -> PikaClient:
        return PikaClient()

    @classmethod
    def make_consumer(cls) -> RabbitMQTaskConsumer:
        return RabbitMQTaskConsumer(client=cls.make_client())

    @classmethod
    def make_sender(cls) -> RabbitMQTaskSender:
        return RabbitMQTaskSender(client=cls.make_client())
