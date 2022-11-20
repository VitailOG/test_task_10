from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from main.models import Hotel, MetaHotel
from main.repositories import BaseRepository
from main.services.update_history import update_hotel_history


class HotelRepository(BaseRepository[Hotel]):
    model: Hotel = Hotel

    def create_hotel(self, values) -> None:
        self.model.objects.create(**values)

    def get_hotels_by_ids(self, ids: list[int]) -> QuerySet[Hotel]:
        return self.model.objects.filter(id__in=ids)

    def bulk_update_hotel(self, qs: QuerySet[Hotel], fields: list[str]) -> None:
        self.model.objects.bulk_update(qs, fields=fields)

    def update_hotel(self, pk: int, meta_hotel: MetaHotel) -> None:
        hotel = get_object_or_404(self.model, pk=pk)
        hotel.meta_hotel_id = meta_hotel.id
        hotel.history = update_hotel_history(hotel.history, meta_hotel)
        hotel.save(update_fields=['history', 'meta_hotel_id'])
