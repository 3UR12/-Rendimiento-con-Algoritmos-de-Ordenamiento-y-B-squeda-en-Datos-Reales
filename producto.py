# producto.py

class Producto:
    contador_id_unico = 1  # Contador estático para asignar ID único a cada producto

    def __init__(self, nombre_producto, precio_producto, categoria_producto, stock_producto, calificacion_promedio_producto):
        self.id = Producto.contador_id_unico  # ID único para identificar el producto
        Producto.contador_id_unico += 1
        self.nombre = nombre_producto         # Nombre descriptivo del producto
        self.precio = precio_producto         # Precio en moneda local
        self.categoria = categoria_producto   # Categoría a la que pertenece el producto
        self.stock = stock_producto           # Cantidad disponible en inventario
        self.calificacion_promedio = calificacion_promedio_producto  # Calificación promedio de usuarios (1.0 - 5.0)

    def __repr__(self):
        # Representación textual clara para debug o impresión rápida
        return (
            f"ID:{self.id} - {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Categoría: {self.categoria} | "
            f"Stock: {self.stock} | "
            f"Calificación: {self.calificacion_promedio}★"
        )
