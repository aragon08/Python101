# for i in 'numero':
#     print(i)

#calcular el numero de vocales de una frase

frase = str(input('ingrese una frase: '))
vocales = 'aeiouAEIOU'
contador = 0
for item in frase:
    if item in vocales:
        contador =  contador + 1
print('el numero de vocales es: ', contador)

 