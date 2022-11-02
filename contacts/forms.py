from django import forms
from .models import Contact

# create a ModelForm
class ContactForm(forms.ModelForm):
    class Meta():
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
          
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'minlength':2,
            'placeholder':'Full name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Your email',
            'pattern':"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"}),
            'subject': forms.TextInput(attrs={'class':'form-control','placeholder':'Subject','minlength':5}),
            'message':forms.Textarea(attrs={'class':'form-control','placeholder':'Message','rows':5, 'minlength':5}),
        }

