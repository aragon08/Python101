#encapsulación
class Cliente:
    def __init__(self):
        self.__codigo = 4321

    def __cuenta(self):
        print('cuenta de procesamiento')

    def getCodigo(self):
        return self.__codigo



persona = Cliente()
#objeto._nombreClase__nombreAtriuto
print(persona._Cliente__codigo)

persona._Cliente__cuenta()
