from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from .models import Event
from .forms import EventForm

# Create your views here.

class EventListView(ListView):    
    model = Event
@method_decorator(staff_member_required, name='dispatch')
class EventCreateView(SuccessMessageMixin, CreateView):
    model = Event
    form_class = EventForm
    success_message = 'Event was created successfully'
@method_decorator(staff_member_required, name='dispatch')
class EventUpdateView(SuccessMessageMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name_suffix = '_update_form'    
    success_message = 'Event was updated successfully'

@method_decorator(staff_member_required, name='dispatch')
class EventDeleteView(SuccessMessageMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events')
    success_message = "Event deleted"