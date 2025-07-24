# projeto\settings\testing.py
# Configurações para testes automatizados
from .base import *

DEBUG = False

#SECRET_KEY = 'test-secret-key' 
# # O Django já herda todas as configurações do base.py. Não é necessário redefinir. 

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
