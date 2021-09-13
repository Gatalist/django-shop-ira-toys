import os

os.environ["PATH"] += r"/usr/lib/libreoffice/program/"
# os.environ.pop("URE_BOOTSTRAP")

import uno
from os.path import abspath
from orders.models import Order, ProductInOrder

# url_input_file = "/home/user/ira-toys/django_product/django_product/office/"
url_input_file = "/home/alex/django_product/django_product/office/"

url_output_file = url_input_file + "orders/"

name_input_file = "orders.xlsx"
type_file = os.path.splitext(name_input_file)[1]

name_output_file = "order"


def copy_file(name_output_file):
    os.system('cp {name_i} {name_o}'.format(name_i = url_input_file + name_input_file, name_o = url_output_file + name_output_file + type_file))
    outputFile = url_output_file + name_output_file + type_file
    return outputFile


def get_document(filename):
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
    context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
    desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
    document = desktop.loadComponentFromURL(uno.systemPathToFileUrl(abspath(copy_file(name_output_file))), "_blank", 0, tuple([]))
    return document


def table(document, order_id):
    sheet = document.getSheets().getByIndex(0)

    order = Order.objects.get(id=order_id)
    product_order = ProductInOrder.objects.filter(order=order_id)

    data_user = {
        "B3": "{lastname}".format(lastname=order.lastname),
        "B4": "{firstname}".format(firstname=order.firstname),
        "B5": "{city}".format(city=order.city),
        "B6": "{phone}".format(phone=order.phone),
        "B7": "{email}".format(email=order.email),   
        }

    for key, text in data_user.items():
        sheet.getCellRangeByName(key).String = text

    n = 12

    for item in product_order:
        A = f"A{n}"
        C = f"C{n}"
        D = f"D{n}"
        E = f"E{n}"

        sheet.getCellRangeByName(A).String = "{title}".format(title=item.product.title)
        sheet.getCellRangeByName(C).String = "{nmb}".format(nmb=item.nmb)
        sheet.getCellRangeByName(D).String = "{price}".format(price=item.price_per_item)
        sheet.getCellRangeByName(E).String = "{sum}".format(sum=item.total_price)
        n += 1

    
    try:
        document.store()
        document.close(True)
        print('Document [Save]')
        
    except:
        print('Error [Save]')
