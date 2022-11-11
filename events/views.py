from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Event
from .forms import EventForm

# Create your views here.

class EventListView(ListView):    
    model = Event

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name_suffix = '_update_form'    

class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('events')