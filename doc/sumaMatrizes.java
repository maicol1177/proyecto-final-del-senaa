import java.util.Scanner;

public class sumaMatrizes {

    public static void main(String[] args) {

        int matriz[][] = new int[5][4];
        Scanner teclado = new Scanner(System.in);
        for (int fila = 0; fila < 5; fila++) {
            for (int columna = 0; columna < 4; columna++) {
                matriz[fila][columna] = (int) (Math.random() * 100);
            }
        }

        for (int fila = 0; fila < 5; fila++) {
            int suma = 0;
            for (int columna = 0; columna < 4; columna++) {
                System.out.print(matriz[fila][columna] + " ");
                suma = suma + matriz[fila][columna];
            }

            System.out.println(" = Suma: " + suma);
        }
    }
}