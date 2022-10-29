from django.shortcuts import render
from .models import Trainer

# Create your views here.

def trainers(request):
     trainers = Trainer.objects.all()
     return render(request, 'mentor/trainers.html', {'trainers': trainers})
