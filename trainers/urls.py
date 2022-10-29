from django.urls import path
from . import views

urlpatterns = [
    path('trainers', views.trainers, name='trainers'),    
]