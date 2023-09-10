from util import obtener_respuesta_valida

def test(opc):
    while True:

        print("ACÁ SE EJECUTARÍA EL CÓDIGO DENTRO DE " + opc + ".\n")

        # Navegacion
        respuesta = obtener_respuesta_valida(opc)
        if respuesta != "S":
            return  # Regresar al menú principal