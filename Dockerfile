# Dockerfile
# Usa uma imagem base leve do Python com Alpine
FROM python:3.11.3-alpine3.18
LABEL maintainer="investidordanillo@gmail.com"

# Variáveis de ambiente do Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/scripts:/venv/bin:$PATH"

# Instala dependências do sistema necessárias para compilar dependências Python
RUN apk update && apk add --no-cache \
    build-base \
    libffi-dev \
    postgresql-dev \
    musl-dev \
    python3-dev \
    gcc \
    py3-pip \
    bash

# Cria o ambiente virtual
RUN python -m venv /venv

# Copia os arquivos de dependência primeiro para usar cache de camadas
COPY requirements.txt /tmp/requirements.txt

# Instala as dependências do projeto dentro do virtualenv
RUN /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /tmp/requirements.txt

# Cria diretórios para arquivos estáticos e mídias
RUN mkdir -p /data/web/static /data/web/media && \
    adduser -D duser && \
    chown -R duser:duser /data/web && \
    chmod -R 755 /data/web

# Copia o projeto Django e os scripts
COPY projeto .projeto
COPY dotenv_files /dotenv_files

# Define o diretório de trabalho
WORKDIR /projeto

# Expõe a porta 8000 para o servidor Django
EXPOSE 8000

# Altera o usuário para duser (não-root)
USER duser

# Define o comando padrão de inicialização
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

