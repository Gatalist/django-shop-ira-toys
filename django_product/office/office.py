from openpyxl import load_workbook
from orders.models import Order, ProductInOrder

folder = "/home/alex/django_product/django_product/office/"
# folder = "/home/user/ira-toys/django_product/django_product/office/"

input_file = folder + "orders.xlsx"


def table(order_id, name):
    wb = load_workbook(input_file)
    ws = wb['Лист1']

    order = Order.objects.get(id=order_id)
    product_order = ProductInOrder.objects.filter(order=order_id)

    ws['B3'] = "{lastname}".format(lastname=order.lastname)
    ws['B4'] = "{firstname}".format(firstname=order.firstname)
    ws['B5'] = "{city}".format(city=order.city)
    ws['B6'] = "{phone}".format(phone=order.phone)
    ws['B7'] = "{email}".format(email=order.email)

    n = 12

    for item in product_order:
        A = f"A{n}"
        C = f"C{n}"
        D = f"D{n}"
        E = f"E{n}"

        ws[A] = "{title}".format(title=item.product.title)
        ws[C] = "{nmb}".format(nmb=item.nmb)
        ws[D] = "{price}".format(price=item.price_per_item)
        ws[E] = "{sum}".format(sum=item.total_price)
        
        n += 1

    try:
        output_file = folder + "orders/" + name + ".xlsx"
        wb.save(output_file)
        print('Document [Save]')
        
    except:
        print('Error [Save]')
