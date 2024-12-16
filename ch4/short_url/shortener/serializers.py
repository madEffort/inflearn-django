from rest_framework import serializers

from shortener.models import ShortURL


class ShortURLReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = "__all__"


class ShortURLCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ["original_url"]
