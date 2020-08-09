from rest_framework import permissions, viewsets

from .models import Type
from .serializers import TypesSerializer


class TypesViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypesSerializer
