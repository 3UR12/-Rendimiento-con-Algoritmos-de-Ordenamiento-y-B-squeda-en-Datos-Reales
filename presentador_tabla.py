# presentador_tabla.py

def mostrar_lista_de_productos_como_tabla(lista_productos):
    """Imprime la lista de productos en formato tabla con columnas alineadas y formato uniforme."""

    # Encabezado con nombres de columnas y espacios para alineación
    encabezado_tabla = f"{'ID':<4} {'Nombre':<25} {'Precio':<10} {'Categoría':<15} {'Stock':<6} {'Calificación'}"
    separador_tabla = "-" * len(encabezado_tabla)

    print(encabezado_tabla)
    print(separador_tabla)

    # Recorre cada producto e imprime sus atributos con formato alineado
    for producto in lista_productos:
        print(
            f"{producto.id:<4} "
            f"{producto.nombre:<25} "
            f"${producto.precio:<9.2f} "
            f"{producto.categoria:<15} "
            f"{producto.stock:<6} "
            f"{producto.calificacion_promedio:.1f}★"  # Formato uniforme con 1 decimal
        )
