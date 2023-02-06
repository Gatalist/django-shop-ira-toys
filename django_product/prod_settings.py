from os import path
from pathlib import Path
from os import environ as env

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", env["SERVER_IP"], env["SERVER_DNS"]]

# Database
DATABASES = {
    'default': {
        'ENGINE': env["DATABASE_ENGINE"],
        'NAME': env["DATABASE_NAME"],
        'USER': env["DATABASE_USER"],
        'PASSWORD': env["DATABASE_PASSWORD"],
        'HOST': env["DATABASE_HOST"],
        'PORT': env["DATABASE_PORT"],
    }
}

STATIC_ROOT = path.join(BASE_DIR, 'static/')
