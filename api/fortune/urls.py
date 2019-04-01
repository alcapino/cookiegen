"""
URL Routing for the locations application.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fortune.views import FortuneViewSet

ROUTER = DefaultRouter()
ROUTER.register(r'', FortuneViewSet, base_name='fortune-api')

urlpatterns = [
    path(r'', include(ROUTER.urls)),
]
