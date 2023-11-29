import socket
import psutil
import pickle

# Definir las direcciones IP y puertos de los servidores
servers = [("192.168.1.1", 5000), ("192.168.1.2", 5000), ("192.168.1.3", 5000)]

# Crear el socket del cliente
client_sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(3)]

# Conectar a los servidores
for i, (server_ip, server_port) in enumerate(servers):
    client_sockets[i].connect((server_ip, server_port))

# Obtener la información del sistema
cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
memory_info = psutil.virtual_memory()
network_info = psutil.net_if_addrs()
system_info = {"cpu_usage": cpu_usage, "memory_info": memory_info, "network_info": network_info}

# Enviar la información del sistema a los servidores
for s in client_sockets:
    s.send(pickle.dumps(system_info))

# Cerrar las conexiones
for s in client_sockets:
    s.close()
