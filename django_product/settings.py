from pathlib import Path
import os
# from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition
INSTALLED_APPS = [
    'modeltranslation',
    # 'rosetta',
    # 'tabbed_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',
    # 'django.contrib.flatpages',
    # 'debug_toolbar',   
    'ckeditor',
    'ckeditor_uploader',
    'products.apps.ProductsConfig',
    'contact.apps.ContactConfig',
    'orders.apps.OrdersConfig',
    'articles.apps.ArticlesConfig',
    'currency.apps.CurrencyConfig',
    # 'site_management',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.contrib.sessions.backends.cached_db', # add
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.core.mail.backends.smtp.EmailBackend',
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'django_product.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',

                'orders.context_processors.getting_basket_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_product.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('uk', 'Ukrainian'),
    ('ru', 'Russian'),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

# текущий язык для заполнения slug
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'ru' 


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# TABBED_ADMIN_USE_JQUERY_UI = True

from .ckeditor_settings import *
 

# SITE_ID = 1

#mail settings
DEFAULT_FROM_EMAIL = 'ira.toys.by7km@gmail.com'  # от кого - почта
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ira.toys.by7km@gmail.com'
EMAIL_HOST_PASSWORD = "ira.toys.by.7km-2021"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

product_count_index = 10 # количество новинок на слайдере - главная
news_count_index = 3 # количество новостей - главная
reviews_count_index = 5 # количество отзывов на слайдере - главная

product_in_page = 6 # количество продуктов на странице

new_product_data = 14 # указываем количество дней за сколько отображать новинки
id_product_new = 2 # id статуса новинок

# redis settings
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'

# celery
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ":" + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ":" + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *
