#herencia
class pokemon:
    pass #indica que esta vacia
    
    def __init__(self, name, type):
      self.name = name
      self.type = type
    
    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.name,self.type)


class pikachu(pokemon):
    def atack(self, atackType):
        return '{} tipo de ataque: {}'.format(self.name, atackType)


class charmander(pokemon):
    def atack(self, atackType):
        return '{} tipo de ataque: {}'.format(self.name, atackType)


newPokemon = pikachu('Terry','electric')
print(newPokemon.descripcion())

print(newPokemon.atack('impact'))