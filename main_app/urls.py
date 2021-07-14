from django.urls import path
from . import views

urlpatterns = [
    path('', views.trips_index, name='index'),
    path('trips/<int:trip_id>/', views.trips_detail, name='detail'),
    path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
    path('trips/<int:trip_id>/add_diary_entry/', views.add_diary_entry, name='add_diary_entry'),
    path('trips/<int:trip_id>/add_note/', views.add_note, name='add_note'),
    path('accounts/signup/', views.signup, name='signup'),
]