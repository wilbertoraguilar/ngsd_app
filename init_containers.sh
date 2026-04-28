docker-compose up --build -d
sleep 5
docker exec books_online_backend /bin/bash -c "/app/init_db.sh"
