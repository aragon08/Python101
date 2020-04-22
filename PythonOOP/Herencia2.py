#herencia ejemplo practico

class Calculadora:
    def __init__(self, num):
      self.n = num
      self.dato = [0 for i in range(num)]
    
    def ingresarDato(self):
        self.dato = [int(input('ingresa dato: '+str(i+1)+' =')) for i in range(self.n)]


class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
      
    def suma(self):
        a,b, = self.dato
        s = a + b
        print('=',s)

    def resta(self):
        a,b, = self.dato
        r = a - b
        print('=',r)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def cuadrada(self):
        import math 
        a, = self.dato
        print('=', math.sqrt(a))

ejemplo = op_basicas()
print(ejemplo.ingresarDato())
print(ejemplo.suma())

ejemplo2 = raiz()
print(ejemplo2.ingresarDato())
print(ejemplo2.cuadrada())