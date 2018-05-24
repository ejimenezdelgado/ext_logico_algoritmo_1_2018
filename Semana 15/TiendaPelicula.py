__author__ = 'Efrén'

#Creado por:Efrén Jiménez
#Fecha:23/05/2018
#Objetivo: Clase TiendaPelicula

class TiendaPelicula():

    listaPeliculas=[]

    def __init__(self):
        return

    #Metodos SET
    def SetId(self,id):
        self.id=id

    def SetNombre(self,nombre):
        self.nombre= nombre

    def SetDireccion(self,direccion):
        self.direccion= direccion

    def SetCedula(self,cedula):
        self.cedula= cedula

    def SetPropetario(self, propetario):
        self.propetario = propetario

     #Metodos GET
    def GetId(self):
        return self.id

    def GetNombre(self):
        return self.nombre

    def GetDireccion(self):
        return self.direccion

    def GetCedula(self):
        return self.cedula

    def GetPropetario(self):
        return self.propetario

    def GetPeliculas(self):
        return self.listaPelicula

    def AgregarPelicula(self,pelicula):
        return self.listaPeliculas.append(pelicula)

    def ImprimirPeliculas(self):
        for i in self.listaPeliculas:
            i.Imprimir()