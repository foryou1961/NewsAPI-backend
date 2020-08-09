from django.urls import include, path
from rest_framework import routers

from .views import TypesViewSet

router = routers.DefaultRouter()
router.register("types", TypesViewSet)


urlpatterns = [
    path("", include(router.urls))
]
