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

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Cliente listo para enviar a {ip} por {puerto}")

nextLine = ""

while nextLine != "FIN":
    nextLine = input("Introduce un mensaje (FIN para salir): ")
    s.sendto(nextLine.encode("utf-8"), (ip, puerto))

s.close()