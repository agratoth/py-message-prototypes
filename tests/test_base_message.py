import pytest
import json

from message_prototypes import BaseMessage
from message_prototypes.exceptions import MissingModelException


class TestMessage2(BaseMessage):
    _serializable_fields = ['dict_val']

    def __init__(self):
        self._dict_val = None

    @property
    def dict_val(self): return self._dict_val

    @dict_val.setter
    def dict_val(self, value): self._dict_val = value


class TestMessage(BaseMessage):
    _serializable_fields = ['int_val', 'str_val', 'dict_val', 'message_val']

    def __init__(self):
        self._int_val = None
        self._str_val = None
        self._dict_val = None
        self._message_val = None

    @property
    def int_val(self): return self._int_val

    @int_val.setter
    def int_val(self, value): self._int_val = value

    @property
    def str_val(self): return self._str_val

    @str_val.setter
    def str_val(self, value): self._str_val = value

    @property
    def dict_val(self): return self._dict_val

    @dict_val.setter
    def dict_val(self, value): self._dict_val = value

    @property
    def message_val(self): return self._message_val

    @message_val.setter
    def message_val(self, value): self._message_val = value


dict_data = {
    'val1': 123,
    'val2': 'test123',
    'val3': [111, 222, 'test321']
}


def test_base_message_pack():
    assert BaseMessage().pack().get('_model', None) == 'BaseMessage'


def test_base_message_pack_without_model_name():
    assert BaseMessage()\
        .pack(unpacking_info=False)\
        .get('_model', None) is None


def test_base_message_unpack():
    try:
        BaseMessage.unpack(BaseMessage().pack())
        assert True
    except MissingModelException:
        assert False


def test_base_message_unpack_without_model_name():
    with pytest.raises(MissingModelException):
        BaseMessage.unpack(BaseMessage().pack(unpacking_info=False))


def test_base_message_json_dump():
    data = {
        '_model': 'BaseMessage',
    }
    message = BaseMessage()

    assert message.json() == json.dumps(data)


def test_pack_scalar_value():
    test = TestMessage()
    test.int_val = 123
    test.str_val = 'test123'

    packed_data = test.pack()

    assert packed_data.get('int_val', None) == 123 \
        and packed_data.get('str_val', None) == 'test123'


def test_pack_dict_value():
    test = TestMessage()
    test.dict_val = dict_data

    assert test.pack().get('dict_val', None) == dict_data


def test_unpack_dict_value():
    unpacked_data = {
        '_model': 'TestMessage',
        'dict_val': {
            'val1': 123,
            'val2': 'test123',
            'val3': [111, 222, 'test321']
        }
    }

    test = TestMessage.unpack(data=unpacked_data)

    assert test.dict_val == dict_data


def test_pack_object_value():
    test = TestMessage()
    test.message_val = TestMessage2()
    test.message_val.dict_val = dict_data

    packed = test.pack()

    assert packed.get('message_val', {}).get('dict_val', None) == dict_data


def test_unpack_object_value():
    unpacked_data = {
        '_model': 'TestMessage',
        'message_val': {
            '_model': 'TestMessage2',
            'dict_val': {
                'val1': 123,
                'val2': 'test123',
                'val3': [111, 222, 'test321']
            }
        }
    }

    test = TestMessage.unpack(unpacked_data)
    assert test.message_val.dict_val == dict_data


def test_unpack_incorrect_model():
    unpacked_data = {
        '_model': 'TestMessage',
        'message_val': {
            '_model': 'TestMessage3',
            'dict_val': {
                'val1': 123,
                'val2': 'test123',
                'val3': [111, 222, 'test321']
            }
        }
    }

    test = TestMessage.unpack(unpacked_data)
    assert test.message_val is None


def test_detect_model():
    unpacked_data = {
        '_model': 'TestMessage',
        'message_val': {
            '_model': 'TestMessage3',
            'dict_val': {
                'val1': 123,
                'val2': 'test123',
                'val3': [111, 222, 'test321']
            }
        }
    }

    assert BaseMessage.detect_model(unpacked_data) == TestMessage


def test_detect_model_without_model_name():
    with pytest.raises(MissingModelException):
        BaseMessage.detect_model(BaseMessage().pack(unpacking_info=False))
