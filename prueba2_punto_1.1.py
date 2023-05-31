import subprocess
import datetime

# Obtener la hora actual
hora_actual = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)

# Calcular la hora de inicio y fin del rango de tiempo (última hora cerrada)
hora_fin = hora_actual.replace(minute=0)
hora_inicio = hora_fin - datetime.timedelta(hours=1)

# Construir el comando para filtrar las líneas en el rango de tiempo
comando = f"grep 'authentication failure' /var/log/secure | grep '{hora_inicio:%b %d %H}'"

# Ejecutar el comando con usuario root y obtener el resultado
resultado = subprocess.check_output(['sudo', 'bash', '-c', comando], universal_newlines=True)

# Contar la cantidad de intentos fallidos de inicio de sesión
cantidad_intentos_fallidos = len(resultado.splitlines())

print(f"La cantidad de intentos fallidos entre {hora_inicio} y {hora_fin} es: {cantidad_intentos_fallidos}")
