
class ErrorCliente(Exception):
    """Error relacionado con los datos de un cliente."""
    pass


class ErrorServicio(Exception):
    """Error relacionado con la creación de servicios."""
    pass


class ErrorReserva(Exception):
    """Error relacionado con las operaciones de reservas."""
    pass


class ErrorOperacion(Exception):
    """Error general durante una operación del sistema."""
    pass
