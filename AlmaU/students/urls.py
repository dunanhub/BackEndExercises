from django.urls import path
from .views import students_list, student_detail

urlpatterns = [
    path('students/', students_list, name='student-list'),
    path('students/<int:student_id>/', student_detail, name='student-detail')
]