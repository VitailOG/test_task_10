import pytest

pytestmark = [pytest.mark.django_db]  # pytest freeze


@pytest.fixture
def send_request_on_detail_hotel(api_client, hotel):
    return lambda: api_client.get(f'/hotel/{hotel.id}/')


def test_detail_hotel_status(send_request_on_detail_hotel):
    res = send_request_on_detail_hotel()
    assert res.status_code == 200


def test_detail_hotel_response(send_request_on_detail_hotel):
    res = send_request_on_detail_hotel()
    assert res.data['name'] == 'Hotel 1'
    assert res.data['supplier_id'] == 'aaa'
    assert res.data['meta_hotel'] == 1
    assert res.data['history']['history'][0]['name'] == 'Meta hotel'
