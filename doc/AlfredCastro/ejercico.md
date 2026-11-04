
## ejercicio echo con zahedys


nversion = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en porcentaje): "))
anos = int(input("Introduce el número de años: "))

print("\n--- Evolución de la inversión ---")


for i in range(1, anos + 1):
    inversion *= 1 + interes / 1000
    print(f"Año {i}: {inversion:.2f} de capital")