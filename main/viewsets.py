from rest_framework.serializers import SerializerMetaclass


class SerializerClassMixin:
    serializers_map: dict[str, SerializerMetaclass] = {}

    def get_serializer_class(self) -> SerializerMetaclass:
        assert self.serializers_map.keys() != 0, 'set default serializer'
        assert 'default' in self.serializers_map

        return self.serializers_map.get(getattr(self, 'action'), self.serializers_map['default'])
