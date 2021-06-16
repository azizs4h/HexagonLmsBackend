from django.db import models
from lesson.models import Lesson


class Meet(models.Model):
    name = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    meet_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.name
