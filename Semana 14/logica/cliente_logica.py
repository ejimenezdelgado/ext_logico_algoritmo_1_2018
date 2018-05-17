#Fecha: 16/05/2018

from acceso_datos.cliente_acceso_datos \
    import ClienteAccesoDatos

class ClienteLogica:
    def CrearCliente(self, cliente):
        clienteAccesoDatos= ClienteAccesoDatos()
        clienteAccesoDatos.CrearCliente(cliente)

    # Elimina un cliente
    def EliminarCliente(self, cliente):
        clienteAccesoDatos = ClienteAccesoDatos()
        clienteAccesoDatos.EliminarCliente(cliente)

    # Edita un cliente
    def EditarCliente(self, cliente):
        clienteAccesoDatos = ClienteAccesoDatos()
        clienteAccesoDatos.EditarCliente(cliente)

    # Obtiene un cliente
    def ObtenerCliente(self, cliente):
        clienteAccesoDatos = ClienteAccesoDatos()
        return clienteAccesoDatos.ObtenerCliente(cliente)


    # Obtiene los clientes
    def ObtenerClientes(self):
        clienteAccesoDatos = ClienteAccesoDatos()
        return clienteAccesoDatos.ObtenerClientes()

    # Obtiene la cantidad de clientes ingresados
    def CantidadClientes(self):
        clienteAccesoDatos = ClienteAccesoDatos()
        return clienteAccesoDatos.CantidadClientes()