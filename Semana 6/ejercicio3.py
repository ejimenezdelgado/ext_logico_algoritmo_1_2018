#Creado por:Efren Jimenez
#Fecha:21/03/2018
#Objetivo: Ejercicio 3

def Primo():
    numero=int(input("Digite un numero"))
    contadorDivisores=0
    contador=1
    while contador<=numero:
        if numero%contador==0:
            contadorDivisores=contadorDivisores+1
        contador=contador+1
    if contadorDivisores==2:
        print("Es un numero primo")
    else:
        print("No es un numero")

Primo()