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

f = s.makefile(mode = "rb")

mensajes_prueba = [
    "HOLA\r\n",
    "HOLAA\r\n",
    "HOLAAA\r\n",
    "HOLAAAA\r\n"
]

for mensaje in mensajes_prueba:
    mensaje_bytes = mensaje.encode("utf-8")
    cabecera_longitud = f"{len(mensaje_bytes)}\n".encode("utf-8")
    s.sendall(cabecera_longitud + mensaje_bytes)
    
for mensaje in mensajes_prueba:
    longitud_respuesta = f.readline()
    if longitud_respuesta:
        longitud = int(longitud_respuesta.strip())

        respuesta_bytes = f.read(longitud)
        respuesta = respuesta_bytes.decode("utf-8")
        
        print(f"Enviado: {mensaje.strip()}\nRecibido: {respuesta.strip()}")

s.close()
print("Cliente desconectado")