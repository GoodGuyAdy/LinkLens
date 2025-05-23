"""
Django settings for LinkLens project.
"""

from pathlib import Path
from Constants.LLM import LLMProvider
from Constants.GraphDB import GraphDBProvider

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-p2__ukdvwlfk2=)7#3sie7!x=fkq37mnc4yg^^boo495^x3#rr"

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Models",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "LinkLens.middleware.LogstashLoggingMiddleware",
]

ROOT_URLCONF = "LinkLens.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "LinkLens.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CURRENT_GRAPH_DB_PROVIDER = GraphDBProvider.neo4j
CURRENT_LLM_PROVIDER = LLMProvider.ai21


NEO4J_URL = "localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"


ELASTIC_HOST = "localhost"
ELASTIC_PORT = 9200


LOG_ALL_REQUESTS = True
LOGSTASH_HOST = "localhost"
LOGSTASH_PORT = 5000


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "logstash": {
            "level": "INFO",
            "class": "logstash.TCPLogstashHandler",
            "host": LOGSTASH_HOST,
            "port": LOGSTASH_PORT,
        },
    },
    "loggers": {
        "api_logger": {
            "handlers": ["logstash"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
