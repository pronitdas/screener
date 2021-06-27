from django.db import models

class Stock(models.Model):
    open = models.FloatField()
    high = models.FloatField()
    date= models.DateField()
    low= models.FloatField()
    adj_close = models.FloatField()
    volume = models.FloatField()
    stock = models.CharField(max_length=200)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['stock', 'date'], name='unique_stock_date'),
        ]
        indexes = [
            models.Index(fields=['stock',]),
            models.Index(fields=['date',])
        ]


        {'Open': 9.0, 'High': 9.25, 'Low': 8.75, 'Close': 9.0, 'Adj Close': 9.0, 'Volume': 10277993.0}