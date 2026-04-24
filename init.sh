#!/bin/bash
rabbitmqctl add_vhost bo_vhost
rabbitmqctl set_permissions -p bo_vhost admin ".*" ".*" ".*"
