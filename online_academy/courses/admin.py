from django.contrib import admin

from .models import Courses, Lessons

class LessonInline(admin.StackedInline):
    model = Lessons

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, ]

admin.site.register(Courses, CourseAdmin)
