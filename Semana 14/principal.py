

from logica.cliente_logica import ClienteLogica
from entidades.cliente import Cliente

cliente_logica =ClienteLogica()

cliente1=Cliente("278282835","Juana La cubana",
                 "La cubanita","hembrita")

cliente_logica.CrearCliente(cliente1)


cliente2=Cliente("278282834","Pedro el escamoso",
                 "Macho men","tamandangapio")

cliente_logica.EditarCliente(cliente2)

cliente3=Cliente("278282834","","","")

cliente_logica.EliminarCliente(cliente3)

cliente4=Cliente("278282834","Pedro el escamoso",
                 "Macho men","tamandangapio")
cliente_logica.CrearCliente(cliente4)
for item in cliente_logica.ObtenerClientes():
    print(item.cedula)
    print(item.nombre)