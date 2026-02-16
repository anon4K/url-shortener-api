from rest_framework import serializers
from .models import URL
import re

class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.ReadOnlyField()

    class Meta:
        model = URL
        fields = ['id', 'original_url', 'short_code', 'short_url', 'created_at', 'clicks']
        read_only_fields = ['short_code', 'created_at', 'clicks']

class URLCreateSerializer(serializers.ModelSerializer):
    custom_code = serializers.CharField(
        max_length=10, 
        required=False, 
        allow_blank=True,
        help_text="Optional custom short code (alphanumeric, and hyphens only. Max 10 chars)"
    )

    class Meta:
        model = URL
        fields = ['original_url', 'custom_code']

    def validate_custom_code(self, value):
        if value:
            if not re.match(r'^[a-zA-Z0-9-]+$', value):
                raise serializers.ValidationError("Custom code can only contain letters, numbers, and hyphens.")
            
            if len(value) < 3:
                raise serializers.ValidationError("Custom code must be at least 3 characters long.")
            
            if URL.objects.filter(short_code=value).exists():
                raise serializers.ValidationError(f"Custom code '{value}' is already in use. Please choose another one.")
            
        return value
    
    def create(self, validated_data):
        custom_code = validated_data.pop('custom_code', None)

        if custom_code:
            validated_data['short_code'] = custom_code

            return URL.objects.create(**validated_data)