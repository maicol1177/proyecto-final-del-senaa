# Investigación: Conceptos básicos de Python
1. Introducción

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Fue creado por Guido van Rossum y publicado inicialmente en 1991. Su diseño busca que el código sea fácil de leer y escribir, por lo que es uno de los lenguajes más utilizados para aprender programación.

Python puede utilizarse para desarrollar aplicaciones, páginas web, automatización de tareas, análisis de datos, inteligencia artificial, videojuegos y muchas otras áreas.

2. ¿Qué es Python?

Python es un lenguaje de programación que permite dar instrucciones a un computador para realizar diferentes tareas.

Una de sus principales características es que utiliza una sintaxis sencilla y cercana al lenguaje humano. Por ejemplo:

print("Hola, mundo")


Este programa muestra el texto "Hola, mundo" en la pantalla.

3. Características principales de Python

Entre las características más importantes de Python se encuentran:

Fácil de aprender: su sintaxis es relativamente sencilla para los principiantes.
Legible: el código está diseñado para ser fácil de entender.
Multiplataforma: puede utilizarse en Windows, macOS y Linux.
Interpretado: el código puede ejecutarse sin necesidad de compilarlo previamente de la misma manera que ocurre con algunos otros lenguajes.
Multipropósito: sirve para diferentes tipos de proyectos.
Gran cantidad de librerías: existen numerosas herramientas que permiten ampliar las capacidades del lenguaje.
Orientado a objetos: permite trabajar con clases y objetos.
Código abierto: Python cuenta con una comunidad mundial de desarrolladores.
4. Variables

Una variable es un espacio donde podemos almacenar información.

En Python no es necesario declarar previamente el tipo de una variable:

nombre = "Carlos"
edad = 20
altura = 1.75


En este ejemplo:

nombre almacena un texto.
edad almacena un número entero.
altura almacena un número decimal.

Los nombres de las variables deben ser claros y seguir las reglas de escritura de Python.

5. Tipos de datos básicos

Python posee diferentes tipos de datos. Los más importantes para comenzar son:

String (str)

Se utiliza para almacenar texto.

nombre = "Juan"

Enteros (int)

Representan números sin decimales.

edad = 18

Decimales (float)

Representan números con decimales.

precio = 15.50

Booleanos (bool)

Representan dos valores:

activo = True


Los valores booleanos son True y False.

6. Entrada de datos

La función input() permite recibir información introducida por el usuario.

nombre = input("¿Cuál es tu nombre? ")
print("Hola", nombre)


Es importante recordar que input() devuelve inicialmente un texto. Si necesitamos recibir un número, podemos convertirlo:

edad = int(input("¿Cuál es tu edad? "))

7. Salida de datos

La función print() permite mostrar información en la pantalla.

nombre = "Ana"
edad = 20

print(nombre)
print(edad)


También podemos combinar texto y variables utilizando f-strings:

nombre = "Ana"
edad = 20

print(f"Mi nombre es {nombre} y tengo {edad} años.")

8. Operadores

Los operadores permiten realizar operaciones con los datos.

Operadores aritméticos
a = 10
b = 3

