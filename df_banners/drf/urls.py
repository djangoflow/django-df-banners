from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from .viewsets import (
    BannerViewSet,
)

urlpatterns = []

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("banners", BannerViewSet, basename="banners")

urlpatterns += router.urls
