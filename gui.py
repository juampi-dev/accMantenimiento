# "GRAPHIC" User Interface

def bienvenida():
    print("\n|-----------------------------------------------------------------------|")
    print("|             PROGRAMA DE MANTENIMIENTO SOFTWARE Y HARDWARE             |")
    print("|                                                                       |")
    print("|                     Agencia Comodoro Conocimiento                     |")
    print("|                                  2023                                 |")
    print("|                                                                       |")
    print("|-----------------------------------------------------------------------|\n")

def mostrar_menu():
    print("\n|-----------------------------------------------------------------------|")
    print("|                                                                       |")
    print("|                            MENU PRINCIPAL                             |")
    print("|                                                                       |")
    print("|-----------------------------------------------------------------------|")
    print("|                                                                       |")
    print("|    1. Diagnosticar problemas de controladores gráficos o de sonido    |") # dxdiag
    print("|    2. Verificar y reparar archivos del sistema dañados o faltantes    |") # sfc /scannow
    print("|    3. Escanear y reparar problemas en el disco duro                   |") # chkdsk
    print("|    4. Supervisar y registrar el rendimiento del sistema               |") # perfmon.msc
    print("|    5. Verificar problemas de memoria RAM                              |") # Memtest86? == Averiguar como portear para USB
    print("|    6. Winsat formal - Evaluar experiencia de Windows                  |") # winsat formal
    print("|    7. Abrir el Administrador de Dispositivos                          |") # devmgmt.msc
    print("|    8. Abrir CCleaner                                                  |") # Portear versión portatil para USB
    print("|    9. Abrir Defraggler                                                |") # Portear versión portatil para USB
    print("|   10. Salir del programa                                              |") # Ejecutar función de salida
    print("|   30. Automatizar prueba                                              |") # Hacer pruebas automaticas (ejecutar diagnósticos en orden)
    print("|                                                                       |")
    print("|-----------------------------------------------------------------------|\n")

def avisoImportante():
    print("\n|-----------------------------------------------------------------------|")
    print("|-                        ¡¡¡ IMPORTANTE !!!                           -|")
    print("|-                                                                     -|")
    print("|-----------------------------------------------------------------------|")
    print("|- RECUERDE EJECUTAR ESTE SCRIPT COMO ADMINISTRADOR ANTES DE CONTINUAR -|")
    print("|-----------------------------------------------------------------------|")
    print("|-                                                                     -|")
    print("|-----------------------------------------------------------------------|\n")

def salida():
    print("Saliendo del programa...\n")