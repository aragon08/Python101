# Las funciones se definene con 'def '
#n= int(input("ingresa un numero: "))
'''
def sumaTres(n):
    print(n+3)

sumaTres(4)
'''

'''def tabla_de_multiplicar(n):
    for item in range(1,11):
        print(n,'*',item,'=',item*n)


tabla_de_multiplicar(5)'''

'''def cadena():
    return 'curso de python'
print(cadena())'''

'''n=5
def funcion():
    print(n)
funcion()'''

'''def dato():
    n=2
    print(n)

dato()

n=4
dato()
print(4)'''

'''def suma(a,b):
    return a+b

r= suma(4,8)
print(r)'''
ex = [3,7,9,5,8,3,7,12]

def separar(l):
    l.sort()
    pares = []
    impares = []

    for item in l:
        if item % 2 ==0:
            pares.append(item)
        else:
            impares.append(item)
    return pares, impares
pares, impares = separar(ex)

print(pares)
print(impares)
     