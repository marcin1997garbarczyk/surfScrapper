from rest_framework import serializers

from .models import Subscriber

class SubscriberFormSerializer(serializers.ModelSerializer):

    def getUserEmail(self, obj):
        return obj.userEmail

    def getTrackedBeaches(self, obj):
        return obj.trackedBeaches
    class Meta:
        model = Subscriber
        fields = ['userEmail', 'trackedBeaches', 'isActive']