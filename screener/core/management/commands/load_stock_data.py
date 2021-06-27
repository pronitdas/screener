import os
from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
from nsetools import Nse
import yfinance as yf
from core.models import StockCode
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
        for stock, value in all_stock_codes.items():
            print(stock, value)
            sCode = StockCode(stock=stock, stock_name= value)
            sCode.save()
            stocks.append(sCode)
        
    print('Fetched data')
        