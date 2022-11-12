from django import forms 
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'text', 'date', 'image']

        widgets = {
                'title': forms.TextInput(attrs={'class':'form-control', 'minlength':2,
                'placeholder':'Event Title'}),
                'text': forms.Textarea(attrs={'class':'form-control','placeholder':'Event Text','rows':5, 'minlength':5}),
                'date': forms.TextInput(attrs={'class':'form-control','placeholder':'Date','minlength':5, 'type': 'datetime-local'}), 
                #'image': forms.TextInput(attrs={'class':'form-control','type':'file', 'accept':'image/*'}),           
            }
