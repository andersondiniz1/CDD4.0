package Aula01;

import java.util.Scanner;

public class Aula07 {
    
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite um número: "); 
        double resp = entrada.nextDouble();

        System.out.println(resp); 

        entrada.close();
    }
}
