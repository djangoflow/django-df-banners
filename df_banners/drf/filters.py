from typing import Any

from django.db.models import QuerySet
from django_filters import rest_framework as filters


class BannerFilterSet(filters.FilterSet):
    id__in = filters.BaseCSVFilter(label="id", lookup_expr="in", field_name="id")

    tags = filters.BaseCSVFilter(method="filter_tags")

    def filter_tags(self, queryset: QuerySet, name: str, value: Any) -> QuerySet:
        return queryset.filter_tags(value)
