from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Diary_Entry, Trip
from .forms import Diary_EntryForm, NoteForm
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
    diary_entry_form = Diary_EntryForm()
    note_form = NoteForm()
    return render(request, 'trips/detail.html', {
      'trip': trip, 'diary_entry_form': diary_entry_form, 'note_form': note_form})


def add_diary_entry(request, trip_id):
  # create a ModelForm instance using the data in request.POST
  form = Diary_EntryForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_diary_entry = form.save(commit=False)
    new_diary_entry.trip_id = trip_id
    new_diary_entry.save()
  return redirect('detail', trip_id=trip_id)

def add_note(request, trip_id):
  # create a ModelForm instance using the data in request.POST
  form = NoteForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_note = form.save(commit=False)
    new_note.trip_id = trip_id
    new_note.save()
  return redirect('detail', trip_id=trip_id)

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
