from django.urls import path
from . import views

urlpatterns = [
    path('courses', views.CourseListView.as_view(), name='courses'),
    path('courses/<int:pk>', views.CourseDetailView.as_view(), name='course-detail')
]