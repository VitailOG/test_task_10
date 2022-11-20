from main.models import MetaHotel
from main.repositories import BaseRepository


class MetaHotelRepository(BaseRepository[MetaHotel]):
    model: MetaHotel = MetaHotel

    def create_meta_hotel(self, name: str) -> MetaHotel:
        return self.model.objects.create(name=name)
