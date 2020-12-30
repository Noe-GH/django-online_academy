from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.available_courses, name='courses_list'),
    path('<int:courses_pk>/<int:lesson_pk>/', views.lesson_detail, name='lesson_detail'),
    path('<int:pk>/', views.courses_detail, name='course_detail'),
]