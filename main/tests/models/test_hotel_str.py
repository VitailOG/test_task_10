import pytest

from mixer.backend.django import mixer

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def hotel():
    return mixer.blend('main.Hotel')


def test_ok(hotel):
    assert str(hotel) == f"{str(hotel.id)}, {hotel.name}"
