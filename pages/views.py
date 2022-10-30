from re import template
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Testimonial


# Create your views here.
class IndexView(TemplateView):
    template_name = 'pages/index.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.all()
        return context
