#contructores

# class Persona:
#     pass
#     def __init__(self,nombre, año):
#         self.nombre = nombre
#         self.año = año
    
#     def descripcion(self):
#         return ' {} tiene {}'.format(self.nombre, self.año)
    
#     def comentario(self, frase):
#         return '{} dice: {}'.format(self.nombre,frase)

# doctor = Persona('Carlos', 31)

# print(doctor.descripcion())

# print(doctor.comentario('Hola que tal'))

#modificar un atributo
class Email:
    def __init__(self):
      self.enviado = False
    
    def enviar_correo(self):
        self.enviado = True

micorreo= Email()

print(micorreo.enviado)

micorreo.enviar_correo()
print(micorreo.enviado)