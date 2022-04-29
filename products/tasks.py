from django_product.celery import app
from .models import Product
import datetime

# delete status new to 10 day
@app.task
def product_new_info():
    products_new = Product.objects.filter(status_id=2)
    
    for product in products_new:
        pdoduct_data = product.dateAdd
        status_delete = pdoduct_data + datetime.timedelta(days=+10)
        print(pdoduct_data, status_delete)

        if datetime.date.today() > status_delete:
            product.status = None
            product.save()
