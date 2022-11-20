import pytest

from mixer.backend.django import mixer

from main.services.update_history import update_hotel_history

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def mh():
    return mixer.blend('main.MetaHotel', id=2)


@pytest.fixture
def data_example_1():
    return {"history": []}


@pytest.fixture
def data_example_2(mh):
    return {
        "history": [
            {'id': 2, "name": mh.name, "join": '2022-11-20T14:38:55.702216+00:00', "leave": None}
        ]
    }


@pytest.fixture
def data_example_3(mh):
    return {
        "history": [
            {'id': 3, "name": mh.name, "join": '2022-11-20T14:38:55.702216+00:00'}
        ]
    }


def test_episode_1(mh, data_example_1):
    """ Start history """
    res = update_hotel_history(data_example_1, mh)
    assert len(res['history']) == 1
    assert res['history'][0]['join'] is not None
    assert res['history'][0]['leave'] is None


def test_episode_2(mh, data_example_2):
    """ Add new row where id equal id last record """
    res = update_hotel_history(data_example_2, mh)
    assert len(res['history']) == 1
    assert res['history'][0]['join'] is not None
    assert res['history'][0]['leave'] is None


def test_episode_3(mh, data_example_3):
    """ Add new row where id not equal id last record """
    res = update_hotel_history(data_example_3, mh)
    assert len(res['history']) == 2
    assert res['history'][-1]['leave'] is None
    assert res['history'][-2]['leave'] is not None
