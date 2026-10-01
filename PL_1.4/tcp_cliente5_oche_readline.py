import socket
import sys


if len(sys.argv) > 1:
    ip = sys.argv[1]
else:
    ip = "localhost"

if len(sys.argv) > 2:
    puerto = int(sys.argv[2])
else:
    puerto = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"Conectando al servidor {ip} por el puerto {puerto}")

s.connect((ip, puerto))
print("Se ha conectado con éxito")

f = s.makefile(encoding = "utf-8", newline="\r\n")

mensajes_prueba = [
    "HOLA\r\n",
    "HOLAA\r\n",
    "HOLAAA\r\n",
    "HOLAAAA\r\n"
]

for mensaje in mensajes_prueba:
    s.sendall(mensaje.encode("utf-8"))
    
for mensaje in mensajes_prueba:
    respuesta = f.readline()
    if respuesta:
        print(f"Enviado: {mensaje.strip()}\nRecibido: {respuesta.strip()}")

s.close()
print("Cliente desconectado")