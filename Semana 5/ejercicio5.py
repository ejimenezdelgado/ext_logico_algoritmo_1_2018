#Creado por Efrén Jiménez Delgado
#Fecha:14/03/2018
#objetivo: Escribir un programa que visualice en pantalla
# los números pares entre 1 y 25.

def ImprimeNumeroPares():
    contador=1
    while contador<26:
        if(contador%2==0):
            print(contador)
        contador=contador+1

ImprimeNumeroPares()