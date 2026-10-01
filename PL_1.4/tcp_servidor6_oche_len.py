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

    f = sd.makefile(mode = "rb")

    while True:
        mensaje_medirLong = f.readline()

        if not mensaje_medirLong:
            print("El cliente cerró la conexión")
            break

        longitud = int(mensaje_medirLong.strip())

        mensaje_bytes = f.read(longitud)
        linea = mensaje_bytes.decode("utf-8")
        
        linea_reves = "".join(reversed(linea))
        
        respuesta_bytes = linea_reves.encode("utf-8")
        cabecera_longitud = f"{len(respuesta_bytes)}\n".encode("utf-8")
        sd.sendall(cabecera_longitud + respuesta_bytes)
    
    sd.close()
