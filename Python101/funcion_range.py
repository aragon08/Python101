#unfion range: range(a), range(a,b), range(a,b,c)
# tabla de multiplicar del 1 al 10

n = int(input('ingrese un numero: '))
for item in range(1,11):
    print(n, 'X',item,'=',n*item)