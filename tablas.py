def imprimir_tabla_ordenamientos(resultados_ordenamiento):
    print("\nTiempos de Ordenamiento (segundos):")
    criterios = list(resultados_ordenamiento.keys())
    algoritmos = list(next(iter(resultados_ordenamiento.values())).keys())

    encabezado = "Criterio \\ Algoritmo".ljust(25) + "".join(a.ljust(20) for a in algoritmos)
    print(encabezado)
    print("-" * len(encabezado))

    for criterio in criterios:
        fila = criterio.ljust(25)
        for algoritmo in algoritmos:
            tiempo = resultados_ordenamiento[criterio][algoritmo]
            fila += f"{tiempo:.6f}".ljust(20)
        print(fila)

def imprimir_tabla_busquedas(resultados_busqueda):
    print("\nTiempos de Búsqueda (segundos):")
    for tipo, tiempo in resultados_busqueda.items():
        print(f"{tipo.ljust(25)}: {tiempo:.6f}")




