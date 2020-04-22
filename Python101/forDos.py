# mostrar la suma de los n primeros numeros

n = int(input('ingrese un numero: '))
suma = 0
for item in range(1,n+1):
    suma = suma + item
print(suma)