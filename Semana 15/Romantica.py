__author__ = 'Efrén'

#Creado por:Efrén Jiménez
#Fecha:23/05/2018
#Objetivo: Clase Romantica


from Peliculas.Entidades.Pelicula import Pelicula

class Romantica(Pelicula):

    def __init__(self):
        return

    def SetCantidadBesos(self,cantidadBesos):
        self.cantidadBesos=cantidadBesos

    def GetCantidadBesos(self):
        return self.cantidadBesos

    def Imprimir(self):
        print("Id : ", self.GetId())
        print("Nombre : ", self.GetNombre())
        print("Director : ", self.GetDirector())
        print("Numero actores : ", self.GetNumeroActores())
        print("Año : ", self.GetAno())
        print("Actor Principal : ", self.GetActorPrincipal())
        print("Cantidad besos : ", self.GetCantidadBesos())


