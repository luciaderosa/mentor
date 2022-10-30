from django.forms import ModelForm, TextInput, Textarea, EmailField
from .models import Contact

# create a ModelForm
class ContactForm(ModelForm):
    class Meta():
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        labels = {
            'name':'Full Name',
            'email':'Email',
            'subject':'Subject',
            'message':'Message',
        }       
        
        

                          # name= Te(label='Full name',max_length=100, widget=TextInput(
    #                                 attrs={
    #                                     'class':'form-control',
    #                                     'placeholder':'FullName',
    #                                 }))
    # email=EmailField(label='Email',max_length=254, 
    #                                 widget=EmailInput(
    #                                 attrs={
    #                                     'class':'form-control',
    #                                     'placeholder':'Your Email',
    #                                 }))
    # subject=CharField(label='Subject',max_length=60,widget=TextInput(
    #                                 attrs={
    #                                     'class':'form-control',
    #                                     'placeholder':'Subject',
    #                                 }))
    # message=CharField(label='Message',max_length=512, widget=Textarea(
    #                                 attrs={
    #                                     'class':'form-control',
    #                                     'placeholder':'Message',
    #                                     'rows': 5
    #                                 }))
	# specify the name of model to use