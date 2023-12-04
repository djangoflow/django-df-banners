from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from ..models import Banner
from .filters import BannerFilterSet
from .serializers import (
    BannerSerializer,
)


class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["id", "title"]

    filterset_class = BannerFilterSet
