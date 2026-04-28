docker-compose up --build -d
sleep 5
docker exec books_online_backend /bin/bash -c "/app/init_db.sh"
docker exec books_online_rabbitmq /bin/bash -c "./init_rabbitmq.sh"
docker exec books_online_rabbitmq /bin/bash -c "echo 'deprecated_features.permit.transient_nonexcl_queues = true' >> /etc/rabbitmq/conf.d/10-defaults.conf"
docker exec books_online_rabbitmq /bin/bash -c "echo 'deprecated_features.permit.global_qos = true' >> /etc/rabbitmq/conf.d/10-defaults.conf"
docker restart books_online_rabbitmq

