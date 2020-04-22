#arreglos
#iprimir por pantalla los numeros impares a 3

A = [1,5,8,9,30,9,13]
B = []
for item in A:
    if item > 3 and item % 2 != 0:
      B.append(item)
print(B) 