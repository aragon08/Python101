#Factorial

n = int(input('ingrese un numero: '))
if n<=0:
    print('ingrese un numero positivo')
else:
    factorial = 1
    for item in range(1,n+1):
        factorial = factorial * item
    print(f'El factorial de {n} es: {factorial}')