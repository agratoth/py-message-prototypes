import json

from message_prototypes.exceptions import MissingModelException


class BaseMessage:
    _serializable_fields = []

    def pack(self, unpacking_info=True):
        result = {
            '_model': self.__class__.__name__,
        } if unpacking_info else {}

        def serialize_node(node=None):
            if isinstance(node, (str, int, type(None))):
                return node
            elif isinstance(node, list):
                return [
                    serialize_node(elem)
                    for elem
                    in node
                ]
            elif isinstance(node, dict):
                return {
                    elem_name: serialize_node(elem)
                    for elem_name, elem
                    in node.items()
                }
            elif isinstance(node, BaseMessage):
                return node.pack(unpacking_info=unpacking_info)

        for field_name in self._serializable_fields:
            field_value = getattr(self, field_name)
            result[field_name] = serialize_node(field_value)

        return result

    def json(self):
        return json.dumps(self.pack())

    @classmethod
    def unpack(cls, data={}):
        result = cls()

        if '_model' not in data:
            raise MissingModelException

        def deserialize_node(node={}):
            if isinstance(node, (str, int, type(None))):
                return node
            elif isinstance(node, list):
                return [
                    deserialize_node(elem)
                    for elem
                    in node
                ]
            elif isinstance(node, dict):
                if '_model' in node:
                    subclass = cls.detect_model(node)
                    if subclass:
                        return subclass.unpack(node)
                    return None
                else:
                    return {
                        elem_name: deserialize_node(elem)
                        for elem_name, elem
                        in node.items()
                    }

        for field_name in cls._serializable_fields:
            field_value = data.get(field_name, None)
            setattr(result, field_name, deserialize_node(field_value))

        return result

    @classmethod
    def detect_model(cls, data={}):
        if '_model' not in data:
            raise MissingModelException

        subclasses = BaseMessage.__subclasses__()
        for subclass in subclasses:
            if subclass.__name__ == data['_model']:
                return subclass
        return None