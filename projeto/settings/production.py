#projeto\settings\production.py
from .base import *
from pathlib import Path
import os

# =========================
# Debug e Hosts Permitidos
# =========================
#DEBUG = os.getenv("DEBUG", "0") == "1"
#if os.getenv("FORCE_PRODUCTION", "0") == "1":
#    DEBUG = False
DEBUG= True
ALLOWED_HOSTS = [host.strip() for host in os.getenv("ALLOWED_HOSTS", "d13100s.vps-kinghost.net,177.153.60.142").split(",")]
#ALLOWED_HOSTS =['*']
#ALLOWED_HOSTS = ["ALLOWED_HOSTS","d13100s.vps-kinghost.net","177.153.60.142"]
print(f"[INFO] Ambiente: PRODUCTION | DEBUG={DEBUG} | ALLOWED_HOSTS={ALLOWED_HOSTS}")

# =========================
# Banco de Dados
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'psql'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# =========================
# Email
# =========================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.empresa.com.br')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'noreply@empresa.com.br')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# =========================
# Segurança
# =========================
SECURE_SSL_REDIRECT = False  # True se tiver certificado SSL ativo
CSRF_COOKIE_SECURE = False   # True se tiver certificado SSL ativo
SESSION_COOKIE_SECURE = False  # True se tiver certificado SSL ativo
SECURE_HSTS_SECONDS = 31536000

# =========================
# Cache (Redis)
# =========================
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/1'),
    }
}

# =========================
# Arquivos Estáticos e Media
# =========================
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'

# =========================
# Logging
# =========================
LOGS_DIR = BASE_DIR / 'logs'
LOGS_DIR.mkdir(parents=True, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': LOGS_DIR / 'django.log',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}



print("ALLOWED_HOSTS do .env:", os.getenv('ALLOWED_HOSTS'))
ALLOWED_HOSTS = [h.strip() for h in os.getenv('ALLOWED_HOSTS', '').split(',') if h.strip()]
print("ALLOWED_HOSTS final:", ALLOWED_HOSTS)
print(f'ALLOWED_HOSTS_FROM_ENV: {os.getenv("ALLOWED_HOSTS")}')
