from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, TextField

# Create your models here.

class Trip(models.Model):
    title = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title   

class Photo(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    image = CharField(max_length=200)

class Diary_Entry(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return f"{self.get_content_display()} on {self.date}"

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    content = TextField()
