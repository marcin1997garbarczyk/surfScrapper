from django.db import models

# Create your models here.

class Subscriber(models.Model):
    userEmail = models.CharField(max_length=200)
    trackedBeaches = models.CharField(max_length=5000)
    isActive = models.BooleanField(default=False)

class Beach(models.Model):
    name = models.CharField(max_length=200)
    textForHtml = models.CharField(max_length=5000)
    totalScore = models.IntegerField(default=0)
