import os
import environ

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

env = environ.Env(
    DEBUG=(bool, False)
)
env.read_env()

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['booktime.zendoc', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_extensions",
    "webpack_loader",
    'django_tables2',
    'django_filters',
    'widget_tweaks',
    'rest_framework',
    'rest_framework.authtoken',

    'main.apps.MainConfig',
    'channels',

    'whitenoise.runserver_nostatic',

]

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "bundles/",
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats.json"),
        'LOADER_CLASS': 'main.webpack.CustomWebpackLoader',
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'main.middlewares.basket_middleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'booktime.urls'
ASGI_APPLICATION = 'booktime.asgi.application'

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
            ],
        },
    },
]


REDIS_URL = env('REDIS_URL')


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts":{"hosts": [REDIS_URL],}
        },
    }
}

if DEBUG:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
else:
    DATABASES = {'default': env.db('DATABASE_URL')}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = "main.User"

LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(levelname)s %(message)s"}
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        }
    },
    "loggers": {
        "main": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "booktime": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap.html"


if not DEBUG: 
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_CONFIG = env.email_url('EMAIL_URL')
vars().update(EMAIL_CONFIG)

