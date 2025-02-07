import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student

def students_list(request):
    students = list(Student.objects.values())
    return JsonResponse(students, safe = False)

def student_detail(request, student_id):
    try:
        student = Student.objects.values().get(id = student_id)
        return JsonResponse(student, safe = False)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status = 404)