from .settings import *
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ongdb',
        'USER': 'root',
        'PASSWORD': '7ux3r0.890',
        'HOST': 'localhost',
        'PORT': '',
    }
}
