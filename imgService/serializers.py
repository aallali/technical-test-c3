from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "description", "image", "uploaded_by", "uploaded_at"]
        read_only_fields = ["uploaded_by", "uploaded_at"]


class ImageDescriptionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["description"]
