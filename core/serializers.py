from rest_framework import serializers


class ProfileValidationSerializer(serializers.Serializer):
    url = serializers.URLField(required=True)
