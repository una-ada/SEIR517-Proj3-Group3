from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trips/', views.trips_index, name='index'),
    path('trips/<int:trip_id>/', views.trips_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('trips/new/', views.trips_create, name='trips_create'),
    path('trips/delete/', views.trips_delete, name='trips_delete'),
]