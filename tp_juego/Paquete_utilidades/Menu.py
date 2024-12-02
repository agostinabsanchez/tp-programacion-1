from Paquete_utilidades.Input import pedir_numero_entero

def imprimir_menu (titulo: str, opciones: list, con_opcion_salida: bool) -> int:
    '''Esta función imprime una lista de opciones y retorna el índice de la opción elegida.
        Si la variable con_opcion_salida == True agrega la opción de salida con valor 0.'''
    print(titulo)

    for i in range(len(opciones)):
        print(f"{i+1}- {opciones[i]}")

    if con_opcion_salida: 
        print(f"0- Salir")

    opcion = -1

    while (con_opcion_salida and opcion < 0) or (con_opcion_salida == False and opcion <= 0) or opcion > len(opciones):

        opcion = pedir_numero_entero("Ingrese una opción del menú: ")

    return opcion
