## Ejercicios de pseint

### primer ejercicio

Algoritmo SumaDosNumeros
    Definir num1, num2, suma Como Entero
    
    Escribir "Ingresa el primer número:"
    Leer num1
    
    Escribir "Ingresa el segundo número:"
    Leer num2
    
    suma <- num1 + num2
    
    Escribir "El resultado de la suma es: ", suma
FinAlgoritmo

### segundo ejercicio

Algoritmo TablaMultiplicar
    Definir num, i, resultado Como Entero
    Escribir "Ingrese el número de la tabla que desea ver:"
    Leer num
    Escribir "Tabla del ", num, ":"
    Para i <- 1 Hasta 10 Con Paso 1 Hacer
        resultado <- num * i
        Escribir num, " x ", i, " = ", resultado
    FinPara
FinAlgoritmo
