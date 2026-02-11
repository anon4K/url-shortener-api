from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import URL
from .serializers import URLSerializer, URLCreateSerializer
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import action


class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return URLCreateSerializer
        return URLSerializer

    @action(detail=False, methods=['post'])
    def shorten(self, request):
        serializer = URLCreateSerializer(data=request.data)
        if serializer.is_valid():
            url_instance = serializer.save()
            return Response(URLSerializer(url_instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def stats(self, request, pk=None):
        url = self.get_object()
        return Response({
            'original_url': url.original_url,
            'short_code': url.short_code,
            'short_url': url.short_url,
            'created_at': url.created_at,
            'clicks': url.clicks
        })
