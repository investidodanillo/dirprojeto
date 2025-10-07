#projeto\settings\base.py
from pathlib import Path
import os
from dotenv import load_dotenv
from django.conf.locale.pt_BR import formats as pt_formats

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Carrega variáveis do .env
load_dotenv(os.path.join(BASE_DIR /'.env'))

# Qual settings está rodando
ENV_NAME = os.getenv("DJANGO_SETTINGS_MODULE", "desconhecido")

# SECRET_KEY agora lê certo do .env
SECRET_KEY = os.getenv('SECRET_KEY','dummy-secret-key')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #terceiros
    'django_tables2',
    'django_filters',

    #meus aplicativos
    'projeto',
    'aplicativo',
    'principal',
    'desing',
    'controles',
    'desenvolvimento',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'projeto.middleware.login_required.LoginRequiredMiddleware',  # Vírgula adicionada
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


LOGIN_URL = "auth:login"
LOGIN_REDIRECT_URL = "/home_inicio_View/"  # Para onde vai após login
LOGOUT_REDIRECT_URL = "/"  # Para onde vai após logout

ROOT_URLCONF = 'projeto.urls'

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

WSGI_APPLICATION = 'projeto.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'projeto' / 'static',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
pt_formats.DATE_FORMAT = "d/m/Y"