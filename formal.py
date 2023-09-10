import subprocess
import sys
from util import obtener_respuesta_valida

# Encoder para caracteres en español y tildes (PONELE QUE FUNCIONA)
sys.stdout.reconfigure(encoding='utf-8')

processName = "winsat formal"

def ejecutar_winsat_formal():
    try:
        # Ejecutar el comando winsat formal y redirigir la salida a la consola en tiempo real
        proceso = subprocess.Popen(["winsat", "formal"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        for linea in proceso.stdout:
            print(linea, end='', flush=True)  # Imprimir cada línea de salida sin buffering

        # Esperar a que termine el proceso
        proceso.wait()

        if proceso.returncode == 0:
            print("\nEl comando winsat formal se ha ejecutado correctamente.")
        else:
            print("\nError al ejecutar el comando winsat formal.")
    except Exception as e:
        print(f"Error: {str(e)}")

    # Navegacion
        respuesta = obtener_respuesta_valida(processName)
        if respuesta != "S":
            return  # Regresar al menú principal