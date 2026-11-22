
from excepciones import ErrorReserva


class Reserva:
    """
    Representa una reserva realizada por un cliente
    en Software FJ.
    """

    def __init__(self, codigo, cliente, servicio, duracion):
        if not codigo:
            raise ErrorReserva("El código de reserva es obligatorio.")

        if cliente is None:
            raise ErrorReserva("Debe existir un cliente.")

        if servicio is None:
            raise ErrorReserva("Debe existir un servicio.")

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorReserva("La duración debe ser mayor que cero.")

        self.codigo = codigo
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        if self.estado != "Pendiente":
            raise ErrorReserva("Solo se pueden confirmar reservas pendientes.")

        self.estado = "Confirmada"
        return "La reserva fue confirmada correctamente."

    def cancelar(self):
        if self.estado == "Cancelada":
            raise ErrorReserva("La reserva ya está cancelada.")

        self.estado = "Cancelada"
        return "La reserva fue cancelada correctamente."

    def procesar(self, impuesto=0, descuento=0):
        if self.estado != "Confirmada":
            raise ErrorReserva("La reserva debe estar confirmada para procesarse.")

        try:
            costo = self.servicio.calcular_costo(
                self.duracion, impuesto, descuento
            )
        except (ValueError, TypeError) as error:
            raise ErrorReserva("No fue posible calcular el costo.") from error

        self.estado = "Procesada"
        return costo

    def mostrar_reserva(self):
        return (
            f"Código: {self.codigo}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.descripcion()}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}"
        )
