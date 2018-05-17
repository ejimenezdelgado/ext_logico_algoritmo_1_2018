

from logica.cliente_logica import ClienteLogica
from entidades.cliente import Cliente

cliente_logica =ClienteLogica()

cliente1=Cliente("278282834","Juana La cubana",
                 "La cubanita","hembrita")

cliente_logica.CrearCliente(cliente1)
