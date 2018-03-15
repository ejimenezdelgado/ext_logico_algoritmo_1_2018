#Creado por Efrén Jiménez Delgado
#Fecha:14/03/2018
#objetivo: Ejercicio 6 pagina 410

def ImprimeSumaNumeros(inicial,final):
    contador=inicial
    suma=0
    while contador<=final:
        suma=contador+suma
        contador=contador+1
    return suma

x1=int(input("Digite el inicio"))
x2=int(input("Digite el final"))
print(ImprimeSumaNumeros(x1,x2))