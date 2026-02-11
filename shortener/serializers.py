from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.ReadOnlyField()

    class Meta:
        model = URL
        fields = ['id', 'original_url', 'short_code', 'short_url', 'created_at', 'clicks']
        read_only_fields = ['short_code', 'created_at', 'clicks']

class URLCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['original_url', 'short_code']
        extra_kwargs = {
            'short_code': {'required': False,}
        }