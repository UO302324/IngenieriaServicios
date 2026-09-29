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

s.settimeout(0.1)

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

    try:
        datagrama, origen = s.recvfrom(1024)
        respuesta = datagrama.decode("utf-8")

        if respuesta == "OK":
            print("Confirmación recibida del servidor.")
        else:
            print(f"Recibido mensaje no esperado: {respuesta}")
            
    except socket.timeout:
        # Por si pasó el tiempo y no llega nada
        print("Timeout agotado. El paquete se ha perdido.")
    except Exception as e:
        # Por si ocurre cualquier otro error de red
        print(f"Error: {e}")
        raise

s.close()