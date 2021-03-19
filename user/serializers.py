from rest_framework import serializers
from .models import *
from teacher.serializers import TeacherSerializer
from student.serializers import StudentSerializer


class UserInfoSerializer(serializers.ModelSerializer):
    teacher_user = TeacherSerializer()
    student_user = StudentSerializer()

    class Meta:
        model = User
        fields = ('username', 'teacher_user', 'student_user', 'email', 'is_student')
