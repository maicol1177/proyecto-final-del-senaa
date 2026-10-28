
asignaturas = ("matematicas","quimica","fisica","historia","lengua")
for asignatura in asignaturas [:]:
    Nota = float(input( f" ¿que nota saco en {asignatura}?" ))
    if Nota >= 5 :
      asignaturas.remove(asignaturas)
print("\nasignaturas que tienes que repetir:")
for asignatura in asignaturas :
    print(asignatura)

