# mostrar la suma de n numeros

n = int(input('ingresa un numero: '))
suma = 0
i = 1
while i<=n:
  suma = suma + i
  i = i + 1
print('la suma de los numeros hasta ',n,' es: ',suma)
