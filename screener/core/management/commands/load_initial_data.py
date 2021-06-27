import os
from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd

class Command(BaseCommand):
    help = 'Displays current time'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    
    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        na_values = ["", 
             "#N/A", 
             "#N/A N/A", 
             "#NA", 
             "-1.#IND", 
             "-1.#QNAN", 
             "-NaN", 
             "-nan", 
             "1.#IND", 
             "1.#QNAN", 
             "<NA>", 
             "N/A", 
#              "NA", 
             "NULL", 
             "NaN", 
             "n/a", 
             "nan", 
             "null"]

        df = pd.read_csv('/home/pronit/test/screener/datadump/screenipy-result_27-06-21_19.36.48.csv')
        print(df)