from aska.consumer.task_consumer import TaskConsumer


class AskaWorker:
    def __init__(self, task_consumer: TaskConsumer):
        self._task_consumer = task_consumer
