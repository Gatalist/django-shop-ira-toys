import datetime
from django import template
from products.models import Category, Product, Reviews, News, SubCategory

from django_product.settings import product_count_index, news_count_index, reviews_count_index, new_product_data, id_product_new

register = template.Library()


@register.simple_tag()
def get_categories():
    """ Рендер категорий в меню """
    return Category.objects.all()

@register.simple_tag()
def get_sub_categories():
    """ Рендер под категорий в меню """
    return SubCategory.objects.all()


@register.inclusion_tag("product/tags/last_product.html")
def get_last_product():
    all_product = Product.objects.filter(draft=True, status_id=id_product_new).order_by('-id')
    product = all_product[:product_count_index]
    return {"last_products": product}


@register.inclusion_tag("product/tags/last_reviews.html")
def get_last_review():
    review = Reviews.objects.order_by("-id")[:reviews_count_index]
    return {"last_reviews": review}


@register.inclusion_tag("product/tags/last_news.html")
def get_last_news():
    all_news = News.objects.filter(draft=True).order_by("-id")
    news = all_news[:news_count_index]
    return {"last_newses": news}


@register.simple_tag()
def get_all_product():
    return Product.objects.filter(draft=True).count()


@register.simple_tag()
def get_all_news():
    return News.objects.filter(draft=True).count()


@register.simple_tag()
def get_date():
    # product = Product.objects.filter(draft=True, status_id=1, dateAdd=date)
    end = datetime.date.today()
    numdays = new_product_data
    dateList = []
    for x in range (0, numdays):
        date = end - datetime.timedelta(days = x)
        date_txt = str(date).replace(',', '-')
        
        product = Product.objects.filter(draft=True, status_id=id_product_new, dateAdd=date).count()
        if product > 0:
            dateList.append(date_txt)
    print(dateList)

    return dateList