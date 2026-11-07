numeros_secretos = [3, 7, 10, 12, 15, 18, 20, 5, 9, 14]

intentos = []
aciertos = []
fallos = []

print("===== JUEGO DE NUMEROS SECRETOS =====")
print("Debes adivinar los numeros secretos.")
print("Tienes 10 intentos y puedes elegir numeros del 1 al 20.")


for i in range(10):
    numero = int(input("\nIntento " + str(i + 1) + ": Escribe un numero: "))

    if numero < 1 or numero > 20:
        print("Error: el numero debe estar entre 1 y 20.")
        continue

    intentos.append(numero)

    if numero in numeros_secretos:
        print("¡Correcto! El numero esta en la lista secreta.")
        aciertos.append(numero)
    else:
        print("Fallaste. Ese numero no esta en la lista secreta.")
        fallos.append(numero)


print("\n===== RESULTADOS =====")

print("Numeros ingresados:", intentos)
print("Aciertos:", aciertos)
print("Fallos:", fallos)

print("Total de aciertos:", len(aciertos))
print("Total de fallos:", len(fallos))


if len(intentos) > 0:
    porcentaje = len(aciertos) / len(intentos) * 100
    print("Porcentaje de aciertos:", round(porcentaje, 2), "%")
else:
    print("No se registraron intentos validos.")


if len(intentos) > 0:
    print("Numero mas alto ingresado:", max(intentos))
    print("Numero mas bajo ingresado:", min(intentos))

    promedio = sum(intentos) / len(intentos)
    print("Promedio de los intentos:", round(promedio, 2))

aciertos_sin_repetir = []

for numero in aciertos:
    if numero not in aciertos_sin_repetir:
        aciertos_sin_repetir.append(numero)

aciertos_sin_repetir.sort()

print("Aciertos sin repetir:", aciertos_sin_repetir)

buscar = int(input("\n¿Qué numero quieres buscar en tus intentos?: "))

veces = intentos.count(buscar)

if veces > 0:
    print("Ingresaste el numero", buscar, veces, "veces.")
else:
    print("Ese numero no aparece en tus intentos.")

print("\nNumeros secretos:", numeros_secretos)

print("\n===== INFORME FINAL =====")
print("Intentos validos:", len(intentos))
print("Aciertos:", len(aciertos))
print("Fallos:", len(fallos))
print("Aciertos ordenados:", aciertos_sin_repetir)

if len(intentos) > 0:
    print("Porcentaje final:", round(len(aciertos) / len(intentos) * 100, 2), "%")

if len(aciertos) == len(intentos) and len(intentos) > 0:
    print("¡Excelente! Acertaste todos los intentos.")
elif len(aciertos) > 0:
    print("¡Bien hecho! Lograste algunos aciertos.")
else:
    print("No acertaste ningun numero esta vez.")
