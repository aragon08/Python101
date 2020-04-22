# modulos (bibliotecas)

from math import pi, factorial, log
from random import choice, randrange
from datetime import date
from fractions import Fraction
from modulos2 import pares, ciclo_pares

a = pi
b = factorial(6)
c = log(8,10)
d = choice(['cara','cruz'])
e = randrange(5)
dia = date(2019,2,22)
year =date(2019,12,31)
end_year = (year - dia)
f = Fraction(2,4)
g = Fraction(4,8)


print(a)
print(b)
print(c)
print(d)
print(e)
print(dia)
print(end_year)

print(Fraction(f+g))

#Llamando nuestro modulo creado pares en modulos2.py
p = pares(8)
print(p)

#Llamando funcion ciclo_pares de modulos2.py
n = int(input('ingresa un número: '))

print('Los números pares hasta ',n, 'son: ')
for item in ciclo_pares(n):
    print(item) 

