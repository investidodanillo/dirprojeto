from .base import *

DEBUG = os.getenv("DEBUG", "1") == "1"
if os.getenv("FORCE_PRODUCTION", "0") == "1":
    DEBUG = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

print(f"[INFO] Ambiente: DEVELOPMENT | DEBUG={DEBUG} | ALLOWED_HOSTS={ALLOWED_HOSTS}")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}