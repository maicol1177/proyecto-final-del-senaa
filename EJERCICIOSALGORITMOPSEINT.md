## Ejercicios pseint

### Primer ejercicio

Algoritmo areadecincunferencia 
	Escribir " digite el valor a" 
	leer a 
	Escribir " digite el valor b " 
	leer b 
	Escribir " digite el valor c " 
	leer c 
	ter = b ^ 2 - 4 * a * c 
	r = raiz ( term) 
	resultado1 = ( - b + r ) / 2 * a 
	resultado2 = ( - b - r ) / 2 * a 
	Escribir " el resultado es: " resultado 
	Escribir " el resultado es : " resultado2
	Finalgoritmo

	### segundo ejercicio

Algoritmo sin_titulo
	Escribir " area del cadro"
	leer lado 
	area = lado * 4 
	Escribir " area del cuadrado es :" area 
	
FinAlgoritmo

### tercer ejercicio
# Ejercicio Básico de Vectores

## Planteamiento del problema
Un barco navega **4 km hacia el Este** y luego **3 km hacia el Norte**. 

Calcula:
1. La **magnitud** (módulo) del vector desplazamiento resultante.
2. La **dirección** (ángulo $\theta$) respecto al Este.

---

## Solución Paso a Paso

### 1. Representación de los componentes
* Componente en $x$ ($A_x$): $4\text{ km}$ (Este)
* Componente en $y$ ($A_y$): $3\text{ km}$ (Norte)

### 2. Magnitud del vector ($|\vec{R}|$)
Usamos el **Teorema de Pitágoras**:

$$|\vec{R}| = \sqrt{A_x^2 + A_y^2}$$

$$|\vec{R}| = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5\text{ km}$$

### 3. Dirección ($\theta$)
Usamos la función **arcotangente**:

$$\theta = \tan^{-1}\left(\frac{A_y}{A_x}\right)$$

$$\theta = \tan^{-1}\left(\frac{3}{4}\right) \approx 36.87^\circ$$