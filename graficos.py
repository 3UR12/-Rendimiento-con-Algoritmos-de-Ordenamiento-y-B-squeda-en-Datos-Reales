import matplotlib.pyplot as plt
import os
import shutil

# Ruta de destino para guardar los gráficos
CARPETA_GUARDADO = r"C:\Users\jw818\Desktop\parcial 2\archivos"

# Crea la carpeta si no existe
os.makedirs(CARPETA_GUARDADO, exist_ok=True)

# Borra imágenes anteriores (.png) antes de guardar nuevas
for archivo in os.listdir(CARPETA_GUARDADO):
    if archivo.endswith(".png"):
        os.remove(os.path.join(CARPETA_GUARDADO, archivo))


def graficar_ordenamientos(resultados_ordenamiento):
    """
    Genera gráficos de barras para los tiempos de ordenamiento por cada criterio.
    """
    criterios = list(resultados_ordenamiento.keys())
    algoritmos = list(next(iter(resultados_ordenamiento.values())).keys())

    for criterio in criterios:
        tiempos = [resultados_ordenamiento[criterio][alg] for alg in algoritmos]

        plt.figure()
        plt.bar(algoritmos, tiempos, color='skyblue')
        plt.title(f"Tiempos de ordenamiento por '{criterio}'")
        plt.ylabel("Tiempo (segundos)")
        plt.xlabel("Algoritmo")
        nombre_archivo = f"grafico_ordenamiento_{criterio.replace(' ', '_').lower()}.png"
        ruta_archivo = os.path.join(CARPETA_GUARDADO, nombre_archivo)
        plt.savefig(ruta_archivo)
        plt.close()


def graficar_busquedas(resultados_busqueda):
    """
    Genera un gráfico de barras para comparar los tiempos de búsqueda.
    """
    tipos = list(resultados_busqueda.keys())
    tiempos = [resultados_busqueda[t] for t in tipos]

    plt.figure()
    plt.bar(tipos, tiempos, color='lightgreen')
    plt.title("Tiempos de búsqueda")
    plt.ylabel("Tiempo (segundos)")
    nombre_archivo = "grafico_busquedas.png"
    ruta_archivo = os.path.join(CARPETA_GUARDADO, nombre_archivo)
    plt.savefig(ruta_archivo)
    plt.close()
