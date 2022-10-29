from django.shortcuts import render
from .models import Event

# Create your views here.

def events(request):
    events = Event.objects.all()
    return render(request, 'mentor/events.html', {'events': events})
