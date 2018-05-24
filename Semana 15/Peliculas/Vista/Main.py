#Elabore un algoritmo en donde se cree dos clases, la primera
# es clase tiendaPelicula que va tener como atributo
#ID,NOMBRE,DIRECCIÓN,CEDULAjuridica, Propietario.
#Generar otra clase llamada Pelicula que tiene como atributos:
#  ID, Nombre,Cantidad de Actores, actor principal, director
#año. La clase tiendaPelicula tendra una lista de peliculas.
# Cree una herencia que permita extender la clase pelicula
#en tres tipos de generos (comedia, romantica, acción) y
# genere un atributo para cada uno de ellas un metodo polimorfico
#llamado imprimir. Luego generar un menú donde se puedan
# agregar, editar e imprimir todas las peliculas de la tienda

from Peliculas.Entidades.Accion import Accion
from Peliculas.Entidades.Romantica import Romantica
from Peliculas.Entidades.Comedia import Comedia
from Peliculas.Controlador.TiendaPelicula import TiendaPelicula

def MenuPrincipal():
    print('\t\t Bienvenido \nDigite:\n'
          '1. Si desea agregar una pelicula\n'
          '2. Si desea editar una pelicula\n'
          '3. Si desea imprimir la informacion\n'
          'Otra tecla para salir...')

    option = input('Opcion:')
    if option == '1':
        print('\t\tDigite:\n'
              '1. Si la pelicula es de accion\n'
              '2. Si la pelicula es romantica\n'
              '3. Si la pelicula es comedia\n'
              'Otra tecla para salir...')

        option = input('Opcion:')
        if option != '1' and option != '2' and option != '3':
            print('Salistes')
            return MenuPrincipal()
        print('Digite los datos que se le piden a continuacion')
        data1 = input('ID:')
        data2 = input('Nombre:')
        data3 = input('Director:')
        data4 = input('Numero de actores:')
        data5 = input('Año:')
        data6 = input('Actor principal:')

        if option == '1':
            kills = input('Numero de muertes:')
            accion = Accion()
            accion.SetId(data1)
            accion.SetNombre(data2)
            accion.SetDirector(data3)
            accion.SetNumeroActores(data4)
            accion.SetAno(data5)
            accion.SetActorPrincipal(data6)
            accion.SetCantidadMuertos(kills)
            Zonax.AgregarPelicula(accion)
            return MenuPrincipal()
        elif option == '2':
            kisses = input('Numero de besos:')
            romantica = Romantica()
            romantica.SetId(data1)
            romantica.SetNombre(data2)
            romantica.SetDirector(data3)
            romantica.SetNumeroActores(data4)
            romantica.SetAno(data5)
            romantica.SetActorPrincipal(data6)
            romantica.SetCantidadMuertos(kisses)
            Zonax.AgregarPelicula(kisses)
        else:
            jokes = input('Numero de bromas:')
            comedia = Comedia()
            comedia.SetId(data1)
            comedia.SetNombre(data2)
            comedia.SetDirector(data3)
            comedia.SetNumeroActores(data4)
            comedia.SetAno(data5)
            comedia.SetActorPrincipal(data6)
            comedia.SetCantidadMuertos(jokes)
            Zonax.AgregarPelicula(comedia)

    elif option == '2':
        print('\nEditar  pelicula\n')
        peliculaACambiar = int(input('Escriba el id de la pelicula que desea editar:'))
        for i in Zonax.listaPeliculas:
            if i.GetId() == peliculaACambiar:
                print('Escriba la nueva informacion\n'
                      'Informacion actual:')
                i.Imprimir()
                print('\nNOTA: si no desea cambiar algo dejelo en blanco\n\n')
                data1 = input('ID:')
                data2 = input('Nombre:')
                data3 = input('Director:')
                data4 = input('Numero de actores:')
                data5 = input('Año:')
                data6 = input('Actor principal:')

                if data1 != '':
                    i.SetId(data1)
                if data2 != '':
                    i.SetNombre(data2)
                if data3 != '':
                    i.SetDirector(data3)
                if data4 != '':
                    i.SetNumeroActores(data4)
                if data5 != '':
                    i.SetAno(data5)
                if data6 != '':
                    i.SetActorPrincipal(data6)

                print('****Actualizado****')
                return MenuPrincipal()

        print('\n******Este id no esta registrado******\n')
        return MenuPrincipal()



    elif option == '3':
        Zonax.ImprimirPeliculas()
        print('\n')  # un espacio
        return MenuPrincipal()


Zonax = TiendaPelicula()
Zonax.SetId(1)
Zonax.SetNombre("Zona X")
Zonax.SetCedula(2015018474)
Zonax.SetDireccion("Costado sur del mundo")
Zonax.SetPropetario("Marco Antonio")

pelicula1=Accion()
pelicula1.SetId(23456)
pelicula1.SetNombre('Pena de muerte')
pelicula1.SetDirector('Manuel')
pelicula1.SetNumeroActores(456)
pelicula1.SetAno(2017)
pelicula1.SetActorPrincipal('Marcos')
pelicula1.SetCantidadMuertos(454)

pelicula2=Romantica()
pelicula2.SetId(233424)
pelicula2.SetNombre('La vida despues de la muerte')
pelicula2.SetDirector('Manuel')
pelicula2.SetNumeroActores(456)
pelicula2.SetAno(2016)
pelicula2.SetActorPrincipal('Romeo')
pelicula2.SetCantidadBesos(50)

pelicula3=Comedia()
pelicula3.SetId(223434)
pelicula3.SetNombre('Agarrame si puedes')
pelicula3.SetDirector('MR.Joy')
pelicula3.SetNumeroActores(232)
pelicula3.SetAno(2017)
pelicula3.SetActorPrincipal('Jeimy')
pelicula3.SetCantidadBromas(77774)

Zonax.AgregarPelicula(pelicula1)
Zonax.AgregarPelicula(pelicula2)
Zonax.AgregarPelicula(pelicula3)

MenuPrincipal()