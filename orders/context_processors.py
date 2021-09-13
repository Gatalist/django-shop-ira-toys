from .models import ProductInBasket

def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)
    products_total_nmb = products_in_basket.count()

    all_sum = 0
    for sum_product in products_in_basket:
       all_sum += sum_product.total_price

    return locals()