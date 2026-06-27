# ====================================================================
# PROYECTO INTEGRADOR - SIMULADOR DE CAJERO AUTOMÁTICO
# Estudiante: Alexander Zambrano 
# Docente: Ing. CARLOS ANDRES AREVALO TORRES
# Materia: Lógica de Programación
# ====================================================================

# ESTRUCTURA DE DATOS: Un diccionario con los datos del cliente
cliente = {
    "nombre": "Alexander",
    "pin": "2323",
    "saldo": 1000.0
}

# ESTRUCTURA DE DATOS: Una lista para el historial de transacciones
historial_transacciones = []

# ====================================================================
# SECCIÓN DE FUNCIONES (Bloques ordenados con def)
# ====================================================================

def consultar_saldo():
    print()
    print("Tu saldo actual es de: $", cliente["saldo"])
    print()
    historial_transacciones.append("Consulta de saldo")

def depositar_dinero():
    try:
        depositar = float(input("Ingrese la cantidad a depositar: "))
        # VALIDACIÓN RECOMENDADA: El monto debe ser estrictamente positivo
        if depositar > 0:
            cliente["saldo"] = cliente["saldo"] + depositar
            print("El deposito fue exitoso")
            print()
            historial_transacciones.append("Deposito realizado")
        else:
            print("Error: No puede ingresar cantidades negativas o equivalentes a cero.")
            print()
    except ValueError:
        print("Error: Por favor, ingrese un valor numerico valido.")
        print()

def retirar_dinero():
    try:
        dinero_retirado = float(input("Ingresa la cantidad que deseas retirar: "))
        # VALIDACIÓN RECOMENDADA: Controlar que no ingresen números negativos o cero
        if dinero_retirado <= 0:
            print("Error: La cantidad a retirar debe ser un numero positivo mayor a cero.")
            print()
        elif dinero_retirado > cliente["saldo"]:
            print("Lo sentimos, no tienes fondos suficientes!!")
            print()
        else:
            cliente["saldo"] = cliente["saldo"] - dinero_retirado
            print("Retiro exitoso")
            print()
            historial_transacciones.append("Retiro realizado")
    except ValueError:
        print("Error: Por favor, ingrese un valor numerico valido.")
        print()

def mostrar_recibo_final():
    print()
    print("-----------------------------------------")
    print("       RESUMEN DE TRANSACCIONES          ")
    print("-----------------------------------------")
    
    if len(historial_transacciones) == 0:
        print("No se realizaron movimientos en esta sesion.")
    else:
        for movimiento in historial_transacciones:
            print("-", movimiento)
            
    print("Saldo final: $", cliente["saldo"])
    print("-----------------------------------------")
    print("Por favor, retire su tarjeta y espere su recibo")
    print("Gracias por preferirnos")
    print("-----------------------------------------")

# ====================================================================
# BLOQUE PRINCIPAL (Inicio del programa)
# ====================================================================

intentos_restantes = 3
autenticado = False

# Bucle de seguridad para el PIN
while intentos_restantes > 0:
    pin_ingresado = input("Estimado cliente, digite su pin de 4 digitos para acceder al portal: ")
    
    if pin_ingresado == cliente["pin"]:
        print("AUTENTICACIÓN CON EXITO")
        print("Accediendo.....")
        print()
        autenticado = True
        break
    else:
        intentos_restantes = intentos_restantes - 1
        print("PIN INCORRECTO")
        print()
else:
    print("-----------------------------------------")
    print("Lo sentimos, has agotado tus 3 intentos.")
    print("Tu tarjeta ha sido retenida por seguridad.")
    print("-----------------------------------------")

# Menú principal
if autenticado:
    ejecutando = True
    lista = ["1.Consultar saldo", "2.Depositar dinero", "3.Retirar dinero", "4.Salir"]
    
    print("-----------------------------------------")
    print("BIENVENIDO ALEXANDER, QUE GUSTO VERTE")
    print("    Banco del desarrollador")
    print("-----------------------------------------")
    
    while ejecutando:
        print("ESCOGE LA ACCIÓN A REALIZAR: ")
        for opcion_menu in lista:
            print(opcion_menu)
            
        opcion = input()
        
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar_dinero()
        elif opcion == "3":
            retirar_dinero()
        elif opcion == "4":
            ejecutando = False
            calificacion = input("En una escala del 1 al 10 como calificarias nuestro sistema?: ")
            mostrar_recibo_final()
        else:
            print("Opcion invalida debes presionar numeros del 1 al 4 según tu necesidad")
            print()
