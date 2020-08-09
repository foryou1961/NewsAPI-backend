from django.db import models


class Type(models.Model):

    title = models.CharField(max_length=50)
    color = models.TextField(max_length=50)
