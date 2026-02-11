from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import URLViewSet
from . import views

router = DefaultRouter()
router.register(r'urls', URLViewSet, basename='url')

urlpatterns = [
    path('api/', include(router.urls)),
]