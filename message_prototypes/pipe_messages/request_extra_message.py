from message_prototypes import BaseMessage


class RequestExtraMessage(BaseMessage):
    _serializable_fields = [
        'json', 'post', 'headers',
    ]

    def __init__(self):
        self._json = {}
        self._post = {}
        self._headers = {}

    @property
    def json(self): return self._json

    @json.setter
    def json(self, value): self._json = value

    @property
    def post(self): return self._post

    @post.setter
    def post(self, value): self._post = value

    @property
    def headers(self): return self._headers

    @headers.setter
    def headers(self, value): self._headers = value
