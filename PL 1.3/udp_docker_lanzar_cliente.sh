#!/bin/bash
IP_BROADCAST="172.18.255.255"

echo "El cliente UDP va a buscar en $IP_BROADCAST"

docker run -it --rm --name cliente --network pruebas -v "$(pwd):/app" python:3.7 python /app/udp_cliente6_broadcast.py $IP_BROADCAST
