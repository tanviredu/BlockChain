from rest_framework import serializers
from .models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id", "user", "content", "image"]


class StatusUpdateSerializer(serializers.ModelSerializer):
    """user can only change the content and the image"""

    class Meta:
        model = Status
        fields = ["content", "image"]
