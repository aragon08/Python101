# arreglos
#calcular 10 numeros aleatorios

import random

def vector_aleatorio(n):
    vector = [0]* n
    for item in range(n):
        vector[item] = random.randint(0,10)
    return vector

print('ingrese cuantos numeros aleatorios desea obtener: ')
n =  int(input())

r = vector_aleatorio(n)
print(r)