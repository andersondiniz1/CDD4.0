package Aula01;

import java.util.Scanner;

public class Aula25 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        int numero[] = new int[5];
        int multiplica[] = new int[5];
        int soma[] = new int[5];

        // Pedir ao usuário para digitar 5 números
        for (int x = 0; x < 5; x++) {
            System.out.println("Digite o " + (x + 1) + "º numero: ");
            numero[x] = entrada.nextInt();
        }

        // Calcular a multiplicação dos números digitados
        for (int z = 0; z < 5; z++) {
            multiplica[z] = numero[z] * 2;
        }

        // Calcular a soma da multiplicação com os números digitados
        for (int y = 0; y < 5; y++) {
            soma[y] = multiplica[y] + numero[y];
        }

        // Exibir resultados
        System.out.println("Números digitados:");
        for (int i = 0; i < 5; i++) {
            System.out.println(numero[i]);
        }

        System.out.println("Resultados da multiplicação:");
        for (int i = 0; i < 5; i++) {
            System.out.println(multiplica[i]);
        }

        System.out.println("Resultados da soma da multiplicação:");
        for (int i = 0; i < 5; i++) {
            System.out.println(soma[i]);
        }
    }
}
