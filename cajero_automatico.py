# ====================================================================
# TAREA: APRENDIZAJE AUTÓNOMO 2 - LÓGICA DE PROGRAMACIÓN
# PROGRAMA: SIMULADOR DE CAJERO AUTOMÁTICO (ATM)
# ====================================================================

# Configuración inicial del sistema (Variables globales simuladas)
saldo_disponible = 500.00  # Cuenta con un saldo inicial de $500
pin_correcto = "2026"      # PIN secreto para el acceso
intentos_restantes = 3     # Límite de seguridad para el usuario
autenticado = False

print("=========================================")
print("       BIENVENIDO BANCO NACIONAL         ")
print("=========================================")

# --------------------------------------------------------------------
# 1. CONTROL DE ACCESO: Estructura repetitiva y condicional para seguridad
# --------------------------------------------------------------------
while intentos_restantes > 0:
    pin_ingresado = input(f"Por favor, ingrese su PIN de 4 dígitos (Intentos: {intentos_restantes}): ")
    
    if pin_ingresado == pin_correcto:
        print("\n[ÉXITO] ¡PIN Correcto! Accediendo al sistema...\n")
        autenticado = True
        break  # Rompe el bucle de intentos si el PIN es correcto
    else:
        intentos_restantes -= 1
        print("[ERROR] PIN incorrecto. Intente nuevamente.\n")

# --------------------------------------------------------------------
# 2. INTERFAZ Y OPERACIONES: Menú interactivo (Bucle principal del cajero)
# --------------------------------------------------------------------
if autenticado:
    ejecutando_programa = True
    
    while ejecutando_programa:
        print("---------- MENÚ DE OPERACIONES ----------")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Salir del Cajero")
        print("-----------------------------------------")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        # --- CONDICIONAL: Opción 1 - Consulta de Saldo ---
        if opcion == "1":
            print(f"\n[SALDO] Su saldo actual disponible es de: ${saldo_disponible:.2f}\n")
            
        # --- CONDICIONAL: Opción 2 - Depósito de Fondos ---
        elif opcion == "2":
            monto_deposito = float(input("\nIngrese el monto en efectivo a depositar: $"))
            if monto_deposito > 0:
                saldo_disponible += monto_deposito  # Suma el monto ingresado al saldo existente
                print(f"[ÉXITO] Depósito procesado. Se han abonado ${monto_deposito:.2f} a su cuenta.\n")
            else:
                print("[ERROR] El monto a depositar debe ser mayor a $0.00.\n")
                
        # --- CONDICIONAL: Opción 3 - Retiro de Efectivo (Con Validación Crítica) ---
        elif opcion == "3":
            monto_retiro = float(input("\nIngrese el monto que desea retirar: $"))
            
            # Validación de Seguridad: Evita sobregiros o retirar valores negativos
            if monto_retiro <= 0:
                print("[ERROR] El monto a retirar debe ser mayor a $0.00.\n")
            elif monto_retiro > saldo_disponible:
                print("\n[RECHAZADO] Fondos insuficientes. No puede retirar más de su saldo actual.\n")
            else:
                saldo_disponible -= monto_retiro  # Resta el monto retirado del saldo disponible
                print(f"[ÉXITO] Transacción aprobada. Retire sus ${monto_retiro:.2f} de la ranura.\n")
                
        # --- CONDICIONAL: Opción 4 - Salida del Sistema ---
        elif opcion == "4":
            print("\n[CIERRE] Retire su tarjeta. Gracias por confiar en nosotros, ¡buen día!")
            ejecutando_programa = False  # Cambia el estado a False para finalizar el bucle principal
            
        # --- Manejo de errores por si digitan cualquier otra cosa ---
        else:
            print("[OPCIÓN INVÁLIDA] Por favor, ingrese un número del 1 al 4.\n")
else:
    print("=========================================")
    print("[BLOQUEADO] Cuenta suspendida temporalmente.")
    print("=========================================")
