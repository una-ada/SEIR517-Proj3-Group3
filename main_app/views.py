from django.forms.models import inlineformset_factory
from django.http.response import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Diary_Entry, Trip, Note, Photo
from .forms import Diary_EntryForm, NoteForm, TripForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
import boto3
import uuid

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'tabbyimages'

def trip_create(request):
  ModelForm = inlineformset_factory(Trip, Photo, exclude=['user'])
  if request.method == 'POST':
    form = TripForm(request.POST)
    if form.is_valid():
      trip = form.save(commit=False)
      trip.user = request.user
      trip.save()
      photo_file = request.FILES.get('photo-file', None)
      if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.
                                                     rfind('.'):]
        try:
          s3.upload_fileobj(photo_file, BUCKET, key)
          url = f"{S3_BASE_URL}{BUCKET}/{key}"
          Photo.objects.create(url=url, trip=trip)
        except:
          print('An error occurred uploading file to S3')
        return redirect('/')
  else:
    return render(request, 'main_app/trip_form.html')

class TripUpdate(LoginRequiredMixin, UpdateView):
  model = Trip
  fields = ['title', 'from_location', 'to_location']

class TripDelete(LoginRequiredMixin, DeleteView):
  model = Trip
  success_url = '/'

def trips_index(request):
  trips = Trip.objects.all()
  photos = Photo.objects.all()
  return render(request, 'home.html', {'trips': trips, 'photos': photos})

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
      return HttpResponseForbidden()
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
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class DiaryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Diary_Entry
  fields = ['date', 'content']
  extra_context = {'diary_entry_form': Diary_EntryForm()}
  
  def test_func(self):
    return self.get_object().trip.user.id is self.request.user.id
  
  def get_success_url(self):
    return self.object.trip.get_absolute_url()

class DiaryDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Diary_Entry
  
  def test_func(self):
    return self.get_object().trip.user.id is self.request.user.id
  
  def get_success_url(self):
    return self.object.trip.get_absolute_url()

class NoteUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Note
  fields = ['content']
  extra_context = {'note_form': NoteForm}
  
  def test_func(self):
    return self.get_object().user.id is self.request.user.id
  
  def get_success_url(self):
    return self.object.trip.get_absolute_url()

class NoteDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Note
  
  def test_func(self):
    return self.get_object().user.id is self.request.user.id
  
  def get_success_url(self):
    return self.object.trip.get_absolute_url()
