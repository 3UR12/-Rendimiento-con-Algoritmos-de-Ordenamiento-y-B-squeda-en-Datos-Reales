# generador_productos.py
import random
from producto import Producto

# Diccionario que asocia nombre base de producto con su categoría real
productos_con_categoria = {
    "Camisa": "Ropa",
    "Pantalón": "Ropa",
    "Laptop": "Electrónica",
    "Libro": "Libros",
    "Taza": "Hogar",
    "Mouse": "Electrónica",
    "Silla": "Hogar",
    "Zapatos": "Ropa",
    "Auriculares": "Electrónica",
    "Lámpara": "Hogar"
}

# Rango de precios coherente según categoría
rango_precios_por_categoria = {
    "Electrónica": (50.0, 1500.0),
    "Ropa": (10.0, 200.0),
    "Libros": (5.0, 100.0),
    "Hogar": (15.0, 500.0)
}

def generar_lista_de_productos(cantidad_productos=50):
    """Genera productos con nombre, categoría y precio coherentes."""
    lista_productos_generados = []

    nombres_base_productos = list(productos_con_categoria.keys())

    for _ in range(cantidad_productos):
        nombre_base = random.choice(nombres_base_productos)
        categoria_correcta = productos_con_categoria[nombre_base]
        rango_precio = rango_precios_por_categoria[categoria_correcta]
        precio_aleatorio = round(random.uniform(rango_precio[0], rango_precio[1]), 2)
        stock_aleatorio = random.randint(0, 100)
        calificacion_aleatoria = round(random.uniform(1.0, 5.0), 1)
        nombre_completo = f"{nombre_base} #{random.randint(1, 100)}"

        producto_nuevo = Producto(
            nombre_producto=nombre_completo,
            precio_producto=precio_aleatorio,
            categoria_producto=categoria_correcta,
            stock_producto=stock_aleatorio,
            calificacion_promedio_producto=calificacion_aleatoria
        )

        lista_productos_generados.append(producto_nuevo)

    return lista_productos_generados
