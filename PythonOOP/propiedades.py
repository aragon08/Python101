#propiedades()

class Empleado:
    def __init__(self, nombre, salario):
      self.__nombre = nombre
      self.__salario = salario
    
    def __getnombre(self):
        return self.__nombre

    def __getsalario(self):
        return self.__salario

    def __setnombre(self, nombre):
        self.__nombre = nombre

    def __setsalario(self, salario):
        self.__salario = salario

    def __delnombre(self):
        del self.__nombre

    def __delsalario(self):
        del self.__salario

# empleado1 = Empleado('carlos', 10000)

# print(empleado1.getNombre(),',',empleado1.getSalario())

# empleado1.setNombre('juan')
# print(empleado1.getNombre(),',',empleado1.getSalario())

nombre = property(fget= __getnombre, fset= __setnombre, fdel= __delnombre)
salario = property(fget= __getSalario)

empleado1 = Empleado('carlos', 10000)

empleado1.nombre = 'juan'
print(empleado1.getNombre(),',',empleado1.getSalario())
help(empleado1)
