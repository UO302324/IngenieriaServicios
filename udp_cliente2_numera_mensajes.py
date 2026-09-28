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
contador = 1

while nextLine != "FIN":
    nextLine = input("Introduce un mensaje (FIN para salir): ")

    if nextLine == "FIN":
        break

    mensaje_numerado = f"{contador}: {nextLine}"
    s.sendto(mensaje_numerado.encode("utf-8"), (ip, puerto))
    contador += 1

s.close()