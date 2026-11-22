README.md
# Sistema Integral de Gestión - Software FJ

## 1. Descripción del proyecto

Este proyecto desarrolla un sistema orientado a objetos para administrar clientes, servicios y reservas de la empresa Software FJ.

El sistema permite registrar clientes, gestionar diferentes tipos de servicios, crear reservas, confirmarlas, cancelarlas y procesarlas.

## 2. Objetivo

Implementar los conceptos de programación orientada a objetos y el manejo de excepciones para desarrollar una aplicación organizada, funcional y capaz de controlar errores durante su ejecución.

## 3. Tecnologías utilizadas

- Lenguaje de programación: Python.
- Programación orientada a objetos.
- Clases, objetos y herencia.
- Encapsulamiento y polimorfismo.
- Manejo de excepciones.
- Registro de eventos y errores mediante archivos de texto.

## 4. Estructura del proyecto

- `main.py`: ejecuta el programa y las pruebas.
- `entidad.py`: contiene la clase abstracta Entidad.
- `cliente.py`: administra la información de los clientes.
- `servicios.py`: contiene los servicios disponibles.
- `reserva.py`: administra las reservas.
- `excepciones.py`: define las excepciones personalizadas.
- `sistema.py`: administra las operaciones generales.
- `logs/`: almacena los registros de eventos y errores.
- `README.md`: contiene la documentación del proyecto.

## 5. Servicios disponibles

El sistema cuenta con tres tipos de servicios:

1. Reserva de salas.
2. Alquiler de equipos.
3. Asesoría especializada.

Cada servicio implementa métodos para calcular costos, mostrar descripciones y validar sus parámetros.

## 6. Manejo de excepciones

El proyecto utiliza bloques `try`, `except`, `else` y `finally`, además de excepciones personalizadas para controlar situaciones incorrectas durante las operaciones.

También implementa el encadenamiento de excepciones para conservar información sobre los errores originales.

## 7. Registro de eventos

Los eventos y errores se almacenan en el archivo `logs/sistema.log`, permitiendo consultar información sobre las operaciones realizadas.

## 8. Ejecución del programa

Para ejecutar el sistema desde la terminal, se utiliza el siguiente comando:

```bash
python main.py