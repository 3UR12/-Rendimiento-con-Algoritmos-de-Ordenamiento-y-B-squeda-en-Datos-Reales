# main.py
from generador_productos import generar_lista_de_productos
from menu import ejecutar_menu_principal

def main():
    lista_productos = generar_lista_de_productos(50)
    ejecutar_menu_principal(lista_productos)

if __name__ == "__main__":
    main()
