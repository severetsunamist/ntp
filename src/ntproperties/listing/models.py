from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=24)
    address = models.CharField(max_length=256)
    type = models.CharField(max_length=64)
    is_built = models.BooleanField(default=True)
    gba = models.PositiveIntegerField(default=10000)
    gla = models.PositiveIntegerField(default=9500)
    owner = models.CharField(max_length=128)

