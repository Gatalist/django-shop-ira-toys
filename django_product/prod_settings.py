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
        'NAME': env["NAME"],
        'USER': env["USER"],
        'PASSWORD': env["PASSWORD"],
        'HOST': env["HOST"],
        'PORT': env["PORT"],
    }
}

STATIC_ROOT = path.join(BASE_DIR, 'static/')
