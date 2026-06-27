# Simulador de Cajero Automático (ATM) - Proyecto Integrador

## Información del Proyecto
* Materia: Lógica de Programación
* Docente: Ing. Carlos Andrés Arévalo Torres
* Estudiante: Alexander Zambrano
* Fecha de Entrega: Junio, 2026

---

## Objetivo del Sistema
El objetivo de este proyecto es desarrollar un simulador interactivo de cajero automático en consola utilizando Python. Se busca aplicar los conocimientos adquiridos en la materia de Lógica de Programación, organizando el código de forma limpia y estructurada para simular un entorno bancario seguro y funcional.

---

## Descripción de Funcionalidades
El programa cuenta con las siguientes operaciones esenciales:

1. Autenticación de usuario: Control de seguridad que valida el PIN del cliente con un límite máximo de 3 intentos antes de bloquear el acceso.
2. Consulta de saldo: Muestra en pantalla los fondos que el usuario tiene disponibles en su cuenta corriente.
3. Depósito de dinero: Permite ingresar montos para sumar al saldo actual, incluyendo una validación para evitar que se coloquen números negativos o en cero.
4. Retiro de efectivo: Permite sacar dinero de la cuenta tras verificar que el usuario tenga saldo suficiente y que la cantidad ingresada sea mayor a cero.
5. Historial de movimientos: Almacena de forma ordenada las acciones que realiza el usuario en su sesión para mostrar un resumen y saldo final al salir del sistema.

---

## Conceptos Aplicados
El programa fue estructurado utilizando las siguientes herramientas de Python que se trabajaron durante el ciclo:
* Estructuras de datos: Uso de un diccionario para manejar la información del cliente y una lista para el historial transaccional mediante métodos como append y la función len.
* Funciones (def): Organización del código en bloques independientes para mejorar el orden y mantenimiento del menú principal.
* Control de flujo: Implementación de bucles while y for para el menú y los intentos de PIN, además de condiciones if-elif-else para procesar las transacciones.
* Manejo de errores: Uso de bloques try-except para evitar que el programa falle si el usuario ingresa letras en lugar de valores numéricos.
