from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=200, blank=True)
    address = models.TextField(null=True, blank=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    request_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.phone


class Dropoff(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    num_bottles = models.IntegerField(default=0)
    num_bags = models.IntegerField(default=0)
    dropoff_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.subscriber)
