
import logging
from pathlib import Path

from cliente import Cliente
from reserva import Reserva
from excepciones import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva
)


# Configuración del archivo de registros
CARPETA_LOGS = Path(__file__).parent / "logs"
CARPETA_LOGS.mkdir(exist_ok=True)

logging.basicConfig(
    filename=CARPETA_LOGS / "sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)


class Sistema:
    """
    Clase principal que administra clientes,
    servicios y reservas de Software FJ.
    """

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []
        logging.info("Sistema Software FJ iniciado.")

    def registrar_cliente(self, cliente):
        try:
            if not isinstance(cliente, Cliente):
                raise ErrorCliente("El objeto no es un cliente válido.")

            if any(c.identificacion == cliente.identificacion
                   for c in self.clientes):
                raise ErrorCliente("El cliente ya está registrado.")

            self.clientes.append(cliente)
            logging.info("Cliente registrado: %s", cliente.nombre)
            print("Cliente registrado correctamente.")

        except (ErrorCliente, ValueError) as error:
            logging.error("Error al registrar cliente: %s", error)
            print("No se pudo registrar el cliente:", error)

    def agregar_servicio(self, servicio):
        try:
            if not hasattr(servicio, "calcular_costo"):
                raise ErrorServicio("El servicio no es válido.")

            if any(s.nombre == servicio.nombre for s in self.servicios):
                raise ErrorServicio("El servicio ya está registrado.")

            self.servicios.append(servicio)
            logging.info("Servicio agregado: %s", servicio.nombre)
            print("Servicio agregado correctamente.")

        except (ErrorServicio, ValueError) as error:
            logging.error("Error al agregar servicio: %s", error)
            print("No se pudo agregar el servicio:", error)

    def crear_reserva(self, codigo, identificacion, nombre_servicio, duracion):
        try:
            cliente = next(
                (c for c in self.clientes
                 if c.identificacion == identificacion),
                None
            )

            servicio = next(
                (s for s in self.servicios
                 if s.nombre == nombre_servicio),
                None
            )

            if cliente is None:
                raise ErrorReserva("El cliente no está registrado.")

            if servicio is None:
                raise ErrorReserva("El servicio no está disponible.")

            if any(r.codigo == codigo for r in self.reservas):
                raise ErrorReserva("El código de reserva ya existe.")

            reserva = Reserva(codigo, cliente, servicio, duracion)
            self.reservas.append(reserva)

            logging.info("Reserva creada: %s", codigo)
            print("Reserva creada correctamente.")
            return reserva

        except (ErrorReserva, ValueError, TypeError) as error:
            logging.error("Error al crear reserva: %s", error)
            print("No se pudo crear la reserva:", error)
            return None

    def buscar_reserva(self, codigo):
        return next(
            (r for r in self.reservas if r.codigo == codigo),
            None
        )

    def confirmar_reserva(self, codigo):
        try:
            reserva = self.buscar_reserva(codigo)

            if reserva is None:
                raise ErrorReserva("La reserva no existe.")

            resultado = reserva.confirmar()
            logging.info("Reserva confirmada: %s", codigo)
            print(resultado)

        except ErrorReserva as error:
            logging.error("Error al confirmar reserva: %s", error)
            print("No se pudo confirmar:", error)

    def cancelar_reserva(self, codigo):
        try:
            reserva = self.buscar_reserva(codigo)

            if reserva is None:
                raise ErrorReserva("La reserva no existe.")

            resultado = reserva.cancelar()
            logging.info("Reserva cancelada: %s", codigo)
            print(resultado)

        except ErrorReserva as error:
            logging.error("Error al cancelar reserva: %s", error)
            print("No se pudo cancelar:", error)

    def procesar_reserva(self, codigo, impuesto=0, descuento=0):
        try:
            reserva = self.buscar_reserva(codigo)

            if reserva is None:
                raise ErrorReserva("La reserva no existe.")

            costo = reserva.procesar(impuesto, descuento)
            logging.info("Reserva procesada: %s", codigo)
            print(f"Costo total de la reserva: ${costo:.2f}")

        except (ErrorReserva, ValueError, TypeError) as error:
            logging.error("Error al procesar reserva: %s", error)
            print("No se pudo procesar:", error)

        else:
            print("Proceso finalizado correctamente.")

        finally:
            print("Operación de procesamiento finalizada.")
