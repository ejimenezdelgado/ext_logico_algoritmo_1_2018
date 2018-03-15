#Creado por Efrén Jiménez Delgado
#Fecha:14/03/2018
#objetivo: Escriba una función convertir_a_letras(),
#  que reciba un número entre 1 y 5, y devuelva
#  el número en letras.

def ConvertirALetras(numero):
    if(int(numero)==1):
        return "Uno"
    if (int(numero) == 2):
        return "Dos"
    if (int(numero) == 3):
        return "Tres"
    if (int(numero) == 4):
        return "Cuatro"
    if (int(numero) == 5):
        return "Cinco"

numerito=int(input("Digite un numero"))
retorno=ConvertirALetras(numerito)
print(retorno)