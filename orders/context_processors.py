from functools import lru_cache
from .models import ProductInBasket


@lru_cache(maxsize=100)
def getting_basket_info(request):
    session_key = request.session.session_key

    if not session_key:
        request.session.cycle_key()
        request.session['valuta'] = "USD"
        request.session.modified = True

    try:
        valuta = request.session.get('valuta', 'USD')
    except:
        valuta = 'USD'

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)
    products_total_nmb = products_in_basket.count()

    all_sum = 0

    if products_total_nmb > 0:
        for product in products_in_basket:
            if product.product.availability.name != 'Нет в наличии':
                if valuta == 'USD':
                    all_sum += product.total_price_usd
                elif valuta == 'ГРН':
                    all_sum += product.total_price_uah

            else:
                product.delete()

    all_sum = round(all_sum, 2)

    return locals()
