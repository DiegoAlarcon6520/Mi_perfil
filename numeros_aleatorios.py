import random

#lista
numeros = []

#guardar 100 numeros aleatorios
for i in range(100):
    numeros.append(random.randint(0,10))

#mostrar lista    
print(numeros)


cont = 0
for i in range(len(numeros)):
    if i%2==0 and i != 0:
        print(f"Pos: {i}   Num: {numeros[i]}")
        if numeros[i] < numeros[i+1]:
            cont += 1
            print(cont)
