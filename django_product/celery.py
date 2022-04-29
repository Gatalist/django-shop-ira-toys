import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_product.settings')

app = Celery('django_product')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()