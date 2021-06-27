import os
from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
from nsetools import Nse
import yfinance as yf
from core.models import Stock
import json
from datetime import date
nse = Nse()

class Command(BaseCommand):
    help = 'Displays current time'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    
    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        all_stock_codes = nse.get_stock_codes()
        stocks = []
        for stock in all_stock_codes:
            if stock != 'SYMBOL':
                data = yf.download(
                    tickers=stock+".NS",
                    period='300d',
                    duration='1h',
                    progress=False,
                )
                stock_price_history = json.loads(data.T.to_json())
                for attribute, value in stock_price_history.items():
                    dt = date.fromtimestamp(int(attribute)/1000)
                    stockObj = Stock(
                        date=dt,
                        stock=stock,
                        high= value['High'], 
                        open=value['Open'], 
                        adj_close = value['Adj Close'], volume= value['Volume'], low=value['Low'])
                    stockObj.save()
                    stocks.append(stockObj)
                    print(dt.strftime("%d/%m/%y"))
        
        Stock.objects.bulkCreate(stocks, ignore_conflicts=True)
                    
    print('Fetched data')
        