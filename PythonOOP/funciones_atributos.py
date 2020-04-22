#funciones para atributos

class Persona:
    edad = 27
    nombre = 'Carlos'
    pais = 'Mexico'

doctor = Persona()

print(doctor.edad)
print('edad con getattr',getattr(doctor,'edad'))

print('el doctor tiene una edad?',hasattr(doctor,'edad'))

print('el doctor tiene una edad?',hasattr(doctor,'apellido'))

print(doctor.nombre)
setattr(doctor,'nombre','Hector')
print(doctor.nombre)

delattr(Persona,'pais')