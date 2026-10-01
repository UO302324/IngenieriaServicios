import socket
import sys
import time
import struct


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

    while True:
        cabecera = sd.recv(2)

        if not cabecera:
            print("El cliente cerró la conexión")
            break

        longitud = struct.unpack(">H", cabecera)[0]
        mensaje_bytes = sd.recv(longitud)
        linea = mensaje_bytes.decode("utf-8")
        
        linea_reves = "".join(reversed(linea))
        
        respuesta_bytes = linea_reves.encode("utf-8")
        cabecera_respuesta = struct.pack(">H", len(respuesta_bytes))
        sd.sendall(cabecera_respuesta + respuesta_bytes)
    
    sd.close()
