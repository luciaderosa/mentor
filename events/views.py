from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

from .models import Event
from .forms import EventForm

# Create your views here.

class EventListView(ListView):    
    model = Event

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm

