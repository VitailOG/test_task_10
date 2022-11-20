from .hotel import HotelRepository
from .meta_hotel import MetaHotelRepository


class MainContainer:
    hotel = HotelRepository()
    meta_hotel = MetaHotelRepository()


__all__ = ['MainContainer']
