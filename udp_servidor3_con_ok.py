import socket
import sys
import random 

if len(sys.argv) > 1:
    puerto = int(sys.argv[1])
else:
    puerto = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# La IP "" indica que escucharemos en todas las interfaces de red de nuestra máquina.
s.bind(("", puerto))

print(f"Servidor UDP escuchando en el puerto {puerto}...")

while True:
    datagrama, origen = s.recvfrom(1024)
    if random.randint(0, 1) == 0:
        print(f"Simulando paquete perdido")
    else:
        mensaje = datagrama.decode("utf-8")
        print(f"Se ha recibido desde {puerto} el siguiente mensaje: {mensaje}")
        s.sendto("OK".encode("utf-8"), origen)