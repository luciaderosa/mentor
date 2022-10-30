from django.views.generic import TemplateView

# Create your views here.
class ContactView(TemplateView):
    template_name = 'mentor/contact.html'