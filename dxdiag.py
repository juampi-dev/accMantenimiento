import subprocess

def ejecutar_dxdiag():
    try:
        # Ejecutar el comando dxdiag y redirigir la salida a la consola en tiempo real
        proceso = subprocess.Popen(["dxdiag"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for linea in proceso.stdout:
            print(linea, end='', flush=True)  # Imprimir cada línea de salida sin buffering

        # Esperar a que termine el proceso
        proceso.wait()

        if proceso.returncode == 0:
            print("\nEl comando dxdiag se ha ejecutado correctamente.")
        else:
            print("\nError al ejecutar el comando dxdiag.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    ejecutar_dxdiag()
