import os
from pathlib import Path

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
BASE_DIR = Path(__file__).resolve().parent.parent
ACDH_IMPRINT_URL = "https://shared.acdh.oeaw.ac.at/acdh-common-assets/api/imprint.php?serviceID="

REDMINE_ID = os.environ.get('REDMINE_ID', 8112)
SECRET_KEY = os.environ.get('SECRET_KEY', 'TZRlajdflsdjflöjflHHwGV')
ADD_ALLOWED_HOST = os.environ.get('ALLOWED_HOST', '*')

if os.environ.get('DEBUG', False):
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    ADD_ALLOWED_HOST,
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'depictions'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTEGRES_PORT', '5432')
    }
}

# Application definition

INSTALLED_APPS = [
    'dal',
    'django.contrib.admin',
    'dal_select2',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reversion',
    'crispy_forms',
    'django_filters',
    'django_tables2',
    'rest_framework',
    'leaflet',
    'idprovider',
    'webpage',
    'browsing',
    'vocabs',
    'entities',
    'cards',
    'charts',
    'handle',
    'archeutils',
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
]

ROOT_URLCONF = 'depictions.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'webpage.webpage_content_processors.installed_apps',
                'webpage.webpage_content_processors.is_dev_version',
                'webpage.webpage_content_processors.get_db_name',
            ],
        },
    },
]

WSGI_APPLICATION = 'depictions.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

ARCHE_SETTINGS = {
    'project_name': ROOT_URLCONF.split('.')[0],
    'base_url': "https://id.acdh.oeaw.ac.at/{}".format(ROOT_URLCONF.split('.')[0])
}

VOCABS_DEFAULT_PEFIX = os.path.basename(BASE_DIR)

VOCABS_SETTINGS = {
    'default_prefix': VOCABS_DEFAULT_PEFIX,
    'default_ns': "http://www.vocabs/{}/".format(VOCABS_DEFAULT_PEFIX),
    'default_lang': "en"
}

APIS_IIIF_SERVER = "https://iiif.acdh-dev.oeaw.ac.at/iiif/images/depictions"
APIS_OSD_JS = "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/2.4.0/openseadragon.min.js"
APIS_OSD_IMG_PREFIX = "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/2.4.0/images/"


LEAFLET_CONFIG = {
    'MAX_ZOOM': 18,
    'DEFAULT_CENTER': (47, 16),
    'DEFAULT_ZOOM': 4,
    'TILES': [
        (
            'BASIC',
            'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            {
                'attribution':
                    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>\
                    contributors',
                'maxZoom': 18,
            }
        )
    ],
}


ARCHE_PROJECT_NAME = "Offizielle Ansichten"
ARCHE_BASE_URL = "https://id.acdh.oeaw.ac.at/official-depictions"
ARCHE_LANG = 'de'

ARCHE_CONST_MAPPINGS = [
    ('hasOwner', "https://d-nb.info/gnd/1058187643",),  # Bürgschwentner
    ('hasContact', "https://d-nb.info/gnd/1058187643",),
    ('hasRightsHolder', "https://d-nb.info/gnd/1058187643",),
    ('hasPrincipalInvestigator', "https://d-nb.info/gnd/1058187643",),
    ('hasLicensor', 'https://d-nb.info/gnd/1058187643',),
    ('hasCreator', 'https://d-nb.info/gnd/1058187643',),
    ('hasLicense', 'https://creativecommons.org/licenses/by/4.0/',),
    ('hasRelatedDiscipline', 'https://vocabs.acdh.oeaw.ac.at/oefosdisciplines/601',),
    ('hasSubject', 'Erster Weltkrieg',),
    ('hasSubject', 'Kriegsfürsorgeamt',),
    ('hasSubject', 'Postkarte',),
    ('hasMetadataCreator', 'https://d-nb.info/gnd/1043833846',),  # pandorfer
    ('hasDepositor', 'https://d-nb.info/gnd/1043833846',),  # pandorfer
]
