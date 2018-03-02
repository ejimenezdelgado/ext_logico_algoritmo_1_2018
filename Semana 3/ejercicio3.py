#Creado por:Efrén Jiménez
#Fecha:28/02/2018
#Objetivo:Elaborar un algoritmo para calcular el promedio final de la materia de algoritmos. Dicha calificación se compone delos siguientes porcentajes:
#55% -----del promedio final de sus calificaciones parciales (3)
#30% ----- de la calificación de promedio de trabajo en clase (2)
#15% ----- de la calificación de un trabajo final

examen1=0
examen2=0
examen3=0
promedioExamen=0
trabajoClase1=0
trabajoClase2=0
promedioTrabajoClase=0
trabajoFinal=0

examen1=int(input("Digite el examen 1"))
examen2=int(input("Digite el examen 2"))
examen3=int(input("Digite el examen 3"))

promedioNota=(((examen1+examen2+examen3)/3)/100)*55

trabajoClase1=int(input("Digite el trabajo clase 1"))
trabajoClase2=int(input("Digite el trabajo clase 2"))

promedioTrabajoClase=((((trabajoClase1+trabajoClase2)/2)/100)*30)

trabajoFinal=(int(input("Digite el trabajo final"))/100)*15

print("Promedio nota",promedioNota)
print("Promedio trabajo clase",promedioTrabajoClase)
print("Promedio trabajo final",trabajoFinal)

print("La nota final es",promedioNota+promedioTrabajoClase+trabajoFinal)