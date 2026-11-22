
from entidad import Entidad


class Cliente(Entidad):
    """
    Representa un cliente registrado en Software FJ.
    """

    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion, nombre)

        if not isinstance(correo, str) or "@" not in correo or "." not in correo:
            raise ValueError("El correo electrónico no es válido.")

        if not str(telefono).isdigit() or len(str(telefono)) < 7:
            raise ValueError("El teléfono debe contener al menos 7 dígitos.")

        self.__correo = correo.strip()
        self.__telefono = str(telefono)

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )
