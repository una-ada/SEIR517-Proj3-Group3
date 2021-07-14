from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Trip
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.generic import ListView, DetailView



class TripCreate(CreateView):
    model = Trip
    fields = '__all__'

class TripUpdate(UpdateView):
    model = Trip
    fields = '__all__'

class TripDelete(DeleteView):
    model = Trip
    success_url = '/'


# Define the home view
# Create your views here.

def trips_index(request):
  trips = Trip.objects.all()
  return render(request, 'home.html', {'trips': trips })

def trips_detail(request,trip_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'trips/detail.html', {'trip': trip})

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
