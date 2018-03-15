#Creado por: Carlos L. Huertas Blanco
#Fecha:28/02/2018
#Objetivo: Ejercicio 10 del Libro Python

metros=0
metros=int(input("Cuántas hectareas hay disponibles:"))*10000

TamañoTerreno=0

if metros >= 1000000:
        print("Pinos necesarios:",((metros*0.70)/10)*8)
        print("Eucaliotos necesarios:", ((metros*0.20)/15)*15)
        print("Cedros necesarios:", ((metros*0.20)/18)*10)

else:
        print("Pinos necesarios:", ((metros * 0.45) / 10) * 8)
        print("Eucaliotos necesarios:", ((metros * 0.30) / 15) * 15)
        print("Cedros necesarios:", int(((metros * 0.25) / 18) * 10))
