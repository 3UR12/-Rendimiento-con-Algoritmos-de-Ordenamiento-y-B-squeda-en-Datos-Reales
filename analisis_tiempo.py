# analisis_tiempos.py
# Este módulo se encarga de medir el rendimiento de los algoritmos de ordenamiento y búsqueda,
# devolviendo los resultados de tiempo para ser presentados en tablas y gráficos.

import time
import random
from ordenamientos import insertion_sort, merge_sort, quick_sort, medir_tiempo_de_ordenamiento
from busquedas import busqueda_binaria_por_id, busqueda_lineal_por_nombre

def medir_tiempos_de_ordenamiento(lista_de_productos):
    """
    Mide el tiempo de ejecución de tres algoritmos de ordenamiento con dos criterios distintos:
    - Por precio (ascendente)
    - Por calificación promedio (descendente)

    Retorna un diccionario con los tiempos de cada combinación.
    """
    # Criterios de ordenamiento con funciones lambda como claves
    criterios = [
        ("Precio ascendente", lambda producto: producto.precio),
        ("Calificación descendente", lambda producto: -producto.calificacion_promedio)
    ]

    # Algoritmos de ordenamiento implementados
    algoritmos = [
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]

    resultados_de_tiempos = {}

    for nombre_criterio, funcion_clave in criterios:
        resultados_de_tiempos[nombre_criterio] = {}

        for nombre_algoritmo, funcion_ordenamiento in algoritmos:
            tiempo_ejecucion, _ = medir_tiempo_de_ordenamiento(
                funcion_ordenamiento,
                lista_de_productos,
                funcion_clave
            )
            resultados_de_tiempos[nombre_criterio][nombre_algoritmo] = tiempo_ejecucion

    return resultados_de_tiempos


def medir_tiempos_de_busqueda(lista_de_productos):
    """
    Mide el tiempo total de ejecución de dos tipos de búsqueda:
    - Búsqueda binaria por ID (10 éxitos y 10 fallos)
    - Búsqueda lineal por nombre (10 éxitos y 10 fallos)

    Retorna un diccionario con los tiempos de ambas búsquedas.
    """
    # Ordenamos la lista por ID para aplicar búsqueda binaria correctamente
    lista_ordenada_por_id = sorted(lista_de_productos, key=lambda producto: producto.id)

    # Seleccionamos 10 IDs existentes aleatorios
    ids_existentes = random.sample([producto.id for producto in lista_ordenada_por_id], 10)

    # Generamos 10 IDs que no existen (mayores que el máximo actual)
    maximo_id = max(producto.id for producto in lista_ordenada_por_id)
    ids_no_existentes = [maximo_id + i + 1 for i in range(10)]

    # Medimos tiempo total de búsqueda binaria (20 búsquedas)
    tiempo_inicio_binaria = time.perf_counter()
    for id_a_buscar in ids_existentes + ids_no_existentes:
        busqueda_binaria_por_id(lista_ordenada_por_id, id_a_buscar)
    tiempo_total_binaria = time.perf_counter() - tiempo_inicio_binaria

    # Subcadenas que deberían coincidir (primeras palabras de nombres reales)
    nombres_existentes = [producto.nombre for producto in lista_de_productos]
    subcadenas_existentes = [nombre.split()[0] for nombre in nombres_existentes[:10]]

    # Subcadenas que no existen en ningún nombre
    subcadenas_falsas = [f"noexiste{i}" for i in range(10)]

    # Medimos tiempo total de búsqueda lineal (20 búsquedas)
    tiempo_inicio_lineal = time.perf_counter()
    for subcadena in subcadenas_existentes + subcadenas_falsas:
        busqueda_lineal_por_nombre(lista_de_productos, subcadena)
    tiempo_total_lineal = time.perf_counter() - tiempo_inicio_lineal

    # Diccionario de resultados finales
    resultados_busquedas = {
        "Búsqueda Binaria por ID": tiempo_total_binaria,
        "Búsqueda Lineal por Nombre": tiempo_total_lineal
    }

    return resultados_busquedas
