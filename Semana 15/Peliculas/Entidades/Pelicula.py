__author__ = 'Efrén'

#Creado por:Efrén Jiménez
#Fecha:23/05/2018
#Objetivo: Clase Pelicula

class Pelicula():

    def __init__(self):
        return

    #Metodos SET
    def SetId(self,id):
        self.id=id

    def SetNombre(self,nombre):
        self.nombre=nombre

    def SetDirector(self,director):
        self.director=director

    def SetNumeroActores(self,numeroActores):
        self.numeroActores=numeroActores

    def SetAno(self,ano):
        self.ano=ano

    def SetActorPrincipal(self,actorPrincipal):
        self.actorPrincipal=actorPrincipal

    #Metodos GET
    def GetId(self):
        return self.id

    def GetNombre(self):
        return self.nombre

    def GetDirector(self):
        return self.director

    def GetNumeroActores(self):
        return self.numeroActores

    def GetAno(self):
        return self.ano

    def GetActorPrincipal(self):
        return self.actorPrincipal

    def Imprimir(self):
        print("Id : ",self.GetId())
        print("Nombre : ", self.GetNombre())
        print("Director : ", self.GetDirector())
        print("Numero actores : ", self.GetNumeroActores())
        print("Año : ", self.GetAno())
        print("Actor Principal : ", self.GetActorPrincipal())