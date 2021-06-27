from tastypie import fields
from tastypie.resources import ModelResource
from core.models import Stock


class StockResource(ModelResource):
    class Meta:
        queryset = Stock.objects.all()
        filtering = {
            'date': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'stock': ['exact', 'startswith'],
            'high': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'low': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'volume': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            
        }
        