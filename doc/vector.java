import java.util.Scanner;

public class vector {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        // Pedimos el número de posiciones
        System.out.print("Introduce el número de posiciones del vector: ");
        int n = teclado.nextInt();

        // Creamos el vector
        int[] vec = new int[n];

        // Pedimos los datos del vector
        for (int i = 0; i < n; i++) {
            System.out.print("Introduce el valor de la posición " + i + ": ");
            vec[i] = teclado.nextInt();
        }

        // Mostramos el vector original
        System.out.println("Vector original:");

        for (int i = 0; i < n; i++) {
            System.out.print(vec[i] + " ");
        }

        // Invertimos el vector
        for (int i = 0; i < n / 2; i++) {

            int aux = vec[i];

            vec[i] = vec[n - 1 - i];

            vec[n - 1 - i] = aux;
        }

        // Mostramos el vector invertido
        System.out.println("\nVector invertido:");

        for (int i = 0; i < n; i++) {
            System.out.print(vec[i] + " ");
        }

        teclado.close();
    }
}
