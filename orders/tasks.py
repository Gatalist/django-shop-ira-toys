from django_product.celery import app
from django.template.loader import render_to_string
from django_product.service_email import send_to_email
from orders.models import Order
from django_product.office.office import *


@app.task
def send_mailing(order_id):
    order = Order.objects.get(id=order_id)

    name = f'заказ_{order}'
    # работа с таблицой
    table(order_id, name)
    
    to_email = order.email
    firstname = order.firstname
    lastname = order.lastname
    price = order.total_price
    context = ({"order": order_id, "firstname": firstname, "lastname": lastname, "price": price})
    title = "Игрульки от Ирульки"
    html_content = render_to_string('mail/message.html', context)
    file = f'django_product/office/orders/{name}.xlsx'
    send_to_email(title, to_email, file, html_content)
