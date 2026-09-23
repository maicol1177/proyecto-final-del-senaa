# Ejercicio 1
Algoritmo sin_titulo
	escribir "digite su numero"
	leer num
	contador = 0
	mientras num > 0 Hacer
		escribir "digite su numero"
		leer num
		contador = contador + 1
		si num < 0 entonces 
			escribir "su numero es negativo"
		FinSi
	FinMientras
	escribir "numeros escritos en total: ", contador
FinAlgoritmo


## Ejercicio 2
Algoritmo sin_titulo
	escribir "ingrese la cantidad de articulos"
	leer n
	escribir "ingrese el precio del articulo"
	leer precio
	para i = 2 hasta n Hacer
		escribir "ingrese el precio del articulo 1 " 
		leer valol
		si valol > mayod Entonces
			mayod = valol
		FinSi
	FinPara
	escribir "el mayor es: " mayod
FinAlgoritmo


## Ejercicio 3
Algoritmo sin_titulo
	escribir "digite su numero"
	leer num
	suma = 0 
	Repetir
		digito = numero mod 10
		suma = suma + digito
		numero = numero / 10
	Hasta Que numero = 0
	escribir "la suma de los digitos es", suma
FinAlgoritmo