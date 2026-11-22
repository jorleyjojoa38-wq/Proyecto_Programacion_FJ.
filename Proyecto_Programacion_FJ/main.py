
import logging

from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from sistema import Sistema


def ejecutar_sistema():
    sistema = Sistema()

    print("\n======================================")
    print(" SISTEMA DE GESTION - SOFTWARE FJ")
    print("======================================\n")

    # OPERACION 1: Registro de cliente valido
    print("\nOPERACION 1: Registrar cliente")
    cliente1 = Cliente(
        "1001", "Carlos Perez",
        "carlos@gmail.com", "3001234567"
    )
    sistema.registrar_cliente(cliente1)

    # OPERACION 2: Registro de otro cliente valido
    print("\nOPERACION 2: Registrar segundo cliente")
    cliente2 = Cliente(
        "1002", "Maria Lopez",
        "maria@gmail.com", "3101234567"
    )
    sistema.registrar_cliente(cliente2)

    # OPERACION 3: Intento de registrar un correo invalido
    print("\nOPERACION 3: Probar correo invalido")
    try:
        cliente_invalido = Cliente(
            "1003", "Pedro Ruiz", "pedrogmail.com", "3201234567"
        )
        sistema.registrar_cliente(cliente_invalido)
    except ValueError as error:
        logging.exception("Registro de cliente invalido")
        print("Error controlado:", error)

    # OPERACION 4: Intento de registrar un telefono invalido
    print("\nOPERACION 4: Probar telefono invalido")
    try:
        Cliente("1004", "Ana Torres", "ana@gmail.com", "123")
    except ValueError as error:
        logging.exception("Telefono invalido")
        print("Error controlado:", error)

    # OPERACION 5: Crear servicio de reserva de sala
    print("\nOPERACION 5: Crear servicio de sala")
    sala = ReservaSala("Sala de reuniones", 50000)
    sistema.agregar_servicio(sala)

    # OPERACION 6: Crear servicio de alquiler de equipo
    print("\nOPERACION 6: Crear servicio de equipo")
    equipo = AlquilerEquipo("Video Beam", 80000)
    sistema.agregar_servicio(equipo)

    # OPERACION 7: Crear servicio de asesoria
    print("\nOPERACION 7: Crear servicio de asesoria")
    asesoria = AsesoriaEspecializada("Asesoria de software", 100000)
    sistema.agregar_servicio(asesoria)

    # OPERACION 8: Intentar crear un servicio con precio incorrecto
    print("\nOPERACION 8: Probar servicio con precio invalido")
    try:
        ReservaSala("Sala incorrecta", -5000)
    except ValueError as error:
        logging.exception("Creacion de servicio invalido")
        print("Error controlado:", error)

    # OPERACION 9: Intentar registrar un cliente duplicado
    print("\nOPERACION 9: Probar cliente duplicado")
    cliente_repetido = Cliente(
        "1001", "Carlos Perez",
        "carlos@gmail.com", "3001234567"
    )
    sistema.registrar_cliente(cliente_repetido)

    # OPERACION 10: Crear una reserva correctamente
    print("\nOPERACION 10: Crear reserva")
    reserva1 = sistema.crear_reserva(
        "R001", "1001", "Sala de reuniones", 2
    )

    # OPERACION 11: Confirmar la reserva
    print("\nOPERACION 11: Confirmar reserva")
    sistema.confirmar_reserva("R001")

    # OPERACION 12: Procesar reserva con impuesto y descuento
    print("\nOPERACION 12: Procesar reserva")
    sistema.procesar_reserva("R001", impuesto=19, descuento=10)

    # OPERACION 13: Intentar reservar con cliente inexistente
    print("\nOPERACION 13: Reserva con cliente inexistente")
    sistema.crear_reserva(
        "R002", "9999", "Video Beam", 1
    )

    # OPERACION 14: Crear una segunda reserva
    print("\nOPERACION 14: Crear segunda reserva")
    reserva2 = sistema.crear_reserva(
        "R003", "1002", "Video Beam", 2
    )

    # OPERACION 15: Cancelar la segunda reserva
    print("\nOPERACION 15: Cancelar reserva")
    sistema.cancelar_reserva("R003")

    # OPERACION 16: Intentar procesar una reserva cancelada
    print("\nOPERACION 16: Procesar reserva cancelada")
    sistema.procesar_reserva("R003")

    # OPERACION 17: Demostrar try, except, else y finally
    print("\nOPERACION 17: Demostracion de excepciones")

    try:
        resultado = 100 / 2
    except ZeroDivisionError as error:
        logging.exception("Error matematico")
        print("Error:", error)
    else:
        print("Calculo realizado correctamente:", resultado)
    finally:
        print("Bloque finally ejecutado.")
    # OPERACION 18: Probar impuesto invalido
    print("\nOPERACION 18: Probar impuesto invalido")
    try:
        sala.calcular_costo(2, impuesto=150)
    except ValueError as error:
        logging.exception("Prueba de impuesto invalido")
        print("Error controlado:", error)

    # OPERACION 19: Probar descuento invalido
    print("\nOPERACION 19: Probar descuento invalido")
    try:
        equipo.calcular_costo(2, descuento=-10)
    except ValueError as error:
        logging.exception("Prueba de descuento invalido")
        print("Error controlado:", error)
    print("\n======================================")
    print(" PRUEBAS DEL SISTEMA FINALIZADAS")
    print(" Revise la carpeta logs para consultar")
    print(" los registros de eventos y errores.")
    print("======================================")


if __name__ == "__main__":
    try:
        ejecutar_sistema()
    except Exception as error:
        logging.exception("Error general en la ejecucion")
        print("Se presento un error controlado:", error)
