import os
from importlib import metadata

REST_FRAMEWORK = {}
BASE_URL = os.getenv('BASE_URL', 'http://127.0.0.1:3000')


def get_package_version() -> str:
    """
    Trying to get the current package version using the metadata module. This
    assumes that the version is indeed set in pyproject.toml and that the
    package was cleanly installed.
    """

    try:
        return metadata.version("sxt_2023")
    except metadata.PackageNotFoundError:
        return "0.0.0"


# Django settings configuration

# ---
# Basic Configuration
# ---

DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
SECRET_KEY = os.getenv('SECRET_KEY', 'NYigVbGuYrwal4SJmh4DvDwsCweshmsb4lxzKWCkpZol9uiYw86zRX')

# Allow all hosts in production/staging, or use specific hosts from env
ALLOWED_HOSTS_ENV = os.getenv('ALLOWED_HOSTS', '')
if ALLOWED_HOSTS_ENV:
    ALLOWED_HOSTS = ALLOWED_HOSTS_ENV.split(',')
else:
    # Default: allow common hosts
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'solidarityxmastree.com', 'www.solidarityxmastree.com', 'sxt2025.slash-digital.io', '72.61.165.170']

# CSRF Configuration
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:3000',
    'http://localhost:3000',
    'http://sxt2025.slash-digital.io',
    'https://sxt2025.slash-digital.io',
    'http://solidarityxmastree.com',
    'https://solidarityxmastree.com',
    'https://www.solidarityxmastree.com',
]

# Session and Cookie settings
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'

# ---
# Database
# ---

# Support both DATABASE_URL and individual DB_* variables
DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL:
    # If DATABASE_URL is provided, use it (Docker/Production)
    try:
        import dj_database_url
        DATABASES = {
            'default': dj_database_url.parse(DATABASE_URL)
        }
        DATABASES['default']['ENGINE'] = 'psqlextra.backend'
    except ImportError:
        # Fallback if dj_database_url is not installed
        DATABASES = {
            'default': {
                'ENGINE': 'psqlextra.backend',
                'NAME': os.getenv('DB_NAME', 'sxt_2023'),
                'USER': os.getenv('DB_USER', 'sxt_2023'),
                'PASSWORD': os.getenv('DB_PASSWORD', 'sxt_2023'),
                'HOST': os.getenv('DB_HOST', 'localhost'),
                'PORT': os.getenv('DB_PORT', '5432'),
            }
        }
else:
    # Use individual variables (Development)
    DATABASES = {
        'default': {
            'ENGINE': 'psqlextra.backend',
            'NAME': os.getenv('DB_NAME', 'sxt_2023'),
            'USER': os.getenv('DB_USER', 'sxt_2023'),
            'PASSWORD': os.getenv('DB_PASSWORD', 'sxt_2023'),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }

# ---
# Apps
# ---

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "sxt_2023.apps.people",
    "sxt_2023.apps.sxt2023_api",
    "wailer",
]

# ---
# Middleware
# ---

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---
# Templates
# ---

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

# ---
# Plumbing
# ---

ROOT_URLCONF = "sxt_2023.django.urls"

WSGI_APPLICATION = "sxt_2023.django.wsgi.application"

# ---
# Auth
# ---

AUTH_USER_MODEL = "people.User"

# ---
# i18n
# ---

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ("en", "English"),
]

# ---
# Static files
# ---

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'staticfiles')

# Static files directories for development
STATICFILES_DIRS = [
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'static'),
]

# ---
# Default primary key field type
# ---

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---
# OpenAPI Schema
# ---

REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "drf_spectacular.openapi.AutoSchema"

SPECTACULAR_SETTINGS = {
    "TITLE": "SXT 2023",
    "VERSION": get_package_version(),
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

# ---
# Wailer
# ---

WAILER_EMAIL_TYPES = {
    "registration": "sxt_2023.apps.sxt2023_api.emails.Registration",
    "raffleconfirmation": "sxt_2023.apps.sxt2023_api.emails.RaffleConfirmation",
}

WAILER_BASE_URL = os.getenv("WAILER_BASE_URL", BASE_URL)

DEFAULT_FROM_EMAIL = os.getenv(
    "DEFAULT_FROM_EMAIL",
    "Solidarity Xmax Tree <no-reply@solidarityxmastree.com>",
)

# ---
# Email Backend (Mailgun)
# ---

EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'

ANYMAIL = {
    "MAILGUN_API_KEY": os.getenv("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": os.getenv("MAILGUN_DOMAIN", "solidarityxmastree.com"),
    "MAILGUN_API_URL": "https://api.eu.mailgun.net/v3",  # Región EU
}
