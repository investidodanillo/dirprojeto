# projeto\settings\__init__.py
# Arquivo de inicialização do pacote settings

import os

# Se não especificar, usa development por padrão
default_settings = 'projeto.settings.development'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', default_settings)