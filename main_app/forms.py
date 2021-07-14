from django.forms import ModelForm
from .models import Diary_Entry, Note

class Diary_EntryForm(ModelForm):
    class Meta:
        model = Diary_Entry
        fields = ['date', 'content']

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['content']