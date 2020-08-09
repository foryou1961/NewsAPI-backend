from django.contrib import admin
from django.urls import include, path

from apps.types.urls import router as types_router


urlpatterns = [
    path("", include("apps.news.urls")),
]

urlpatterns += types_router.urls
