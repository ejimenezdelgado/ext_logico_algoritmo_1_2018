#Fecha: 25/04/2018
#Objetivo: Ejercicio 1

lista=[]

cantidad=int(input("Digite la cantidad de valores"))

for item in range(0,cantidad):
    lista.append(int(input("Digite el numero")))

indice1=int(input("Digite el indice 1"))
indice2=int(input("Digite el indice 2"))

sumatoria=0

contador=0
while (contador<cantidad):
    if(contador==indice1):
        sumatoria=sumatoria+lista[indice1]

    if (contador == indice2):
        sumatoria = sumatoria + lista[indice2]

    contador=contador+1

contador=0
sumatoria=0
for item in lista:
    if (contador == indice1):
        sumatoria = sumatoria + lista[indice1]

    if (contador == indice2):
        sumatoria = sumatoria + lista[indice2]

    contador = contador + 1

print("La sumatoria es ",sumatoria)

contador=0
for item in lista:
    if(contador%2==0):
        print("Es par",contador)
    else:
        print("Es impar",contador)
    contador=contador+1
    

contador=0
for item in lista:
    if(item%2==0):
        print("Es par",item)
    else:
        print("Es impar",item)
    contador=contador+1


