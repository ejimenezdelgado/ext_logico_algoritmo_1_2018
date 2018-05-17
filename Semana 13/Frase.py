#Fecha: 09/05/2018
#Objetivo: Clase Frase

class Frase:

    def __init__(self,autor,lista):
        self.autor = autor
        self.lista=lista

    def AgregarFrase(self,frase):
        self.lista.append(frase)

    def PrimerFrase(self):
        if len(self.lista)>0:
            return self.lista[0]
        else:
            return "no hay nada"

    def UltimaFrase(self):
        if len(self.lista)>1:
            return self.lista[len(self.lista)-1]
        else:
            return "no hay nada"

    def Imprimir(self):
        print("El autor es :", self.autor)
        for item in self.lista:
            print(item)
