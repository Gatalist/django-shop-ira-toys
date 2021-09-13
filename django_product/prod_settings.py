import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", ".ira-toys-by-7km.com"]


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'xxxxxx',
        'USER': 'xxxxxx',
        'PASSWORD': 'xxxxxxxxx',
        'HOST': 'localhost',
        'PORT': 'xxxx',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
