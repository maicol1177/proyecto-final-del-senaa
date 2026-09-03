# Tres ejercicios resueltos en PSeInt

## 1. Sumar dos números

```pseudocode
Algoritmo SumarDosNumeros
    Definir num1, num2, resultado Como Real

    Escribir "Ingrese el primer número:"
    Leer num1

    Escribir "Ingrese el segundo número:"
    Leer num2

    resultado <- num1 + num2

    Escribir "La suma es: ", resultado
FinAlgoritmo
Algoritmo NumeroParOImpar
    Definir numero Como Entero

    Escribir "Ingrese un número:"
    Leer numero

    Si numero MOD 2 = 0 Entonces
        Escribir "El número es par"
    SiNo
        Escribir "El número es impar"
    FinSi
FinAlgoritmo
Algoritmo CalcularPromedio
    Definir nota1, nota2, nota3, promedio Como Real

    Escribir "Ingrese la primera nota:"
    Leer nota1

    Escribir "Ingrese la segunda nota:"
    Leer nota2

    Escribir "Ingrese la tercera nota:"
    Leer nota3

    promedio <- (nota1 + nota2 + nota3) / 3

    Escribir "El promedio es: ", promedio
FinAlgoritmo