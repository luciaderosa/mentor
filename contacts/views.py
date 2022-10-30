from typing import Concatenate
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    if request.method=='POST':
        contact_form= ContactForm(request.POST)
        # check if form data is valid
        if contact_form.is_valid():
            # save the form data to model
            contact_form.save()
            html= "Your message was sent!"
        else:
            html= "Verify your data"
    else:
        initial={'name':' ','email':' ','subject':' ','message':' '}
        html=''
        contact_form=ContactForm(initial=initial)
            
    return render(request, 'mentor/contact.html', {'contact_form': contact_form, 'html':html})

    