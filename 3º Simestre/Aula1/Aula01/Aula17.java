package Aula01;

import java.util.Scanner;

public class Aula17 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Digite o numero: ");
        int numero = input.nextInt();

        if(numero % 2 == 0){
            numero = numero / 2;
            System.out.println("Numero: " + numero);
        }

        if(numero % 2 == 1){
            numero = 3 * numero + 1;
            System.out.println("Numero: " + numero);
        }
    input.close();
    }
}


