#Creado por:Efren Jimenez
#Fecha:04/04/2018
#Objetivo: Ejercicio 1

def IngresarPalabra():
    lista=[]
    cantidadPalabras=int(input("Digite la cantidad a palabras a ingresar"))
    contador=0
    while contador<cantidadPalabras:
        lista.append(input("Digite la palabra"))
        contador+=1
    for item in lista:
        print(item)

IngresarPalabra()