package Aula01;

public class Aula16 {
    public static void main(String[] args) {

    int count = 0;
        for(int x = 1; x < 100; x++){

            if (x % 3 == 0) { // Multiplo de 3
                System.out.print(x + " ");
                count++;
            }
        }
    System.out.println(" ");
    System.out.println("Quantidade de multiplos de 3: " + count);
    }
}


