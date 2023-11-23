package Aula01;

import java.util.Scanner;

public class Desafio06 {
    
        public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Telefonou para a vítima? /n Digite 1 para sim, 2 para não: "); 
        int resp1 = entrada.nextInt();

        System.out.println("Esteve no local do crime? /n Digite 1 para sim, 2 para não: "); 
        int resp2 = entrada.nextInt();

        System.out.println("Mora perto da vítima? /n Digite 1 para sim, 2 para não: "); 
        int resp3 = entrada.nextInt();
            
        System.out.println("Devia para a vítima? /n Digite 1 para sim, 2 para não: "); 
        int resp4 = entrada.nextInt();

        System.out.println("Já trabalhou com a vítima? /n Digite 1 para sim, 2 para não: "); 
        int resp5 = entrada.nextInt();     

        int resultado = resp1 + resp2 + resp3 + resp4 + resp5;
    
        if (resultado == 8){
            System.out.println("Suspeito"); 
        } else if (resultado == 7 && resultado == 6){
            System.out.println("Cúmplice"); 
        } else if (resultado == 5){
            System.out.println("Assasino"); 
        } else {
            System.out.println("Inocente"); 
        }
    }

}
