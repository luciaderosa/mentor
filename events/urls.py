from django.urls import path
from . import views

urlpatterns = [
    path('events', views.EventListView.as_view(), name='events'),
    path('events/new-event', views.EventCreateView.as_view(), name='new-event')
]