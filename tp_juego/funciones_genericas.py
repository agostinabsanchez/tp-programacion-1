import random
import pygame 

def obtener_fuente(size: int):
    return pygame.font.Font("tp_juego/fonts/Jaro-Regular.ttf", size)

def criterio_numero_positivo(numero):
    return numero > 0

def modificar_dato(diccionario_jugador:dict, clave:str, nuevo_dato, criterio)->bool:
    claves = diccionario_jugador.keys()
    for elemento in claves: 
        if elemento == clave and ( criterio == None or criterio(nuevo_dato) == True):
            diccionario_jugador[clave] = nuevo_dato
            return True
    return False

def modificar_vidas(diccionario_jugador:dict, clave:str, vida_nueva:int)->bool:
    return modificar_dato(diccionario_jugador, clave, vida_nueva, criterio_numero_positivo)

def modificar_puntaje(diccionario_jugador:dict, clave:str, nuevo_puntaje:int)->bool:
    return modificar_dato(diccionario_jugador, clave, nuevo_puntaje, criterio_numero_positivo)

def modificar_estadistica_jugador(usuario_modificar:dict, clave:str, valor:any)->bool:
    return modificar_dato(usuario_modificar, clave, valor, None)

def generar_respuesta_aleatoria(minimo:int, maximo:int)->int:
    return random.randint(minimo, maximo)

def mezclar_lista(lista_elementos:list)->bool:
    for i in range(len(lista_elementos)- 1 ):
        numero_aleatorio = generar_respuesta_aleatoria(0, (len(lista_elementos)-1))
        if numero_aleatorio != i:
            aux = lista_elementos[i]
            lista_elementos[i] = lista_elementos[numero_aleatorio]
            lista_elementos[numero_aleatorio] = aux
    return True

def obtener_elemento_aleatorio(lista_elementos:list)->any:
    if lista_elementos:
        return random.choice(lista_elementos)
    else: 
        return None

def mostrar_dato(diccionario:dict, clave:str)->bool:
    claves = diccionario.keys()
    if clave not in claves:
        return False
    else:
        print(diccionario[clave])
        return True

def obtener_dato(diccionario:dict, clave:str)->any:
    claves = diccionario.keys()
    if clave not in claves:
        return None
    else:
        return diccionario[clave]

def guardar_puntuacion(lista_rankings:list, diccionario_jugador:int)->bool:
    claves = diccionario_jugador.keys()
    if "Nombre" in claves and "Puntaje" in claves:
        for registro in lista_rankings:
            if registro["Nombre"] == diccionario_jugador["Nombre"] and registro["Puntaje"] == diccionario_jugador["Puntaje"]:
                return False
            else:
                lista_rankings.append(diccionario_jugador)
                return True
    else:
        return False

def ordenar_lista(lista: list, criterio) -> bool:
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if criterio(lista[i], lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return True

def ordenar_lista_dic(lista: list, criterio, clave) -> bool:
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):

            if criterio(lista[i][clave], lista[j][clave]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    return True

def funcion_criterio_desc_numerico(valor1, valor2) -> bool:
    return int(valor1) < int(valor2)

def funcion_criterio_desc_texto(valor1, valor2) -> bool:
    return valor1 < valor2

def ordenar_por_criterio(lista_rankings:list, criterio, clave: str)->bool:
    return ordenar_lista(lista_rankings, lambda x,y: criterio(x[clave], y[clave]))

def obtener_imagen_escala(imagen, ancho, alto):
    return pygame.transform.scale(imagen,(ancho, alto))
