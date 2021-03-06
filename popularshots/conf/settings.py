import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'i3p5y8*0ul&vnj2df(!rwi8&^1xjxu8#7&$2%h)nq2a)+(o(iv'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = (
    'admin_bootstrap',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'shot',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'conf.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'TEST_NAME': os.path.join(os.path.dirname(__file__), 'test.db'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'media')

USE_ETAGS = True

CORS_ORIGIN_ALLOW_ALL = True

DATE_FORMAT = '%d/%m/%Y'
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%Y-%m-%d')
DATETIME_INPUT_FORMATS = ('%d/%m/%Y', '%Y-%m-%d')
