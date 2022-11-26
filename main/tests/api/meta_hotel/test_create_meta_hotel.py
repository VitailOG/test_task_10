import pytest

from main.models import MetaHotel

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def send_request_on_create_meta_hotel(api_client, hotel):
    data = {
        "name": "new meta hotel",
        "hotels": [hotel.id]
    }
    return lambda: api_client.post('/meta-hotel/', data)


def test_create_meta_hotel_status(send_request_on_create_meta_hotel, hotel):
    res = send_request_on_create_meta_hotel()
    hotel.refresh_from_db()
    assert res.status_code == 201


def test_create_in_db_new_meta_hotel(send_request_on_create_meta_hotel):
    assert not MetaHotel.objects.filter(name="new meta hotel").exists()
    send_request_on_create_meta_hotel()
    assert MetaHotel.objects.filter(name="new meta hotel").exists()


def test_create_meta_hotel_response(send_request_on_create_meta_hotel, hotel):
    res = send_request_on_create_meta_hotel()
    assert res.data['name'] == 'new meta hotel'
    assert res.data['hotels'] == [1]
