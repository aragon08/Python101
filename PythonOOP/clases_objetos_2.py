#Clases y objetos II

#antes de Pytho3, se puede seguir haciendo class persona(object):

# class jugadores_A:
#     j1 = 'messi'
#     j2 = 'c.ronaldo'

# print(jugadores_A.j2)

# class jugadores_B:
#     j3 = 'marcelo'
#     j1 = 'falcao'

# print(jugadores_B.j1)

class nombre:
    pass

carlos = nombre()
Andie = nombre()

# objeto.atributo = valor

carlos.edad = 31
carlos.sexo = 'masculino'
carlos.pais = 'mexico'

Andie.edad = 29
Andie.sexo = 'femenino'
Andie.pais = 'mexico'

print(carlos.edad)
print(Andie.edad)