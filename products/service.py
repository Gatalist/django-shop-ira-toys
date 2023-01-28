import datetime
from django_product.settings import new_product_data
from functools import lru_cache

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


@lru_cache(maxsize=50)
def range_date():
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=-new_product_data)

    start_date_split = str(start_date).split('-')
    end_date_split = str(end_date).split('-')

    start_Y_M_D = datetime.date(int(start_date_split[0]), int(start_date_split[1]), int(start_date_split[2]))
    end_Y_M_D = datetime.date(int(end_date_split[0]), int(end_date_split[1]), int(end_date_split[2]))

    return [end_Y_M_D, start_Y_M_D]
