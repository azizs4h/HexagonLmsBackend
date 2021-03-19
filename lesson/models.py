from django.db import models

from student.models import Student
from teacher.models import Teacher


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    lesson_code = models.IntegerField()
    lesson_credit = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=None, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default=None, blank=True)
    date_joined = models.DateField()
    exam1 = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    exam2 = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

    class Meta:
        unique_together = [['student', 'lesson']]

    def __str__(self):
        return str(self.student)+str(self.teacher)+str(self.lesson)


class LessonNotes(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    note_publish_date = models.DateField()
    note_title = models.CharField(max_length=255)
    note_description = models.TextField()
    file = models.FileField(blank=True, null=True,)
    file_description = models.CharField(blank=True, null=True, max_length=255)
    file_uploaded_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.note_title

