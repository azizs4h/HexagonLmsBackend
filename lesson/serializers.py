from rest_framework import serializers

from student.serializers import StudentSerializer
from teacher.serializers import TeacherSerializer
from .models import *


class LessonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    teacher = TeacherSerializer()
    lesson = LessonsSerializer()

    class Meta:
        model = Enrollment
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    lesson = LessonsSerializer()

    class Meta:
        model = Enrollment
        fields = ['lesson']


class LessonInfoSerializer(serializers.ModelSerializer):
    lesson = LessonsSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = Enrollment
        fields = ['lesson', 'teacher']


class LessonNotesSerializer(serializers.ModelSerializer):
    lesson = LessonsSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = LessonNotes
        fields = '__all__'


class AddLessonNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonNotes
        fields = '__all__'
