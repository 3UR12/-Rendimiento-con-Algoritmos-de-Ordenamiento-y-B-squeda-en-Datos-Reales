# Proyecto: Rendimiento con Algoritmos de Ordenamiento y Búsqueda en Datos Reales

## Descripción

Este proyecto simula la gestión de un catálogo de productos para una tienda en línea, implementando algoritmos de ordenamiento y búsqueda sobre datos reales generados aleatoriamente. Está desarrollado en Python y cumple con los requerimientos de la actividad académica.

---

## Estructura del Proyecto

| Archivo                  | Descripción                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `producto.py`            | Clase `Producto` que modela los atributos de un producto con ID único automático.                          |
| `generador_productos.py` | Genera una lista de 50 productos con datos coherentes y aleatorios para pruebas.                           |
| `ordenamientos.py`       | Implementa 3 algoritmos de ordenamiento: Insertion Sort, Merge Sort y Quick Sort, con medición de tiempos. |
| `busquedas.py`           | Implementa búsqueda binaria por ID y búsqueda lineal por nombre, con medición de tiempos.                  |
| `presentador_tabla.py`   | Funciones para mostrar la lista de productos en formato tabular en consola.                                |
| `menu.py`                | Menú interactivo para seleccionar opciones de mostrar, ordenar y buscar productos.                         |
| `main.py`                | Punto de entrada que genera productos y lanza el menú principal.                                           |

---

## Cumplimiento de Instrucciones

### Parte 1: Modelado y Generación de Datos

* **Modelo Producto (`producto.py`)**: La clase `Producto` incluye los atributos `id`, `nombre`, `precio`, `categoria`, `stock`, y `calificacion_promedio`, generando un ID único incremental para cada instancia.
* **Generación de Datos (`generador_productos.py`)**: Se crean 50 productos con valores aleatorios pero coherentes, asegurando diversidad en nombres, categorías y rangos de precios realistas.

### Parte 2: Ordenamiento de Productos

* **Algoritmos Implementados (`ordenamientos.py`)**: Se incluyeron Insertion Sort, Merge Sort y Quick Sort.
* **Criterios de Ordenamiento**: Se permite ordenar por `precio` (ascendente) y por `calificacion_promedio` (descendente), usando funciones clave (`lambda`).
* **Medición de Tiempos**: Cada ordenamiento mide su tiempo de ejecución con `time.perf_counter()`.
* **Menú Interactivo (`menu.py`)**: El usuario elige criterio y algoritmo para ordenar, y se muestra la lista ordenada con el tiempo de ejecución.

### Parte 3: Búsqueda de Productos

* **Búsqueda Binaria por ID (`busquedas.py`)**: La búsqueda binaria se realiza en la lista ordenada por ID, realizando 10 búsquedas con IDs existentes y 10 con IDs no existentes, midiendo el tiempo total.
* **Búsqueda Lineal por Nombre (`busquedas.py`)**: Se busca productos que contengan una subcadena dada, realizando 10 búsquedas con resultados y 10 sin resultados, midiendo el tiempo.
* **Análisis**: En consola se imprime una explicación clara sobre las diferencias de rendimiento y las ventajas de cada método, además de sugerencias para optimización en producción.

---

## Uso

1. Clonar el repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. Ejecutar el programa:

```bash
python main.py
```

3. Seguir el menú para mostrar productos, ordenar o buscar según se desee.

---

## Reflexiones y Conclusiones

* **Ordenamiento**: Los algoritmos eficientes como Merge Sort y Quick Sort mostraron mejores tiempos comparados con Insertion Sort, especialmente en listas mayores.
* **Búsqueda**: La búsqueda binaria es mucho más eficiente que la lineal al trabajar con datos ordenados, lo que justifica ordenar previamente por ID para búsquedas rápidas.
* **Búsqueda por Texto**: La búsqueda lineal por subcadena es sencilla pero ineficiente para catálogos grandes; para entornos productivos, se recomienda implementar índices de texto completo o estructuras de datos específicas como árboles de prefijos.
* **Trabajar con objetos complejos**: La implementación de funciones clave (`lambda`) facilita la reutilización de algoritmos para diferentes criterios, adaptándose a objetos complejos más allá de valores primitivos.

---

## Créditos

* Autor: \[3UR12]
* Proyecto para la asignatura de Estructuras de Datos y Algoritmos
* Universidad Interamericana de Panamá
