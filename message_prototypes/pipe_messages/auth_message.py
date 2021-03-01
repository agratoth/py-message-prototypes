from message_prototypes import BaseMessage


class AuthMessage(BaseMessage):
    _serializable_fields = [
        'user_id', 'secret'
    ]

    def __init__(self):
        self._user_id = None
        self._secret = None

    @property
    def user_id(self): return self._user_id

    @user_id.setter
    def user_id(self, value): self._user_id = value

    @property
    def secret(self): return self._secret

    @secret.setter
    def secret(self, value): self._secret = value
