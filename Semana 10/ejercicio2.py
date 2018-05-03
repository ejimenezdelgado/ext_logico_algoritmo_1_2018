#Ejercicio tarea1

lista1=[1,3,5,9]
lista2=[2,4,5,6]
lista3=[]

contador=0
for item in lista1:
    if lista1[contador] > lista2[contador]:
        lista3.append(lista2[contador])
        lista3.append(lista1[contador])
    else:
        if lista1[contador] == lista2[contador]:
            lista3.append(lista1[contador])
        else:
            lista3.append(lista1[contador])
            lista3.append(lista2[contador])
    contador=contador+1
print(lista3)
