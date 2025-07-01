from Funciones import *

while True:

    print("""MENU PRINCIPAL
          
1.- Registrar producto.
2.- Listar productos con stock.
3.- Eliminar producto por código.
4.- Salir
          """)

    seleccion = int(input("seleccione una opcion : "))

    match seleccion:
        case 1:
            registrar_p()
        case 2:
            listar_p()
        case 3:
            eliminar_p(codigo=input("ingrese codigo producto a eliminar : "))
        case 4:
            print("programa terminado...")
            break
        case _:
            print("Seleccion invalida")