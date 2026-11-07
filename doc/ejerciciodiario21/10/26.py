
saldo = 1000.0

while True:
    print("\n=== CAJERO AUTOMÁTICO ===")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo:.2f}")

    elif opcion == "2":
        cantidad = float(input("¿Cuánto deseas depositar?: $"))

        if cantidad > 0:
            saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
        else:
            print("La cantidad debe ser mayor que cero.")

    elif opcion == "3":
        cantidad = float(input("¿Cuánto deseas retirar?: $"))

        if cantidad <= 0:
            print("Ingresa una cantidad válida.")
        elif cantidad > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")

    elif opcion == "4":
        print("Gracias por usar el cajero.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
