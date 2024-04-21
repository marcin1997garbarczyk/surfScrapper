from django.db import models

# Create your models here.

class Subscriber(models.Model):
    userEmail = models.CharField(max_length=200)
    trackedBeaches = models.CharField(max_length=5000)