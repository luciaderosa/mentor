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
            msg= color_msg('Your message was sent!','success')           
        else:            
            msg= color_msg('Verify your data!','danger')    
    else:
        initial={'name':'','email':'','subject':'','message':''}
        contact_form=ContactForm(initial=initial)
        msg= color_msg('','')
            
    return render(request, 'mentor/contact.html',{'contact_form': contact_form, 'msg':msg})

def color_msg(text,color):
    return {'text':text, 'color':color}    