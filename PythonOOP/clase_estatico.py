#clase y estatico ep12
import math

class Pastel:
    def __init__(self, ingredientes, tamaño):
      self.ingredientes = ingredientes
      self.tamaño = tamaño
#     def __repr__(self):
#         return f'pastel({self.ingredientes !r})'

#     @classmethod
#     def Pastel_chocoate(cls):
#         return cls(['harina','leche','chocolate'])

#     @classmethod
#     def Pastel_vainilla(cls):
#         return cls(['harina','leche','vainilla'])    

# print(Pastel.Pastel_chocoate())

    def __repr__(self):
       return (f'Pastel({self.ingredientes !r}, 'f'{self.tamaño})')
    
    def area(self):
        return self.tamaño_area(self.tamaño)

    @staticmethod
    def tamaño_area(A):
        return A ** 2 * math.pi

nuevo_pastel = Pastel(['harina','azucar','leche','crema'],4)
print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamaño)

print(nuevo_pastel.tamaño_area(12))