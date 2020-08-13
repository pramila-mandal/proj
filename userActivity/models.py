from django.db import models

# Create your models here.
class User(models.Model):
    real_name = models.CharField(max_length=512, blank=False, null=False)
    user_id = models.CharField(max_length=32, blank=False, null=False)
    time_zone = models.CharField(max_length=52, blank=False, null=False)


class Activity(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    startTime = models.DateTimeField(blank=False, null=False)
    endTime = models.DateTimeField(blank=False, null=False)