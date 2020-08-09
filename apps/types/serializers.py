from rest_framework import serializers

from .models import Type


class TypesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Type
        fields = ("url", "id", "title", "color",)
