from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Trip(models.Model):
    title = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
