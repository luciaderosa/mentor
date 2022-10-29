from django.shortcuts import render
from .models import Course

# Create your views here.

def courses(request):
    courses = Course.objects.all()
    return render(request, 'mentor/courses.html', {'courses': courses})

def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'mentor/course-details.html', {'course': course})