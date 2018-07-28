from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=200, blank=True)
    address = models.TextField(null=True, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    request_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.phone
