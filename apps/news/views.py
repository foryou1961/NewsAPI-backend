from rest_framework import permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['news_type',]
