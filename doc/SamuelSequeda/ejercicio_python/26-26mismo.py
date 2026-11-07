


estudiantes = [
    "Carlos", "Maria", "Juan", "Laura",
    "Pedro", "Ana", "Sofia", "Andres"
]

notas = [4.5, 2.8, 3.7, 4.0, 2.5, 4.8, 3.0, 1.9]


print("===== LISTA DE ESTUDIANTES =====")

for i in range(len(estudiantes)):
    print(estudiantes[i], "-", notas[i])


suma = 0

for nota in notas:
    suma += nota

promedio = suma / len(notas)
print("\nPromedio general:", round(promedio, 2))

print("Nota mas alta:", max(notas))
print("Nota mas baja:", min(notas))


aprobados = []
reprobados = []

for i in range(len(notas)):
    if notas[i] >= 3.0:
        aprobados.append(estudiantes[i])
    else:
        reprobados.append(estudiantes[i])

print("\nEstudiantes aprobados:")
for nombre in aprobados:
    print(nombre)

print("\nEstudiantes reprobados:")
for nombre in reprobados:
    print(nombre)

print("Total de aprobados:", len(aprobados))
print("Total de reprobados:", len(reprobados))

notas_ordenadas = sorted(notas)
print("\nNotas de menor a mayor:", notas_ordenadas)


busqueda = input("\nEscribe el nombre del estudiante que buscas: ")
encontrado = False

for i in range(len(estudiantes)):
    if estudiantes[i].lower() == busqueda.lower():
        print("Nota de", estudiantes[i], ":", notas[i])
        encontrado = True

if not encontrado:
    print("Estudiante no encontrado.")


modificar = input("\n¿Quieres modificar una nota? (si/no): ")

if modificar.lower() == "si":
    nombre = input("Nombre del estudiante: ")
    encontrado = False

    for i in range(len(estudiantes)):
        if estudiantes[i].lower() == nombre.lower():
            nueva_nota = float(input("Escribe la nueva nota (0 a 5): "))

            if 0 <= nueva_nota <= 5:
                notas[i] = nueva_nota
                print("Nota actualizada correctamente.")
            else:
                print("La nota debe estar entre 0 y 5.")

            encontrado = True
            break

    if not encontrado:
        print("Estudiante no encontrado.")


print("\n===== INFORME FINAL =====")

suma = 0
aprobados_final = 0
reprobados_final = 0

for i in range(len(estudiantes)):
    print(estudiantes[i], "-", notas[i])
    suma += notas[i]

    if notas[i] >= 3.0:
        aprobados_final += 1
    else:
        reprobados_final += 1

print("Promedio final:", round(suma / len(notas), 2))
print("Aprobados:", aprobados_final)
print("Reprobados:", reprobados_final)
print("Nota maxima:", max(notas))
print("Nota minima:", min(notas))
