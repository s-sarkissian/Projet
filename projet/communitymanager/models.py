from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=200)
    subscribers = models.ManyToManyField(User)
