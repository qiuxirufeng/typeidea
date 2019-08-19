from .base import *     # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'USER': 'root',
        'PASSWORD': '000000',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}