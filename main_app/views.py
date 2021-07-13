from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def trips_create(request):
  return render(request, 'trips/create.html')

def trips_delete(request):
  return render(request, 'trips/confirm_delete.html')