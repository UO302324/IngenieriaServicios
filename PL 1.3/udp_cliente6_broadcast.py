import socket
import sys

# Si el usuario pasa una ip específica la usamos
if len(sys.argv) > 1:
    broadcast = sys.argv[1]
else:
    broadcast = "<broadcast>"

puerto = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Habilitar el modo broadcast
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print(f"Buscando servidores en ({broadcast}).")

s.sendto(b"BUSCANDO HOLA", (broadcast, puerto))

s.settimeout(2.0)
primer_server = None

print("Esperando respuestas.")

while True:
    try:
        datagrama, origen = s.recvfrom(1024)
        respuesta = datagrama.decode("utf-8")
        
        if respuesta == "IMPLEMENTO HOLA":
            print(f"Servidor encontrado. IP: {origen[0]}")
            
            # Si es el primero que encuentra, se guarda su IP y puerto
            if primer_server is None:
                primer_server = origen
                
    except socket.timeout:
        # Se acaba el tiempo de búsqueda
        print("Fin de la búsqueda (timeout).")
        break

# Si encontra al menos un servidor, pide el servicio
if primer_server:
    print(f"\nProbando el servicio con el primer servidor ({primer_server[0]})...")
    
    s.sendto(b"HOLA", primer_server)
    
    try:
        datagrama, origen = s.recvfrom(1024)
        print(f"Respuesta del servidor: {datagrama.decode('utf-8')}")
    except socket.timeout:
        print("Error: El servidor no respondió a la petición de servicio.")
else:
    print("No se encontró ningún servidor en la red local.")

s.close()