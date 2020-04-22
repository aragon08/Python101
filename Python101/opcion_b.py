#opcion B (elif)

b = int(input('introduce un numero: '))
if b< 0:
    r = 'negativo'
elif b==0:
    r='neutro'
else:
        r = 'positivo'

print('el numero es: ', r)