from aska.client.client import Client


class TaskSender:
    def __init__(self, client: Client):
        self._client = client
