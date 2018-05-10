#Fecha: 09/05/2018
#Objetivo: Clase Frase

class Frase:

    def __init__(self,lista):
        self.lista=lista

    def AgregarFrase(self,frase):
        self.lista.append(frase)