#Polimorfismo por funcion
# class Tomate:
#     def tipo(self):
#         print('vegetal')
    
#     def color(self):
#         print('rojo')

# class Manzana:
#     def tipo(self):
#         print('fruta')
    
#     def color(self):
#         print('verde')
    

# def funcion(objeto):
#     objeto.tipo()
#     objeto.color()

# nuevo_tomate = Tomate()
# funcion(nuevo_tomate)

# nueva_manzana = Manzana()
# funcion(nueva_manzana)

#**********************************************

#Polimorfismo con metodos
# class Colombia:
#     def capital(self):
#         print('Bogota')
#     def idioma(self):
#         print('español')

# class Francia:
#     def capital(self):
#         print('Paris')
#     def idioma(self):
#         print('frances')

# colombiano = Colombia()

# frances = Francia()

# for pais in (colombiano, frances):
#     pais.capital()
#     pais.idioma()
 
#**********************************************

#Polimorfismo con herencia
class Aves:
    def volar(self):
        print('La mayoria de las aves pueden volar pero algunas no')

class Aguila(Aves):
    def volar(self):
        print('Las aguilas pueden volar')

class Gallina:
    def volar(self):
        print('Las gallinas no pueden volar')

obj_ave = Aves()
obj_aguila = Aguila()
obj_gallina = Gallina()

obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()