# Ejercicio de python

n1 = float(input ("digite su nota 1: "))
n2 = float(input ("digite su nota 2: "))
n3 = float(input ("digite su nota 3: "))
n4 = float(input ("digite su nota 4: "))
n5 = float(input ("digite su nota 5: "))
promedio = (n1 + n2 + n3 + n4 + n5) / 5
print(f"el promedio es: {promedio}")

## Ejercicio de dartpad

import 'dart:io';

void main(){

print("ingrese la nota: 1");
double n1 = double.parse(stdin.readLineSync()!);
print(n1);

print("ingrese la nota: 2");
double n2 = double.parse(stdin.readLineSync()!);
print(n2);

print("ingrese la nota: 3");
double n3 = double.parse(stdin.readLineSync()!);
print(n3);

print("ingrese la nota: 4");
double n4 = double.parse(stdin.readLineSync()!);
print(n4);

print("ingrese la nota: 5");
double n5 = double.parse(stdin.readLineSync()!);
print(n5);

double promedio = (n1 + n2 + n3 + n4 + n5) / 5;
print("el promedio es: $promedio");
}