from rest_framework import serializers

from .models import Subscriber

class SubscriberFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['userEmail', 'trackedBeaches']