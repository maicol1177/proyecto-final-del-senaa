# Ejercicio visual basic

Sub cagada()
   A = InputBox("¿cuantos años tienes?")
   MsgBox ("EL INTRUCTOR HENRY TIENE " & A & " AÑOS ")
End Sub

## Ejercicios dartpad

void main() {
   String a = "60";
  print("el instructor henry tiene " + a + " años");
}

## Ejercicio javascript

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("¿Cuántos años tienes? ");
        int edad = scanner.nextInt();

        if (edad >= 18) {
            System.out.println("Eres mayor de edad");
        } else {
            System.out.println("Eres menor de edad");
        }
    }
}