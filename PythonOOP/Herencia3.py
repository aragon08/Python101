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


objeto = op_basicas()
print(isinstance(objeto,op_basicas))
print(isinstance(objeto,raiz))

print(issubclass(Calculadora,op_basicas))
print(issubclass(op_basicas,Calculadora))