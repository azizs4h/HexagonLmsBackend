# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from meet.models import Meet
from meet.serializers import MeetSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_meet(request, data_id):
    if request.method == 'GET':
        meet = Meet.objects.filter(lesson=data_id)
        serializer = MeetSerializer(meet, many=True)
        if not meet.exists():
            data = {"message": "Böyle bir şey yok."}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_meet(request):
    if request.method == 'POST':
        serializer = MeetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
