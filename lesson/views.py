from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .permissions import isOwner
from .serializers import *


class LessonsView(APIView):
    permission_classes = [IsAuthenticated, isOwner]
    id = None
    user = None

    def post(self, request):
        self.user = request.user
        self.id = request.data['id']
        if self.user.is_student:
            lesson = Enrollment.objects.filter(student_id=self.id)
            serializer = LessonSerializer(lesson, many=True)
            return Response(serializer.data)
        else:
            print(self.user.pk)
            lesson = Enrollment.objects.filter(teacher_id=self.id)
            print(self.user.id)
            serializer = LessonSerializer(lesson, many=True)
            return Response(serializer.data)


class LessonsInfoView(APIView):
    permission_classes = [IsAuthenticated, isOwner]
    id = None
    user = None

    def post(self, request):
        self.id = request.data['id']
        lesson = Enrollment.objects.filter(lesson_id=self.id)
        serializer = LessonInfoSerializer(lesson, many=True)
        return Response(serializer.data)

"""
    def post(self, request, format=None):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            saved_obj = serializer.save()
            response_data = ProductDisplaySerializer(saved_obj).data
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""


class LessonNotesView(APIView):
    permission_classes = [IsAuthenticated, isOwner]

    def post(self, request):
        user = request.user
        if user.is_student:
            notes = LessonNotes.objects.filter(lesson_id=request.data['id'])
            serializer = LessonNotesSerializer(notes, many=True)
            return Response(serializer.data)
        else:
            notes = LessonNotes.objects.filter(lesson_id=request.data['id'])
            serializer = LessonNotesSerializer(notes, many=True)
            return Response(serializer.data)
