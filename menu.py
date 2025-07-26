# menu.py
from presentador_tabla import mostrar_lista_de_productos_como_tabla
from ordenamientos import insertion_sort, merge_sort, quick_sort, medir_tiempo_de_ordenamiento
from busquedas import medir_tiempo_busqueda_binaria, medir_tiempo_busqueda_lineal_por_nombre
from tablas import  imprimir_tabla_ordenamientos, imprimir_tabla_busquedas
from graficos import graficar_ordenamientos, graficar_busquedas
from analisis_tiempo import medir_tiempos_de_ordenamiento, medir_tiempos_de_busqueda
from busquedas import busqueda_binaria_por_id, busqueda_lineal_por_nombre

def mostrar_menu_principal():
    """Imprime el menú principal con las opciones disponibles."""
    print("\n----- Menú Principal -----")
    print("1. Mostrar lista de productos")
    print("2. Ordenar productos")
    print("3. Buscar productos")
    print("4. Ejecutar análisis completo de tiempos")
    print("5. Salir")

def menu_de_ordenamiento(lista_productos):
    """Permite al usuario seleccionar criterio y algoritmo de ordenamiento y muestra el resultado."""
    criterios_de_orden = [
        # Uso de lambda para crear función clave para ordenar por precio ascendente
        ("Precio ascendente", lambda producto: producto.precio),
        # Uso de lambda para ordenar por calificación descendente (negativo para invertir orden)
        ("Calificación descendente", lambda producto: -producto.calificacion_promedio)
    ]

    algoritmos_de_orden = [
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]

    # Solicitar y validar opción de criterio de ordenamiento
    while True:
        print("\nSeleccione el criterio para ordenar:")
        for indice, (nombre_criterio, _) in enumerate(criterios_de_orden, start=1):
            print(f"{indice}. {nombre_criterio}")
        try:
            opcion_criterio = int(input("Opción: ")) - 1
            if opcion_criterio not in range(len(criterios_de_orden)):
                print(f"Opción inválida. Por favor elige un número entre 1 y {len(criterios_de_orden)}.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

    # Solicitar y validar opción de algoritmo de ordenamiento
    while True:
        print("\nSeleccione el algoritmo de ordenamiento:")
        for indice, (nombre_algo, _) in enumerate(algoritmos_de_orden, start=1):
            print(f"{indice}. {nombre_algo}")
        try:
            opcion_algoritmo = int(input("Opción: ")) - 1
            if opcion_algoritmo not in range(len(algoritmos_de_orden)):
                print(f"Opción inválida. Por favor elige un número entre 1 y {len(algoritmos_de_orden)}.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

    funcion_clave_seleccionada = criterios_de_orden[opcion_criterio][1]
    funcion_orden_seleccionada = algoritmos_de_orden[opcion_algoritmo][1]
    nombre_criterio_seleccionado = criterios_de_orden[opcion_criterio][0]
    nombre_algoritmo_seleccionado = algoritmos_de_orden[opcion_algoritmo][0]

    # Medir tiempo y obtener lista ordenada
    tiempo_ejecucion, lista_productos_ordenada = medir_tiempo_de_ordenamiento(
        funcion_orden_seleccionada,
        lista_productos,
        funcion_clave_seleccionada
    )

    print(f"\nProductos ordenados por '{nombre_criterio_seleccionado}' usando '{nombre_algoritmo_seleccionado}' en {tiempo_ejecucion:.6f} segundos:")
    mostrar_lista_de_productos_como_tabla(lista_productos_ordenada)

from busquedas import busqueda_binaria_por_id, busqueda_lineal_por_nombre
from presentador_tabla import mostrar_lista_de_productos_como_tabla

def menu_de_busqueda(lista_productos):
    while True:
        print("\nOpciones de búsqueda:")
        print("1. Buscar producto por ID")
        print("2. Buscar productos por nombre")
        print("3. Volver al menú principal")

        opcion = input("Selecciona opción: ").strip()
        if opcion == "1":
            try:
                id_buscado = int(input("Ingrese el ID del producto a buscar: "))
            except ValueError:
                print("ID inválido, debe ser un número entero.")
                continue
            lista_ordenada = sorted(lista_productos, key=lambda p: p.id)
            resultado = busqueda_binaria_por_id(lista_ordenada, id_buscado)
            if resultado:
                print("\nProducto encontrado:")
                mostrar_lista_de_productos_como_tabla([resultado])
            else:
                print(f"\nNo se encontró producto con ID {id_buscado}.")

        elif opcion == "2":
            subcadena = input("Ingrese la subcadena para buscar en el nombre: ").strip()
            resultados = busqueda_lineal_por_nombre(lista_productos, subcadena)
            if resultados:
                print(f"\nSe encontraron {len(resultados)} producto(s) con '{subcadena}':")
                mostrar_lista_de_productos_como_tabla(resultados)
            else:
                print(f"\nNo se encontraron productos que contengan '{subcadena}'.")

        elif opcion == "3":
            break
        else:
            print("Opción inválida, intente de nuevo.")


def ejecutar_analisis_completo(lista_productos):
    print("\nEjecutando análisis completo de tiempos...")

    resultados_orden = medir_tiempos_de_ordenamiento(lista_productos)
    resultados_busq = medir_tiempos_de_busqueda(lista_productos)

    imprimir_tabla_ordenamientos(resultados_orden)
    imprimir_tabla_busquedas(resultados_busq)

    graficar_ordenamientos(resultados_orden)
    graficar_busquedas(resultados_busq)

    print("Análisis completo finalizado. Gráficos guardados en archivos PNG.\n")

def ejecutar_menu_principal(lista_productos):
    """Ejecuta el menú principal con todas las opciones hasta que el usuario decida salir."""
    while True:
        mostrar_menu_principal()
        try:
            opcion_seleccionada = int(input("Selecciona una opción: "))
            if opcion_seleccionada not in [1, 2, 3, 4,5]:
                print("Opción inválida, por favor intenta de nuevo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")
            continue

        if opcion_seleccionada == 1:
            mostrar_lista_de_productos_como_tabla(lista_productos)
        elif opcion_seleccionada == 2:
            menu_de_ordenamiento(lista_productos)
        elif opcion_seleccionada == 3:
            menu_de_busqueda(lista_productos)
        elif opcion_seleccionada == 4:
            ejecutar_analisis_completo(lista_productos)
        elif opcion_seleccionada == 5:
            print("Saliendo del programa...")
            break
