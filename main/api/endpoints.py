from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import CreateHotelSerializer, MetaHotelSerializer, CreateMetaHotelSerializer
from ..models import MetaHotel, Hotel
from ..repositories.containers import MainContainer
from ..services.create_meta_hotel import create_meta_hotel


class HotelAPI(GenericViewSet):
    serializer_class = CreateHotelSerializer
    queryset = Hotel.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        MainContainer.hotel.create_hotel(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        meta_hotel = serializer.validated_data['meta_hotel']
        MainContainer.hotel.update_hotel(kwargs['pk'], meta_hotel)
        return Response({"update_ok": True}, status=status.HTTP_200_OK)


class MetaHotelAPI(mixins.ListModelMixin, GenericViewSet):
    serializer_class = MetaHotelSerializer
    queryset = MetaHotel.objects.all()

    def create(self, request):
        serializer = CreateMetaHotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_meta_hotel(serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
