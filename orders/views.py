from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import OrderForm
from .tasks import send_mailing
from .models import *


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id")
    product_remove = data.get("remove")
    nmb = data.get('numbers')

    if product_remove == 'true':
        product = ProductInBasket.objects.get(id=product_id, session_key=session_key)
        product.delete()

    elif product_remove == 'false':      
        img = data.get('image')
        image = img[7:]

        if ProductInBasket.objects.filter(session_key=session_key, id=product_id):
            product = ProductInBasket.objects.get(session_key=session_key, id=product_id)
            product.nmb = int(nmb)
            product.save(force_update=True)

        else:
            new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, defaults={"nmb": int(nmb), "poster": image})
            if not created:
                new_product.nmb = int(nmb)
                new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)
    
    if request.session['valuta']:
        valuta = request.session['valuta']
    else:
        valuta = 'USD'
        request.session['valuta'] = 'USD'

    request.session.modified = True

    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb

    if valuta == 'EUR':
        return_dict["valuta"] = ' €'
    if valuta == 'USD':
        return_dict["valuta"] = ' $'
    if valuta == 'ГРН':
        return_dict["valuta"] = ' грн'

    return_dict["products"] = list()
    products_sum = 0

    for item in  products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.title
        product_dict["numbers"] = item.nmb
        if valuta == 'USD':
            product_dict["price"] = item.product.retail_usd
            product_dict["sum"] = item.total_price_usd

        if valuta == 'EUR':
            product_dict["price"] = item.product.retail_eur
            product_dict["sum"] = item.total_price_eur

        if valuta == 'ГРН':
            product_dict["price"] = item.product.retail_uah
            product_dict["sum"] = item.total_price_uah

        product_dict["img"] = item.poster.url
        return_dict["products"].append(product_dict)

        products_sum += product_dict["sum"]
    return_dict['products_sum'] = products_sum
    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)

    form = OrderForm(request.POST)

    if form.is_valid():
        data = request.POST
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        city = data.get('city')
        phone = data.get('phone')
        
        # create user
        user, created = User.objects.get_or_create(username=phone, defaults={'first_name':firstname})
        # создаем заказ
        order = Order.objects.create(user=user, firstname=firstname, lastname=lastname,
                                     email=email, city=city, phone=phone, status_id=1)
        order_id = order.id

        # add in order
        checkout_sum = 0
        for product in products_in_basket:
            
            ProductInOrder.objects.create(order=order, product=product.product, nmb=product.nmb, 
                                          price_per_item=product.price_per_item,
                                          total_price = product.total_price)
            checkout_sum += product.total_price
        
        # check basket > 100 $
        if checkout_sum < 100:
            return render(request, "product/checkout.html", locals())

        # order send email
        send_mailing.delay(order_id)


        #clear basket
        for item_clear in products_in_basket:
            item_clear.delete()

        return render(request, "product/order_accepted.html", {"order": order_id})

    else:
        print("form invalide")

    return render(request, "product/checkout.html", locals())
