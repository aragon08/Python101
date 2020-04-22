# Diccionarios con funciones

notas = {'david':85,'carlos':60, 'victor':98, 'hector':75}
print(str(notas))
print(type(notas))

print(notas.clear())

notas2 =  notas.copy()
print(notas2)

notas = dict.fromkeys(['david', 'carlos', 'victor', 'hector'], 100)
print(notas)

notas = {'david':85,'carlos':60, 'victor':98, 'hector':75}
valor = notas.get('carlos')
print(valor)

items = notas.items()
print(items)

keys =  notas.keys()
print(keys)

dic1 = {'a':1,'b':2, 'c':3, 'd':4}
dic2 = {'d':5, 'e':6, 'f':7, 'g':8}
dic1.update(dic2)

value = dic1.values()
print(value)

Fpop = dic1.pop('c')
print(Fpop)
print(dic1)