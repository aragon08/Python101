# tabla de multiplicar

n = int(input('ingrese la tabla que desea ver: : '))
i = 1

while i<=10:
  print(n, 'x', i, '=', n*i)
  #print(n * i)
  i = i + 1
print('tabla de multiplicar del: ', n)