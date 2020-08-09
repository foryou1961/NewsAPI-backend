from django.urls import include, path
from rest_framework import routers

from .views import NewsViewSet

router = routers.DefaultRouter()
router.register("news", NewsViewSet)


urlpatterns = [
    path("", include(router.urls))
]
