
import 'dart:io';

void main() {
  List<double> notas = [];

  stdout.write('Nombre del estudiante: ');
  String nombre = stdin.readLineSync() ?? 'Estudiante';

  stdout.write('¿Cuántas notas deseas ingresar?: ');
  int cantidad = int.tryParse(stdin.readLineSync() ?? '') ?? 0;

  if (cantidad <= 0) {
    print('Debes ingresar una cantidad válida de notas.');
    return;
  }

  for (int i = 0; i < cantidad; i++) {
    while (true) {
      stdout.write('Ingresa la nota ${i + 1} (0 a 5): ');
      double? nota = double.tryParse(stdin.readLineSync() ?? '');

      if (nota != null && nota >= 0 && nota <= 5) {
        notas.add(nota);
        break;
      } else {
        print('Nota inválida. Intenta de nuevo.');
      }
    }
  }

  double suma = notas.reduce((a, b) => a + b);
  double promedio = suma / notas.length;

  double notaMaxima = notas.reduce((a, b) => a > b ? a : b);
  double notaMinima = notas.reduce((a, b) => a < b ? a : b);

  print('\n=== RESULTADOS ===');
  print('Estudiante: $nombre');
  print('Notas: $notas');
  print('Promedio: ${promedio.toStringAsFixed(2)}');
  print('Nota más alta: $notaMaxima');
  print('Nota más baja: $notaMinima');

  if (promedio >= 3.0) {
    print('Estado: APROBADO');
  } else {
    print('Estado: REPROBADO');
  }
}
