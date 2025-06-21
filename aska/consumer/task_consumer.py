from aska.client.client import Client


class TaskConsumer:
    def __init__(self, client: Client):
        self._client = client
