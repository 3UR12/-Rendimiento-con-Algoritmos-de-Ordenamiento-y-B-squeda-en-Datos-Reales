# Proyecto: Rendimiento con Algoritmos de Ordenamiento y Búsqueda en Datos Reales

## Descripción

Este proyecto simula la gestión de un catálogo de productos para una tienda en línea, implementando algoritmos de ordenamiento y búsqueda sobre datos reales generados aleatoriamente. Está desarrollado en Python y cumple con los requerimientos de la actividad académica.

Incluye funcionalidades de visualización en consola, medición y análisis de tiempos de ejecución, y generación de gráficos guardados en archivos PNG.

---

## Estructura del Proyecto

| Archivo                  | Descripción                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `producto.py`            | Clase que modela los atributos de un producto con ID único automático.                                     |
| `generador_productos.py` | Genera una lista de 50 productos con datos coherentes y aleatorios para pruebas.                           |
| `ordenamientos.py`       | Implementa 3 algoritmos de ordenamiento: Insertion Sort, Merge Sort y Quick Sort, con medición de tiempos. |
| `busquedas.py`           | Implementa búsqueda binaria por ID y búsqueda lineal por nombre, con medición de tiempos.                  |
| `presentador_tabla.py`   | Funciones para mostrar la lista de productos en formato tabular en consola.                                |
| `analisis_tiempos.py`    | Funciones para medir los tiempos de ejecución de los algoritmos de ordenamiento y búsqueda.                |
| `graficas.py`            | Funciones para graficar los resultados de los tiempos y guardar las imágenes en disco.                     |
| `menu.py`                | Menú interactivo para seleccionar opciones de mostrar, ordenar, buscar productos y análisis completo.      |
| `main.py`                | Punto de entrada que genera productos y lanza el menú principal.                                           |

---

## Cumplimiento de Instrucciones

### Parte 1: Modelado y Generación de Datos

* **Modelo Producto (`producto.py`)**: La clase incluye los atributos `id`, `nombre`, `precio`, `categoria`, `stock` y `calificacion_promedio`. El `id` se genera automáticamente y de forma única para cada producto.
* **Generación de Datos (`generador_productos.py`)**: Se crean 50 productos con valores aleatorios coherentes, asegurando diversidad en nombres, categorías y rangos de precios realistas.

### Parte 2: Ordenamiento de Productos

* **Algoritmos implementados (`ordenamientos.py`)**: Se incluyeron Insertion Sort, Merge Sort y Quick Sort.
* **Criterios de Ordenamiento**: Se permite ordenar por precio (ascendente) y por calificación promedio (descendente), usando funciones clave (`lambda`).
* **Medición de Tiempos (`analisis_tiempos.py`)**: Cada ordenamiento mide su tiempo de ejecución usando `time.perf_counter()`.
* **Menú Interactivo (`menu.py`)**: El usuario elige criterio y algoritmo para ordenar, y se muestra la lista ordenada junto con el tiempo de ejecución.

---

### Parte 3: Búsqueda de Productos

* **Búsqueda Binaria por ID (`busquedas.py`)**: La búsqueda binaria se realiza en la lista ordenada por ID, realizando 10 búsquedas con IDs existentes y 10 con IDs no existentes, midiendo el tiempo total.
* **Búsqueda Lineal por Nombre (`busquedas.py`)**: Se busca productos que contengan una subcadena dada, realizando 10 búsquedas con resultados y 10 sin resultados, midiendo el tiempo total.
* **Menú Interactivo (`menu.py`)**: Se permite buscar productos por ID o por nombre, mostrando resultados individuales en pantalla para búsquedas por ID y listados para búsquedas por nombre.

---

### Análisis Completo de Tiempos

* **Medición y presentación (`analisis_tiempos.py` y `menu.py`)**: Se ejecuta un análisis completo que mide tiempos de todos los algoritmos de ordenamiento y búsqueda, imprime tablas con resultados en consola y genera gráficos.
* **Gráficos (`graficas.py`)**: Los gráficos de barras para tiempos de ordenamiento y búsqueda se guardan automáticamente como imágenes PNG en la carpeta `archivos` dentro del proyecto. La carpeta se crea si no existe.
* **Actualización automática**: Al ejecutar el análisis completo varias veces, se eliminan los gráficos previos para evitar acumulación de archivos obsoletos.

---

## Uso

1. Clonar el repositorio:

   ```
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. Ejecutar el programa:

   ```
   python main.py
   ```

3. Seguir el menú para:

   * Mostrar productos
   * Ordenar productos según criterio y algoritmo
   * Buscar productos por ID o por nombre (subcadena)
   * Ejecutar análisis completo de tiempos (genera tablas y gráficos guardados)


## Reflexiones y Conclusiones

* **Ordenamiento:**

  * Los algoritmos eficientes como Merge Sort y Quick Sort mostraron mejores tiempos en comparación con Insertion Sort, especialmente a medida que crece el tamaño de la lista.
  * El uso de funciones clave (`lambda`) permitió adaptar los algoritmos para ordenar objetos complejos según diferentes atributos, facilitando la reutilización.

* **Búsqueda:**

  * La búsqueda binaria es mucho más eficiente que la lineal para búsquedas por ID, siempre que la lista esté ordenada por dicho criterio.
  * La búsqueda lineal por nombre es sencilla pero menos eficiente para listas grandes, ya que revisa secuencialmente todos los productos.
  * Para optimizar búsquedas por texto en aplicaciones reales, se recomiendan índices de texto completo, árboles de prefijos, o bases de datos especializadas.

* **Visualización y Reportes:**

  * La generación automática de tablas y gráficos facilita la interpretación y comparación de resultados.
  * Guardar los gráficos en archivos permite documentar el análisis y compartirlo fácilmente.

* **Manejo de Archivos:**

  * La creación dinámica de carpetas y el borrado automático de gráficos antiguos ayudan a mantener organizado el proyecto y evitan archivos obsoletos.

---

## Créditos

* **Autor:** \[3UR12]
* **Asignatura:** Estructuras de Datos y Algoritmos
* **Universidad:** Universidad Interamericana de Panamá



