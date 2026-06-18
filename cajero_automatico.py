# ====================================================================
# TAREA: APRENDIZAJE AUTÓNOMO 2 - SIMULADOR DE CAJERO AUTOMÁTICO
# Estudiante: Alexander Zambrano 
# Docente: Ing. CARLOS ANDRES AREVALO TORRES
# Materia: Lógica de Programación
# ====================================================================

# Variables globales para el control del estado y saldo del cajero
saldo_disponible = 1000
pin_correcto = "2323"
intentos_restantes = 3
autenticado = False

# Bucle de seguridad para validar el acceso con un límite de 3 intentos
while intentos_restantes > 0:
    pin_ingresado = input("Estimado cliente, digite su pin de 4 digitos para accder a la portal: ")

    # Validación del PIN ingresado por el usuario
    if pin_ingresado == pin_correcto:
        print("AUTENTICACIÓN CON EXITO")
        print("Accediendo.....")
        autenticado = True
        break  # Rompe el bucle si el pin es correcto
    else:
        intentos_restantes -= 1
        print("PIN INCORRECTO")
else:
    # Mensaje de seguridad si el ususario agoto todos sus intentos disponibles
    print("-----------------------------------------")
    print("Lo sentimos, has agotado tus 3 intentos.")
    print("Tu tarjeta ha sido retenida por seguridad.")
    print("-----------------------------------------")

# Bloque principal de operaciones que solo es ejecutado si la autenticación es valida
if autenticado:
    ejecutando = True
    lista = ["1.Consultar saldo","2.Depositar dinero", "3.Retirar dinero", "4.Salir"]
    
    print("-----------------------------------------")
    print("BIENVENIDO CLIENTE, QUE GUSTO VERTE")
    print("    Banco del desarrollador")
    print("-----------------------------------------")
    
    # Bucle repetitivo para mantener el menú activo hasta que el usuario decida salir
    while ejecutando:
        print("ESCOGE LA ACCIÓN A REALIZAR: ")
        
        # Bucle 'for' para mostrar dinámicamente las opciones de la lista
        for opcion_menu in lista:
            print(opcion_menu)

        opcion = input()
        
        # Opción 1: Consulta de fondos disponibles
        if opcion == "1":
            print("Tu saldo actual es de: ", saldo_disponible)

        # Opción 2: Depósito e incremento del saldo
        elif opcion == "2":
            depositar = float(input("Ingrese la cantidad a depositar: "))
            saldo_disponible = depositar + saldo_disponible
            print("El deposito fue exitoso")

        # Opción 3: Retiro con verificación de fondos insuficientes
        elif opcion == "3":
            dinero_retirado = float(input("Ingresa la cantidad que deseas retirar: "))
            if dinero_retirado > saldo_disponible:
                print("Lo sentimos, no tienes fondos suficientes!!")
            else:
                saldo_disponible = saldo_disponible - dinero_retirado
                print("Retiro exitoso")
                
        # Opción 4: Cierre de sesión 
        elif opcion == "4":
            ejecutando = False
            calificacion = input("En una escala del 1 al 10 como calificarias nuestro sistema?: ")
            print("-----------------------------------------")
            print("Por favor, retire su tarjeta y espere su recibo")
            print("Gracias por preferirnos")
            print("-----------------------------------------")
            
        # Manejo de excepciones para capturar entradas inválidas en el menú
        else:
            print("Opcion invalida debes presionar numeros del 1 al 4 según tu necesidad")
