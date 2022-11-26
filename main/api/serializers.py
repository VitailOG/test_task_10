from rest_framework import serializers

from ..models import MetaHotel


class CreateHotelSerializer(serializers.Serializer):
    name = serializers.CharField(label='Назва готеля', max_length=32)
    supplier_id = serializers.CharField(label='Поставщик', max_length=3)
    meta_hotel = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=MetaHotel.objects.all(), required=False)


class DetailHotelSerializer(CreateHotelSerializer):
    history = serializers.JSONField()


class MetaHotelSerializer(serializers.ModelSerializer):
    hotels = CreateHotelSerializer(many=True)

    class Meta:
        model = MetaHotel
        fields = ('id', 'name', 'hotels')


class CreateMetaHotelSerializer(serializers.Serializer):
    name = serializers.CharField(label='Назва готеля', max_length=32)
    hotels = serializers.ListField(
        child=serializers.IntegerField(min_value=1), min_length=1
    )
