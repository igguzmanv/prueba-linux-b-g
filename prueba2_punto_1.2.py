import psutil
# Obtener información sobre la CPU
cpu_percent = psutil.cpu_percent()
cpu_count_logical = psutil.cpu_count()
cpu_count_physical = psutil.cpu_count(logical=False)

# Imprimir los resultados
print("\nInformación de la CPU:")
print("Uso de CPU: ", cpu_percent, "%")
print("Número de núcleos lógicos: ", cpu_count_logical)
print("Número de núcleos físicos: ", cpu_count_physical)
# Obtener información sobre el disco
disk = psutil.disk_usage('/')
total_disk = disk.total
used_disk = disk.used
free_disk = disk.free

# Obtener información sobre la memoria
memory = psutil.virtual_memory()
total_memory = memory.total
used_memory = memory.used
free_memory = memory.available

# Obtener información sobre la red
network = psutil.net_if_addrs()
network_interfaces = list(network.keys())

# Imprimir los resultados
print("Información del disco:")
print("Total: ", total_disk)
print("Usado: ", used_disk)
print("Libre: ", free_disk)

print("\nInformación de la memoria:")
print("Total: ", total_memory)
print("Usada: ", used_memory)
print("Libre: ", free_memory)

print("\nInterfaces de red:")
for interface in network_interfaces:
    print(interface)
