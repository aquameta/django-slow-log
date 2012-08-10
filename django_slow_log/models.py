from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):

    pid = models.IntegerField()
    status_code = models.IntegerField(null=True, blank=True)
    time_delta = models.FloatField(null=True, blank=True)
    request_method = models.CharField(max_length=6)
    path = models.TextField()
    django_view = models.CharField(max_length=255)
    memory_delta = models.IntegerField(null=True, blank=True)
    load_delta = models.FloatField(null=True, blank=True)
    queries = models.IntegerField(null=True, blank=True)
    hostname = models.CharField(max_length=255, null=True, blank=True)
    request_started = models.DateTimeField(null=True, blank=True, auto_now=False)
    response_started = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User,
            null=True, blank=True)
