#Creado por:Efren Jimenez
#Fecha:21/03/2018
#Objetivo: Ejercicio 1

def ObtenerDatos():
    contador=0
    variable1=0
    variable2 = 0
    variable3 = 0
    variable4 = 0
    variable5 = 0

    while contador<5:
        valor=int(input("Digite un numero"))
        if(contador==0):
            variable1=valor
        if (contador == 1):
            variable2 = valor
        if (contador == 2):
            variable3 = valor
        if (contador == 3):
            variable4 = valor
        if (contador == 4):
            variable5 = valor
        contador=contador+1
    retorno=Duplicados(variable1,variable2,variable3,variable4,variable5)
    if retorno==True:
        print("Si hay valores repetidos")
    else:
        print("No hay valores repetidos")

def Duplicados(variable1,variable2,variable3,variable4,variable5):
    if(variable1==variable2) or (variable1==variable3) or (variable1==variable4) \
            or (variable1==variable5) :
        return True
    if (variable2 == variable3) or (variable2 == variable4) or (variable2 == variable5):
        return True
    if (variable3 == variable4) or (variable3 == variable5):
        return True
    if (variable4 == variable5):
        return True
    return False

ObtenerDatos()