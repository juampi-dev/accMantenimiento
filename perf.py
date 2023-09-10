import subprocess

def ejecutar_perfmon_msc():
    try:
        print("Iniciando perfmon.msc...\n")
        
        # Ejecutar el comando mmc.exe con perfmon.msc como argumento
        proceso = subprocess.Popen(["mmc.exe", "perfmon.msc"])
        
        # Esperar a que el proceso termine
        proceso.wait()
        
        print("\nLa ejecución de perfmon.msc ha finalizado.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    ejecutar_perfmon_msc()
