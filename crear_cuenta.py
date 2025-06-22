def verificar_rut_chileno_simple(rut):
    if not isinstance(rut, str):
        return False
   
    try:
        numero_rut_str, dv_str = rut.split("-")
    except ValueError:
        return False 

    try:
        numero_rut = int(numero_rut_str)
    except ValueError:
        return False 

    dv_str = dv_str.lower()

    suma = 0
    multiplicador = 2
    temp_rut = numero_rut

    while temp_rut > 0:
        digito = temp_rut % 10
        suma += digito * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
        temp_rut //= 10

    dv_calculado_num = 11 - (suma % 11)

    if dv_calculado_num == 11:
        dv_calculado = '0'
    elif dv_calculado_num == 10:
        dv_calculado = 'k'
    else:
        dv_calculado = str(dv_calculado_num)

    return dv_str == dv_calculado


def existe_RUT(rut):
    return verificar_rut_chileno_simple(rut)

def contraseña_valida(contraseña):
    if len(contraseña) < 6:
        print("La contraseña debe tener al menos 6 caracteres.")
        return False
    return True

def crear_cuenta_completa():
    print("\n--- Inicio del proceso de creación de una cuenta ---")

    print("\n--- Registrando datos del usuario ---")
    apellido_paterno = input("Ingrese su Apellido paterno: ").title()
    apellido_materno = input("Ingrese su Apellido materno: ").title()

    rut_valido = False
    while not rut_valido:
        rut = input("Ingrese su RUT (ej. 12345678-9): ")
        if existe_RUT(rut): 
            rut_valido = True
            print("RUT válido y verificado.")
        else:
            print("RUT inválido o no existente. Intente de nuevo.")

    print(f"Datos registrados: Apellido Paterno = {apellido_paterno}, Apellido Materno = {apellido_materno}, RUT = A{rut}")

    print("\n--- Creación de Contraseña ---")
    contraseña_ok = False
    while not contraseña_ok:
        contraseña = input("Cree su contraseña: ")
        if contraseña_valida(contraseña):
            contraseña_ok = True
            print("Contraseña creada exitosamente.")
        else:
            print("La contraseña no cumple con los requisitos. Intente de nuevo.")
    
    print("\n--- Cuenta creada exitosamente ---")
    return True 

if __name__ == "__main__":
    print("Programa de Creación de Cuentas")
    
    continuar_creando_cuentas = True
    while continuar_creando_cuentas:
        creacion_exitosa = crear_cuenta_completa() 

        opcion = input("\n¿Desea crear otra cuenta? (Sí/No): ").lower()
        if opcion != 'si':
            continuar_creando_cuentas = False
            print("Finalizando el programa.")
        else:
            print("Preparando para crear otra cuenta...")

    print("\n--- Fin del programa ---")