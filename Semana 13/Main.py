#Fecha: 09/05/2018
#Objetivo: Proyecto POO

from Frase import Frase

opcion=0
listaFrases=[]
print("Bienvenidos al mejor sistema del mundo para las frases")

while(opcion<7):
    print("1. Agregar un autor")
    print("2. Agregar una frase a un autor")
    print("3. Primera frase de un autor")
    print("4. Ultima frase de un autor")
    print("5. Imprimir frases de un autor")
    print("6. Buscar frases por palabra")
    print("7. Salir")

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
    if opcion == 3:
        seleccionado=None
        autor = input("Digite el autor")
        for item in listaFrases:
            if item.autor==autor:
                seleccionado=item
        print(seleccionado.PrimerFrase())
    if opcion == 4:
        seleccionado=None
        autor = input("Digite el autor")
        for item in listaFrases:
            if item.autor==autor:
                seleccionado=item
        print(seleccionado.UltimaFrase())
    if opcion == 5:
        seleccionado=None
        autor = input("Digite el autor")
        for item in listaFrases:
            if item.autor==autor:
                seleccionado=item
        seleccionado.Imprimir()
    if opcion == 6:
        palabra = input("Digite la palabra a buscar")
        for item in listaFrases:
            for frase in item.lista:
                if palabra in frase:
                    print("Autor",item.autor)
                    print("Frase", frase)


