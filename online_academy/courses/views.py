from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Courses, Lessons

def available_courses(request):
    courses_list = Courses.objects.all()
    email = 'noe2gracida@hotmail.com'
    return render(request, 'courses/course_list.html', {'courses':courses_list, 'email':email})

def courses_detail(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def lesson_detail(request, courses_pk, lesson_pk):
    lesson = get_object_or_404(Lessons, course_id=courses_pk, pk=lesson_pk)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})