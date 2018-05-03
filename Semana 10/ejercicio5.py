lista=[100,-5,200,-1,1000,-0,-600,-50,301,300]
listaBuena=[]

for item in lista:
    if item <0:
        listaBuena.append(0)
    else:
        listaBuena.append(item)

print(listaBuena)


