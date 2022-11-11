from django.urls import path
from . import views

urlpatterns = [
    path('events', views.EventListView.as_view(), name='events'),
    path('events/new', views.EventCreateView.as_view(), name='new-event'),
    path('events/<int:pk>/edit', views.EventUpdateView.as_view(), name='edit-event'),
]