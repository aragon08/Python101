#f-string

#format %

# curso = 'python'

# print("tutoriales de % s"%curso)

# nombre = 'Carlos'
# edad = 31
# print("hola soy, %s y tengo %s años"%(nombre,edad))

# #str.format()
# print('que tal soy {} y mi edad es {} años.'.format(nombre,edad))

# #f-string
# print(f"hola soy {nombre} y mi edad es {edad}")

class Estudiante:
    def __init__(self, name,lastname, age):
      self.name = name
      self.lastname = lastname
      self.age = age
    
    def __str__(self):
        return f"{self.name} {self.lastname} {self.age}"
    
    def __repr__(self):
        return f"{self.name} {self.lastname} {self.age}"


new_student = Estudiante('carlos','aragon', 31)

print(f"{new_student}")

print(f"{new_student !r}")