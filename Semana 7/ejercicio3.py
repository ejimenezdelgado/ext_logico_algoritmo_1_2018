#Creado por:Efren Jimenez
#Fecha:04/04/2018
#Objetivo: Ejercicio 2


def IngresarPalabra():
    lista=[]
    listaInvertida=[]
    cantidadPalabras=int(input("Digite la cantidad a palabras a ingresar"))
    contador=0

    while contador<cantidadPalabras:
        lista.append(input("Digite la palabra"))
        contador+=1

    contador=cantidadPalabras-1
    while contador>=0:
        listaInvertida.append(lista[contador])
        contador-=1

    print("La lista es :",lista)
    print("La invertida es :", listaInvertida)

IngresarPalabra()