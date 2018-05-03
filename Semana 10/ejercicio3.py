lista=[100,5,200,1,1000,0,600,50,301,300]
listaPares=[]
listaImpares=[]

contador=0
for item in lista:
    if contador%2==0:
        listaPares.append(item)
    else:
        listaImpares.append(item)
    contador=contador+1

contador=0
bandera=True
for item in listaPares:
    if listaPares[contador]<listaImpares[contador]:
        bandera=False
        break
    contador=contador+1
if bandera==False:
    print("No es partidario")
else:
    print("Es partidario")