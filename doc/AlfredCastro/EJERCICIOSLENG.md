## Ejercicio de visual basic
Sub programa()
   a = inputBox("Cuantos años tienes")
    MsgBox("Tu edad es & a & años")
    endsub  
 ### ejercicio de dart
     import 'dart:io';

void main() {
  print('¿Cuántos años tienes?');
  int a = int.parse(stdin.readLineSync()!);

  print('Tu edad es + a + años');
}
#### Ejercicio de java
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
##### investigacion
¿Por qué Java es diferente?

Java es diferente de otros lenguajes porque tiene una forma particular de escribir y ejecutar los programas. Una de sus características principales es que utiliza la JVM (Java Virtual Machine), que permite ejecutar el mismo programa en diferentes sistemas operativos.

También tiene una sintaxis propia. Por ejemplo, para unir texto con una variable Java utiliza el símbolo +, mientras que otros lenguajes pueden utilizar símbolos diferentes.

Además, Java trabaja principalmente con clases y objetos, por lo que incluso los programas sencillos suelen tener una estructura más organizada.

En conclusión, Java se diferencia por su sintaxis, su forma de ejecución mediante la JVM y su uso de la programación orientada a objetos.
