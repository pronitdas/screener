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

class StockCode(models.Model):
    stock = models.CharField(max_length=200)
    stock_name=models.CharField(max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['stock'], name='unique_stock'),
        ]
        indexes = [
            models.Index(fields=['stock',]),
        ]