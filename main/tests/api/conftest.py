import pytest
from mixer.backend.django import mixer


# @pytest.fixture
# def hotel():
#     return mixer.blend(
#         'main.Hotel',
#         history=[{
#             "id": 16,
#             "name": "new meta hotel",
#             "join": "2022-11-20T14:11:52.499948+00:00",
#             "leave": "2022-11-20T20:55:30.552826+00:00"
#         }]
#     )


@pytest.fixture
def meta_hotel():
    return mixer.blend('main.MetaHotel', name='First')


@pytest.fixture
def hotel(meta_hotel):
    return mixer.blend(
        'main.Hotel',
        name='Hotel 1',
        supplier_id='aaa',
        meta_hotel_id=meta_hotel.id,
        history={"history": [{"id": 16, "name": "Meta hotel", "join": "2022-11-20", "leave": "2022-11-20"}]}
    )
