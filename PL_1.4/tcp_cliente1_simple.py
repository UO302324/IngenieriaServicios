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

for i in range(5):
    mensaje = "ABCDE"
    s.send(mensaje.encode("ascii"))
    print("Enviado: %s" % mensaje)

mensaje_final = "FINAL"
s.send(mensaje_final.encode("ascii"))
print("Enviado: %s" % mensaje_final)

s.close()
print("Cliente desconectado")