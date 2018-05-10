#Fecha: 09/05/2018
#Objetivo: Proyecto POO

from Frase import Frase

opcion=0
listaFrases=[]
print("Bienvenidos al mejor sistema del mundo para las frases")

while(opcion<3):
    print("1. Agregar un autor")
    print("2. Agregar una frase a un autor")
    print("3. Salir")
    opcion=int(input("Digite la opcion"))
    if opcion==1:
        autor=input("Digite el autor")
        frase=Frase(autor,[])
        listaFrases.append(frase)
    if opcion == 2:
        seleccionado=None
        autor = input("Digite el autor")
        for item in listaFrases:
            if item.autor==autor:
                seleccionado=item
        frase = input("Digite la frase")
        seleccionado.AgregarFrase(frase)
        index=listaFrases.index(seleccionado)
        listaFrases[index]=seleccionado


