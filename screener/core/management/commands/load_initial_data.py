import os
from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
from nsetools import Nse
import yfinance as yf


nse = Nse()

class Command(BaseCommand):
    help = 'Displays current time'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    
    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        all_stock_codes = nse.get_stock_codes()
        for stock in all_stock_codes:
            if stock != 'SYMBOL':
                data = yf.download(
                    tickers=stock+".NS",
                    period='300d',
                    duration='1h',
                    progress=False,
                )
                stock_price_history = data.T.to_dict().values()
                stock
                    
            # print(nse.get_quo, valuete(stock))
        