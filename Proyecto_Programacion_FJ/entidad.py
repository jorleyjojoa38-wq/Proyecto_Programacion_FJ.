
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    dentro del sistema Software FJ.
    """

    def __init__(self, identificacion, nombre):
        if not identificacion:
            raise ValueError("La identificación es obligatoria.")

        if not nombre or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")

        self._identificacion = identificacion
        self._nombre = nombre.strip()

    @property
    def identificacion(self):
        return self._identificacion

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def mostrar_informacion(self):
        """Método que deben implementar las clases hijas."""
        pass
