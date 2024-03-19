from datetime import datetime, timedelta
from django.http import JsonResponse
from .models import StockData
from .tickers_list import get_available_tickers

tickers_list = get_available_tickers()

def get_ticker_data(request):
    global tickers_list
    ticker = request.GET.get('ticker')
    columns = request.GET.get('column')
    period = request.GET.get('period')

    if not ticker:
        return JsonResponse({'error': 'Ticker parameter is required'}, status=400)
    
    if ticker not in tickers_list:
        return JsonResponse({'error': 'Ticker Not Available in Dataset'} ,status=400)
    
    queryset = StockData.objects.filter(ticker=ticker)

    if columns:
        valid_columns = [col.strip() for col in columns.split(',') if col.strip() in ['id', 'ticker', 'date', 'revenue', 'gp', 'fcf', 'capex']]
        
        if not valid_columns:
            return JsonResponse({'error': 'Invalid columns specified'}, status=400)

        if 'ticker' not in valid_columns:
            valid_columns.insert(0,'ticker')
        
        valid_columns.insert(1,'date')
        
        filtered_queryset = queryset.values_list(*valid_columns)

    
    if period:
        period_values = period.split('y')
        if len(period_values) != 2 or not period_values[0].isdigit():
            return JsonResponse({'error': 'Invalid period format. Use e.g., "5y" for 5 years'}, status=400)
        num_years = int(period_values[0])

        earliest_date = queryset.order_by('date').values_list('date', flat=True).first()

        end_date = earliest_date + timedelta(days=num_years * 365)

        
        filtered_queryset = filtered_queryset.filter(date__range=[earliest_date, end_date])

       

    
    ticker_data = []
    for item in filtered_queryset:
        ticker_data.append(dict(zip(valid_columns, item)))

    
    return JsonResponse({'data': ticker_data}, status=200)


     

