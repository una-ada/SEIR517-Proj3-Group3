from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Trip

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def trips_index(request):
  trips = Trip.objects.all()
  return render(request, 'trips/index.html', {'trips': trips })

def trips_detail(request,trip_id):
    trips = Trip.objects.get(id=trip_id)
    return render(request, 'trips/detail.html',{'trip' : trips})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def trips_create(request):
  return render(request, 'trips/create.html')

def trips_delete(request):
  return render(request, 'trips/confirm_delete.html')

