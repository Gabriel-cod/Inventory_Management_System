import json
from django.shortcuts import render
from .metrics import get_products_metrics, get_sales_metrics, get_daily_sales_data, get_daily_quantity_sales_data


def home(request, *args, **kwargs):
    products_metrics = get_products_metrics()
    sales_metrics = get_sales_metrics()
    daily_sales_data = get_daily_sales_data()
    daily_quantity_sales_data = get_daily_quantity_sales_data()
    context = {
        'products_metrics': products_metrics,
        'sales_metrics': sales_metrics,
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_quantity_sales_data),
    }
    return render(request, 'home.html', context)
