#Herencia multiple, multinivel

class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print('llamando...')
    def ocupado(self):
        print('ocupado...')

class Camara:
    def __init__(self):
        pass

    def Foto(self):
        print('tomando foto...')


class Reproduccion:
    def __init__(self):
        pass
    def musica(self):
        print('reproduciendo musica...')
    def video(self):
        print('reproducir video')

class smartphone(Telefono,Camara,Reproduccion):
    def __del__(self):
        print('telefono apagado')

movil = smartphone()
#print(dir(movil))
print(movil.Foto())
print(movil.llamar())
