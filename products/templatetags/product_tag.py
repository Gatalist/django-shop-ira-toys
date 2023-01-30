import datetime
from django import template
from products.models import Category, Product, Reviews, News, SubCategory
from django_product.settings import news_count_index, reviews_count_index, new_product_data, id_product_new
# from site_management.models import GoogleAnalytics
from django.core.cache import cache


register = template.Library()


@register.simple_tag()
def get_categories():
    """ Рендер категорий в меню """
    return Category.objects.all()


@register.simple_tag()
def get_sub_categories():
    """ Рендер под категорий в меню """
    return SubCategory.objects.all().select_related('category')


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
def get_date():
    cache_menu = cache.get('cache_menu')
    if not cache_menu:
        cache_menu = []
        for x in range (0, new_product_data):
            date = datetime.date.today() - datetime.timedelta(days = x)
            date_txt = str(date).replace(',', '-')
            product = Product.objects.filter(draft=True, status_id=id_product_new, dateAdd=date).count()
            if product > 0:
                cache_menu.append(date_txt)
        cache.set('cache_menu', cache_menu, 60 * 10)

    print(cache_menu)
    return cache_menu


# @register.simple_tag()
# def script_google_analytics():
#     cache_google_script = cache.get('cache_google_script')
#     if not cache_google_script:
#         google_script = GoogleAnalytics.objects.latest('id').script
#         cache.set('cache_google_script', google_script, 60 * 60)
    
#     return cache_google_script
