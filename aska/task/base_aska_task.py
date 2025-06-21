from aska.sender.task_sender import TaskSender


class BaseAskaTask:
    def __init__(self, task_sender: TaskSender):
        self._task_sender = task_sender
