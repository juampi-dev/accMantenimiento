import time
import gui
import formal
import tempModule
import dxdiag
import sfc
import chkdsk
import perf
import devmgmt

welcomeFlag = True

def main():

    global welcomeFlag

    while True:

        #Inicialización y Bienvenida al programa
        if welcomeFlag:
            gui.bienvenida()
            time.sleep(2)
            gui.avisoImportante()
            time.sleep(1.5)
            welcomeFlag = False

        #Inicialización de menu principal
        gui.mostrar_menu()
        opcSeleccionada = None
        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            # Acción para dxdiag
            opcSeleccionada = "dxdiag"
            print("Ha seleccionado " + opcSeleccionada + ".\n")
            
            dxdiag.ejecutar_dxdiag()
            #LLAMAR FUNCION DESDE MODULO
        elif seleccion == "2":
            # Acción para sfc /scannow
            opcSeleccionada = "sfc /scannow"
            print("Ha seleccionado " + opcSeleccionada + ".\n")
            
            sfc.ejecutar_sfc_scannow()
            #LLAMAR FUNCION DESDE MODULO
        elif seleccion == "3":
            # Acción para chkdsk
            opcSeleccionada = "chkdsk"
            print("Ha seleccionado " + opcSeleccionada + ".\n")
            
            chkdsk.ejecutar_chkdsk()
            #LLAMAR FUNCION DESDE MODULO
        elif seleccion == "4":
            # Acción para perfmon.msc
            opcSeleccionada = "perfmon.msc"
            print("Ha seleccionado " + opcSeleccionada + ".\n")
            
            perf.ejecutar_perfmon_msc()
            #LLAMAR FUNCION DESDE MODULO
        elif seleccion == "5":
            # Acción para Memtest86
            opcSeleccionada = "Memtest86"
            print("Ha seleccionado " + opcSeleccionada + ".\n")
            
            tempModule.test(opcSeleccionada)
            #LLAMAR FUNCION DESDE MODULO
        elif seleccion == "6":
            # Acción para winsat formal
            opcSeleccionada = "winsat formal"
            print("Ha seleccionado " + opcSeleccionada + ".\n")
            
            formal.ejecutar_winsat_formal()
        elif seleccion == "7":
            # Acción para devmgmt.msc
            opcSeleccionada = "devmgmt.msc"
            print("Ha seleccionado " + opcSeleccionada + ".\n")
            
            devmgmt.ejecutar_devmgmt_msc()
            #LLAMAR FUNCION DESDE MODULO
        elif seleccion == "8":
            # Acción para abrir CCleaner Portable
            opcSeleccionada = "CCleaner Portable"
            print("Ha seleccionado " + opcSeleccionada + ".\n")
            
            tempModule.test(opcSeleccionada)
            #LLAMAR FUNCION DESDE MODULO
        elif seleccion == "9":
            # Acción para abrir Defraggler
            opcSeleccionada = "Defraggler"
            print("Ha seleccionado " + opcSeleccionada + ".\n")
            
            tempModule.test(opcSeleccionada)
            #LLAMAR FUNCION DESDE MODULO
        elif seleccion == "10":
            # Salir del programa
            gui.salida()
            break
        elif seleccion == "30":
            # Acción para iniciar pruebas y diagnósticos automáticos
            opcSeleccionada = "pruebas automáticas"
            print("Iniciando " + opcSeleccionada + "...\n")
            
            tempModule.test(opcSeleccionada)
            #LLAMAR FUNCION DESDE MODULO
        else:
            print("Selección no válida. Intente de nuevo.\n")
            
if __name__ == "__main__":
    main()