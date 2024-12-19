from django.db.models import Sum, F
from django.utils.formats import number_format
from django.utils import timezone
from products.models import Product
from outflows.models import Outflow


def get_products_metrics():
    products = Product.objects.all()
    products_quantity = products.count() or 0
    higher_profit = lower_profit = {
        'name': None,
        'value': 0
    }
    lower_qty = {
            'name': None,
            'value': 0
        }

    lower_qty_product = products.order_by('quantity').first() or None
    if lower_qty_product:
        lower_qty = {
            'name': lower_qty_product.title,
            'value': lower_qty_product.quantity
        }

    for pos, product in enumerate(products):

        cost_price = product.cost_price
        selling_price = product.selling_price
        profit_margin = round((selling_price / cost_price) * 100, 0)

        if profit_margin > higher_profit['value'] or pos == 0:
            higher_profit['name'] = product.title
            higher_profit['value'] = profit_margin

        if profit_margin < lower_profit['value'] or pos == 0:
            lower_profit['name'] = product.title
            lower_profit['value'] = profit_margin

    products_metrics = {
        'quantity': products_quantity,
        'higher_profit': higher_profit,
        'lower_profit': lower_profit,
        'lower_qty': lower_qty
    }
    return products_metrics


def get_sales_metrics():
    best_selling_name = best_selling_quantity = underground_name = underground_quantity = None
    outflows = Outflow.objects.all()
    selled_products = Product.objects\
        .annotate(selled_quantity=Sum("outflows__quantity", default=0))
    best_selling_product = selled_products\
        .order_by("-selled_quantity")\
        .first() or None

    if best_selling_product:
        best_selling_name = best_selling_product.title
        best_selling_quantity = best_selling_product.selled_quantity

    underground_product = selled_products\
        .order_by("selled_quantity")\
        .first() or None

    if underground_product:
        underground_name = underground_product.title
        underground_quantity = underground_product.selled_quantity

    total_spent = outflows.aggregate(total=Sum(F("quantity") * F("product__cost_price")))['total'] or 0

    total_invoiced = outflows.aggregate(total=Sum(F("quantity") * F("product__selling_price")))['total'] or 0

    profit_margin = 0
    if total_spent > 0:
        profit_margin = (total_invoiced - total_spent) / total_spent * 100

    sales_matrics = {
        "best_seller_product": {'name': best_selling_name, 'value': best_selling_quantity},
        "underground_product": {'name': underground_name, 'value': underground_quantity},
        "total_invoiced": number_format(total_invoiced, decimal_pos=2, force_grouping=True),
        "profit_margin": number_format(profit_margin, decimal_pos=0)
    }

    return sales_matrics


def get_daily_sales_data():
    today = timezone.now().date()
    last_7_days = [str(today - timezone.timedelta(days=day)) for day in range(6, -1, -1)]
    values = list()

    for date in last_7_days:
        sales_total = Outflow.objects.filter(created_at__date=date)\
            .aggregate(total_value=Sum(F('product__selling_price') * F('quantity')))['total_value'] or 0
        values.append(float(sales_total))

    return {
        'dates': last_7_days,
        'values': values
    }


def get_daily_quantity_sales_data():
    today = timezone.now().date()
    last_7_days = [str(today - timezone.timedelta(days=day)) for day in range(6, -1, -1)]
    values = list()
    for day in last_7_days:
        quantity = Outflow.objects.filter(created_at__date=day).count() or 0
        values.append(quantity)
    return {
        'dates': last_7_days,
        'values': values
    }
