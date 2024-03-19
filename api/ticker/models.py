from django.db import models

class StockData(models.Model):
    id = models.AutoField(primary_key=True)  
    ticker = models.CharField(max_length=10, null=False)
    date = models.DateField(null=True)  
    revenue = models.DecimalField(max_digits=20, decimal_places=4, null=True)
    gp = models.DecimalField(max_digits=20, decimal_places=4, null=True)
    fcf = models.DecimalField(max_digits=20, decimal_places=4, null=True)
    capex = models.DecimalField(max_digits=20, decimal_places=4, null=True)
    
    class Meta:
        db_table = 'stock_data'
        indexes = [
            models.Index(fields=['ticker']),
            models.Index(fields=['date']),
            
        ]
