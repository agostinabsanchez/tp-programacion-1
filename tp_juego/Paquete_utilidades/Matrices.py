# ordena bubble sort cuando la matriz tiene una entidad por fila
def bubble_sort_horizontal(matriz, posicion):
    n = len(matriz)
    for i in range(n):
        swapped = False #Bandera para detectar si hubo intercambios
        for j in range(0, n - i - 1):
            if matriz[j][posicion] > matriz[j+1][posicion]: # Si el elemento actual es mayor al siguiente
                matriz[j],matriz[j+1] = matriz[j+1], matriz[j] # Intercambiar
                swapped = True # Se realizo un intercambio

        if not swapped: #Si no hubo intercambios, el arreglo ya está ordenado
            break
    
    return matriz

# ordena bubble sort cuando la matriz tiene una entidad por columna
def bubble_sort_vertical_ascendente(matriz, criterio):
    for i in range(len(matriz[0])):
        for j in range(len(matriz[0])):
            if matriz[criterio][i] < matriz[criterio][j]:
                for k in range(len(matriz)):
                    aux = matriz[k][i]
                    matriz[k][i] = matriz[k][j]
                    matriz[k][j] = aux

# ordena bubble sort cuando la matriz tiene una entidad por columna
def bubble_sort_vertical_descendente(matriz, criterio):
    for i in range(len(matriz[0])):
        for j in range(len(matriz[0])):
            if matriz[criterio][i] > matriz[criterio][j]:
                for k in range(len(matriz)):
                    aux = matriz[k][i]
                    matriz[k][i] = matriz[k][j]
                    matriz[k][j] = aux
