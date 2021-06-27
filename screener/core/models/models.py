from django.db import models

class Stock(models.Model):
    open = models.FloatField()
    high = models.FloatField()
    date= models.DateField()
    low= models.FloatField()
    adj_close = models.FloatField()
    volume = models.FloatField()
    stock = models.FloatField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['stock', 'date'], name='unique_stock_date'),
        ]
        indexes = [
            models.Index(fields=['stock',]),
            models.Index(fields=['date',])
        ]