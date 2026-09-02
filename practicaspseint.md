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