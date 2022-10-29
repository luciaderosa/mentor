from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('', include('contacts.urls')),
    path('', include('courses.urls')),
    path('', include('trainers.urls')),
    path('', include('events.urls')),

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)