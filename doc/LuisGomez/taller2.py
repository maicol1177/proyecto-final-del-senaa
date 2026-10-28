cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años? "))

for año in range(1, años + 1):
    cantidad = cantidad * (1 + interes / 100)
    print(f"Capital tras {año} años: {cantidad}")