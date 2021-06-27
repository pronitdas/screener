from tastypie import fields
from tastypie.resources import ModelResource
from core.models import StockCode


class StockCodeResource(ModelResource):
    
    class Meta:
        queryset = StockCode.objects.all()
        filtering = {
            'stock': ['exact', 'startswith'],
            'stock_name':['exact', 'startswith']
            }
