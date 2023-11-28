package Aula01;

import java.util.Scanner;

public class Aula11 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Digite o numero: "); 
        int numero = input.nextInt();
        int numero2 = numero;

        int cont = 0;

        System.out.println("Numeros Pares: "); 
        while (cont <= numero){
            
            if (cont % 2 == 0){
                System.out.print(cont + " "); 
            }
            cont++;
        }
        numero = numero2;
        cont = 0;

        System.out.println(" "); 
        System.out.println("Numeros ímpares: "); 

        while (cont <= numero){

            if (cont % 2 == 1) {
                System.out.print(cont + " "); 
            }
            cont++;
        }
    input.close();
    }
}
