__author__ = 'Efrén'

#Creado por:Efrén Jiménez
#Fecha:23/05/2018
#Objetivo: Clase Romantica


from Peliculas.Entidades.Pelicula import Pelicula

class Comedia(Pelicula):

    def __init__(self):
        return

    def SetCantidadBromas(self,cantidadBromas):
        self.cantidadBromas=cantidadBromas

    def GetCantidadBromas(self):
        return self.cantidadBromas

    def Imprimir(self):
        print("Id : ", self.GetId())
        print("Nombre : ", self.GetNombre())
        print("Director : ", self.GetDirector())
        print("Numero actores : ", self.GetNumeroActores())
        print("Año : ", self.GetAno())
        print("Actor Principal : ", self.GetActorPrincipal())
        print("Cantidad bromas : ", self.GetCantidadBromas())


