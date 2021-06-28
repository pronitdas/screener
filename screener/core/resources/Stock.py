from tastypie.utils import trailing_slash
from psqlextra.query import ConflictAction

from tastypie.resources import ModelResource
from core.models import Stock
from nsetools import Nse
import yfinance as yf
from django.conf.urls import url
import json
from datetime import date
nse = Nse()

class StockResource(ModelResource):
    def prepend_urls(self):
        return [
            url(
                r"^(?P<resource_name>%s)/store%s$"
                % (self._meta.resource_name, trailing_slash()), self.wrap_view('store_stock_prices'),
                name="store_stock_prices")
        ]
    class Meta:
        queryset = Stock.objects.all()
        filtering = {
            'date': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'stock': ['exact', 'startswith'],
            'high': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'low': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'volume': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],        
        }

   
    def store_stock_prices(self, request, **kwargs):
        stock = request.GET.get('stock')
        print(request)
        stocks = []
        data = yf.download(
                    tickers="%s.NS" % stock,
                    period='300d',
                    duration='1h',
                    progress=False,
                )
        stock_price_history = json.loads(data.T.to_json())
        for attribute, value in stock_price_history.items():
            dt = date.fromtimestamp(int(attribute)/1000)
            stockObj = {
                "date":dt,
                "stock":stock,
                "high": value['High'], 
                "open":value['Open'], 
                "adj_close" : value['Adj Close'], "volume": value['Volume'], "low":value['Low']
            }
                
            
            stocks.append(stockObj)
        Stock.objects.on_conflict(['stock','date'], ConflictAction.UPDATE).bulk_insert(stocks)
        return self.create_response(request, {'asdf': "asd"})