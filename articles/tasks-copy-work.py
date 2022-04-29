from django_product.celery import app
from .models import UpdateStatusPrduct, UpdateStatusView
from products.models import Product, Availability
import pandas as pd
from django_product.settings import MEDIA_ROOT

@app.task()
def update_status(status_id):
    update_article_id = UpdateStatusPrduct.objects.get(id=status_id)
    # path to file
    update_file = update_article_id.upload.url
    full_url = MEDIA_ROOT + update_file[6:]

    def parseTable(dataset):
        for index, row in dataset.iterrows():
            yield row
            
    files = pd.read_excel(full_url, sheet_name = 'Страница 0')
    all_rows = parseTable(files)
    
    text = ''
    num = 2

    availability_1 = Availability.objects.get(id=1)
    availability_2 = Availability.objects.get(id=2)

    for elem in all_rows:
        artticl_str = str(elem[5])
        artticl_split = artticl_str.split('.')
        articl = artticl_split[0]
        
        count_str = str(elem[7])
        count_split = count_str.split('.')
        count = count_split[0]
        
        if count != 'nan':
            try:
                print(num, articl, count)
                product = Product.objects.get(article=articl)
                if int(count) > 0:
                    product.availability = availability_1 #'Есть в наличии'
                    product.save()
                    print(product.availability.name)
                elif int(count) == 0:
                    product.availability = availability_2 #'Нет в наличии'
                    product.save()
            except:
                text += f'{num} line - error search article\n'
                continue
            
        else:
            text += f'{num} line - error red, line not integer\n'
        num += 1
        
    UpdateStatusView.objects.create(title=update_article_id.title, status='ok', date=update_article_id.date, description=text)
    
    return "go updatte status product:", status_id, full_url