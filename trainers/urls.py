from django.urls import path
from . import views

urlpatterns = [
    path('trainers', views.TrainerListView.as_view(), name='trainers'),    
]