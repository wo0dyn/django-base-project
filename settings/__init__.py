import datetime
import os
from environment import base_dir as BASE_DIR

DEBUG = False

SITE_ID = 1
ALLOWED_HOSTS = []

SITE_TITLE = 'Base Project'
SITE_ADMIN_TITLE = '{} Administration'.format(SITE_TITLE)


INSTALLED_APPS = (
    'apps.articles'
    'apps.foo',
    'apps.main',    
    'apps.menus',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_extensions',
    'mptt',
    'rest_framework',
    'suit',
)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_camel.render.CamelCaseJSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_camel.parser.CamelCaseJSONParser',
    ),
    'DEFAULT_METADATA_CLASS': 'apps.main.metadata.NoMetadata',

    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_camel.render.CamelCaseJSONRenderer',
    )
}


TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(BASE_DIR, 'templates')
    ],
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.media',
            'django.template.context_processors.static',

            'django.template.context_processors.request',
        ],
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]
    },
}]

ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_ALGORITHM': 'HS512',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=360),
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# import choices/constants
from settings._choices import *

# import django-suit configuration
from settings._suit import *
