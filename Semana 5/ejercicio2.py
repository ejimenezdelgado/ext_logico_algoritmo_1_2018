#Creado por Efrén Jiménez Delgado
#Fecha:14/03/2018
#objetivo: En geometría,
#  se especifican dos puntos
# de una recta usando las coordenadas
# (x1,x2) y (y1,y2). Escriba una función
# calcular_pendiente(), que reciba las coordenadas y
#  calcule la pendiente m, según la fórmula:
# m = (y2-y1)/(x2-x1)


def Coordenadas(x1,x2,y1,y2):
    m=(y2-y1)/(x2-x1)
    return m

x1=int(input("Digite x1"))
x2=int(input("Digite x2"))
y1=int(input("Digite y1"))
y2=int(input("Digite y2"))
retorno=Coordenadas(x1,x2,y1,y2)
print(retorno)

