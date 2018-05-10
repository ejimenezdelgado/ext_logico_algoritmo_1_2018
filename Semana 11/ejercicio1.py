
#Ejercicio1

#

class Persona():

    def __init__(self,nombre,primerApellido,segundoApellido,edad):
        self.nombre=nombre
        self.primerApellido = primerApellido
        self.segundoApellido = segundoApellido
        self.edad = edad

    def Imprimir(self):
        print("El nombre es ",self.nombre)
        print("El primer apellido es ", self.primerApellido)
        print("El segundo apellido es ", self.segundoApellido)
        print("La edad es ", self.edad)

persona1=Persona("Juana la cubana","Perez","Lopez",89)
persona2=Persona("Pedro el escamoso","Mena","Berra",40)
persona3=Persona("Marito mortadela","Castro","Leon",40)
persona1.Imprimir()
persona3.Imprimir()
persona2.Imprimir()
