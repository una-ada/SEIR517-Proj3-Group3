from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trips/new/', views.trips_create, name='trips_create')
]