from django.db import models

class Courses(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Lessons(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.title