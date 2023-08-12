import os
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_DIR = BASE_DIR.parent

if os.path.exists('%s/.env' % PROJECT_DIR):
    load_dotenv('%s/.env' % PROJECT_DIR)

env = os.environ

DEBUG = bool(int(env['DEBUG']))
DEBUG_SHOW_LOGGING = bool(int(env.get('DEBUG_SHOW_LOGGING', 1)))
DISABLE_CACHE = bool(int(env.get('DISABLE_CACHE', 0)))

# SECURITY
SECRET_KEY = env['SECRET_KEY']

# Вказує, на яких домен, може працювати app
ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    *env['ALLOWED_HOSTS'].split(',')
]

CSRF_TRUSTED_ORIGINS = [
    *env['CSRF_ORIGINS'].split(',')
]
CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

SECURE_HSTS_SECONDS = bool(int(env.get('SECURE_HSTS_INCLUDE_SUBDOMAINS', 10)))

SECURE_HSTS_INCLUDE_SUBDOMAINS = bool(int(env.get('SECURE_HSTS_INCLUDE_SUBDOMAINS', 1)))

SECURE_SSL_REDIRECT = bool(int(env.get('SECURE_SSL_REDIRECT', 0)))

SESSION_COOKIE_SECURE = bool(int(env.get('SESSION_COOKIE_SECURE', 1)))

CSRF_COOKIE_SECURE = bool(int(env.get('CSRF_COOKIE_SECURE', 1)))

SECURE_HSTS_PRELOAD = bool(int(env.get('SECURE_HSTS_PRELOAD', 1)))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',  # rest api framework
    # 'rest_framework.authtoken' # для роботи token
    'adrf',  # fix for work async in rest api framework
    'drf_standardized_errors',  #
    'cacheops',  # caching system
    'corsheaders',  # for support cors
    'drf_spectacular',  # generator swagger
    'drf_spectacular_sidecar',  # required for Django collectstatic discovery

    'translate',
    'services',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    "corsheaders.middleware.CorsMiddleware",  # For support cors
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For support get static
    'core.middleware.ignoreAllowHostForCheckHeartStatus.IgnoreAllowedHostsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database and redis

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        'ENGINE': 'mysql.connector.django',
        'NAME': env['DB_NAME'],
        'USER': env['DB_USER'],
        'PASSWORD': env['DB_PASSWORD'],
        'HOST': env.get('DB_HOST', '127.0.0.1'),
        'PORT': env.get('DB_PORT', '3306'),
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}
CACHEOPS_REDIS = {
    'host': env.get('REDIS_HOST', '127.0.0.1'),  # redis-server is on same machine
    'port': env.get('REDIS_PORT', '6379'),  # default redis port
    'db': env.get('REDIS_DB', '0'),  # SELECT non-default redis database

    'password': env.get('REDIS_PASSWORD', 'password'),
}

# Password validation

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

# Setting rest API
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # Мінімальний результат JSON
        # 'rest_framework.renderers.JSONOpenAPIRenderer', # Розширений, зручний для перегляду в браузері
    ],
    # 'EXCEPTION_HANDLER': 'app.api.utils.exception_handler'
    'EXCEPTION_HANDLER': 'drf_standardized_errors.handler.exception_handler',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
DRF_STANDARDIZED_ERRORS = {
    "EXCEPTION_FORMATTER_CLASS": 'api.utils.exception.formatter.MyExceptionFormatter',
    "ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": False
}

# docs
SPECTACULAR_SETTINGS = {
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    # OTHER SETTINGS
}
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles/'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom param
APPEND_SLASH = False

# Settings for cache ops
CACHEOPS = {
    'api.*': {'ops': 'all'},
}

if DISABLE_CACHE:
    # час кешування 1 секунда, менше не було можливості
    CACHEOPS_DEFAULTS = {
        'timeout': 1
    }

else:
    CACHEOPS_DEFAULTS = {
        'timeout': 24 * 60 * 60
    }

if DEBUG_SHOW_LOGGING is True:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                'format': '%(name)-12s %(levelname)-8s %(message)s'
            },
            'file': {
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'formatter': 'file',
                'filename': 'debug.log'
            }
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['console', 'file']
            }
        }
    }
