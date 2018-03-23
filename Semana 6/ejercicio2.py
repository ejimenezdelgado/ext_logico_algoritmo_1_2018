#Creado por:Efren Jimenez
#Fecha:21/03/2018
#Objetivo: Ejercicio 2

def Perfectos():
    contador=1
    sumaDivisores=0
    numero=int(input("Digite el numero"))
    while contador<numero:
        if numero%contador==0:
            sumaDivisores=sumaDivisores+contador
        contador=contador+1
    if numero==sumaDivisores:
        print("Es un numero perfecto")
    else:
        print("No es un numero perfecto")


#LLamada de la funcion
Perfectos()