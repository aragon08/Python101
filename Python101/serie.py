#generar los multiplos de 3
# m = interruptor
n = int(input('ingrese un numero: '))
m = 3
for item in range(1, n+1):
    print(m, end= '-')
    m = m + 3