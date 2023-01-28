from django.http import JsonResponse
from orders.models import ProductInBasket


def get_valuta(request):
    return_dict = dict()
    data = request.POST.get("valuta")
    request.session['valuta'] = data
    request.session.modified = True
    session_key = request.session.session_key
    
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)

    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()
    
    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.title
        product_dict["price"] = item.price_per_item
        product_dict["numbers"] = item.nmb
        product_dict["sum"] = item.total_price
        product_dict["img"] = item.poster.url
        return_dict["products"].append(product_dict)

    return_dict["valuta_change"] = data
    return JsonResponse(return_dict)     
