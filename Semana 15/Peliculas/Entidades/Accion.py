__author__ = 'Efrén'

#Creado por:Efrén Jiménez
#Fecha:23/05/2018
#Objetivo: Clase Accion


from Peliculas.Entidades.Pelicula import Pelicula

class Accion(Pelicula):

    def __init__(self):
        return

    def SetCantidadMuertos(self,cantidadMuertos):
        self.cantidadMuertos=cantidadMuertos

    def GetCantidadMuertos(self):
        return self.cantidadMuertos

    def Imprimir(self):
        print("Id : ", self.GetId())
        print("Nombre : ", self.GetNombre())
        print("Director : ", self.GetDirector())
        print("Numero actores : ", self.GetNumeroActores())
        print("Año : ", self.GetAno())
        print("Actor Principal : ", self.GetActorPrincipal())
        print("Cantidad muertos : ", self.GetCantidadMuertos())
