from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm

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
        msg= self.color_msg('','')
        return render(request, self.template_name, {'form': form, 'msg':msg})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg= self.color_msg('Your message was sent!','success')           
        else:            
            msg= self.color_msg('Verify your data!','danger')    
        return render(request, self.template_name, {'form': form, 'msg':msg})    

    def color_msg(self,text,color):
        return {'text':text, 'color':color}            