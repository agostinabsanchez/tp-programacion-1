def validar_es_numerico(numero) -> bool:

    for caracter in numero:
        if caracter < "0" or caracter > "9":
            return False
        
    return True

def validar_es_texto(texto) -> bool:

    for caracter in texto:
        if caracter >= "0" and caracter <= "9":
            return False
        
    return True

def validar_existe_en_lista(lista : list, valor) -> bool:
    '''Esta función recibe como parametro una lista y un valor de busqueda. 
    Verifica si el valor existe en la lista y retorna un booleano.'''
    for i in range(len(lista)):
        if lista[i] == valor:
            return True

    return False