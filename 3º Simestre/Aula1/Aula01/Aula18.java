package Aula01;

public class Aula18 {
    public static void main(String[] args) {

    int soma1 = 0;
    int soma2 = 0;
        for(int x = 1; x < 21; x++){

            if (x % 3 == 0) { // Multiplo de 3
                System.out.println(x + " Multiplo de 3 ");
                soma1 += x;
            }

            if (x % 5 == 0) { // Multiplo de 5
                System.out.println(x + " Multiplo de 5 ");
                soma2 += x;
            }
        }
    System.out.println(" ");
    System.out.println("Soma de 3: " + soma1);
    System.out.println("Soma de 5: " + soma2);
    System.out.println("Soma total: " + (soma1 + soma2));
    
    }
}


