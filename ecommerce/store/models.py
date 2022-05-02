from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneTonOneField(User, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
