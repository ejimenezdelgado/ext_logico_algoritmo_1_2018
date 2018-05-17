#Fecha: 16/05/2018
#Objetivo: Realizar un sistema para el manejo de clientes

from constantes import path
from entidades.cliente import Cliente

class ClienteAccesoDatos:

    def __init__(self):
        return

    #Crear un cliente
    def CrearCliente(self,cliente):
        archivo = open(path + "\\archivos\cliente.txt", "a+")
        archivo.write(str(cliente.cedula) + "," +
                      str(cliente.nombre) + "," +
                      str(cliente.sexo) + "," +
                      str(cliente.direccion) +"\n")
        archivo.close()

    # Elimina un cliente
    def EliminarCliente(self, cliente):
        archivo = open(path + "\archivos\cliente.txt", "r")
        escribir = ""
        for linea in archivo.readlines():
            if linea.split(',')[0] != str(cliente.cedula):
                escribir += linea
        archivo.close()
        archivo = open(path + "\archivos\cliente.txt" "w")
        archivo.write(escribir)
        archivo.close()

    # Edita un cliente
    def EditarCliente(self, cliente):
        archivo = open(path + "\archivos\cliente.txt", "r")
        escribir = ""
        for linea in archivo.readlines():
            if linea.split(',')[0] == str(cliente.cedula):
                escribir += \
                    (str(cliente.cedula) + "," +
                      str(cliente.nombre) + "," +
                      str(cliente.sexo) + "," +
                      str(cliente.direccion) +"\n")
            else:
                escribir += linea
        archivo.close()
        archivo = open(path + "\archivos\cliente.txt", "w")
        archivo.write(escribir);
        archivo.close()

    # Obtiene un cliente
    def ObtenerCliente(self, cliente):
        archivo = open(path + "\archivos\cliente.txt", "r")
        for linea in archivo.readlines():
            if linea.split(',')[0] == str(cliente.cedula):
                cliente = Cliente()
                cliente.cedula=linea.split(',')[0]
                cliente.nombre=linea.split(',')[1]
                cliente.sexo=linea.split(',')[2]
                cliente.direccion=linea.split(',')[3]
            return cliente

    # Obtiene los clientes
    def ObtenerClientes(self):
        archivo = open(path + "\archivos\cliente.txt", "r")
        lista=[]
        for linea in archivo.readlines():
            cliente = Cliente()
            cliente.cedula = linea.split(',')[0]
            cliente.nombre = linea.split(',')[1]
            cliente.sexo = linea.split(',')[2]
            cliente.direccion = linea.split(',')[3]
            lista.append(cliente)
        return lista

    # Obtiene la cantidad de clientes ingresados
    def CantidadClientes(self):
        contador = 0
        try:
            archivo = open(path + "\archivos\cliente.txt", "r+")
            contador = len(archivo.readlines())
            archivo.close()
        except ValueError:
            print(ValueError)
        return contador