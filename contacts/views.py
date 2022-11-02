from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
# class ContactView(TemplateView):
#     template_name = 'contacts/contact.html'


class ContactView(FormView):
    template_name = 'contacts/contact.html'
    form_class = ContactForm
    #initial = {'key': 'value'}
    initial = {'name':'','email':'','subject':'','message':''}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'button': True})

    def post(self, request, *args, **kwargs):
        button = True
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            button= False
            messages.success(request, "Your message was sent!" )        
        else:       
            messages.error(request, "Error. Verify your data")     
        return render(request, self.template_name, {'form': form, 'button':button})    

    