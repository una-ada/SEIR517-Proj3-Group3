from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def trips_create(request):
  return render(request, 'main_app/trip_form.html')

def trips_delete(request):
  return render(request, 'main_app/trip_confirm_delete.html')