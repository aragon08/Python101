#arrays (vectores)

n =  int(input('ingrese el tamaño del arreglo: '))
m =  int(input('ingrese el número de multiplos: '))
A = []
for item in range(0,n):
    A.append(item*m)

print(A)
 