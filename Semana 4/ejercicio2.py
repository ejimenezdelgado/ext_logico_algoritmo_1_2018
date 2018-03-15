#Creado por: Carlos L. Huertas Blanco
#Fecha:07/03/2018
#Objetivo: Whatsapp

Compra=0
Compra =int(input("Cuánto es el monto de compra?"))

import random
aleatorio=random.randint(0,100)

if aleatorio < 50:
    print("Su descuento:",Compra*0.15)

if aleatorio >= 50:
    print("Su descuento:", Compra*0.20)