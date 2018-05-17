#Fecha: 16/05/2018
#Objetivo: Realizar un sistema para el manejo de clientes

from constantes import path

class ClienteAccesoDatos:

    def __init__(self):
        return

    #Crear un cliente
    def CrearCliente(self,cliente):
        archivo = open(path + "\archivos\cliente.txt", "a+")
        archivo.write(str(self.cedula) + "," +
                      str(self.nombre) + "," +
                      str(self.sexo) + "," +
                      str(self.direccion) +"\n")
        archivo.close()
