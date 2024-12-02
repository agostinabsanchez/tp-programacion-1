from .Validaciones import *


def pedir_numero_entero(mensaje : str) -> int:
    '''Esta función pide que se ingrese un número y valida que el valor ingresado sea numérico, retornando un número entero.'''
    numero = input(f"{mensaje}") 

    while validar_es_numerico(numero)== False:
        numero = input(f"Error, el valor ingresado no es un número. {mensaje}")

    return int(numero)

def pedir_numero_entero_con_rango(mensaje : str, minimo, maximo) -> int:
    numero = pedir_numero_entero(mensaje)

    while numero < minimo or numero > maximo:
        print(f"Numero ingresado fuera de rango.")
        numero = pedir_numero_entero_con_rango(mensaje,minimo,maximo)
    
    return numero


def pedir_texto(mensaje : str) -> str:
    '''Esta función pide que se ingrese un texto alfanumérico y retorna el mismo.'''
    texto = input(f"{mensaje}")

    return texto

def pedir_texto_numerico(mensaje : str) -> str:
    '''Esta función pide que se ingrese un texto conformado solo por números y retorna el mismo.'''
    texto = input(f"{mensaje}")

    while validar_es_numerico(texto)== False:
        texto = input(f"Error, el valor ingresado no es un número. {mensaje}")  
    return texto

def pedir_texto_solo_letras(mensaje : str) ->str:
    '''Esta función pide que se ingrese un texto, valida que contenga sólo letras y retorna el mismo.'''
    texto = input(f"{mensaje}")

    while validar_es_texto(texto) == False:
        texto = input(f"Error, el valor ingresado no es un texto. {mensaje}")

    return texto


# def pedir_numero_flotante(mensaje : str) -> float:
#     '''Esta función pide un número y valida que el valor ingresado sea numérico, retornando un número flotante.'''
#     numero = input(f"{mensaje}") 

#     while validar_es_numerico(numero)== False:
#         numero = input(f"Error, el valor ingresado no es un número. {mensaje}")

#     return float(numero)
#falla porque el "validar_es_numerico" toma el caracter punto y devuelve False.

