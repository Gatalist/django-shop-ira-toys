import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "njf+pl=n!ri$9%&lt)-#$&_-437#%^*^_356?9o)o83c+4^kg^#1pl13sb0r3lf)xc^%"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "104.248.203.111", ".ira-toys-by-7km.com"]


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'product',
        'USER': 'user_db',
        'PASSWORD': 'She3348Jdfurfghs',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
