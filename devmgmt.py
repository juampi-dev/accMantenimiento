import subprocess

def ejecutar_devmgmt_msc():
    try:
        print("Iniciando devmgmt.msc...\n")
        
        # Ejecutar el comando mmc.exe con devmgmt.msc como argumento
        proceso = subprocess.Popen(["mmc.exe", "devmgmt.msc"])
        
        # Esperar a que el proceso termine
        proceso.wait()
        
        print("\nLa ejecución de devmgmt.msc ha finalizado.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    ejecutar_devmgmt_msc()
