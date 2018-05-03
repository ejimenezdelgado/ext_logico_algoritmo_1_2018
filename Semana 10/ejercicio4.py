import random

cantidad=random.randint(1,1000000)
suma=0
lista=[]
for item in range(0,cantidad):
    lista.append(random.randint(1,1000000))

for item in lista:
    suma=suma+item

print("La sumatoria",suma)