print(a + b)  # Suma
print(a - b)  # Resta
print(a * b)  # Multiplicación
print(a / b)  # División
print(a // b) # División entera
print(a % b)  # Módulo
print(a ** b) # Potencia

Operadores de comparación

Se utilizan para comparar valores:

a == b   # Igual
a != b   # Diferente
a > b    # Mayor que
a < b    # Menor que
a >= b   # Mayor o igual
a <= b   # Menor o igual


El resultado de una comparación es True o False.

9. Condicionales

Los condicionales permiten que un programa tome decisiones.

El principal condicional es if:

edad = 18

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


También podemos utilizar elif para evaluar diferentes posibilidades:

nota = 4

if nota >= 4.5:
    print("Excelente")
elif nota >= 3:
    print("Aprobado")
else:
    print("Reprobado")


La indentación es fundamental en Python, porque permite indicar qué instrucciones pertenecen a un bloque de código.

10. Bucles

Los bucles permiten repetir instrucciones.

Bucle for

Se utiliza cuando queremos recorrer una secuencia o repetir una acción un número determinado de veces.

for i in range(5):
    print(i)


El resultado será:

0
1
2
3
4

Bucle while

Se ejecuta mientras una condición sea verdadera:

contador = 0

while contador < 5:
    print(contador)
    contador += 1

11. Listas

Las listas permiten almacenar varios valores dentro de una misma variable.

frutas = ["manzana", "pera", "banana"]

print(frutas[0])


Las posiciones de una lista comienzan desde 0, por lo que frutas[0] corresponde a "manzana".

También podemos agregar elementos:

frutas.append("naranja")


Y eliminar elementos:

frutas.remove("pera")

12. Funciones

Las funciones permiten organizar el código y reutilizar instrucciones.

Se crean utilizando def:

def saludar():
    print("Hola, bienvenido")

saludar()


Las funciones también pueden recibir parámetros:

def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Carlos")


Y pueden devolver un resultado mediante return:

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)

13. Diccionarios

Los diccionarios almacenan información mediante pares de clave y valor.

persona = {
    "nombre": "Carlos",
    "edad": 20,
    "ciudad": "Barranquilla"
}

print(persona["nombre"])


Son muy utilizados para representar información estructurada.

14. Comentarios

Los comentarios sirven para explicar el código y no son ejecutados por Python.

# Este es un comentario
nombre = "Carlos"


Los comentarios son útiles para documentar programas y facilitar su mantenimiento.

15. Módulos y librerías

Python permite utilizar módulos y librerías para agregar funcionalidades.

Por ejemplo, el módulo math proporciona diferentes funciones matemáticas:

import math

resultado = math.sqrt(25)
print(resultado)


El uso de librerías permite desarrollar programas más completos sin tener que crear todas las funcionalidades desde cero.

16. Manejo de errores

Los errores pueden ocurrir durante la ejecución de un programa. Python permite manejarlos mediante try y except.

try:
    numero = int(input("Ingrese un número: "))
    print(10 / numero)
except ValueError:
    print("Debe ingresar un número válido.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")


Esto permite evitar que determinados errores detengan inesperadamente el programa.

17. Ejemplo de un programa básico

El siguiente programa combina varios conceptos fundamentales:

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    mensaje = "eres mayor de edad"
else:
    mensaje = "eres menor de edad"

print(f"Hola {nombre}, {mensaje}.")

for numero in range(1, 4):
    print(f"Número: {numero}")


En este ejemplo se utilizan:

Variables.
Entrada de datos.
Conversión de tipos.
Condicionales.
Bucles for.
Función print().
F-strings.
18. Importancia de aprender Python

Aprender Python permite desarrollar una base sólida en programación. Sus conceptos fundamentales, como variables, tipos de datos, condicionales, ciclos, funciones y estructuras de datos, son esenciales para aprender a resolver problemas mediante código.

Además, Python tiene aplicaciones profesionales en áreas como:

Desarrollo web.
Automatización.
Ciencia de datos.
Inteligencia artificial.
Machine Learning.
Desarrollo de software.
Ciberseguridad.
Administración de sistemas.
Análisis de información.
19. Conclusión

Python es un lenguaje de programación adecuado tanto para principiantes como para desarrolladores profesionales. Su sintaxis sencilla facilita el aprendizaje de los fundamentos de la programación y permite avanzar posteriormente hacia proyectos más complejos.

Para aprender Python correctamente no basta con memorizar instrucciones. Es necesario practicar, desarrollar pequeños proyectos, cometer errores y aprender a solucionarlos. La perseverancia y la voluntad de aprender son fundamentales para convertirse progresivamente en un buen programador.

Por esta razón, dominar conceptos como variables, tipos de datos, operadores, condicionales, ciclos, listas, diccionarios y funciones constituye una excelente base para comenzar una carrera en programación.