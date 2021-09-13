from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from django.http import JsonResponse, HttpResponse
from .models import *
from .forms import OrderForm
from django.contrib.auth.models import User

from .tasks import send_mailing


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    print(data)
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
    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()
    
    for item in  products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.title
        product_dict["price"] = item.price_per_item
        product_dict["numbers"] = item.nmb
        product_dict["sum"] = item.total_price
        product_dict["img"] = item.poster.url
        return_dict["products"].append(product_dict)

    print(return_dict)
    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)
    form = OrderForm(request.POST)
    print(request.POST)

    if form.is_valid():
        print("form vavide")
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
        for product in products_in_basket:
            
            ProductInOrder.objects.create(order=order, product=product.product, nmb=product.nmb, 
                                          price_per_item=product.price_per_item,
                                          total_price = product.total_price)
        # order send email
        send_mailing.delay(order_id)


        # clear basket
        # for item_clear in products_in_basket:
        #     item_clear.delete()

        return render(request, "product/order_accepted.html", {"order": order_id})

    else:
        print("form invalide")

    return render(request, "product/checkout.html", locals())