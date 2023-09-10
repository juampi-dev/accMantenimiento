import subprocess

def ejecutar_sfc_scannow():
    try:
        # Ejecutar el comando sfc /scannow y redirigir la salida a la consola en tiempo real
        proceso = subprocess.Popen(["sfc", "/scannow"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for linea in proceso.stdout:
            print(linea, end='', flush=True)  # Imprimir cada línea de salida sin buffering

        # Esperar a que termine el proceso
        proceso.wait()

        if proceso.returncode == 0:
            print("\nEl comando sfc /scannow se ha ejecutado correctamente.")
        else:
            print("\nError al ejecutar el comando sfc /scannow.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    ejecutar_sfc_scannow()
