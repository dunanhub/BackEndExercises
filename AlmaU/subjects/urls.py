from django.urls import path
from .views import courses_list, course_detail

urlpatterns = [
    path('courses/', courses_list, name='courses-list'),
    path('courses/<int:course_id>/', course_detail, name='course-detail')
]