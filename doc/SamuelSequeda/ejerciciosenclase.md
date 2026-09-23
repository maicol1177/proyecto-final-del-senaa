## Ejercicio en Visual Basic 
Sub programa()
   a = inputBox("Cuantos años tienes")
    MsgBox("Tu edad es & a & años")
    endsub
 ## Ejercicio en Dart
import 'dart:io';

void main() {
  print('¿Cuántos años tienes?');
  int a = int.parse(stdin.readLineSync()!);

  print('Tu edad es $a años');
}
## Ejercicio en java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("¿Cuántos años tienes? ");
        int a = sc.nextInt();

        System.out.println("Tu edad es " + a + " años");

        sc.close();
    }
}
### investigacion de porque java es diferente
¿Por qué Java es diferente de otros lenguajes de programación?

Java es un lenguaje de programación que tiene características diferentes a otros lenguajes como Visual Basic, C++ o Dart. Estas diferencias se deben principalmente a la forma en que fue diseñado y a la manera en que ejecuta los programas.

Una de las principales diferencias es que Java utiliza una Máquina Virtual de Java (JVM). Cuando escribimos un programa en Java, el código se transforma en un formato llamado bytecode. Este puede ser ejecutado por la JVM en diferentes sistemas operativos. Por eso Java utiliza la idea de “escribir una vez y ejecutar en cualquier lugar”.

Otra diferencia importante es la sintaxis. Cada lenguaje tiene sus propias reglas para escribir instrucciones. Por ejemplo, en Visual Basic se puede utilizar & para unir texto y variables, mientras que en Java se utiliza +. Por esta razón, aunque dos programas hagan exactamente lo mismo, pueden escribirse de manera diferente.

Java también está basado principalmente en la programación orientada a objetos. Esto significa que los programas normalmente se organizan mediante clases y objetos. Incluso un programa pequeño, como uno que pregunta la edad de una persona, suele utilizar una clase y un método main.

Además, Java tiene un sistema de tipos estático y fuerte, por lo que normalmente debemos indicar qué tipo de dato estamos utilizando. Por ejemplo:

int edad = 18;


Aquí int indica que la variable edad almacena un número entero.

En conclusión, Java es diferente porque tiene su propia sintaxis, utiliza la JVM para ejecutar los programas y está diseñado alrededor de la programación orientada a objetos. Estas características hacen que al principio pueda parecer más complicado que lenguajes como Visual Basic, pero también permiten crear programas grandes, organizados y que pueden ejecutarse en diferentes plataformas.
    
