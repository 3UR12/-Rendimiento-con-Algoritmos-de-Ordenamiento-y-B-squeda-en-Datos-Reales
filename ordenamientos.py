# ordenamientos.py
import time

def insertion_sort(lista_productos, funcion_clave):
    """Ordena la lista de productos usando Insertion Sort basado en la función_clave."""
    productos_ordenados = lista_productos.copy()  # No modificar lista original

    for indice_actual in range(1, len(productos_ordenados)):
        producto_actual = productos_ordenados[indice_actual]
        posicion = indice_actual

        # Mueve producto_actual hacia izquierda mientras sea menor que el anterior según funcion_clave
        while posicion > 0 and funcion_clave(productos_ordenados[posicion - 1]) > funcion_clave(producto_actual):
            productos_ordenados[posicion] = productos_ordenados[posicion - 1]
            posicion -= 1

        productos_ordenados[posicion] = producto_actual

    return productos_ordenados


def merge_sort(lista_productos, funcion_clave):
    """Ordena la lista de productos usando Merge Sort basado en la función_clave."""
    if len(lista_productos) <= 1:
        return lista_productos.copy()

    punto_medio = len(lista_productos) // 2

    lista_izquierda = merge_sort(lista_productos[:punto_medio], funcion_clave)
    lista_derecha = merge_sort(lista_productos[punto_medio:], funcion_clave)

    lista_ordenada = []
    indice_izquierda = 0
    indice_derecha = 0

    # Combina ambas listas ya ordenadas
    while indice_izquierda < len(lista_izquierda) and indice_derecha < len(lista_derecha):
        if funcion_clave(lista_izquierda[indice_izquierda]) <= funcion_clave(lista_derecha[indice_derecha]):
            lista_ordenada.append(lista_izquierda[indice_izquierda])
            indice_izquierda += 1
        else:
            lista_ordenada.append(lista_derecha[indice_derecha])
            indice_derecha += 1

    # Añade el resto de elementos que queden en alguna lista
    lista_ordenada.extend(lista_izquierda[indice_izquierda:])
    lista_ordenada.extend(lista_derecha[indice_derecha:])

    return lista_ordenada


def quick_sort(lista_productos, funcion_clave):
    """Ordena la lista de productos usando Quick Sort basado en la función_clave."""
    if len(lista_productos) <= 1:
        return lista_productos.copy()

    pivote_producto = lista_productos[0]
    lista_menores = [producto for producto in lista_productos[1:] if funcion_clave(producto) <= funcion_clave(pivote_producto)]
    lista_mayores = [producto for producto in lista_productos[1:] if funcion_clave(producto) > funcion_clave(pivote_producto)]

    return quick_sort(lista_menores, funcion_clave) + [pivote_producto] + quick_sort(lista_mayores, funcion_clave)


def medir_tiempo_de_ordenamiento(funcion_ordenamiento, lista_productos, funcion_clave):
    """Mide el tiempo que tarda en ordenar una lista usando la función de ordenamiento dada."""
    tiempo_inicio = time.perf_counter()
    lista_ordenada = funcion_ordenamiento(lista_productos, funcion_clave)
    tiempo_final = time.perf_counter()
    tiempo_total = tiempo_final - tiempo_inicio

    return tiempo_total, lista_ordenada
