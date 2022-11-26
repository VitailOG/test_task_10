import pytest

from mixer.backend.django import mixer

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def meta_hotels():
    return mixer.cycle(2).blend('main.MetaHotel')


# @pytest.fixture
# def hotel():
#     return mixer.blend(
#         'main.Hotel',
#         meta_hotel_id=1,
#         history={"history": [{"id": 16, "name": "Meta hotel", "join": "2022-11-20", "leave": "2022-11-20"}]}
#     )


@pytest.fixture
def send_request_on_update_hotel(api_client, hotel, meta_hotels):
    data = {
        "meta_hotel": 2
    }
    return lambda: api_client.put(f'/hotel/{hotel.id}/', data)


def test_update_status(send_request_on_update_hotel):
    res = send_request_on_update_hotel()
    assert res.status_code == 200


def test_update_in_db(send_request_on_update_hotel, hotel):
    assert len(hotel.history['history']) == 1
    assert hotel.meta_hotel_id == 1
    send_request_on_update_hotel()
    hotel.refresh_from_db()
    assert len(hotel.history['history']) == 2
    assert hotel.meta_hotel_id == 2
