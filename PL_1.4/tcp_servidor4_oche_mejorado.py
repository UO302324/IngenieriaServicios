import socket
import sys
import time

def recibe_mensaje(sock):
    buffer = []

    while True:
        byte = sock.recv(1)

        if not byte:
            if buffer:
                return b"".join(buffer)
            else:
                return None  

        buffer.append(byte)

        if len(buffer) >= 2 and buffer[-2] == b"\r" and buffer[-1] == b"\n":
            break  

    return b"".join(buffer)        


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

    while True:
        mensaje_cod = sd.recv(80)

        if not mensaje_cod:
            print("El cliente cerró la conexión")
            break

        mensaje = mensaje_cod.decode("utf-8")
        linea = mensaje.strip()  # Quitamos "\r\n"
        linea_reves = "".join(reversed(linea))
        respuesta = linea_reves + "\r\n"

        sd.sendall(respuesta.encode("utf-8"))
    
    sd.close()
