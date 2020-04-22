#identificar pares e impares
n1 = int(input('escriba numero: '))
n2 = int(input('escriba otro numero: '))

if n2<n1:
  print(f'ingrese un numero mayoro igual que {n1:} ')
else:
    for item in range(n1,n2+1):
        if item%2==0:
            print(f'{item}Par')
        else:
            print(f'{item}Impar')

     