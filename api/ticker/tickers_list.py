from django.core.cache import cache
from .models import StockData

def get_available_tickers():
    
    tickers_list = cache.get('tickers_list')
    
    if tickers_list is None:
     
        tickers = StockData.objects.values_list('ticker', flat=True).distinct()

        
        tickers_list = list(tickers)

        
        cache.set('tickers_list', tickers_list)

    return tickers_list

