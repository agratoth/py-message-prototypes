from message_prototypes import BaseMessage
from message_prototypes.pipe_messages import ActionPathMessage
from message_prototypes.pipe_messages import RequestExtraMessage


class RequestMessage(BaseMessage):
    _serializable_fields = [
        'path', 'action', 'extra',
    ]

    def __init__(self):
        self._path = ActionPathMessage()
        self._action = None
        self._extra = RequestExtraMessage()

    @property
    def path(self): return self._path

    @path.setter
    def path(self, value): self._path = value

    @property
    def action(self): return self._action

    @action.setter
    def action(self, value): self._action = value

    @property
    def extra(self): return self._extra

    @extra.setter
    def extra(self, value): self._extra = value
