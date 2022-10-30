from django.views.generic import ListView, DetailView

from .models import Course

# Create your views here.

class CourseListView(ListView):
    template_name = 'mentor/courses.html'
    model = Course
    

class CourseDetailView(DetailView):
    template_name = 'mentor/course-details.html'
    model = Course