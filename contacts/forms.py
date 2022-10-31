from django import forms
from .models import Contact

# create a ModelForm
class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
          
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Full name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Your email'}),
            'subject': forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}),
            'message':forms.Textarea(attrs={'class':'form-control','placeholder':'Message','rows':5}),
        }

