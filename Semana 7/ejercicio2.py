#Creado por:Efren Jimenez
#Fecha:04/04/2018
#Objetivo: Ejercicio 2


def IngresarPalabra():
    lista=[]
    cantidadPalabras=int(input("Digite la cantidad a palabras a ingresar"))
    contador=0
    while contador<cantidadPalabras:
        lista.append(input("Digite la palabra"))
        contador+=1
    palabra = input("Digite la palabra a buscar")
    contadorVeces=0
    for item in lista:
        if item==palabra:
            contadorVeces=contadorVeces+1
    print("La cantidad de veces es:"+ str(contadorVeces))

IngresarPalabra()