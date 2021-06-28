import os
from django.core.management.base import BaseCommand
from django.utils import timezone
from psqlextra.query import ConflictAction
import multiprocessing as mp

import pandas as pd
from nsetools import Nse
import yfinance as yf
from core.models import Stock
import json
from datetime import date
nse = Nse()
def fetchStock(stock):
        stocks = []
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
                print(value)
                stockObj = {
                    "date":dt,
                    "stock":stock,
                    "high": value['High'], 
                    "open":value['Open'], 
                    "adj_close" : value['Adj Close'],
                    "volume": value['Volume'], 
                    "low":value['Low']
                }
                print(stockObj)
                stocks.append(stockObj)
            Stock.objects.on_conflict(['stock','date'], ConflictAction.UPDATE).bulk_insert(stocks)
            print('Fetched data%s'% stock)
class Command(BaseCommand):
    help = 'Displays current time'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

    

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        all_stock_codes = nse.get_stock_codes()
        stocks = []
        pool = mp.Pool(mp.cpu_count())
        result = pool.map(fetchStock, list(all_stock_codes.values()))
        
            
    
        