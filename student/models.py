from django.db import models

from user.models import User


class Student(models.Model):
    student_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_user')
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name
