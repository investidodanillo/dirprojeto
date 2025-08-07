# README.md



docker compose down -v
docker-compose up -d --build
docker exec -it container_projeto python manage.py collectstatic --noinput
docker exec -it container_projeto python manage.py collectstatic --noinput --settings=projeto.settings.development
