from django.db.transaction import atomic

from .update_history import update_hotel_history
from ..repositories.containers import MainContainer


def create_meta_hotel(data):
    with atomic():
        new_meta_hotel = MainContainer.meta_hotel.create_meta_hotel(data['name'])  # mock error
        hotels = MainContainer.hotel.get_hotels_by_ids(data['hotels'])
        for i in hotels:
            i.meta_hotel_id = new_meta_hotel.id
            i.history = update_hotel_history(i.history, new_meta_hotel)

        MainContainer.hotel.bulk_update_hotel(hotels, ['meta_hotel_id', 'history'])
