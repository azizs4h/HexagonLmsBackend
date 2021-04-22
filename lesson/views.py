from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .permissions import isOwner
from .serializers import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_lessons(request):
    user = request.user
    user_id = request.data['id']

    if request.method == 'POST' and user.is_student:
        lesson = Enrollment.objects.filter(student_id=user_id)
        serializer = LessonSerializer(lesson, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        lesson = Enrollment.objects.filter(teacher_id=user_id)
        serializer = LessonSerializer(lesson, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def lesson_info(request, data_id):  # not ekliyon
    if request.method == 'GET':
        lesson = Enrollment.objects.filter(lesson=data_id)
        serializer = LessonInfoSerializer(lesson, many=True)
        if not lesson.exists():
            data = {"message": "Böyle bir şey yok."}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def lesson_notes(request, data_id):  # not ekliyon
    if request.method == 'GET':
        notes = LessonNotes.objects.filter(lesson=data_id)
        if not notes.exists():
            data = {"message": "Böyle bir şey yok."}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        serializer = LessonNotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        notes = LessonNotes.objects.filter(pk=data_id) #not pk geliyo
        if not notes.exists():
            data = {"message": "Böyle bir şey yok."}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        operation = notes.delete()
        data = {}
        if operation:
            data["message"] = "Duyuru silindi."
        else:
            data["message"] = "Duyuru silinemedi."
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        ...


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_lesson_notes(request):
    if request.method == 'POST':
        serializer = LessonNotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
