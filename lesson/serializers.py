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

    def create(self, validated_data):
        ...

    def update(self, validated_data):
        ...


class LessonSerializer(serializers.ModelSerializer):
    lesson = LessonsSerializer()

    class Meta:
        model = Enrollment
        fields = ['lesson']

    def create(self, validated_data):
        ...

    def update(self, validated_data):
        ...


class LessonInfoSerializer(serializers.ModelSerializer):
    lesson = LessonsSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = Enrollment
        fields = ['lesson', 'teacher']

    def create(self, validated_data):
        ...

    def update(self, validated_data):
        ...


class LessonNotesSerializer(serializers.ModelSerializer):
    lesson = LessonsSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = LessonNotes
        fields = '__all__'
