from django.shortcuts import render
from .models import Testimonial


# Create your views here.
def index(request):
    return render(request, 'mentor/index.html')

def about(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'mentor/about.html', {'testimonials': testimonials})
