import socket
import sys
import time


if len(sys.argv) > 1:
    puerto = int(sys.argv[1])
else:
    puerto = 9999

# Creación del socket de escucha
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Podríamos haber omitido los parámetros, pues por defecto `socket()` en python
# crea un socket de tipo TCP

# Asignarle puerto
s.bind(("", puerto))

# Ponerlo en modo pasivo
s.listen(5)  # Máximo de clientes en la cola de espera al accept()

# Bucle principal de espera por clientes
while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)

    time.sleep(1)

    f = sd.makefile(encoding = "utf-8", newline = "\r\n")

    while True:
        mensaje = f.readline()

        if not mensaje:
            print("El cliente cerró la conexión")
            break

        linea = mensaje.strip()  # Quitamos "\r\n"
        linea_reves = "".join(reversed(linea))
        respuesta = linea_reves + "\r\n"

        sd.sendall(respuesta.encode("utf-8"))
    
    sd.close()
