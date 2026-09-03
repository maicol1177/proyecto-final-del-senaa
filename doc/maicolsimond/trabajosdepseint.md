## ejercicio 1
Algoritmo departamentos
	Definir dep, mayoresDep, menoresDep Como Entero
	Definir totalMayores, totalMenores, totalPersonas Como Entero
	
	totalMayores <- 0
	totalMenores <- 0
	
	Para dep <- 1 Hasta 10 Con Paso 1 Hacer
		Escribir "--- Departamento ", dep, " ---"
		Escribir "Ingrese cantidad de personas mayores de edad (0 si está desocupado):"
		Leer mayoresDep
		
		Escribir "Ingrese cantidad de personas menores de edad (0 si está desocupado):"
		Leer menoresDep
		
		totalMayores <- totalMayores + mayoresDep
		totalMenores <- totalMenores + menoresDep
		
	FinPara
	totalPersonas <- totalMayores + totalMenores
	Escribir "--------------------------------------"
	Escribir "En el edificio viven ", totalPersonas, " personas."
	
	Si totalMayores > totalMenores Entonces
		Escribir "Viven más personas mayores y son ", totalMayores
	Sino
		Si totalMenores > totalMayores Entonces
			Escribir "Viven más personas menores y son ", totalMenores
		Sino
			Escribir "Hay la misma cantidad de personas mayores y menores (", totalMayores, " de cada una)."
		FinSi
	FinSi
FinAlgoritmo

## ejercicio 2
Algoritmo comision1
	Escribir "ingrese la cantidad de articulos de ventas (N)"
	leer N
	
	comisiontotal=0
	Para i = 1 hasta N con paso 1 Hacer
		Escribir "ingrese el monto de venta, " i ""
		leer venta
		Si Venta > 50000 Entonces
            ComisionTotal = ComisionTotal + (Venta * 0.07)
        Sino
			ComisionTotal = ComisionTotal + (venta * 0.05)
		FinSi
		Escribir "la comision total obtenida por el vendedor es: ", ComisionTotal
	FinPara
FinAlgoritmo

## ejercicio 3
Algoritmo preciomayor 
	Definir N, i Como Entero
	Definir precio, mayor Como Real
	
	Escribir "Ingrese la cantidad de artículos (N):"
	Leer N
	
	Si N <= 0 Entonces
		Escribir "La cantidad de artículos debe ser mayor a 0."
	Sino
		Para i <- 1 Hasta N Con Paso 1 Hacer
			Escribir "Ingrese el precio del artículo ", i, ":"
			Leer precio
			
			Si i = 1 O precio > mayor Entonces
				mayor <- precio
			FinSi
		FinPara
		
		Escribir "El precio del artículo de mayor valor es: ", mayor
	FinSi
FinAlgoritmo.
