# busquedas.py
import time
import random

def busqueda_binaria_por_id(lista_productos_ordenada_por_id, id_buscado):
    """Busca un producto por su id usando búsqueda binaria."""
    indice_inicio = 0
    indice_final = len(lista_productos_ordenada_por_id) - 1

    while indice_inicio <= indice_final:
        indice_medio = (indice_inicio + indice_final) // 2
        producto_medio = lista_productos_ordenada_por_id[indice_medio]

        if producto_medio.id == id_buscado:
            return producto_medio
        elif producto_medio.id < id_buscado:
            indice_inicio = indice_medio + 1
        else:
            indice_final = indice_medio - 1

    return None  # No encontrado


def medir_tiempo_busqueda_binaria(lista_productos):
    """Mide el tiempo total de 10 búsquedas con id existentes y 10 sin existir usando búsqueda binaria."""
    lista_ordenada_por_id = sorted(lista_productos, key=lambda producto: producto.id)
    ids_existentes = random.sample([producto.id for producto in lista_ordenada_por_id], 10)
    max_id_actual = max(producto.id for producto in lista_ordenada_por_id)
    ids_no_existentes = [max_id_actual + i + 1 for i in range(10)]

    tiempo_inicio = time.perf_counter()
    for id_a_buscar in ids_existentes + ids_no_existentes:
        busqueda_binaria_por_id(lista_ordenada_por_id, id_a_buscar)
    tiempo_final = time.perf_counter()

    tiempo_total_busqueda = tiempo_final - tiempo_inicio

    print(f"\nTiempo total búsqueda binaria (10 existentes + 10 no existentes): {tiempo_total_busqueda:.6f} segundos")

def busqueda_lineal_por_nombre(lista_productos, subcadena_a_buscar):
    """Busca productos cuyo nombre contiene la subcadena dada (búsqueda lineal)."""
    subcadena_minuscula = subcadena_a_buscar.lower()
    productos_encontrados = []

    for producto in lista_productos:
        if subcadena_minuscula in producto.nombre.lower():
            productos_encontrados.append(producto)

    return productos_encontrados


def medir_tiempo_busqueda_lineal_por_nombre(lista_productos):
    """Mide el tiempo total de 10 búsquedas con subcadenas que existen y 10 que no existen."""
    nombres_productos = [producto.nombre for producto in lista_productos]
    subcadenas_que_dan_resultado = [nombre.split()[0] for nombre in nombres_productos[:10]]
    subcadenas_sin_resultado = [f"noexiste{i}" for i in range(10)]

    tiempo_inicio = time.perf_counter()
    for subcadena in subcadenas_que_dan_resultado + subcadenas_sin_resultado:
        busqueda_lineal_por_nombre(lista_productos, subcadena)
    tiempo_final = time.perf_counter()

    tiempo_total_busqueda = tiempo_final - tiempo_inicio

    print(f"\nTiempo total búsqueda lineal por nombre (10 con resultados + 10 sin resultados): {tiempo_total_busqueda:.6f} segundos")
