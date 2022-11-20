from rest_framework import routers

from main.api.endpoints import HotelAPI, MetaHotelAPI

router = routers.SimpleRouter()

router.register('hotel', HotelAPI, basename='hotel')

router.register('meta-hotel', MetaHotelAPI, basename='meta-hotel')

urlpatterns = []

urlpatterns += router.urls
