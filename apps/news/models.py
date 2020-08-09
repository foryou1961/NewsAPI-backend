from django.db import models

from apps.types.models import Type


class News(models.Model):

    title = models.CharField(max_length=50)
    short_text = models.TextField(max_length=100)
    full_text = models.TextField(max_length=500)
    news_type = models.ForeignKey(Type, on_delete=models.CASCADE)
