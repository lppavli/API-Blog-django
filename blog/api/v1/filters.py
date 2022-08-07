import django_filters
from django_filters import rest_framework as filters


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PostFilter(filters.FilterSet):
    posts = CharFilterInFilter(field_name="author__name", lookup_expr="in")

    class Meta:
        fields = ["author"]
