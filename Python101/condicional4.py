# Calificacion de notas
'''
Datos:
n= notas
r= respuesta
'''

n = float(input('ingrese su nota: '))
if n<= 50:
    r = 'Reprobado'
elif n<=80:
    r = 'Aprobado'
elif n<=90:
    r = 'Sobresaliente'
else:
    r = 'Excelente'

print('su nota ', n, r)