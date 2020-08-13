from rest_framework import serializers
from backend_test.models import User, ActivityPeriod

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')

class UserDataSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)
    
    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')