En PseInt, los ciclos (o bucles) son estructuras de control que permiten repetir un conjunto de instrucciones varias veces. Existen 3 ciclos principales:

1. Ciclo Mientras (Mientras ... Hacer)
Cómo funciona: Evalúa una condición antes de ejecutar el código. Si la condición es verdadera, ejecuta las instrucciones y vuelve a evaluar. Si desde el inicio es falsa, nunca se ejecuta.

Cuándo usarlo: Cuando no sabes cuántas veces se repetirá el proceso y depende de que una condición se cumpla.

Sintaxis:

Code snippet
Mientras condicion Hacer
    // Instrucciones a repetir
FinMientras


2. Ciclo Repetir (Repetir ... Hasta Que)
Cómo funciona: Ejecuta el bloque de código al menos una vez y evalúa la condición al final. El bucle se detiene cuando la condición se vuelve verdadera.

Cuándo usarlo: Cuando necesitas que el código se ejecute sí o sí una vez (por ejemplo, al mostrar un menú de opciones o validar una entrada de datos).

Sintaxis:

Code snippet
Repetir
    // Instrucciones a repetir
Hasta Que condicion


3. Ciclo Para (Para ... Hasta ... Con Paso)
Cómo funciona: Utiliza una variable contadora que incrementa (o decrementa) automáticamente desde un valor inicial hasta un valor final.

Cuándo usarlo: Cuando sabes exactamente cuántas veces se debe repetir el bloque de código.

Sintaxis:

Code snippet
Para variable <- inicio Hasta fin Con Paso paso Hacer
    // Instrucciones a repetir
FinPara.