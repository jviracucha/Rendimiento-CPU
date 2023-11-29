import psutil
import cpuinfo

# Obtener el uso de CPU actual
def mostrar_rendimiento_cpu():

    uso_cpu = psutil.cpu_percent()

    print(f"Uso de CPU: {uso_cpu}%")

mostrar_rendimiento_cpu()

# Obtener el uso de memoria actual
def mostrar_rendimiento_memoria():

    uso_memoria = psutil.virtual_memory().percent

    print(f"Uso de memoria: {uso_memoria}%")

mostrar_rendimiento_memoria()

# Obtener las estadísticas de red actuales
def mostrar_rendimiento_red():

    estadisticas_red = psutil.net_io_counters()

    rendimiento_mb = estadisticas_red.bytes_sent / (1024 * 1024)

    print(f"Estadísticas de red (MB/s): {rendimiento_mb:.2f}")

mostrar_rendimiento_red()

# Obtener la temperatura de la CPU
def obtener_temperatura_cpu():
    info = cpuinfo.get_cpu_info()

    if 'temperature' in info:
        temperatura = info['temperature']
        print(f"Temperatura de la CPU: {temperatura}°C")
    else:
        print("No se pudo obtener la temperatura de la CPU.")

obtener_temperatura_cpu()
