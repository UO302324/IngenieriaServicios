import socket
import sys
import struct


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

mensajes_prueba = [
    "HOLA",
    "HOLAA",
    "HOLAAA",
    "HOLAAAA"
]

for mensaje in mensajes_prueba:
    mensaje_bytes = mensaje.encode("utf-8")
    cabecera_longitud = struct.pack(">H", len(mensaje_bytes))
    s.sendall(cabecera_longitud + mensaje_bytes)
    
for mensaje in mensajes_prueba:
    cabecera = s.recv(2)

    if cabecera:
        longitud = struct.unpack(">H", cabecera)[0]

        respuesta_bytes = s.recv(longitud)
        respuesta = respuesta_bytes.decode("utf-8")
        
        print(f"Enviado: {mensaje.strip()}\nRecibido: {respuesta.strip()}")

s.close()
print("Cliente desconectado")