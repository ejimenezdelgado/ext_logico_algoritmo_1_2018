#Creado por Diego Hidalgo
#Fecha:7/03/2018
#objetivo: ayudar a la persona a decidirse
valorterreno=0
valorautomovil=0
incrementoterreno=0
devaluoautomovil=0
valorautomovil=int(input("digite el valor del automovil "))
valorterreno=int(input("digite el valor del terreno "))
devaluoautomovil=int(input("digite el devaluo del automovil por año"))
incrementoterreno=int(input("digite el incremento del terreno por año"))
if valorterreno + ((valorterreno*(incrementoterreno)/100)*3)\
        >=valorautomovil - ((valorautomovil*(devaluoautomovil)/100)*3):
    print("comprar terreno")
else:
    print("comprar automovil")