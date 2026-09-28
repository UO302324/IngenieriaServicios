import socket

puerto = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# SO_BROADCAST para habilitar el modo broadcast
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.bind(("", puerto))
print(f"Escuchando en el puerto {puerto}...")

while True:
    datagrama, origen = s.recvfrom(1024)
    mensaje = datagrama.decode("utf-8")
    
    # origen[0] contiene la IP del cliente y origen[1] el puerto
    ip = origen[0] 
    
    if mensaje == "BUSCANDO HOLA":
        print(f"Petición de búsqueda recibida de {ip}")
        s.sendto(b"IMPLEMENTO HOLA", origen)
        
    elif mensaje == "HOLA":
        print(f"Petición de servicio recibida de {ip}")
        respuesta = f"HOLA: {ip}"
        s.sendto(respuesta.encode("utf-8"), origen)