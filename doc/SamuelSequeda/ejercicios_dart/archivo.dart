import 'dart:io';
void main() {
  print('ingrese la nota 1');
  double nota1 = double.parse(stdin.readLineSync()!);
  print('ingrese la nota 2');
  double nota2 = double.parse(stdin.readLineSync()!);
  print('ingrese la nota 3');
  double nota3 = double.parse(stdin.readLineSync()!);
  print('ingrese la nota 4');
  double nota4 = double.parse(stdin.readLineSync()!);
  print('ingrese la nota 5');
  double nota5 = double.parse(stdin.readLineSync()!);
  double promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5;
  print('El promedio es: $promedio');
}
