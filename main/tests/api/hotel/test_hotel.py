import pytest

from main.models import Hotel

pytestmark = [pytest.mark.django_db]  # pytest freeze


@pytest.fixture
def send_request_on_create_hotel(api_client):
    data = {
        "name": "hotel 2",
        "supplier_id": "hot"
    }
    return lambda: api_client.post('/hotel/', data)


def test_create_in_db_new_hotel(send_request_on_create_hotel):
    assert not Hotel.objects.filter(name="hotel 2").exists()
    send_request_on_create_hotel()
    assert Hotel.objects.filter(name="hotel 2").exists()


def test_create_hotel_status(send_request_on_create_hotel):
    res = send_request_on_create_hotel()
    assert res.status_code == 201


def test_create_hotel_response(send_request_on_create_hotel):
    res = send_request_on_create_hotel()
    assert len(res.data) == 3
    assert res.data['name'] == 'hotel 2'
    assert res.data['supplier_id'] == 'hot'
    assert res.data['meta_hotel'] is None

