import datetime
from django import template
from products.models import Category, Product, Reviews, News, SubCategory
from django_product.settings import news_count_index, reviews_count_index, new_product_data, id_product_new
# from site_management.models import GoogleAnalytics
from django.core.cache import cache
from django_product.settings import time_cached_menu

register = template.Library()

# def decorate_category(cat_menu):
#     def decorate():
#         cache_categories = cache.get('cache_categories')
#         if not cache_categories:
#             cache_categories = cat_menu
#             cache.set('cache_categories', cache_categories, 60 * time_cached_menu)
#         print(cache_categories)
#         return cache_categories
#     return decorate


@register.simple_tag()
def get_categories():
    """ Рендер категорий в меню """
    cache_categories = cache.get('cache_categories')
    if not cache_categories:
        cache_categories = Category.objects.all()
        cache.set('cache_categories', cache_categories, 60 * time_cached_menu)
    return cache_categories


@register.simple_tag()
def get_sub_categories():
    """ Рендер под категорий в меню """
    cache_categories = cache.get('cache_categories')
    if not cache_categories:
        cache_categories = SubCategory.objects.all().select_related('category')
        cache.set('cache_categories', cache_categories, 60 * time_cached_menu)
    return cache_categories


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
            product = Product.objects.filter(draft=True, status_id=id_product_new, dateAdd=date)
            if product:
                cache_menu.append(date_txt)
            cache.set('cache_menu', cache_menu, 60 * time_cached_menu)
    return cache_menu


# @register.simple_tag()
# def script_google_analytics():
#     cache_google_script = cache.get('cache_google_script')
#     if not cache_google_script:
#         google_script = GoogleAnalytics.objects.latest('id').script
#         cache.set('cache_google_script', google_script, 60 * 60)
    
#     return cache_google_script
