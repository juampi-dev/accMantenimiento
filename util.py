#MODULO DE NAVEGABILIDAD ENTRE SUBPROGRAMAS

def obtener_respuesta_valida(opc):
    while True:
        respuesta = input("¿Desea ejecutar nuevamente [" + opc + "]? (S/N): \n").strip().upper()
        if respuesta == "S" or respuesta == "N":
            return respuesta
        else:
            print("Respuesta no válida. Por favor, ingrese 'S' o 'N'.\n")
