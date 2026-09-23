import socket
import sys

puerto = 9999    # Por defecto

if len(sys.argv) > 1:
    puerto = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", puerto))

while True:
    datagrama, origen = s.recvfrom(1024)
    mensaje = datagrama.decode("utf-8")
    print(f"Se ha recibido desde {puerto} el siguiente mensaje: {mensaje}")