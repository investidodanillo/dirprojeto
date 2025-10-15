FROM python:3.11.3-alpine3.18

LABEL maintainer="investidordanillo@gmail.com"

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/venv/bin:$PATH" \
    DJANGO_SETTINGS_MODULE="projeto.settings.production"

# Instala dependências
RUN apk update && apk add --no-cache \
    build-base \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    libffi-dev \
    bash \
    gettext \
    curl  # 🔹 Adicionado curl para healthcheck e testes

# Cria e ativa o ambiente virtual
RUN python -m venv /venv

# Instala dependências Python
COPY requirements.txt /tmp/requirements.txt
RUN /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install --no-cache-dir -r /tmp/requirements.txt && \
    /venv/bin/pip install gunicorn psycopg2-binary

# 🔹 Sugestão mínima: copiar e buildar CSS antes do Gunicorn
# COPY build_css.py /app/  # já está na raiz do projeto, então COPY geral funciona

# Cria estrutura de diretórios e usuário não-root
RUN mkdir -p /app && \
    adduser -D -u 1000 duser && \
    mkdir -p /app/static /app/media /app/logs && \
    chown -R duser:duser /app && \
    chmod -R 755 /app

# Copia o projeto (com .dockerignore)
COPY --chown=duser:duser . /app
WORKDIR /app

# USER root é necessário para algumas operações (ex: gunicorn binds <1024 se necessário)
USER root

# Healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health/ || exit 1

# Comando de inicialização
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--log-file", "-", "projeto.wsgi:application"]
