rabbitmqctl add_vhost bo_vhost
rabbitmqctl set_user_tags admin bo_tag
rabbitmqctl set_permissions -p bo_vhost admin ".*" ".*" ".*"
