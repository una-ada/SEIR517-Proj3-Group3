from django.contrib import admin
from .models import Trip, Photo, Diary_Entry, Notes

# Register your models here.
admin.site.register(Trip)
admin.site.register(Photo)
admin.site.register(Diary_Entry)
admin.site.register(Notes)
