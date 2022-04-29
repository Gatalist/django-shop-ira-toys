from .models import ProductInBasket
from products.tasks import product_new_info

def getting_basket_info(request):
    session_key = request.session.session_key
    
    if not session_key:
        request.session.cycle_key()

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)
    products_total_nmb = products_in_basket.count()

    all_sum = 0

    if products_total_nmb > 0:
        for product in products_in_basket:
            if product.product.availability.name != 'Нет в наличии':
                if request.session['valuta'] == 'USD':
                    all_sum += product.total_price_usd
                if request.session['valuta'] == 'EUR':
                    all_sum += product.total_price_eur
                if request.session['valuta'] == 'ГРН':
                    all_sum += product.total_price_uah

            else:
                product.delete()

    all_sum = round(all_sum, 2)
    product_new_info.delay()

    return locals()
