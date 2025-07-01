#a) El código no debe estar registrado previamente.
#b) El nombre debe tener al menos 3 caracteres alfabéticos.
#c) El stock debe ser un número entero mayor o igual a 0.
#d) El precio debe ser un número mayor a 0.

#lista = [{"Codigo": codigo, "Nombre" : nombre, "Stock" : stock, "Precio" : precio,}]

codigo = any
nombre = any
stock = any
precio = any

lista = []

def registrar_p():
    while True:
        try:
            codigo = input("ingrese codigo de producto : ")
            if codigo in lista:
                print("codigo ya registrado")
                codigo = any
                break
            
            nombre = input("ingrese nombre producto : ")
            if len(nombre) < 3:
                print("el nombre debe tener 3  letras al menos")
                nombre = any
                break
            
            stock = int(input("ingrese cantidad de Stock : "))
            if stock < 0:
                print("el stock debe ser mayor o igual a 0")
                stock = any
                break

            precio = int(input("ingrese precio : "))
            if precio < 1:
                print("el precio debe ser mayor que 0")
                precio = any
                break

            if codigo and nombre and stock and precio != any:
                producto = {"Codigo": codigo, "Nombre" : nombre, "Stock" : stock, "Precio" : precio,}
                print("Producto registrado con exito")
                lista.append(producto)
            else: print("ingresos invalidos")

        except Exception as error:
            print(error)
        return producto

def listar_p():
    print("productos con Stock :")
    print(lista)

def eliminar_p(codigo):
    if codigo == codigo in lista:
        lista.pop(codigo)
        print("producto eliminado con exito")
    else:
        print("no se encontro codigo de producto")