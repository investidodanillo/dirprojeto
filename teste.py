# teste.py

import projeto.settings.development as dev

def teste():
    print("Iniciando o teste de configuração...")
    print(f"DEBUG: {dev.DEBUG}")
    print(f"ALLOWED_HOSTS: {dev.ALLOWED_HOSTS}")
    print(f"DATABASES: {dev.DATABASES}")
    print(f"EMAIL_BACKEND: {dev.EMAIL_BACKEND}")
    print(f"CACHES: {dev.CACHES}")

if __name__ == "__main__":
    teste()
