def cel_fah(ce):
    resultado = (ce * 9/5) + 32
    return resultado
def temperatura(celsius):
    if celsius < 0:
        return "Temperatura bajo cero"
    if celsius < 15:
        return "Temperatura baja"
    if celsius < 25:
        return "Temperatura media"
    if celsius < 35:
        return "Temperatura alta"
    if celsius < 45:
        return "Temperatura muy alta"
    if celsius >= 45:
        return "Temperatura extremadamente alta"

grados = float(input("Ingrese los grados Celsius: "))
farenheit = cel_fah(grados)
sensacion = temperatura(grados)
print(f"Los {grados} grados Celsius equivalen a {farenheit} grados Fahrenheit.")
print(f"La sensación térmica es: {sensacion}")
print("¡Gracias por usar el programa!")