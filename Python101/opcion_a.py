#opcion A (if - else)

a = int(input('ingrese n numero: '))
if a<0:
    r = 'negativo'
else:
    if a==0:
        r = 'neutro'
    else:
        r = 'positivo'

print('el numero es: ', r)