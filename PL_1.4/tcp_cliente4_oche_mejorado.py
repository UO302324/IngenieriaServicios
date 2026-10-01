import socket
import sys

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
    ip = sys.argv[1]
else:
    ip = "localhost"

if len(sys.argv) > 2:
    puerto = int(sys.argv[2])
else:
    puerto = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"Conectando al servidor {ip} por el puerto {puerto}")

s.connect((ip, puerto))
print("Se ha conectado con éxito")

mensajes_prueba = [
    "HOLA\r\n",
    "HOLAA\r\n",
    "HOLAAA\r\n",
    "HOLAAAA\r\n"
]

for mensaje in mensajes_prueba:
    s.sendall(mensaje.encode("utf-8"))
    
for _ in mensajes_prueba:
    respuesta_cod = recibe_mensaje(s)
    if respuesta_cod:
        respuesta = respuesta_cod.decode("utf-8")
        print(f"Enviado: {mensaje.strip()}\nRecibido: {respuesta.strip()}")

s.close()
print("Cliente desconectado")