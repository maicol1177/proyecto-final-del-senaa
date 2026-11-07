Asignaturas = ["Matematicas","Fisica","Sociales","Ingles","Quimica"]
notas = []
for asignatura in asignaturas:
    nota = input(f"Que nota has sacado en {asignatura}?:")
    notas.append(nota)
print("\n--- Resultados del curso---")
for i in range(len(asignaturas)):
    print(f"En {asignaturas [i]} has sacado {notas[i]}")