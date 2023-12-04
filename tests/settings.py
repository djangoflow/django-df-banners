from df_api_drf.defaults import (
    DF_API_DRF_INSTALLED_APPS,
)
from df_api_drf.defaults import (
    REST_FRAMEWORK as DEFAULT_REST_FRAMEWORK,
)
from df_api_drf.defaults import (
    SPECTACULAR_SETTINGS as DEFAULT_SPECTACULAR_SETTINGS,
)

from df_banners.defaults import (
    DF_BANNERS_VIDEO_INSTALLED_APPS,
)

from .celery import *  # noqa: F401, F403

DEBUG = True

ROOT_URLCONF = "tests.urls"
SECRET_KEY = "111111"  # noqa: S105
HASHID_FIELD_SALT = "111111"
HASHID_FIELD_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


CELERY_BROKER_URL = "memory://"
CELERY_RESULT_BACKEND = "cache+memory://"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

USE_TZ = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    *DF_API_DRF_INSTALLED_APPS,
    *DF_BANNERS_VIDEO_INSTALLED_APPS,
    "tests.test_app.apps.TestAppConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]

SITE_ID = 1

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

STATIC_URL = "/static/"

ALLOWED_HOSTS = ["*"]

REST_FRAMEWORK = {
    **DEFAULT_REST_FRAMEWORK,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

SPECTACULAR_SETTINGS = {
    **DEFAULT_SPECTACULAR_SETTINGS,
}
