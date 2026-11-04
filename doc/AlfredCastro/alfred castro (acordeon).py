
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]


asignaturas_pendientes = []


for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}?: "))
    
    
    if nota < 5:
        asignaturas_pendientes.append(asignatura)

print("\n--- Resultado ---")

#
if len(asignaturas_pendientes) > 0:
    print("Tienes que repetir las siguientes asignaturas:")
    for asignatura in asignaturas_pendientes:
        print(f"- {asignatura}")
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")