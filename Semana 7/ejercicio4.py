#Creado por:Efren Jimenez
#Fecha:04/04/2018
#Objetivo: Ejercicio 4

def Suma():
    lista=[3,4,6,7,8]
    listaSumatoria=[]
    contador=0
    sumatoria=0
    while contador < len(lista):
        sumatoria=sumatoria+lista[contador]
        listaSumatoria.append(sumatoria)
        contador=contador+1
    print(listaSumatoria +"\n")

Suma()