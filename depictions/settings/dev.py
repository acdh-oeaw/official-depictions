
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#(&h$k5$9hxjnj9d@n2gn$q3fi2%0blcwbp(iu083(#6lilfo4'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
