from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.cache import cache
from .models import URL
from .serializers import URLSerializer, URLCreateSerializer

class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    
    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'shorten':
            return URLCreateSerializer
        return URLSerializer
    
    def retrieve(self, request, pk=None):
        cache_key = f'url_{pk}'
        
        cached_url = cache.get(cache_key)
        if cached_url:
            cached_url['from_cache'] = True
            return Response(cached_url)
        
        url = self.get_object()
        serializer = URLSerializer(url)
        data = serializer.data
        
        cache.set(cache_key, data, timeout=3600)
        data['from_cache'] = False
        
        return Response(data)
    
    @action(detail=False, methods=['post'])
    def shorten(self, request):
        serializer = URLCreateSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.save()
            
            cache_key = f'url_{url.id}'
            cache.set(cache_key, URLSerializer(url).data, timeout=3600)
            
            return Response(
                URLSerializer(url).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def stats(self, request, pk=None):
        url = self.get_object()
        return Response({
            'short_code': url.short_code,
            'original_url': url.original_url,
            'clicks': url.clicks,
            'created_at': url.created_at
        })
