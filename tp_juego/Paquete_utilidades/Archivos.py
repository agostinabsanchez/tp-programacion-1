def leer_list_diccionarios(ruta: str, separador: str) -> list:
    lista_retorno = []

    with open(ruta, "r+") as archivo:
        linea_claves = archivo.readline()
        lista_lineas = archivo.readlines()
    
    claves = linea_claves.strip().split(separador)

    for linea in lista_lineas:
        linea_sin_saltos = linea.strip()
        linea_separada = linea_sin_saltos.split(separador)
        diccionario = {}
        for i in range(len(claves)):
            diccionario_agregar_dato(diccionario, claves[i], linea_separada[i])

        lista_retorno.append(diccionario)
    
    return lista_retorno

def diccionario_agregar_dato(diccionario: dict, clave: str, valor: any)->bool:
    claves = diccionario.keys()
    if clave in claves:
        return False
    else: 
        diccionario[clave] = valor
        return True

def escribir_diccionario(ruta:str, diccionario: dict, separador : str):

    with open(ruta, "a") as archivo:
        claves = diccionario.keys()
        lineas = "\n"

        for clave in claves:
            lineas += str(diccionario[clave]) + separador
        lineas = lineas[:len(lineas)-1]

        archivo.writelines(lineas)