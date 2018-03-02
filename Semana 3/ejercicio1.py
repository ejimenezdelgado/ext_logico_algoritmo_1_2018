#Creado por:Efrén Jiménez
#Fecha:28/02/2018
#Objetivo:Desarrolle un algoritmo que
# permita leer dos valores, determinar cuál
# de los dos valores es el menor y escríbalo.

numero1=0
numero2=0
numero1=int(input("Digite el numero 1"))
numero2=int(input("Digite el numero 2"))
if numero1 > numero2:
    print("El numero mayor es ",numero1)
    print("El numero menor es",numero2)
else:
    print("El numero mayor es ",numero2)
    print("El numero menor es",numero1)