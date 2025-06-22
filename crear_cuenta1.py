def crear_cuenta():
    print("\n--- Inicio ---\n")
    print("Crear cuenta\n")
    
    nombre = input("Nombre: ")
    while not nombre:
        print("Debe ingresar un nombre")
        nombre = input("Nombre: ")
    
    apellido = input("Apellido: ").lower()
    while not apellido:
        print("Debe de ingresar un apellido")
        apellido = input("Apellido: ").lower()
    
    print("\nCrear contraseña")
    contraseña_valida = False
    
    while not contraseña_valida:
        contraseña = input("Contraseña: ")
        
        if len(contraseña) < 6:
            print("No válida (Contraseña)")
            print("La contraseña debe tener al menos 6 caracteres")
        else:
            contraseña_valida = True
    
    print("\nCuenta creada")
    print(f"\nResumen:")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print("Estado de la cuenta: Activa")

if __name__ == "__main__":
    crear_cuenta()