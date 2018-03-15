## ejercio 14

num_pul=0
sexo=0
edad=0

sexo=int(input('MASCULINO=1 o FEMENINO=2'))
edad=int(input('digite la edad'))

if sexo==1:
    num_pul=(220-edad)/10
    print('LA CANTIDAD DE PULSEACIONES SI ES HOMBRE Y CON EDAD DE',edad,'es de',num_pul)
else:
    num_pul=(210-edad)/10
    print('LA CANTIDAD DE PULSEACIONES SI ES MUJER Y CON EDAD DE', edad, 'es de', num_pul)