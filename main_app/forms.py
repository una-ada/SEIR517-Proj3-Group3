from django.forms import ModelForm
from .models import Diary_Entry, Note, Trip

class Diary_EntryForm(ModelForm):
    class Meta:
        model = Diary_Entry
        fields = ['date', 'content']

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['content']

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'to_location', 'from_location']

