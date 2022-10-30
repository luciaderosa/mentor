from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('', include('contacts.urls')),
    path('', include('courses.urls')),
    path('', include('trainers.urls')),
    path('', include('events.urls')),

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)