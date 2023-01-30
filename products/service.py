import datetime
from django_product.settings import new_product_data
# from functools import lru_cache


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_session_key(request):
    session_key = request.session.session_key
    return session_key


# @lru_cache(maxsize=50)
def range_date():
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=-new_product_data)
    
    return [end_date, start_date]
