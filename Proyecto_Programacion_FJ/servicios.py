
from abc import ABC, abstractmethod


class Servicio(ABC):
    """
    Clase abstracta para representar los servicios
    ofrecidos por Software FJ.
    """

    def __init__(self, nombre, precio_base):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if not isinstance(precio_base, (int, float)) or precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self.nombre = nombre.strip()
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    def validar_duracion(self, duracion):
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")
    def validar_impuestos_descuentos(self, impuesto, descuento):
        if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

class ReservaSala(Servicio):
    """Servicio de reserva de salas por horas."""
    def validar_duracion(self, duracion):
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duración de la reserva debe ser mayor que cero.")
        if duracion > 24:
            raise ValueError("La reserva de sala no puede superar 24 horas.")
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_duracion(duracion)  
        self.validar_impuestos_descuentos(impuesto, descuento)
        subtotal = self.precio_base * duracion
        return subtotal + subtotal * impuesto / 100 - subtotal * descuento / 100

    def descripcion(self):
        return f"Reserva de sala: {self.nombre}"


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos por días."""
    def validar_duracion(self, duracion):
        if not isinstance(duracion, int) or duracion <= 0:
            raise ValueError(
                "El alquiler debe tener una duración en días enteros y positivos."
            )
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_duracion(duracion)
        self.validar_impuestos_descuentos(impuesto, descuento)
        subtotal = self.precio_base * duracion
        return subtotal + subtotal * impuesto / 100 - subtotal * descuento / 100

    def descripcion(self):
        return f"Alquiler de equipo: {self.nombre}"


class AsesoriaEspecializada(Servicio):
    """Servicio de asesoría especializada por horas."""
    def validar_duracion(self, duracion):
        self.validar_impuestos_descuentos(impuesto, descuento)
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duración de la asesoría debe ser mayor que cero.")
        if duracion > 8:
            raise ValueError("La asesoría no puede superar 8 horas por sesión.")
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_duracion(duracion)
        subtotal = self.precio_base * duracion
        return subtotal + subtotal * impuesto / 100 - subtotal * descuento / 100

    def descripcion(self):
        return f"Asesoría especializada: {self.nombre}"
