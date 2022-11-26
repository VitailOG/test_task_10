import pytest

from mixer.backend.django import mixer

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def meta_hotel():
    return mixer.blend('main.MetaHotel', name='First')


@pytest.fixture
def hotel(meta_hotel):
    return mixer.cycle(2).blend('main.Hotel', meta_hotel_id=meta_hotel.id)


@pytest.fixture
def send_request_on_list_meta_hotel(api_client, hotel, meta_hotel):
    return lambda: api_client.get('/meta-hotel/')


def test_meta_hotel_list(send_request_on_list_meta_hotel):
    res = send_request_on_list_meta_hotel()
    assert res.status_code == 200
    assert len(res.data) == 1
    assert len(res.data[0]['hotels']) == 2


def test_meta_hotel_list_response(send_request_on_list_meta_hotel):
    res = send_request_on_list_meta_hotel()
    data = res.data[0]
    assert data['name'] == 'First'
    assert all([hotel['meta_hotel'] == data['id'] for hotel in data['hotels']])
