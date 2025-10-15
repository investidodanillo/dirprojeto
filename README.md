# Atualize pacotes do sistema
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl software-properties-common

🟨 1. Instalar Docker e Docker Compose
# 1. Instalar dependências
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release

# 2. Adicionar chave GPG do Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 3. Adicionar repositório Docker
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 4. Instalar Docker Engine
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# 5. Verificar instalação
docker --version

📌 Instalar Docker Compose
# Baixar versão estável
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Permissões de execução
sudo chmod +x /usr/local/bin/docker-compose

# Verificar
docker-compose --version

👤 (Opcional) Rodar Docker sem sudo
sudo usermod -aG docker $USER
# ⚠️ Depois disso, saia do SSH e entre novamente para aplicar
exit
# Reentre:
ssh seu_usuario@177.153.60.142

🟩 2. Clonar seu projeto
cd ~
git clone https://github.com/investidodanillo/dirprojeto.git
cd dirprojeto

🟧 3. Construir e subir os containers

Antes de subir, garanta que o arquivo docker-compose.yml está correto e sem atributo version: (pois agora é obsoleto).

👉 Agora rode:

docker compose build --no-cache
docker compose up -d


Verifique se tudo subiu:

docker ps

🟦 4. Instalar dependências dentro do container (se necessário)

Caso seu Dockerfile já instale os pacotes via requirements.txt, esta etapa não é necessária.
Mas se quiser garantir:

docker compose exec web pip install --upgrade pip setuptools wheel
docker compose exec web pip install -r requirements.txt

🟨 5. Rodar migrações e criar superusuário
5.1     docker compose exec web python manage.py makemigrations
5.2     docker compose exec web python manage.py migrate
5.3     docker compose exec web python manage.py createsuperuser

🟩 6. Coletar arquivos estáticos
docker compose exec web python manage.py collectstatic --noinput


Se estiver usando múltiplos settings, especifique:

docker compose exec web python manage.py collectstatic --noinput --settings=projeto.settings.production

🟥 7. Reiniciar os containers para aplicar tudo
docker compose down -v
docker compose up -d --build

🟦 8. Configurar firewall (opcional, recomendado)

Se o firewall estiver ativo, libere as portas 80 (HTTP) e 443 (HTTPS):

sudo ufw allow OpenSSH
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable

🟨 9. Testar no navegador

Acesse:

http://177.153.60.142/


ou se tiver configurado domínio:

http://seudominio.com/

📁 Checklist importante dentro do projeto

✅ docker-compose.yml correto, sem version:

✅ Dockerfile instalando requirements.txt corretamente

✅ ALLOWED_HOSTS no settings.py configurado com IP e domínio:

ALLOWED_HOSTS = ["177.153.60.142", "seudominio.com"]


✅ Volume persistente para banco de dados (se estiver usando PostgreSQL no docker-compose)

✅ Porta 80 redirecionada para Nginx (reverse proxy para Gunicorn)

📝 Roteiro Final Resumido

1️⃣ Instalar Docker + Compose
2️⃣ Clonar repositório
3️⃣ Build + Up containers
4️⃣ Instalar dependências (se necessário)
5️⃣ Migrations + Superuser
6️⃣ Collectstatic
7️⃣ Reiniciar containers
8️⃣ Liberar firewall
9️⃣ Testar no navegador


# bild
docker compose down -v
docker-compose up -d --build

# collectstatic
docker exec -it container_projeto python manage.py collectstatic --noinput
docker exec -it container_projeto python manage.py collectstatic --noinput --settings=projeto.settings.development




docker compose exec web python manage.py createsuperuser




# v2 30/08/2025
