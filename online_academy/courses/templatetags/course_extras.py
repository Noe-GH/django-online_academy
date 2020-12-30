from django import template
from django.utils.safestring import mark_safe
from courses.models import Courses
import markdown2

register = template.Library()

@register.simple_tag
def last_course():
    """
    Tag that gets the last course registered.
    """
    return Courses.objects.latest('created_at')


@register.filter('time_estimate')
def time_estimate(word_count):
    """
    Filter that determines the hypothethical number of minutes that would take a student to finish each course.
    """
    minutes = round(word_count/5)
    return minutes


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """
    Filter that converts markdown text into HTML code.
    """
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
