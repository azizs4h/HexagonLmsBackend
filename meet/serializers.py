from rest_framework import serializers

from meet.models import Meet


class MeetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meet
        fields = '__all__'


class AddMeetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meet
        fields = '__all__'
