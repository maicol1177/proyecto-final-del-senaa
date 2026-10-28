import java.util.Scanner;

public class invertido {
    
    public static void mmain(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("introduce numero posiciones:");
        int n= teclado.nextInt();

        int[] vec= new int[n];

        for (int i = 0; i < n; i++) {
            System.out.print("introduce valor posicion" + i + ":");
            vec[i] = teclado.nextInt();

        }
    }
}
