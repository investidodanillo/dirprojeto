# projeto\settings\__init__.py
# Arquivo de inicialização do pacote settings

import os

# Define o ambiente baseado na variável de ambiente
environment = os.environ.get('DJANGO_ENV', 'production')

if environment == 'production':
    default_settings = 'projeto.settings.production'
else:
    default_settings = 'projeto.settings.development'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', default_settings)

# Se não especificar, usa development por padrão
#default_settings = 'projeto.settings.development'
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', default_settings)
