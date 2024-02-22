import django_filters
from .models import Block
from django import forms


class BlockFilter(django_filters.FilterSet):
    whs_area = django_filters.RangeFilter()
    lease_offered = django_filters.BooleanFilter()
    lease_whs_price = django_filters.RangeFilter()
    sale_offered = django_filters.BooleanFilter()
    sale_total_price = django_filters.RangeFilter()
    class Meta:
        model = Block
        fields = {
            'id': ['exact'],
        }


# class BlockFilter(django_filters.FilterSet):
#     class Meta:
#         model = Block
#         fields = {
#             'id': ['exact'],
#             'whs_area': ['lt', 'gt'],
#             'office_area': ['lt', 'gt'],
#             'mez_area': ['lt', 'gt'],
#             'lease_offered': ['exact'],
#             'lease_whs_price' : ['lt', 'gt'],
#             'lease_office_price' : ['lt', 'gt'],
#             'lease_mez_price': ['lt', 'gt'],
#             'sale_offered': ['exact'],
#             'sale_total_price': ['lt', 'gt'],
#         }