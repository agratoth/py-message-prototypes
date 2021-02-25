from message_prototypes import BaseMessage


class ResponseMessage(BaseMessage):
    _serializable_fields = [
        'status', 'result', 'error_code', 'error',
    ]

    def __init__(self):
        self._status = False
        self._result = None
        self._error_code = None
        self._error = None

    @property
    def status(self): return self._status

    @status.setter
    def status(self, value): self._status = value

    @property
    def result(self): return self._result

    @result.setter
    def result(self, value): self._result = value

    @property
    def error_code(self): return self._error_code

    @error_code.setter
    def error_code(self, value): self._error_code = value

    @property
    def error(self): return self._error

    @error.setter
    def error(self, value): self._error = value
