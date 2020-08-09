from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = News
        fields = ("url", "id", "title", "short_text", "full_text", "news_type",)
