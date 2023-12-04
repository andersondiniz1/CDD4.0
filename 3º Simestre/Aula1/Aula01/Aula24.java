package Aula01;

import java.util.Scanner;

public class Aula24 {

    public static void main(String[] args) {

        double medias[] = new double[10];
        double notas[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        Scanner entrada = new Scanner(System.in);

        for(int x = 0; x < 10; x++) {
            System.out.println("Digite uma media: ");
            medias[x] = entrada.nextDouble();
        }
    
        for(int e = 0; e < 10; e++) {
            System.out.println(medias[e]);
        }

        for(double z: medias) { // para cada valor dentro de medias 
            System.out.println(z);
        }
    }
}