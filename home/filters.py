import django_filters
from django_filters import *

from catalog.models import *

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = 'category', 'brand', 'color', 'size_variant', 'status'
