#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
               #cla      0       1       2     3       4          5         6


productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
             'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
             '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
             '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050']}

#stock = {modelo: [precio, stock], ...]


stock = {'8475HD':  [387990,10],
         '2175HD':  [327990,4],
         'JjfFHD':  [424990,1],
         'fgdxFHD': [664990,21],
         '123FHD':  [290890,32],
         '342FHD':  [444990,7],
         'GF75HD':  [749990,2],
         'UWU131HD':[349990,1],}



def stock_marca(marca):
    for cla in productos:
        mar = productos [cla] [0]
        sto = stock [cla] [1]
        if mar == marca :
            print(f"MARCA {mar} STOCK {sto}")

#stock_marca(marca = str(input("Ingrese marca : ")))


def busqueda_precio(p_min : int, p_max : int):
    for cla in stock:
        pre = stock [cla] [0]
        mar = productos [cla] [0]
        if p_min <= pre <= p_max:
            print(f"${pre} MARCA {mar} MODELO {cla}")
    
#busqueda_precio(p_min=int(input("Ingrese precio minimo : ")) , p_max=int(input("Ingrese precio maximo : ")))


def ordenar_productos():
    for cla in productos:
        mod = cla
        mar = productos [cla] [0]
        ram = productos [cla] [2]
        mem = productos [cla] [4]  

        print(f"{mar} - {mod} - {ram} - {mem}")

#ordenar_productos()
