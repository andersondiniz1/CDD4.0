package Aula01;

import java.util.Scanner;

public class Desafio01 {
    
        public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite um número: "); 
        double resp = entrada.nextDouble();

        System.out.println(resp); 

        if(resp > 0){
            System.out.println("Numero é positivo."); 
        } else {
            System.out.println("Numero NÃO é positivo."); 
        }
    }

}
