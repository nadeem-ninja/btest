from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from activity.models import Profile, ActivityPeriod

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class ProfileSerializer(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(many=True)
    # activityperiod_set = serializers.HyperlinkedIdentityField(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'real_name', 'tz', 'activity_periods']


# class UserSerializer(serializers.Serializer):
#     profile = ProfileSerializer(many=True)
#     activi = ProfileSerializer(many=True)

