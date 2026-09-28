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

    timeout = 0.1
    entregado = False

    while timeout <= 2:
        s.settimeout(timeout)
        s.sendto(mensaje_numerado.encode("utf-8"), (ip, puerto))   

        try:
            datagrama, origen = s.recvfrom(1024)
            respuesta = datagrama.decode("utf-8")

            if respuesta == "OK":
                print("Confirmación recibida del servidor.")
                entregado = True
                break
                
        except socket.timeout:
            # Por si pasó el tiempo y no llega nada
            # Para el próximo intento duplicamos el tiempo
            print("Timeout agotado. Reintentando enviar el datagrama...")
            timeout = timeout * 2
        except Exception as e:
            # Por si ocurre cualquier otro error de red
            print(f"Error: {e}")
            break

    if entregado == False:
        # Superamos los 2 segundos y nunca se puso a True
        print("Puede que el servidor esté caído. Inténtelo más tarde")
        break

    contador += 1

s.close()