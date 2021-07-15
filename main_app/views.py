from django.http.response import HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls.base import reverse
from .models import Diary_Entry, Trip
from .forms import Diary_EntryForm, NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.views.generic import ListView, DetailView

class TripCreate(LoginRequiredMixin, CreateView):
  model = Trip
  # This can't be '__all__', probably because the form is missing the user
  # field which needs to be added by the validation method!
  fields = ['title', 'from_location', 'to_location']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TripUpdate(LoginRequiredMixin, UpdateView):
  model = Trip
  fields = '__all__'

class TripDelete(LoginRequiredMixin, DeleteView):
  model = Trip
  success_url = '/'

# Define the home view
# Create your views here.

def trips_index(request):
  trips = Trip.objects.all()
  return render(request, 'home.html', {'trips': trips})

def trips_detail(request, trip_id):
  trip = Trip.objects.get(id=trip_id)
  diary_entry_form = Diary_EntryForm()
  note_form = NoteForm()
  return render(
      request, 'trips/detail.html', {
          'trip': trip,
          'diary_entry_form': diary_entry_form,
          'note_form': note_form
      }
  )

@login_required
def add_diary_entry(request, trip_id):
  form = Diary_EntryForm(request.POST)
  if form.is_valid():
    if Trip.objects.get(pk=trip_id).user == request.user:
      new_diary_entry = form.save(commit=False)
      new_diary_entry.trip_id = trip_id
      new_diary_entry.save()
    else:
      return HttpResponseForbidden('403: You do not own this trip!')
  return redirect('detail', trip_id=trip_id)

@login_required
def add_note(request, trip_id):
  form = NoteForm(request.POST)
  if form.is_valid():
    new_note = form.save(commit=False)
    new_note.trip_id = trip_id
    new_note.user = request.user
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

class DiaryUpdate(UpdateView):
  model = Diary_Entry
  fields = ['date','content']
  extra_context = {'diary_entry_form': Diary_EntryForm()}
  
  def get_success_url(self):
    return self.object.trip.get_absolute_url()

class DiaryDelete(DeleteView):
  model = Diary_Entry
  
  def get_success_url(self):
    return self.object.trip.get_absolute_url()
