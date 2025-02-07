from django.http import JsonResponse
from .models import Course

def courses_list(request):
    courses = list(Course.objects.values())
    return JsonResponse(courses, safe = False)

def course_detail(request, course_id):
    try:
        course = Course.objects.values().get(id = course_id)
        return JsonResponse(course, safe = False)
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status = 404)