# README.md



docker compose down -v
docker-compose up -d --build
docker exec -it container_projeto python manage.py collectstatic --noinput
docker exec -it container_projeto python manage.py collectstatic --noinput --settings=projeto.settings.development


# INSTALAR O DOCKER: Instalar Docker no Ubuntu VPS
# 1  Atualize o apt e instale dependências:
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# 2 Adicione a chave GPG oficial do Docker:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 3 Adicione o repositório oficial do Docker:
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 4 Atualize o apt e instale o Docker Engine:
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# 5 Verifique a instalação do Docker:
sudo docker --version


# 6 Baixe a versão estável do Docker Compose (exemplo 2.20.2):
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 7 Dê permissão para executar:
sudo chmod +x /usr/local/bin/docker-compose

# 8 Verifique a instalação:
docker-compose --version
# Opcional: rodar Docker sem sudo

# 9 Adicione seu usuário ao grupo docker (troque seu_usuario pelo seu user):
sudo usermod -aG docker $USER

# 10 Depois faça logout/login para aplicar.
# 11 Depois de instalado, volte para o diretório do seu projeto e rode:
docker compose up -d --build

# 12 migrações
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
# criar user

docker compose exec web python manage.py createsuperuser
# v2 30/08/2025
