from django.views.generic import ListView

from .models import Trainer

# Create your views here.

class TrainerListView(ListView):     
     model = Trainer
