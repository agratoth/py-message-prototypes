from message_prototypes import BaseMessage


class ActionPathMessage(BaseMessage):
    _serializable_fields = [
        'base', 'point', 'action', 'params'
    ]

    def __init__(self):
        self._base = None
        self._point = None
        self._action = None
        self._params = None

    @property
    def base(self): return self._base

    @base.setter
    def base(self, value): self._base = value

    @property
    def point(self): return self._point

    @point.setter
    def point(self, value): self._point = value

    @property
    def action(self): return self._action

    @action.setter
    def action(self, value): self._action = value

    @property
    def params(self): return self._params

    @params.setter
    def params(self, value): self._params = value
