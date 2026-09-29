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

procesados = set()

while True:
    datagrama, origen = s.recvfrom(1024)
    if random.randint(0, 1) == 0:
        print(f"Simulando paquete perdido")
    else:
        mensaje = datagrama.decode("utf-8")
        print(f"Se ha recibido desde {puerto} el siguiente mensaje: {mensaje}")

        partes = mensaje.split(":", 1)
        id = partes[0]

        if id in procesados:
            print(f"Mensaje {id} duplicado. Reenviando ACK...")
        else:
            procesados.add(id)
            print(f"Recibido de {origen}: {mensaje}")

        respuesta = f"OK {id}"
        s.sendto(respuesta.encode("utf-8"), origen)