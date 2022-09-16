def maxheapify(array, tamaño, nodo_padre):
    # Declarando los nodos.
    nodo_izq = 2 * nodo_padre + 1
    nodo_der = 2 * nodo_padre + 2
    nodo_grande = nodo_padre

    # Buscando el nodo más grande.
    if nodo_izq < tamaño and array[nodo_izq] > array[nodo_grande]:
        nodo_grande = nodo_izq
    if nodo_der < tamaño and array[nodo_der] > array[nodo_grande]:
        nodo_grande = nodo_der

    # Si el nodo padre no es el más grande, intercambiarlo por el más grande y ordenar el heap.
    if nodo_grande != nodo_padre:
        array[nodo_padre], array[nodo_grande] = array[nodo_grande], array[nodo_padre]
        maxheapify(array, tamaño, nodo_grande)


def heapsort(array):
    tamaño = len(array)

    # Creando max heap.
    for i in range((tamaño // 2) -1, -1, -1):
        maxheapify(array, tamaño, i)
    
    # Intercambiando el elemento más grande por el último y ordenando el heap desde la raíz.
    for i in range(tamaño-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        maxheapify(array, i, 0)
    

# Ejemplo:
#
# matriz1 = [4, 77, 22, 1, 17, 8, 99]
#
# heapsort(matriz1)
#
# print(matriz1)