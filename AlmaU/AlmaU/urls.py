from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('students.urls')),
    path('api/', include('subjects.urls')),
    path('todos/', include('todos.urls')),
    path('todoss/', include('todoss.urls')),
]