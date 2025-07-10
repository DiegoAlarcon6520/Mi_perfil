from funciones import *
from os import system
from msvcrt import getch

while True:
    print("""*** MENU PRINCIPAL ***
1. Stock marca.
2. Búsqueda por precio.
3. Listado de productos.
4. Salir.""")
    

    try:
        opcion = int(input("Ingrese opcion : "))
        match opcion:
            case 1:
                try:
                    stock_marca(marca = str(input("Ingrese marca : ")))
                    print("presione una tecla para continuar ")
                    getch()
                    system("cls")
                except:
                    system("cls")
                    print(ValueError)
                    print("Debe ingresar una opcion valida ")
                    print("presione una tecla para continuar ")
                    getch()
                    system("cls")
            case 2:
                try:
                    busqueda_precio(p_min=int(input("Ingrese precio minimo : ")) , p_max=int(input("Ingrese precio maximo : ")))
                    print("presione una tecla para continuar ")
                    getch()
                    system("cls")
                except:
                    system("cls")
                    print(ValueError)
                    print("Debe ingresar una opcion valida ")
                    print("presione una tecla para continuar ")
                    getch()
                    system("cls")
            case 3:
                system("cls")
                ordenar_productos()
                print("presione una tecla para continuar ")
                getch()
                system("cls")
            case 4:
                system("cls")
                print("PROGRAMA FINALIZADO")
                break
            case _:
                system("cls")
                print("debe ingresar una opcion valida")
                print("presione una tecla para continuar ")
                getch()
                system("cls")
    except:
        system("cls")
        print("debe ingresar una opcion valida")
        print("presione una tecla para continuar ")
        getch()
        system("cls")